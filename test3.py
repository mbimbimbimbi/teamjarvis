import streamlit as st
import time

# This should be the first Streamlit command used
st.set_page_config(page_title="Team J.A.R.V.I.S.", layout="wide")

# Function to get the response from the chatbot
def get_iletisimkocu_response(message):
    responses = {
        "hi": "Hello! How can I help you today?",
        "how are you?": "I'm a bot, so I don't have feelings, but thanks for asking!",
        "bye": "Goodbye! Have a great day!"
    }
    return responses.get(message.lower(), "I'm sorry, I don't understand that.")

# Main function for the Streamlit app
def main():
    st.title("Team J.A.R.V.I.S.")

    # Initialize chat history in session state
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
        st.session_state.chat_history.append(user_message)

        # Simulate typing delay
        with st.spinner("J.A.R.V.I.S. yaziyor..."):
            time.sleep(2)

        # Get and display bot response
        bot_response = "J.A.R.V.I.S.: " + get_iletisimkocu_response(user_input)
        st.session_state.chat_history.append(bot_response)

        # Clear the user input field
        st.session_state.user_input = ""

        # Refresh the chat display
        with chat_container:
            display_chat()

# Run the main function
if __name__ == "__main__":
    main()
