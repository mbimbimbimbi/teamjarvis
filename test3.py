import streamlit as st
import time

# This should be the first Streamlit command used
st.set_page_config(page_title="Team J.A.R.V.I.S.", layout="wide")

# Function to get the response from the chatbot
def get_iletisimkocu_response(message):
    responses = {
        "hi": "Hello! How can I help you today?",
        "how are you?": "I'm a bot, so I don't have feelings, but thanks for asking!",
        "bye": "Goodbye! Have a great day!",
        "greetings": "Greetings! What can I do for you?"
    }
    return responses.get(message.lower(), "I'm sorry, I don't understand that.")

# Main function for the Streamlit app
def main():
    st.title("Team J.A.R.V.I.S.")

    # Initialize chat history and reset trigger in session state
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    # Function to display the chat history
    def display_chat():
        for message in st.session_state.chat_history:
            st.text(message)

    # Chat container for history
    chat_container = st.container()
    with chat_container:
        display_chat()

    # User input and submit button
    user_input = st.text_input("Kullanıcı", placeholder="Lütfen sorunuzu yazınız", key="user_input")

    submit_button = st.button("Send")

    # Handling user input when the button is clicked
    if submit_button and user_input:
        user_message = "Kullanici: " + user_input
        bot_response = "J.A.R.V.I.S.: " + get_iletisimkocu_response(user_input)

        # Update chat history
        st.session_state.chat_history.extend([user_message, bot_response])

        # Clear the user input field
        st.session_state.user_input = ""

        # Refresh the chat display
        with chat_container:
            display_chat()

# Run the main function
if __name__ == 
