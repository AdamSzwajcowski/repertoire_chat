from classpredictor import ClassPredictor
from enum import Enum

# context enum for varying the response based on the previous message
Context = Enum('Context', ['SOLODUO','REPHRASE'])

class ResponseGenerator:
    
    def __init__(self):
        self.predictor = ClassPredictor()
        self.soloduo = []  # solo or duo context
        self.context = []
        
        
    def check_soloduo(self, sentence):
        """
        Check whether the context of solo/duo repertoire has changed and return
        the current value.
        """
        if 'solo' in sentence or 'fingerstyle' in sentence:
            self.soloduo = 'solo'
        elif 'duo' in sentence:
            self.soloduo = 'duo'

        return self.soloduo
    
    def ask_for_soloduo(self):
        """
        Request for the user to establish the context of the conversation
        (solo/duo repertoire).
        """
        return('''Do you mean solo (fingerstyle) or in a duo?''')
            
    def greetings(self):
        """
        Return the response to greetings.
        """
        return(''''Hello! How can I help you?''')
               
    def summary(self):
        """
        Return the summary of the scope of the chatbot
        """
        return(''''I'm here to help you with repertoire-based queries. You can
               ask for my solo or duo repertoire, as well as search for
               specific songs, artists or genres. If you want to search for a
               specific song, please put it in the double quotation mark (e.g.
               "Dancing Queen") - this will make my job easier!''')
            

    def take_action(self, category, proper_name):
        """
        Perform an action based on the recognized category.
        """
        if category == self.predictor.classes.GREETINGS:
            return(self.greetings())
        elif category == self.predictor.classes.SUMMARY:
            return(self.summary())
        elif category == self.predictor.classes.REPERTOIRE:
            if not self.check_soloduo(sentence)
                
            print("Here's my repertoire:")  # call do bazy danych

    def respond(self, sentence):
        """
        Return a response based on the input sentence (prompt).
        """
        # empty the context queue if applicable
        while self.context:
            if self.context[0] == Context.SOLODUO:
                
        
        # run the model if there is no context left
        else:   
            category, probability, proper_name = self.predictor.predict(sentence)
            if probability > 0.95:   # understood with very good certainty
                funkcja_do_analizy
            else:
                przeszukaj_baze # przeszukiwanie baz
                if znalezione:
                    return(odpowiednia_funkcja)
                elif probability > 0.7: # less certain, but still quite probable
                    funkcja_do_analizy
                else:
                    return(funkcja_do_nierozumienia)