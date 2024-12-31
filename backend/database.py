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
                host="db",       # "localhost" for local uses
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
          
    def find_best_match(self, nametype, searched_name, soloduo, singer, truncate=False):
        """
        Find the best matching artist or title to the requested one.
        NAMETYPE: STR, either 'title' or 'artist'
        TRUNCATE: BOOL, determines whether or not the searched name should be truncated to
        the length of the compared name. Set true for general artist search to counteract
        the simplistic NLP rule of detecting the artist name being prone to overfetching.
        """
        def update_best_match(name, searched_name, best_match, best_name):
            """
            Check name match and update if it is the best one yet.
            """
            if truncate:
                searched_name = searched_name[:len(name)]
            name_match = fuzz.ratio(name.lower(), searched_name.lower())                    
            if name_match > best_match:
                best_match, best_name = name_match, name
            return best_match, best_name
        if singer:  
            self.cur.execute(f'SELECT {nametype}, {nametype}_alternative FROM {soloduo} '
                             f'WHERE {singer} IS NOT NULL')
        else:
            self.cur.execute(f'SELECT {nametype}, {nametype}_alternative FROM {soloduo}')
        name_rows = self.cur.fetchall()
        best_match = 0
        best_name = ''
        for main_name, name_alternative in name_rows:
            if main_name:
                best_match, best_name = update_best_match(main_name, searched_name, best_match, best_name)                  
                if best_match == 100: break    # stop searching if perfect match found
            if name_alternative:   
                for name in name_alternative:
                    best_match, best_name = update_best_match(name, searched_name, best_match, best_name)    
                    if best_match == 100: break    # stop searching if perfect match found
        return best_name, best_match
    
    
    def find_songs_by_artist(self, artist, soloduo, singer):
        """
        Return a list of songs by a given artist (including duos, covers, etc.).
        """
        if singer:
            self.cur.execute(f'SELECT id, artist, artist_alternative FROM {soloduo} '
                             f'WHERE {singer} IS NOT NULL')
        else:
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
    
    def ambiguous_search(self, sentence, soloduo, singer):
        """
        Search through titles and artists to see if the sentence matches any of them.
        """
        # search through titles
        title, match_title = self.find_best_match('title', sentence, soloduo, singer)
        # check if the found title is a subset of the sentence
        sentence_ngrams = ngrams(sentence.split(),len(title.split()))
        for ngram in sentence_ngrams:
            match_title = max(fuzz.ratio(' '.join(list(ngram)), title.lower()), match_title)
            
        # search through artists
        artist, match_artist = self.find_best_match('artist', sentence, soloduo, singer)
        # check if the found artist is a subset of the sentence
        sentence_ngrams = ngrams(sentence.split(),len(artist.split()))
        for ngram in sentence_ngrams:
            match_artist = max(fuzz.ratio(' '.join(list(ngram)), artist.lower()), match_artist)
            
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
    
    def get_response(self, category, proper_name, soloduo, singer):
        """
        Returns information from the database based on the information extracted
        from the prompt.
        """
        
        if category == Categories.REPERTOIRE:
            
            if singer:
                self.cur.execute(f"SELECT title, artist, known_from FROM {soloduo} "
                                 f"WHERE {singer} IS NOT NULL")
                song_list = self.format_songs(self.cur.fetchall())
                return(f"Here's my repertoire with {singer.capitalize()}:\n" + song_list)
            else:
                self.cur.execute(f"SELECT title, artist, known_from FROM {soloduo}")
                song_list = self.format_songs(self.cur.fetchall())
                return(f"Here's my {soloduo} repertoire:\n" + song_list)

                
        elif category == Categories.SONG_NAME:
            title, match = self.find_best_match('title', proper_name, soloduo, singer)
            title = title.replace("'", "''") # double the apostrophes for SQL query
            if match > 75:
                if singer:
                    self.cur.execute(f'''SELECT title, artist, known_from FROM {soloduo}
                                     WHERE (title = \'{title}\' OR \'{title}\' = ANY(title_alternative))
                                     AND {singer} IS NOT NULL''')    
                else:
                    self.cur.execute(f'''SELECT title, artist, known_from FROM {soloduo}
                                     WHERE title = \'{title}\' OR \'{title}\' = ANY(title_alternative)''')
                title, artist, known_from = self.cur.fetchall()[0]  # overwrite title with the default one
                if artist:
                    song = (f'"{title}" by {artist}')
                elif known_from:
                    song = (f'"{title}" from "{known_from}"')
                    
                if singer:
                    return(f"Yes, I play this song with {singer.capitalize()}!")
                else:                        
                    return(f"Yes, I have {song} in my {soloduo} repertoire!")
                
            else:
                if singer:
                    return(f"I'm afraid I don't play this song with {singer.capitalize()}.")
                else:
                    return(f"I'm afraid I don't have this song in my {soloduo} repertoire.")
                
        elif category == Categories.ARTIST_NAME:
            artist, match = self.find_best_match('artist', proper_name, soloduo, singer, True)
            artist = artist.replace("'", "''") # double the apostrophes for SQL query
            if match > 75:
                # if matching enough artist found, return their all songs from relevant repertoire
                song_ids = self.find_songs_by_artist(artist, soloduo, singer)
                self.cur.execute(f'''SELECT title, artist, known_from FROM {soloduo}
                                 WHERE id IN({', '.join(map(str, song_ids))})''')
                song_list = self.format_songs(self.cur.fetchall())
                if singer:
                    return(f"Here are all the songs by {artist} from my repertoire "
                           f"with {singer.capitalize()}:\n" + song_list)
                else:
                    return(f"Here are all the songs by {artist} from my {soloduo} "
                           f"repertoire:\n" + song_list)
                
            else:
                if singer:
                    return(f"I'm afraid I don't have any music by this artist in my "
                           f"repertoire with {singer.capitalize()}.")         
                else:
                    return(f"I'm afraid I don't have any music by this artist in my "
                           f"{soloduo} repertoire.")        
        
        elif category == Categories.TAG_NAME:
            if singer:
                self.cur.execute(f'''SELECT title, artist, known_from FROM {soloduo}
                                 WHERE '{proper_name}' ILIKE ANY(tags)
                                 AND {singer} IS NOT NULL''') 
                song_list = self.format_songs(self.cur.fetchall())
                return(f"Here are the songs from my repertoire with {singer.capitalize()} "
                       f"that are labeled as {proper_name}:\n" + song_list)
            else:
                self.cur.execute(f'''SELECT title, artist, known_from FROM {soloduo}
                                 WHERE '{proper_name}' ILIKE ANY(tags)''')
                song_list = self.format_songs(self.cur.fetchall())                         
                return(f"Here are the songs from my {soloduo} repertoire that are labeled as {proper_name}:\n" + song_list)