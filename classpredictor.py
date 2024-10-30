import pickle
import numpy as np
import re
from enum import Enum

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

class ClassPredictor:

    def __init__(self):
        """
        Initialize the object    
        """        
        self.lemmatizer = WordNetLemmatizer()
        self.words = pickle.load(open('model/words.pkl', 'rb'))
        self.Classes = Enum("Classes", pickle.load(open('model/classes.pkl', 'rb')))
        self.model = load_model('model/chatbot_model.keras')
        self.genres = ['pop','rock','jazz','film','polish','soul',
                       'musical','ballad', '70','80','90']
        self.context = []  # solo or duo

    def check_context(self, sentence):
        """
        Check whether the context of solo/duo repertoire has changed.
        """
        if 'solo' in sentence or 'fingerstyle' in sentence:
            self.context = 'solo'
        elif 'duo' in sentence:
            self.context = 'duo'

    def check_for_song_name(self, sentence):
        """
        Check if the sentence includes a song name (anything in "*").
        """
        pattern = r'\"(.{1,}?)\"'
        song_name = re.findall(pattern, sentence)
        if song_name:
            song_name = song_name[0]
            sentence = sentence.replace(f'"{song_name}"', 'song_name')
        
        return sentence, song_name

    def check_for_artist_name(self, sentence):
        """
        Check if the sentence includes an artist name (anything after "by").
        """
        pattern = "by"
        match = re.search(f'{pattern}(.*)', sentence)
        if match:
            artist_name = match.group(1).strip()
            if artist_name[-1] in {'?','.','!'}:
                artist_name = artist_name[:-1]  # delete punctuation from the end of the sentence
            sentence = sentence.replace(artist_name, 'artist_name')
        else:
            artist_name = []
        
        return sentence, artist_name        
        
    def check_for_genre_name(self, sentence):
        """
        Check if the sentence includes any genre names.
        """
        for genre in self.genres:
            if genre in sentence:
                sentence = sentence.replace(genre, 'genre_name')
                return sentence, genre
        else:
            return sentence, []

    def check_for_names(self, sentence):
        """
        Check if the sentence includes any names of song, artist or genre.
        If yes, replace it with a placeholder and return the edited sentence and the name.
        """
        sentence, song_name = self.check_for_song_name(sentence)
        if song_name:
            return sentence, song_name
        else:
            sentence, artist_name = self.check_for_artist_name(sentence)
            if artist_name:
                return sentence, artist_name
            else:
                sentence, genre_name = self.check_for_genre_name(sentence)
                return sentence, genre_name

    def clean_up_sentence(self, sentence):
        """
        Tokenize and lemmatize the sentence.
        """       
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        
        return sentence_words

    def bag_of_words(self, sentence):
        """
        Return the bag of words representation of the sentence.
        """        
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0] * len(self.words)
        for sentence_word in sentence_words:
            for ind, word in enumerate(self.words):
                if word == sentence_word:
                    bag[ind] = 1
                    
        return np.array(bag)

    def predict(self, sentence):
        """
        Predict the class based on the sentence.
        """
        self.check_context(sentence)
        sentence, proper_name = self.check_for_names(sentence)
        bag = self.bag_of_words(sentence)
        results = self.model.predict(np.array([bag]))[0]
        ind_max = np.argmax(results)
        probability = results[ind_max]
    
        return self.Classes(ind_max+1), probability, proper_name, self.context
    
# if __name__ == "__main__":
#     predictor = ClassPredictor()
#     sentence, song_name = predictor.check_for_names('Do you play "Smoke on the Water"?')
#     print(sentence, song_name)
#     sentence, artist_name = predictor.check_for_names('Do you play anything by ABBA?')
#     print(sentence, artist_name)
#     sentence, genre_name = predictor.check_for_names('Do you play any film music?')
#     print(sentence, genre_name)
#     sentence, genre_name = predictor.check_for_names('What is your repertoire?')
#     print(sentence, genre_name)
