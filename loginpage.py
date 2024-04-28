import streamlit as st
import sqlite3 
from dotenv import load_dotenv
from langchain_community.utilities import sql_database

load_dotenv()
if 'user_name' not in st.session_state:
    st.session_state['user_name'] = ''
if 'password' not in st.session_state:
    st.session_state['password'] = ''

def process_login(user_name, password, c, conn):
    if user_name != '' and password != '':
        c.execute('SELECT * FROM Customer WHERE username=? AND password=?', (user_name, password))
        conn.commit()
        data = c.fetchall()
        conn.close()
        if len(data) > 0:
            st.success('Login Successful')
            st.session_state['user_name'] = user_name
            st.session_state['password'] = password
            # You can perform further actions here based on the successful login
        else:
            st.error('Please Enter Your Correct Details.')
            st.session_state['user_name'] = ''
            st.session_state['password'] = ''
    else:
        st.error('Please enter your details')

def app():
    conn = sqlite3.connect('customer_database.db')
    c = conn.cursor()

    st.header('Input Your Details')

    if 'user_name' not in st.session_state:
        st.session_state['user_name'] = ''
    if 'password' not in st.session_state:
        st.session_state['password'] = ''

    user_name = st.text_input('Enter Your Username', value=st.session_state['user_name'])
    password = st.text_input('Password', type='password', value=st.session_state['password'])

    

    if st.button('Login'):
        process_login(user_name, password, c, conn)
        
    if st.button('Logout'):
        st.session_state['user_name'] = ''
        st.session_state['password'] = ''

if __name__ == '__main__':
    app()
