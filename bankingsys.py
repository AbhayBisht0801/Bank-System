import sqlite3
import streamlit as st
import pickle
from src.Banking_System.utils.common import load_object
import numpy as np
import os
import pandas as pd
conn = sqlite3.connect('customer_database.db')

def load_model(path):
    return load_object(path)

def authenticate_user(conn, username, password):
    c = conn.cursor()
    c.execute('SELECT * FROM Customer WHERE username=? AND password=?', (username, password))
    return c.fetchone()

def check_receiver_exists(conn, receiver_account_no, receiver_name):
    c = conn.cursor()
    c.execute('SELECT * FROM Customer WHERE AccountNo=? AND name=?', (receiver_account_no, receiver_name))
    return c.fetchone()

def update_balances(conn, sender_username, sender_balance, receiver_account_no, receiver_balance):
    c = conn.cursor()
    c.execute('UPDATE Customer SET Balance=? WHERE username=?', (sender_balance, sender_username))
    c.execute('UPDATE Customer SET Balance=? WHERE AccountNo=?', (receiver_balance, receiver_account_no))
    conn.commit()

def record_transaction(conn, R_account_name, R_account_no, amount, sender_balance, S_customer_id , is_fraud):
    c = conn.cursor()
    c.execute("INSERT INTO 'Transaction' (R_account_name, R_account_no,Rec_amount, Bank_bal, S_customer_id , is_fraud) VALUES (?,?,?,?,?,?)", 
              (R_account_name, R_account_no, amount, sender_balance, S_customer_id , is_fraud))
    conn.commit()

def app():
    paths = 'artifacts\\data_ingestion\\transaction_data\\incoming_transaction.csv'
    user_name = st.session_state.get('user_name', '')
    password = st.session_state.get('password', '')
    fraud_model_path = 'artifacts\\training\\transaction_model.pkl'
    
    model = load_model(fraud_model_path)

    if user_name and password:  # Simplified condition
        user_data = authenticate_user(conn, user_name, password)
       
        if user_data is not None:  # User exists
            receiver_account_no = st.text_input("Enter receiver's account no:")
            receiver_name = st.text_input("Enter receiver's name:")
            amount = st.number_input("Enter amount to transfer:", min_value=0)
            
            if st.button('Transfer'):
                st.session_state['transfer_clicked'] = True  # Track that Transfer button was clicked
                st.session_state['receiver_account_no'] = receiver_account_no
                st.session_state['receiver_name'] = receiver_name
                st.session_state['amount'] = amount

            if st.session_state.get('transfer_clicked', False):
                if amount > user_data[-1]:
                    st.error('Insufficient balance')
                else:
                    receiver_data = check_receiver_exists(conn, receiver_account_no, receiver_name)
            
                    if receiver_data is not None:  # Receiver exists
                        sender_balance = user_data[-1] - amount
                        receiver_balance = receiver_data[-1] + amount
                        s_acc_no = user_data[4]
                        print(s_acc_no)
                        sender_id=user_data[0]
                        input_data = np.array([amount, user_data[-1], sender_balance]).reshape(1, -1)
                        pred = model.predict(input_data)
                
                        if pred == 0:
                            update_balances(conn, user_name, sender_balance, receiver_account_no, receiver_balance)
                            record_transaction(conn,  receiver_name,receiver_account_no, amount, sender_balance, sender_id, 0)
                            st.success(f'Transaction successful! Your new balance: {sender_balance}')
                        else:
                            Account_Number = st.text_input("Enter your Account Number")
                            print(Account_Number)
                            if st.button('Submit'):
                                st.session_state['submit_clicked'] = True  # Track that Submit button was clicked
                                st.session_state['Account_Number'] = Account_Number
                                print(int(Account_Number) == int(s_acc_no))
                            if st.session_state.get('submit_clicked',True):
                            
                                if int(Account_Number) == int(s_acc_no):
                                    update_balances(conn, user_name, sender_balance, receiver_account_no, receiver_balance)
                                    record_transaction(conn, receiver_name,receiver_account_no, amount, sender_balance, sender_id, 0)
                                    st.success(f'Transaction successful! Your new balance: {sender_balance}')
                                else:
                                    st.error('Invalid Account Number')
                                    record_transaction(conn, receiver_name,receiver_account_no, amount, sender_balance, sender_id, 1)
                                    st.session_state['user_name'] = ''
                                    st.session_state['password'] = ''
                                    st.session_state['transfer_clicked'] = False
                                    st.session_state['submit_clicked'] = False
                                    st.experimental_rerun()

                    else:
                        st.error('Receiver account not found.')
        else:
            st.error('Invalid username or password.')
    else:
        st.warning('Please Login First')
    
    conn.close()

if __name__ == '__main__':
    st.header('Banking System')
    app()
