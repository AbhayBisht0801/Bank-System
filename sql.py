import sqlite3 
conn=sqlite3.connect('customer.db')
c=conn.cursor()
c.execute('Select * from customer')
print(c.fetchall()[0])
print('Command execute Successfully')
conn.commit()
conn.close()