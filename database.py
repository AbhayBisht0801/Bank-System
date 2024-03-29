import sqlite3

conn = sqlite3.connect('customer_data.db')
c = conn.cursor()

# Create Customer table
c.execute('''CREATE TABLE Customer (
                    customer_id INTEGER PRIMARY KEY,
                    name TEXT,
                    username TEXT,
                    password TEXT,
                    Age INTEGER,
                    Income INTEGER,
                    Education TEXT,
                    NumChildren INTEGER,
                    Gender TEXT,
                    MaritalStatus TEXT,
                    HomeOwnership_Rented TEXT,
                    Balance INTEGER
                )''')
c.execute("""INSERT INTO Customer values (1,'Alice', 'alice123', 'password1', 30, 50000, "Bachelor's Degree", 1, 'Female', 'Married', 'Owned', 2000),
    (2,'Bob', 'bob456', 'password2', 40, 60000, "Master's Degree", 2,  'Male', 'Single', 'Rented', 3000),
    (3,'Charlie', 'charlie789', 'password3', 35, 55000, "Bachelor's Degree", 0,  'Male', 'Divorced', 'Rented', 1000),
    (4,'David', 'david001', 'password4', 45, 70000, 'Doctorate', 3,  'Male', 'Married', 'Owned', 4000),
    (5,'Emma', 'emma007', 'password5', 28, 48000, 'High School Diploma', 1,  'Female', 'Single', 'Owned', 1500)""")
# Create InsuranceType table
c.execute('''CREATE TABLE InsuranceType(
                    insurance_type_id INTEGER PRIMARY KEY,
                    Insurance_NAME TEXT,
                    crack_covered INTEGER,
                    dent_covered INTEGER,
                    glassshatter_covered INTEGER,
                    lampbroken_covered INTEGER,
                    scratch_covered INTEGER,
                    tireflat_covered INTEGER
                )''')
c.execute("""insert  into InsuranceType values (1,'Type1_Insurance',0,1,0,1,1,0),(2,'Type2_Insurance',1,1,0,1,1,1),(3,'Type3_Insurance',1,1,1,1,1,1)""")

# Create Insurance table
c.execute('''CREATE TABLE Insurance (
                    insurance_id INTEGER PRIMARY KEY,
                    customer_id INTEGER,
                    insurance_type_id INTEGER,
                    car_number_plate TEXT,
                    FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
                    FOREIGN KEY (insurance_type_id) REFERENCES InsuranceType(insurance_type_id)
                )''')
c.execute("""insert into Insurance values (1,2,3,'BJ69 HED'),(2,5,1,'HZ13 WWD')""")


conn.commit()
conn.close()
