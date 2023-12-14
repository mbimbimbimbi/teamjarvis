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

# Streamlit app layout
def main():
    st.title("Team J.A.R.V.I.S.")

    # Kullanıcının sorusunu sormayı tarif ettiğimiz alan burası
    user_input = st.text_input("Lütfen sorunuzu yaziniz:")
    if user_input:
        col1, col2 = st.columns(2)  # Create two columns
        with col1:  # Left column for user input
            st.text_area("User:", value=user_input, height=100, max_chars=None, key="user")


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
        with col2:  # Right column for bot response
            bot_response = get_iletisimkocu_response(user_input)
            st.text_area("Bot:", value=bot_response, height=100, max_chars=None, key="bot")

# Çalıştırma  
if __name__ == "__main__":
    main() 
