import json
import random
import pickle
import numpy as np
import difflib

import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD

# load the file with the training data
intents = json.loads(open('intents.json').read())

# initialize lists
words = []      # list of all words
categories = []    # list of all categories
documents = []  # list of tuples (words, corresponding category)
ignore_letters = ['?', '!', ',', '.']

# iterate over the JSON file to create documents
for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_list = nltk.word_tokenize(pattern)
        words.extend(word_list)
        documents.append((word_list, intent['category']))
        if intent['category'] not in categories:
            categories.append(intent['category'])

# lemmatize the word list and delete repeating items
lemmatizer = WordNetLemmatizer()
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_letters]
words = sorted(set(words))

# save the words to binary file
with open('model/words.pkl', 'wb') as words_file:
    pickle.dump(words, words_file)

# transform training data to numerical form    
training = []
output_empty = [0] * len(categories)

# iterate over the documents to change the character of the data from text to binary
for document in documents:
    bag = []
    word_patterns = document[0]
    word_patterns = [lemmatizer.lemmatize(word.lower()) for word in word_patterns]
    for word in words:
        # mark the indices of the words used
        bag.append(1) if word in word_patterns else bag.append(0)   

    # mark the index of the class (tag)    
    output_row = output_empty.copy()
    output_row[categories.index(document[1])] = 1  
    training.append([bag, output_row])

# shuffle the training data
random.shuffle(training)   

# prepare the data for training
train_x = []
train_y = []

for item in training:           
    train_x.append(item[0])
    train_y.append(item[1])
    

# build a model
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(32, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# compile the model
sgd = SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

# train the model
model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save('model/chatbot_model.keras')
print("Done")

# check if the category list matches the enum in categorypredictor.py
from categories import categorylist
if [category.upper() for category in categories] != categorylist:
    print("\n Warning: Category list doesn't match the category enum defined categorypredictor!")
    diff = difflib.ndiff([c.upper() for c in categories], categorylist)
    print("\n".join(diff))
    
    