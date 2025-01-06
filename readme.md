# 1. Project Overview
The goal of the presented chatbot is to help navigate around my repertoire stored in a Postgres database. The chatbot itself is a simple app using mostly two approaches to gather the user's intent - keyword detection and neural network (NN) based on a bag-of-words model. The chatbot is available on {URL}.
# 2. Project Objective
While the chatbot is somewhat useful to me, it was created mostly as a portfolio project, aiming to present my programming abilities and fill some gaps in my technology stack. Since I'm not particularly interested in the frontend, I delegated it to ChatGPT - the UI is by no means perfect, but it is enough to effectively demonstrate how the chatbot works. For backend, I also used ChatGPT extensively, but only as a partner to discuss pros and cons of various approaches to the application design.
# 3. File Description
- `development/training.py` - script used to train the NN model for user's intent prediction
- `development/intents.json` - example prompt data to train the NN model
- `backend/model/chatbot_model.keras` - the trained NN model file
- `backend/model/words.pkl` - binary file with word list for the bag-of-words, required by the NN model
- `backend/categories.py` - defines Categories enum used in other files; the categories correspond to the user's intents
- `backend/categorypredictor.py` - CategoryPredictor class definition; detects proper names in the prompt and classifies them using the NN model
- `backend/Repertoire.sql` - PostgreSQL script to initialize the repertoire database
- `backend/database.py` - Database class definition; handles the database connection and formats the database query outputs accordingly
- `backend/responsegenerator.py` - ResponseGenerator class definition - the core of the chatbot; handles the conversation and keeps track of the context
- `backend/main.py` - FastAPI API, manages sessions and defines and generates responses based on the user input
- `frontend/app.py` - a simple UI made in Streamlit
# 4. Features
Below are described the key features of the application, how it works, what were the challenges, and how they were tackled.
### 4.1. Neural Network Core
The core of the chatbot is inspired by [the video by NeuralNine](https://youtu.be/1lwddP0KUEg). I manually created a couple of exemplary prompts for each of the following main categories of the user's intents:
- greetings (e.g., "Hello!")
- repertoire request (e.g., "What is your solo repertoire?")
- asking for a specific song (e.g., "Can you play "Yesterday"?")
- asking for music by a specific artist (e.g., "Do you play any songs by The Beatles?")
- asking for a specific tag (e.g., "Do you have any jazz songs in your duo repertoire?")
- thank you (e.g., "Thanks!")
- bye (e.g., "Goodbye!")

In `training.py`, the prompts are loaded and turned into a [bag-of-words model](https://en.wikipedia.org/wiki/Bag-of-words_model). Then, a neural network is trained using a simple model built in Keras, featuring a single hidden layer and softmax function on the output to return the probability of each of the intent category based on the input sentence.
### 4.2. Proper Name Detection
One of the biggest challenges in repertoire-based queries is to detect proper names such as song titles or artist names. In human interaction, this is often based on prior knowledge of a large number of respective proper names, or on a common sense - for example, if some word combination doesn't make sense in a natural language, it is likely to be some kind of a proper name. The bag-of-words approach is useless in this case, so the following rules were set:
##### 4.2.1. Song Title
The user is advised to input any song title in quotation marks (e.g. "Yesterday"). If the model finds anything in the quotation marks, it assumes it is a song title, and it replaces it with a placeholder 'song_name'.
##### 4.2.2. Artist Name
The rule for detecting the artist name is based on the natural language - usually, in the music context, the artist is mentioned after the word "by", e.g., "Can you play something by The Beatles?", "Any songs by Michael Jackson?". If the word "by" is detected, anything that comes after is assumed to be an artist name, and is replaced with a placeholder 'artist_name'.
##### 4.2.3. Tag Name
During the initialization, the model connects to the database repertoire and fetches all the tags used in the database. This includes music genres like rock, jazz, or film/play names. If any of the tags is detected, it is replaced with a placeholder 'tag_name'.

When reading the prompt, the `CategoryPredictor` defined in `categorypredictor.py` first checks for the above rules in the following order - title, artist, tag. If any of the rules applies, the proper name is saved in a separate variable, an appropriate placeholder is swapped into the sentence, and only then the sentence is converted to the bag-of-words model and uses the neural network to detect the intent category.
### 4.3. Repertoire Type Context
The user can input queries regarding my solo repertoire or repertoire with a singer - either a specific one or any of them. For each prompt, the `ResponseGenerator` checks for keywords indicating the type of repertoire the user is interested in. The repertoire context is stored in two attributes of the ResponseGenerator class - `soloduo` (either 'solo' or 'duo', corresponding to the names of the tables in Postgres) and `singer` (name of the singer or empty string). If any keywords are detected, the repertoire context is updated, otherwise it remains the same. This way, the user doesn't need to specify the type of repertoire in each prompt, only when they want to change it. The generated responses always indicate the current repertoire context.
### 4.4. Search Context
The other type of context handled by the chatbot is the search context, allowing the user to change the repertoire type while keeping track of the rest of the query. For example, after querying for something from my duo repertoire, the user can ask 'How about solo?', and the chatbot will proceed with the same query, but within a different repertoire context. It is achieved by having another context attribute of the class, named simply `context`. Every time a search request is made, the value is changed to the enum `Context.SEARCH`, and a tuple with category and extracted proper name is appended to the `context` attribute.
### 4.5 Database Search
The primary functionality of the chatbot is to search the database to answer queries related to my solo and duo repertoire. There are several possible types of database queries:
##### 4.5.1. Repertoire List
For solo and duo (with any singer) repertoire, simply returns all records from the respective tables. For a repertoire with a specific singer, the model checks their respective column in the `duo` table - if I play a song with that singer, that column includes the information on key, otherwise it is NULL. This list can be either returned directly or further filtered as described below
##### 4.5.2. Song Title Search
The model iterates over the repertoire and compares the titles (including possible alternative titles) to the song title extracted from the user's prompt using `fuzz.ratio` from the `rapidfuzz` library. If the best match is above 75 (out of 100), the model confirms to the user that I play the requested song. This approach allows for some typos in the title provided by the user. 
##### 4.5.3. Artist Search
To find songs by a given artist, the model first searches for the best matching artist using the same method as above, except the extracted artist name is possibly truncated to match the length of the compared artist name; this is useful if the prompt doesn't stop at the artist name and the simple rule of extracting everything coming after the "by" word results in overfetching, e.g., "Do you have any songs by The Beatles in your solo repertoire?". Once the correct artist name is found (best match > 75), the model returns all the songs from a repertoire where this artist is listed.
##### 4.5.4. Tag Search
All the tags are read during the initialization and then they are detected by keywording, so there is no typo allowance in this type of search. The function simply returns all songs from the repertoire featuring the requested tag.
##### 4.5.5. Ambiguous Search
If the model isn't sure what the user means with a given prompt, it will perform an ambiguous search to check if the prompt includes an artist name or a song name, which escaped the initial filtering. This way, the model has high chances to succeed even if the user doesn't bother to put quotation marks around the title or simply inputs an artist name as a prompt.
### 4.6. Misunderstandings
If the user intent is not clear to the model, and the ambiguous search doesn't return any results, the chatbot will ask the user for clarification, keeping the context. If there are two misunderstandings in a row, the user likely calls for an unfeasible action - in such a case, the model informs the user that it is unable to help them and clears the conversation context.
### 4.7. Session Management
Each time the API endpoint is called, the API checks if there are any inactive sessions (no message in 10+ minutes) and deletes them. Then it checks the user's IP using  `request.headers.get("X-Forwarded-For")`. If there is an active session for the IP, the prompt is assigned to that session, otherwise, a new session is created. This process allows for different users to use the chatbot simultaneously, as each of them has their own `ResponseGenerator` object storing the context of the conversation.

# 5. List of Technologies
- Python - main programming language
- Keras (TensorFlow) - for the core of the intent recognition
- PostgreSQL - for the repertoire database
- FastAPI - for backend API
- Streamlit - for UI
- Git/Github - for version control
- Docker - for containerization
- AWS - for cloud hosting