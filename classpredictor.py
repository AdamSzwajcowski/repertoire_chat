import pickle
import numpy as np
import re

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
        self.model = load_model('model/chatbot_model.keras')
        self.genres = ['TBD']

    def check_for_song_name(self, sentence):
        """
        Check if the sentence includes a song name
        """
        pattern = r'\"(.{1,}?)\"'
        song_name = re.findall(pattern, sentence)
        if song_name:
            song_name = song_name[0]
            sentence = sentence.replace(f'"{song_name}"', 'song_name')
        
        return sentence, song_name

    def check_for_artist_name(self, sentence):
        """
        Check if the sentence includes an artist name
        """
        
    def check_for_genre_name(self, sentence):
        """
        Check if the sentence includes a genre name
        """
        

    def clean_up_sentence(self, sentence):
        """
        Tokenize and lemmatize the sentence
        """       
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [self.lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        
        return sentence_words

    def bag_of_words(self, sentence):
        """
        Return the bag of words representation of the sentence
        """        
        sentence_words = self.clean_up_sentence(sentence)
        bag = [0] * len(self.words)
        for w in sentence_words:
            for i, word in enumerate(self.words):
                if word == w:
                    bag[i] = 1
                    
        return np.array(bag)

    def predict(self, sentence):
        """
        Predict the class based on the sentence
        """
        bag = self.bag_of_words(sentence)
        results = self.model.predict(np.array([bag]))[0]
        ind_max = np.argmax(results)
        probability = results[ind_max]
    
        return ind_max, probability
    
if __name__ == "__main__":
    predictor = ClassPredictor()
    sentence, song_name = predictor.check_for_song_name('Do you play "Smoke on the Water"?')
    print(sentence)
