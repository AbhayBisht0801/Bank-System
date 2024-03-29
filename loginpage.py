import streamlit as st
import sqlite3 



conn=sqlite3.connect('customer.db')
c=conn.cursor()

st.header('Input Your Details')

user_name = st.text_input('Enter Your Username')
password = st.text_input('Password', type='password')  # Use type='password' to hide password input

if st.button('Login'):
    if user_name !='' and password!='':
        c.execute('SELECT * FROM Customer WHERE username=? AND password=?', (user_name, password))
        conn.commit()
        data=c.fetchall()
        if len(data)>0:
            st.session_state['user_name'] = user_name
            st.session_state['password']=password
            st.success('Login Successfull')
        else:
            st.error('No user Exist')
         # Use st.success() to display success message
else:
    st.error('Please enter your details')
conn.close()

