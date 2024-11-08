from categories import Categories

from rapidfuzz import fuzz
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
                    best_name = main_name if nametype == 'title' else name    # return the default title but a specific artist
            if best_match == 100:    # stop searching if perfect match found
                break
        return best_name, best_match
            
    
    def get_data(self, category, proper_name, soloduo):
        """
        Returns song from the database based on the information extracted
        from the prompt.
        """
        
        if category == Categories.REPERTOIRE:
            self.cur.execute(f'SELECT title, artist, known_from FROM {soloduo}')
            song_list = self.cur.fetchall()
            song_list = self.format_repertoire(song_list)
            return(f"Here's my {soloduo} repertoire:\n" + song_list)

                
        elif category == Categories.SONG_NAME:
            title, match = self.find_best_match('title', proper_name, soloduo)
            if match > 75:
                self.cur.execute(f'SELECT artist, known_from FROM {soloduo} WHERE title = \'{title}\'')
                artist, known_from = self.cur.fetchall()[0]
                if artist:
                    song = (f'"{title}" by {artist}')
                elif known_from:
                    song = (f'"{title}" from "{known_from}"')
                return(f"Yes, I have {song} in my {soloduo} repertoire!")
            else:
                return("I'm afraid I don't have this song in my {soloduo} repertoire.")
                
        elif category == Categories.ARTIST_NAME:
            if soloduo == 'solo':
                return(f"Here are the songs by {proper_name} that I play solo:")
            else:
                return(f"Here are the songs by {proper_name} that I play in a duo:")
            
        elif category == Categories.TAG_NAME:
            if soloduo == 'solo':
                return(f"Here are the songs from my solo repertoire that are labeled as {proper_name}:")
            else:
                return(f"Here are the songs from my solo repertoire that are labeled as {proper_name}:")
            
            
if __name__ == '__main__':
    db = Database()
    best_name, best_match = db.find_best_match('title','What\'s Up','duo')