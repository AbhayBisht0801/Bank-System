import streamlit as st
import sqlite3 
from dotenv import load_dotenv
from langchain_community.utilities import sql_database
load_dotenv()
conn=sqlite3.connect('customer.db')
c=conn.cursor()

st.header('Input Your Details')

user_name = st.text_input('Enter Your Username')
password = st.text_input('Password', type='password')  # Use type='password' to hide password input

if st.button('Login'):
    if user_name !='' and password!='':
        c.execute('SELECT * FROM customer WHERE username=? AND password=?', (user_name, password))
        conn.commit()
        data=c.fetchall()
        if len(data)>0:
            st.success('Login Successfull')
        else:
            st.error('No user Exist')
         # Use st.success() to display success message
else:
    st.error('Please enter your details')
conn.close()

        