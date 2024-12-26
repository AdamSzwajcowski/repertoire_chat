from categorypredictor import CategoryPredictor
from database import Database
from categories import Categories
from enum import Enum


# context enum for varying the response based on the previous message
Context = Enum('Context', ['NONE','SOLODUO','SEARCH'])

class ResponseGenerator:
    """
    ResponseGenerator handles the conversation based on the user's input.
    """
    
    def __init__(self):
        self.database = Database()
        self.predictor = CategoryPredictor(self.database)     
        self.soloduo = []  # type of repertoire context
        self.singer = []   # singer context
        self.context = [Context.NONE]  # general conversational context
        self.rephrase_counter = 0
        self.last_activity = 0
        
        
    def check_repertoire_context(self, sentence):
        """
        Check the current context of solo/duo repertoire and return True if it has changed.
        """
        # save previous values to check if they changed
        soloduo_prev = self.soloduo
        singer_prev = self.singer
        sentence = sentence.lower()
        if 'solo' in sentence or 'fingerstyle' in sentence:
            self.soloduo = 'solo'
            self.singer = []
        elif 'dominika' in sentence:
            self.soloduo = 'duo'
            self.singer = 'dominika'
        elif 'sara' in sentence or 'salia' in sentence:
            self.soloduo = 'duo'
            self.singer = 'sara'
        elif 'ania' in sentence or 'anna' in sentence:
            self.soloduo = 'duo'
            self.singer = 'ania'
        elif 'duo' in sentence or 'singer' in sentence:
            self.soloduo = 'duo'
            self.singer = []
        return (self.soloduo != soloduo_prev) or (self.singer != singer_prev)

    def misunderstand(self):
        """
        Punt if there are two misunderstandings in a row. Otherwise, ask for rephrasing.
        """
        if self.rephrase_counter:
            # reset the conversation
            self.context = [Context.NONE]
            self.soloduo = []
            self.singer = []
            self.rephrase_counter = 0
            return("I'm afraid I can't help you with that. Can I do anything else for you?")
        else:
            # maintain the context
            self.rephrase_counter += 1
            return("I couldn't quite understand, could you rephrase?")
        
    def ambiguous_search(self, sentence):
        """
        Call the database to check if the sentence resembles any title or artist.
        Used when the sentence doesn't conform to any category according to the model.
        """
        if self.soloduo:
            # perform ambiguous search to see if the sentence matches any titles or artists
            category, proper_name = self.database.ambiguous_search(sentence, self.soloduo, self.singer)
            if category:    # if found anything relevant
                return(self.take_action(category, proper_name))            
            else:
                return(self.misunderstand())
        else:  # if soloduo not specified yet, search both (solo prioritized)
             category, proper_name = self.database.ambiguous_search(sentence, 'solo', [])
             if category:    # if found anything relevant
                 self.soloduo = 'solo'
                 return(self.take_action(category, proper_name))
             else:
                 category, proper_name = self.database.ambiguous_search(sentence, 'duo', [])
                 if category:    # if found anything relevant
                     self.soloduo = 'duo'
                     return(self.take_action(category, proper_name))            
                 else:
                     return(self.misunderstand())
              

    def take_action(self, category, proper_name):
        """
        Perform an action based on the recognized category.
        """
        self.rephrase_counter = 0
        self.context = [Context.NONE]    # any previous context becomes irrelevant
        
        if category == Categories.GREETINGS:
            return('Hello! How can I help you?')
        
        elif category == Categories.THANKS:
            return(("You're welcome! Is there anything else I can do for you?"))
        
        elif category == Categories.BYE:
            return('Bye!')
        
        else:  # REPERTOIRE, SONG_NAME, ARTIST_NAME or TAG_NAME
            if category != Categories.REPERTOIRE and not proper_name:
                # if there should be a proper name but there is none
                return(self.misunderstand())
            if not self.soloduo:
                self.context = [Context.SOLODUO]
                # append tuple with intended action to take once solo/duo is specified
                self.context.append((category,proper_name))
                return('Do you mean solo (fingerstyle) or in a duo?')
            else:
                self.context = [Context.SEARCH]
                self.context.append((category, proper_name))
                return(self.database.get_response(category, proper_name, self.soloduo, self.singer)) 

    def respond(self, sentence):
        """
        Return a response based on the input sentence (prompt).
        """
        print(self.context)

        if self.context[0] == Context.NONE:
            self.check_repertoire_context(sentence)
            category, probability, proper_name = self.predictor.predict(sentence)
            print(category, probability)
            if probability > 0.95:   # understood with very good certainty
                return(self.take_action(category, proper_name))
            else:
                return(self.ambiguous_search(sentence))
            
        elif self.context[0] == Context.SOLODUO:            
            repertoire_context_changed = self.check_repertoire_context(sentence) 
            # check if some other request was made despite only asking for clarification
            category, probability, proper_name = self.predictor.predict(sentence)
            print(category, probability)
            if probability > 0.95:                   
                return(self.take_action(category, proper_name))                     
            elif repertoire_context_changed:
                # come back to the previously saved request
                category, proper_name = self.context[1]
                return(self.take_action(category, proper_name))
            else:   # if the user still hasn't specified solo/duo
                return(self.ambiguous_search(sentence))
            
        elif self.context[0] == Context.SEARCH: 
            repertoire_context_changed = self.check_repertoire_context(sentence) 
            category, probability, proper_name = self.predictor.predict(sentence)
            print(category, probability)
            if probability > 0.95:                   
                return(self.take_action(category, proper_name))                     
            elif repertoire_context_changed:   # if context changed
                # perform the same search but with changed repertoire context
                category, proper_name = self.context[1]
                return(self.take_action(category, proper_name))
            else:
                return(self.ambiguous_search(sentence))
                          

# test
if __name__ == "__main__":
    generator = ResponseGenerator()
    print("The bot is running.")
    while True:
        output = generator.respond(input())
        print(output)
        if output == 'Bye!':
            break