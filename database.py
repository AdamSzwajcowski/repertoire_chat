

class Database:
    """
    Database handles connection to a database.
    """
    
    def __init__(self, predictor):
        self.predictor = predictor
           
        
    def getData(category, proper_name, soloduo):