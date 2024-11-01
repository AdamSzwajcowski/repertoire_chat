from categorypredictor import CategoryPredictor
from enum import Enum

# context enum for varying the response based on the previous message
Context = Enum('Context', ['NONE','SOLODUO'])

class ResponseGenerator:
    """
    ResponseGenerator handles the conversation based on the user's input.
    """
    
    def __init__(self):
        self.predictor = CategoryPredictor()
        self.soloduo = []  # solo or duo context
        self.context = [Context.NONE]  # general conversational context
        self.rephrase_counter = 0
        
        
    def check_soloduo(self, sentence):
        """
        Check whether the context of solo/duo repertoire has changed.
        """
        if 'solo' in sentence or 'fingerstyle' in sentence:
            self.soloduo = 'solo'
        elif 'duo' in sentence:
            self.soloduo = 'duo'

    def misunderstand(self):
        '''
        Punt if there are two misunderstandings in a row. Otherwise, ask for rephrasing.
        '''
        if self.rephrase_counter:
            return("I'm afraid I can't help you with that. Can I do anything else for you?")
            self.context = [Context.NONE]
            self.rephrase_counter = 0
        else:
            return("I couldn't quite understand, could you rephrase?")
            self.rephrase_counter += 1                 

    def take_action(self, category, proper_name):
        """
        Perform an action based on the recognized category.
        """
        self.rephrase_counter = 0
        self.context = [Context.NONE]    # any previous context becomes irrelevant
        
        if category == self.predictor.categories.GREETINGS:
            return('Hello! How can I help you?')
        
        elif category == self.predictor.categories.SUMMARY:
            return(" ".join(["I play a wide variety of songs and pieces both solo, as a",
                    "fingerstyle guitarist, and in a duo with singers. This chatbot",
                    "is meant to help you navigate around my repertoire - you can",
                    "ask for a specific song, artist or genre."]))
        
        elif category == self.predictor.categories.THANKS:
            return(("You're welcome! Is there anything else I can do for you?"))
        
        elif category == self.predictor.categories.BYE:
            return('Bye!')
        
        else:  # REPERTOIRE, SONG_NAME, ARTIST_NAME or GENRE_NAME
            if not self.soloduo:
                self.context = [Context.SOLODUO]
                # append tuple with intended action to take once solo/duo is specified
                self.context.append((category,proper_name))
                return('Do you mean solo (fingerstyle) or in a duo?')
            else:
                return("Here's the database output:")  # call do bazy danych

    def respond(self, sentence):
        """
        Return a response based on the input sentence (prompt).
        """
        print(self.context)

        if self.context[0] == Context.NONE:
            self.check_soloduo(sentence)
            category, probability, proper_name = self.predictor.predict(sentence)
            print(category, probability)
            if probability > 0.95:   # understood with very good certainty
                return(self.take_action(category, proper_name))
            else:
                #przeszukaj_baze # przeszukiwanie baz
                if False:   # if znalezione
                    return(1)
                elif probability > 0.8: # less certain, but still quite probable
                    return(self.take_action(category, proper_name))               
                else:
                    return(self.misunderstand())
                
        elif self.context[0] == Context.SOLODUO:              
            self.check_soloduo(sentence)               
            # check if some other request was made despite only asking for clarification
            category, probability, proper_name = self.predictor.predict(sentence)
            print(category, probability)
            if probability > 0.95:                   
                return(self.take_action(category, proper_name))                     
            elif not self.soloduo:   # if the user still hasn't specified solo/duo
                return(self.misunderstand())
            else:   # if the user simply provided solo/duo
                # come back to the previously saved request
                category, proper_name = self.context[1]
                return(self.take_action(category, proper_name))
                

# test
if __name__ == "__main__":
    generator = ResponseGenerator()
    while True:
        print(generator.respond(input()))
    