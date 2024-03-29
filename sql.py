import sqlite3 
conn=sqlite3.connect('customer.db')
c=conn.cursor()

def get_schema(conn):
    c = conn.cursor()
    c.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = c.fetchall()
    schema = {}
    for table in tables:
        table_name = table[0]
        c.execute("PRAGMA table_info({})".format(table_name))
        columns = c.fetchall()
        schema[table_name] = [col[1] for col in columns]
    return schema
schema = get_schema(conn)
print(schema)
conn.commit()
conn.close()