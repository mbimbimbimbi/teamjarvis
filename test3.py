import streamlit as st
import time

# Set the page config as the first thing in your script
st.set_page_config(page_title="Team J.A.R.V.I.S.", layout="wide")

def get_iletisimkocu_response(message):
    responses = {
        "hi": "Hello! How can I help you today?",
        "how are you?": "I'm a bot, so I don't have feelings, but thanks for asking!",
        "bye": "Goodbye! Have a great day!"
    }
    return responses.get(message.lower(), "I'm sorry, I don't understand that.")


def main():
    st.set_page_config(page_title="Team J.A.R.V.I.S.", layout="wide")
    st.title("Team J.A.R.V.I.S.")

    # Initialize session state for chat history and user input
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []
    if 'user_input' not in st.session_state:
        st.session_state.user_input = ""

    # Display chat history
    def display_chat():
        for message in st.session_state.chat_history:
            st.text(message)

    # User input at the bottom
    user_input = st.text_input("Kullanıcı", placeholder="Lütfen sorunuzu yazınız", key="user_input", value=st.session_state.user_input)

    # Chat container for history
    chat_container = st.container()

    with chat_container:
        display_chat()

    # When user sends a message
    if user_input:
        user_message = "Kullanici: " + user_input
        st.session_state.chat_history.append(user_message)

        # Simulate typing
        with st.spinner("J.A.R.V.I.S. yaziyor..."):
            time.sleep(2)

        # Get and display response
        bot_response = "J.A.R.V.I.S.: " + get_iletisimkocu_response(user_input)
        st.session_state.chat_history.append(bot_response)

        # Clear input box and update chat
        st.session_state.user_input = ""
        display_chat()

if __name__ == "__main__":
    main()
