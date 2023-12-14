import streamlit as st
# Koyu tema
##st.set_page_config(layout="wide", page_title="Team J.A.R.V.I.S.", page_icon="🤖", theme="dark")

import time

# İletişim koçunun(iletisimkocu) oluşturduğu cevabı buradan alıyoruz. Şimdilik random cevaplar ekledim, fakat buraya iletişim koçunun API'nı bağlamak gerekiyor
def get_iletisimkocu_response(message):
    responses = {
        "hi": "Hello! How can I help you today?",
        "how are you?": "I'm a bot, so I don't have feelings, but thanks for asking!",
        "bye": "Goodbye! Have a great day!"
    }
    # Konu dışı konuları da buradan ayarlamamız gerekecek, fakat bunu iletisimkocundan mı yapmak gerek yoksa router agent'tan mı yapmak gerek bunu bir düşünelim belki buraya ilave bir katman gerekebilir
    return responses.get(message.lower(), "I'm sorry, I don't understand that.")

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Initialize a flag to keep track of the first question
if 'first_question_asked' not in st.session_state:
    st.session_state['first_question_asked'] = False

# Streamlit app layout
def main():
    st.title("Team J.A.R.V.I.S.")
    

    # Kullanıcının sorusunu sormayı tarif ettiğimiz alan burası
    user_input = st.text_input("Lütfen sorunuzu yaziniz:")

     # Only show the prompt before the first question is asked
    if not st.session_state['first_question_asked']:
        user_input = st.text_input("Lütfen sorunuzu yazınız:", key="user_input")
    else:
        user_input = st.text_input("", key="user_input")

    if user_input:
        # Set the flag to True as the first question has been asked
        st.session_state['first_question_asked'] = True

        # Append user message to chat history without the "User" label
        st.session_state['chat_history'].append(user_input)

        # Get bot response and append to chat history without the "Bot" label
        bot_response = get_chatbot_response(user_input)
        st.session_state['chat_history'].append(bot_response)

        # Clear the input box after the message is sent
        st.session_state.user_input = ""

    # Display chat history
    for message in st.session_state['chat_history']:
        st.text(message)

   
    # Kullanıcı soru sordugunda
    if user_input:
        # Kullanıcının mesajını gösterir
        st.text_area("Kullanici:", value=user_input, height=100, max_chars=None, key="kullanici")

        # Yazı yazma efekti
        with st.spinner("J.A.R.V.I.S. yaziyor..."):
            time.sleep(2)  # yazı yazma efektini göstermek için birkaç saniyelik pause

        # iletisim kocunun cevabını alma ve gosterme
        bot_response = get_iletisimkocu_response(user_input)
        st.text_area("J.A.R.V.I.S.:", value=bot_response, height=100, max_chars=None, key="J.A.R.V.I.S.")
        
# Çalıştırma  
if __name__ == "__main__":
    main() 
