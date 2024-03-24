import streamlit as st
from dotenv import load_dotenv
import tkinter as tk
load_dotenv()
def main():
    load_dotenv()
    st.set_page_config(page_title='Chatbot for customer Service',page_icon=':bank:')
    st.header('Ask Your Queries')
    message=st.chat_message('assistant')
    message.write('Hello How can I help you?')
    message1=st.chat_message('Customer')
    
    option = message1.radio("Choose an option:", ("Bank Balance", "Credit Score", "Insurance Settlement"))

    if option == "Bank Balance":
        st.info("Tenzin lodu")
    elif option == "Credit Score":
        st.info("Here's information about credit score...")
    elif option == "Insurance Settlement":
        st.file_uploader('Upload Car Number Plate Image and Damage Image',type=['jpg','png'])
  







if __name__=='__main__':
    main()