from categories import Categories
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
            if soloduo == 'solo':
                return(f"Yes, I have \"{proper_name}\" in my solo repertoire!")
            else:
                return(f"Yes, I have \"{proper_name}\" in my duo repertoire!")
                
        elif category == Categories.ARTIST_NAME:
            if soloduo == 'solo':
                return(f"Here are the songs by {proper_name} that I play solo:")
            else:
                return(f"Here are the songs by {proper_name} that I play in a duo:")
            
        elif category == Categories.GENRE_NAME:
            if soloduo == 'solo':
                return(f"Here are the songs from my solo repertoire that are labeled as {proper_name}:")
            else:
                return(f"Here are the songs from my solo repertoire that are labeled as {proper_name}:")