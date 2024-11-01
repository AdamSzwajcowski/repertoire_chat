from categorypredictor import Categories

class Database:
    """
    Database handles connection to a database.
    """
    
    def __init__(self):
        a = 1   # placeholder
           
        
    def getData(self, category, proper_name, soloduo):
        """
        Returns song from the database based on the information extracted
        from the prompt.
        """
        
        if category == Categories.REPERTOIRE:
            if soloduo == 'solo':
                return("Here's my solo repertoire:")
            else:
                return("Here's my duo repertoire:")
                
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