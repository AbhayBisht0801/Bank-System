import sqlite3 
conn=sqlite3.connect('customer.db')
c=conn.cursor()

c.execute("create table customer (Name text,username text,password text)")
c.execute("insert into customer values ('Abhay','ababhay','Abhay2001')")
conn.commit()