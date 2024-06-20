import sqlite3
import streamlit as st

def app():
    user_name = st.session_state.get('user_name')
    password = st.session_state.get('password')
    receiver_account_no = st.text_input('Enter receiver\'s account no:')
    receiver_name = st.text_input('Enter receiver\'s name:')
    amount = st.number_input('Enter amount to transfer:', min_value=0)
    if st.button('Transfer'):
        if user_name!='' and password!='':
            conn = sqlite3.connect('customer_database.db')
            c = conn.cursor()

            # Check if the user exists
            c.execute('SELECT * FROM Customer WHERE username=? AND password=?', (user_name, password))
            
            user_data = c.fetchone()
       
            if len(user_data)>0:
                
                # Check if the receiver's account exists
                c.execute('SELECT * FROM Customer WHERE AccountNo=? AND name=?', (receiver_account_no, receiver_name))
                receiver_data = c.fetchone()

                if receiver_data:
                    # Update balances
                    sender_balance = user_data[-1] - amount
                    receiver_balance = receiver_data[-1] + amount
                    s_acc_no = user_data[0]

                    c.execute('UPDATE Customer SET Balance=? WHERE username=?', (sender_balance, user_name))
                    c.execute('UPDATE Customer SET Balance=? WHERE AccountNo=?', (receiver_balance, receiver_account_no))
                    c.execute("insert into 'Transaction' values (?,?,?,?,?)",(receiver_account_no,receiver_name,amount,user_data[-1],user_data[0]))
                    conn.commit()

                    st.success(f'Transaction successful! Your new balance: {sender_balance}')
                else:
                    st.error('Receiver account not found.')
        else:
            st.error('Invalid username or password.')

        conn.close()

if __name__ == '__main__':
    st.header('Banking System')
    app()
