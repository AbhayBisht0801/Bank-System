import streamlit as st
from dotenv import load_dotenv
import tkinter as tk
from sklearn.preprocessing import OrdinalEncoder
import sqlite3
load_dotenv()
import numpy as np
from PIL import Image
import pandas as pd
from src.Banking_System.utils.common import load_object,model_prediction
from keras.models import load_model
from chat_withsql import get_gemini_response,prompt,read_sql_query
cnn_model=load_model('artifacts\\training\car_model.h5')
credit_score=load_object('artifacts\\training\creditscore_model.pkl')
label_encoder=load_object('artifacts\data_ingestion\preprocess\encodelabelcredit.pkl')
ordinal_encoder=load_object

labels=a={'crack': 0,
 'dent': 1,
 'glass shatter': 2,
 'lamp broken': 3,
 'scratch': 4,
 'tire flat': 5}
 
def app():
    user_name = st.session_state.get('user_name')
    password = st.session_state.get('password')
    if user_name != "" and password != "":
        st.header('Ask Your Queries')
        message = st.chat_message('assistant')
        message.write('Hello! How can I help you?')
        message1 = st.chat_message('Human')
        
        option = message1.radio("Choose an option:", ("Bank Balance", "Credit Score", "Insurance Settlement","Other"))

        if option == "Bank Balance":
            conn = sqlite3.connect('customer_data.db')
            cur = conn.cursor()
            cur.execute('SELECT Balance FROM Customer WHERE username=? AND password=?', (user_name, password))
            conn.commit()
            data=cur.fetchall()
            balance = data
            st.write('The Balance in your Account is {}'.format(balance))
            conn.close()
            
        elif option == "Credit Score":
            conn = sqlite3.connect('customer_data.db')
            cur = conn.cursor()
            cur.execute('SELECT * FROM Customer WHERE username=? AND password=?', (user_name, password))
            conn.commit()
            data = cur.fetchall()
            conn.close()
            data1 = list(data[0])
            indexs = [0, 1, 2, 3, 11]
            data1 = [value for index, value in enumerate(data1) if index not in indexs]
            pred_data = pd.DataFrame([data1], columns=['Age', 'Income', 'Education', 'Number of Children', 'Gender', 'Marital Status', 'Home Ownership'])
            pred_data.replace({'Male': True, 'Female': False, 'Single': True, 'Married': False, 'Owned': False, 'Rented': True}, inplace=True)
            oe = OrdinalEncoder(categories=[['High School Diploma', "Associate's Degree", "Bachelor's Degree", "Master's Degree", 'Doctorate']])
            pred_data['Education'] = oe.fit_transform(pred_data[['Education']])
            data_pred = pred_data.to_numpy()
            prediction = credit_score.predict([data_pred[0]])
            
            
            
            st.write('Your credit score is {}'.format(label_encoder.inverse_transform(prediction)[0]))
            
        elif option == "Insurance Settlement":
            Car_damage_image = st.file_uploader('Upload Car damage image', type=['jpg', 'png'])
            if Car_damage_image:
                img = Image.open(Car_damage_image)
                prediction = np.argmax(model_prediction(img, cnn_model),axis=1)
                
                damage=None
                for key, value in a.items():
                    if value == prediction[0]:
                        damage=key
                response=get_gemini_response(prompt[0],f'Does Customer with username  {user_name} and password {password} have a insurance in Insurance Table if yes then check and does that insurance  cover the {damage}.show two boolean value one does a person have car insurance and other is does it cover the {damage} in InsuranceType')
                data=read_sql_query(response,'customer_data.db')
                if data[0][0]==0:
                    st.warning('Sir/Madam you dont have a Car Insurance')
                elif data[0][0]==1:
                    if data[0][1]==0:
                        st.warning(f'Sir/Madam The Car Insurance Does not cover the damage of {damage}')
                    else:
                        st.success(f'Sir/Madam The Car Insurance  cover the damage of {damage}.Our team will contact you for further enquiry')
                        
            else:
                st.error("Please upload an image.")
        elif option =='Other':
            st.write('Please Contact our team for other queries')
        if st.button("Refresh Page"):
                
            st.experimental_rerun()
            

    else:
        st.error('Please Login First')
        

            

  







if __name__=='__main__':
    app()