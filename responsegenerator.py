from classpredictor import ClassPredictor
from enum import Enum

# context enum for varying the response based on the previous message
Context = Enum('Context', ['NONE','SOLODUO','REPHRASE'])

class ResponseGenerator:
    
    def __init__(self):
        self.predictor = ClassPredictor()
        self.soloduo = []  # solo or duo context
        self.context = [Context.NONE]  # general conversational context
        
        
    def check_soloduo(self, sentence):
        """
        Check whether the context of solo/duo repertoire has changed.
        """
        if 'solo' in sentence or 'fingerstyle' in sentence:
            self.soloduo = 'solo'
        elif 'duo' in sentence:
            self.soloduo = 'duo'
    
    def ask_for_soloduo(self):
        return('Do you mean solo (fingerstyle) or in a duo?')
            
    def greetings(self):
        return('Hello! How can I help you?')
               
    def summary(self):
        return("to be fixed")
    
    def bye(self):
        return('Bye!')

    def misunderstand(self):
        '''
        Punt if there are two misunderstandings in a row. Otherwise, ask for rephrasing.
        '''
        if self.context[0] == Context.REPHRASE:
            return("I'm afraid I can't help you with that. Can I do anything else for you?")
            self.context = [Context.NONE]           
        else:
            return("I couldn't quite understand, could you rephrase?")
            self.context.insert(0,Context.REPHRASE)
            
        

    def take_action(self, category, proper_name):
        """
        Perform an action based on the recognized category.
        """
        self.context = [Context.NONE]    # any previous context becomes irrelevant
        if category == self.predictor.classes.GREETINGS:
            return(self.greetings())
        elif category == self.predictor.classes.SUMMARY:
            return(self.summary())
        elif category == self.predictor.classes.BYE:
            return(self.bye())
        else:  # REPERTOIRE, SONG_NAME, ARTIST_NAME or GENRE_NAME
            if not self.soloduo:
                self.context = [Context.SOLODUO]
                # append tuple with intended action to take once solo/duo is specified
                self.context.append((category,proper_name))
                return(self.ask_for_soloduo())
            else:
                return("Here's the database output:")  # call do bazy danych

    def respond(self, sentence):
        """
        Return a response based on the input sentence (prompt).
        """
        print(self.context)
        if self.context[0] == Context.SOLODUO:              
            self.check_soloduo(sentence)               
            # check if some other request was made despite only asking for clarification
            category, probability, proper_name = self.predictor.predict(sentence)
            print(category, probability)
            if probability > 0.95:                   
                return(self.take_action(category, proper_name))                     
            elif not self.soloduo:   # if the user still hasn't specified solo/duo
                return(self.misunderstand())
            else:   # if the user simply provided solo/duo
                # read the category and proper_name from the context after SOLODUO
                category, proper_name = self.context[1]
                return(self.take_action(category, proper_name))
                    
        elif self.context[0] == Context.NONE:
            self.check_soloduo(sentence)
            category, probability, proper_name = self.predictor.predict(sentence)
            print(category, probability)
            if probability > 0.95:   # understood with very good certainty
                return(self.take_action(category, proper_name))
            else:
                #przeszukaj_baze # przeszukiwanie baz
                if False:   # if znalezione
                    return(1)
                elif probability > 0.7: # less certain, but still quite probable
                    return(self.take_action(category, proper_name))               
                else:
                    return(self.misunderstand())
                

# test
if __name__ == "__main__":
    generator = ResponseGenerator()
    while True:
        print(generator.respond(input()))
    