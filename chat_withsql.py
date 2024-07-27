import sqlite3 
from sql import schema

import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt,question])
    return response.text
def read_sql_query(sql,connection):
    conn=connection
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    return rows
prompt=["""Your are an expert in Converting English question to SQL query!
    The DataBase with tables Customer table with columns as follows customer_id', 'name', 'username',
      'password', 'Age', 'Income', 'Education', 'NumChildren',  'Gender', 'MaritalStatus', 'HomeOwnership_Rented', 'Balance' and other table is InsuranceType with columns
        as follows'insurance_type_id', 'Insurance_NAME', 'crack_covered', 'dent_covered', 'glassshatter_covered', 'lampbroken_covered', 'scratch_covered', 'tireflat_covered',
        and another table Insurance with columns as follow'insurance_id', 'customer_id', 'insurance_type_id', 'car_number_plate'.
        \nExample 1 - Tell me the number of Customer in Customer table?, 
    the SQL command will be something like this SELECT count(*) FROM Customer; 
    also the sql code should not have ``` in beginning or end and sql word in output
        
 """]


