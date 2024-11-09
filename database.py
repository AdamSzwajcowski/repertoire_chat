from categories import Categories

from rapidfuzz import fuzz
from nltk.util import ngrams
import psycopg2

class Database:
    """
    Database handles connection to the database.
    """
    
    def __init__(self):
        """
        Initialize the connection to the database
        """
        try:
            self.conn = psycopg2.connect(
                dbname="Repertoire",
                user="adam",
                password="adam1234",
                host="localhost",
                port="5432")
            self.cur = self.conn.cursor()
        except Exception as e:
            print('Could not connect to the database.', e)
                
    def __del__(self):
        """
        Close connection to the database.
        """
        if self.conn:
           self.cur.close()
           self.conn.close()
           
    def list_tags(self):
        """
        List unique tags found in both solo and duo reperoitre.
        """
        tag_list = []
        def append_unique_tags(table_name, tag_list):
            self.cur.execute(f'SELECT tags FROM {table_name}')
            tags_rows = self.cur.fetchall()
            for tags in tags_rows:
                tags = tags[0] # detuple
                for tag in tags:
                    if tag not in tag_list:
                        tag_list.append(tag)
                    
        append_unique_tags('solo', tag_list)
        append_unique_tags('duo', tag_list)
        return tag_list
                
           
    def format_songs(self, song_list):
        """
        Output the song list with aritsts and/or information where they are known from.
        """
        output = ''
        for title, artist, known_from in song_list:
            if known_from and artist:
                output += (f'"{title}" from "{known_from}", by {artist}\n')
            elif artist:
                output += (f'"{title}" by {artist}\n')
            elif known_from:
                output += (f'"{title}" from "{known_from}"\n')
        if output:
            output = output[:-1] # remove '\n' from the last line
        return output
          
    def find_best_match(self, nametype, searched_name, soloduo):
        """
        Find the best matching title or artist to the requested name.
        nametype: STRING, either 'title' or 'artist'
        """
        self.cur.execute(f'SELECT {nametype}, {nametype}_alternative FROM {soloduo}')
        name_rows = self.cur.fetchall()
        best_match = 0
        best_name = ''
        for main_name, name_alternative in name_rows:
            names = [main_name] if main_name else []    # empty array if there is no main artist
            if name_alternative:   
                for n_a in name_alternative:  
                    names.append(n_a)
            for name in names:
                name_match = fuzz.ratio(name.lower(), searched_name.lower())                    
                if name_match > best_match:
                    best_match = name_match
                    best_name = name    # return the default title but a specific artist
            if best_match == 100:    # stop searching if perfect match found
                break
        return best_name, best_match
    
    def find_songs_by_artist(self, artist, soloduo):
        """
        Return a list of songs by a given artist (including duos, covers, etc.).
        """
        self.cur.execute(f'SELECT id, artist, artist_alternative FROM {soloduo}')
        artist_rows = self.cur.fetchall()
        ids = []    # list of song IDs
        for ID, main_artist, artist_alternative in artist_rows:
            if main_artist == artist:
                ids.append(ID)
            elif artist_alternative:
                for a_a in artist_alternative:
                    if a_a == artist:
                        ids.append(ID)
                        break
        return ids
    
    def ambiguous_search(self, sentence, soloduo):
        """
        Search through titles and artists to see if the sentence matches any of them.
        """
        # search through titles
        title, match_title = self.find_best_match('title', sentence, soloduo)
        # check if the found title is a subset of the sentence
        sentence_ngrams = ngrams(sentence.split(),len(title.split()))
        for ngram in sentence_ngrams:
            match_title = max(fuzz.ratio(' '.join(list(ngram)), title), match_title)
            
        # search through artists
        artist, match_artist = self.find_best_match('artist', sentence, soloduo)
        # check if the found artist is a subset of the sentence
        sentence_ngrams = ngrams(sentence.split(),len(artist.split()))
        for ngram in sentence_ngrams:
            match_artist = max(fuzz.ratio(' '.join(list(ngram)), artist), match_artist)
            
        if match_title < 75 and match_artist < 75: # nothing found, call misunderstanding
            category = []
            proper_name = []
        elif match_title > match_artist:
            category = Categories.SONG_NAME
            proper_name = title
        else:
            category = Categories.ARTIST_NAME
            proper_name = artist
        return category, proper_name        
    
    def get_data(self, category, proper_name, soloduo):
        """
        Returns song from the database based on the information extracted
        from the prompt.
        """
        
        if category == Categories.REPERTOIRE:
            self.cur.execute(f'SELECT title, artist, known_from FROM {soloduo}')
            song_list = self.format_songs(self.cur.fetchall())
            return(f"Here's my {soloduo} repertoire:\n" + song_list)

                
        elif category == Categories.SONG_NAME:
            title, match = self.find_best_match('title', proper_name, soloduo)
            if match > 75:
                self.cur.execute(f'''SELECT title, artist, known_from FROM {soloduo}
                                 WHERE title = \'{title}\' OR \'{title}\' = ANY(title_alternative)''')
                title, artist, known_from = self.cur.fetchall()[0]  # overwrite title with the default one
                if artist:
                    song = (f'"{title}" by {artist}')
                elif known_from:
                    song = (f'"{title}" from "{known_from}"')
                return(f"Yes, I have {song} in my {soloduo} repertoire!")
            else:
                return("I'm afraid I don't have this song in my {soloduo} repertoire.")
                
        elif category == Categories.ARTIST_NAME:
            artist, match = self.find_best_match('artist', proper_name, soloduo)
            if match > 75:
                # if matching enough artist found, return their all songs from relevant repertoire
                song_ids = self.find_songs_by_artist(artist, soloduo)
                self.cur.execute(f'''SELECT title, artist, known_from FROM {soloduo}
                                 WHERE id IN({', '.join(map(str, song_ids))})''')
                song_list = self.format_songs(self.cur.fetchall())
                return(f"Here are all the songs by {artist} from my {soloduo} repertoire:\n" + song_list)
            else:
                return(f"I'm afraid I don't have any music by this artist in my {soloduo} repertoire.")        
        
        elif category == Categories.TAG_NAME:
            self.cur.execute(f'''SELECT title, artist, known_from FROM {soloduo}
                             WHERE '{proper_name}' ILIKE ANY(tags)''')
            song_list = self.format_songs(self.cur.fetchall())                     
            return(f"Here are the songs from my {soloduo} repertoire that are labeled as {proper_name}:\n" + song_list)
            
            
if __name__ == '__main__':
    db = Database()
    print(db.ambiguous_search('any abba songs?', 'solo'))