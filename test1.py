import streamlit as st

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

    # Set the page to wide mode for better chat layout
    st.set_page_config(page_title="Team J.A.R.V.I.S.", layout="wide")
    
    st.title("Team J.A.R.V.I.S.")

    
    # Chat container
    chat_container = st.container()

    # Kullanıcının sorusunu sormayı tarif ettiğimiz alan burası
    user_input = st.text_input("Lütfen sorunuzu yaziniz:")

    # Kullanıcı soru sordugunda
    if user_input:
        # Kullanıcının mesajını gösterir
        with chat_container:
            col1, col2 = st.columns([1, 1])
            with col1:
                st.text_area("Kullanici:", value=user_input, height=100, max_chars=None, key="kullanici")

        # Yazı yazma efekti
            with st.spinner("J.A.R.V.I.S. yaziyor..."):
                time.sleep(2)  # yazı yazma efektini göstermek için birkaç saniyelik pause

        # iletisim kocunun cevabını alma ve gosterme
        bot_response = get_iletisimkocu_response(user_input)
        with chat_container:
            col1, col2 = st.columns([1, 1])
            with col2:
                st.text_area("J.A.R.V.I.S.:", value=bot_response, height=100, max_chars=None, key="J.A.R.V.I.S.")
        
# Çalıştırma  
if __name__ == "__main__":
    main() 
