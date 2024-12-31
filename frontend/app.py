import streamlit as st
import requests

# Set the API URL
API_URL = "http://backend:80/generate-response/"

# Configure the page layout
st.set_page_config(page_title="Chatbot Interface", layout="wide")

# Title of the app
st.title("Repertoire Chatbot")

# Information text
info_text = """
I play a wide variety of songs and pieces both solo, as a fingerstyle guitarist, and in a duo with singers (Dominika, Sara, and Ania). 
This chatbot is meant to help you navigate around my repertoire - you can ask for a specific song, artist, or genre, or request the entire repertoire - 
all of that either solo or as a duo (in general or with a specific singer). Song titles are more likely to be properly detected when put in quotation marks, e.g. "Yesterday".
"""

# Display the information text
st.markdown(info_text)

# Initialize session state for conversation history
if "messages" not in st.session_state:
    st.session_state.messages = []


# Define CSS for chat messages
custom_css = """
<style>
.message {
    padding: 10px;
    border-radius: 10px;
    margin-bottom: 10px;
    max-width: 70%;
    clear: both;
    color: #fff; /* White text color */
}
.user {
    background-color: #388e3c; /* Darker green */
    float: right;
    text-align: right;
}
.bot {
    background-color: #616161; /* Darker gray */
    float: left;
    text-align: left;
}
.error {
    background-color: #d32f2f; /* Darker red */
    float: left;
    text-align: left;
}
</style>
"""

# Inject custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Render chat messages directly
for msg in st.session_state.messages:
    formatted_message = msg["message"].replace('\n', '<br>')
    
    if msg["sender"] == "You":
        st.markdown(
            f"""
            <div class="message user">
                <strong>You:</strong><br>
                {formatted_message}
            </div>
            """,
            unsafe_allow_html=True,
        )
    elif msg["sender"] == "Bot":
        st.markdown(
            f"""
            <div class="message bot">
                <strong>Bot:</strong><br>
                {formatted_message}
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="message error">
                <strong>{msg["sender"]}:</strong><br>
                {formatted_message}
            </div>
            """,
            unsafe_allow_html=True,
        )

# Spacer to push the input form to the bottom
st.markdown("<br><br>", unsafe_allow_html=True)


# Create a form for user input at the bottom
with st.form(key="chat_form", clear_on_submit=True):
    col1, col2, col3 = st.columns([1, 6, 1])
    with col1:
        st.write("")
    with col2:
        user_input = st.text_input("You:", "", key="input")
    with col3:
        submit_button = st.form_submit_button(label="Send")
    


# Handle form submission
if submit_button and user_input.strip():
    # Append user message to the conversation history
    st.session_state.messages.append({"sender": "You", "message": user_input.strip()})
    
    try:
        # Send a POST request to the FastAPI endpoint with the user input
        response = requests.post(API_URL, json={"sentence": user_input.strip()})
        
        # Check if the request was successful
        if response.status_code == 200:
            # Extract the chatbot's response from the JSON data
            bot_response = response.json().get("response", "No response received.")
            
            # Append bot response to the conversation history
            st.session_state.messages.append({"sender": "Bot", "message": bot_response})
        else:
            # Append error message to the conversation history
            st.session_state.messages.append({
                "sender": "Error",
                "message": f"Error {response.status_code}: {response.text}"
            })
    except requests.exceptions.RequestException as e:
        # Append exception error message to the conversation history
        st.session_state.messages.append({
            "sender": "Error",
            "message": f"An error occurred: {e}"
        })
    
    # After appending messages, rerun to update the UI
    st.rerun()
elif submit_button and not user_input.strip():
    # Warn the user if the input box is empty but the send button was pressed
    st.warning("Please enter a message.")
    