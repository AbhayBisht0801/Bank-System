import sqlite3

def CreateAccount():
        con = sqlite3.connect('customer_database.db')
        c = con.cursor()
        
        c.execute('''CREATE TABLE if not exists Customer (
                    customer_id INTEGER PRIMARY KEY,
                    name TEXT,
                    username TEXT,
                    password TEXT,
                    AccountNo INTEGER,
                    Age INTEGER,
                    Gender TEXT,
                    Income INTEGER,
                    Education TEXT,
                    MaritalStatus TEXT,
                    NumChildren INTEGER,
                    HomeOwnership_Rented TEXT,
                    Balance INTEGER
                )''')
        c.execute("""INSERT INTO Customer values (1,'Alice', 'alice123', 'password1',3333333, 30,'Female', 50000, "Bachelor's Degree",  'Married',1, 'Owned', 2000),
            (2,'Bob', 'bob456', 'password2',3333334, 40,'Male', 60000, "Master's Degree",'Single', 2, 'Rented', 3000),
            (3,'Charlie', 'charlie789', 'password3',3333335, 35,'Male', 55000, "Bachelor's Degree",'Single', 0, 'Rented', 1000),
            (4,'David', 'david001', 'password4',3333337, 45,'Male', 70000, 'Doctorate','Married', 3, 'Owned', 4000),
            (5,'Emma', 'emma007', 'password5',3333338, 28,'Female', 48000, 'High School Diploma','Single', 1, 'Owned', 1500)""")
# Create InsuranceType table
        c.execute("""create table if not exists "Transaction" (
                       R_account_name text,
                       R_account_no integer,
                       Rec_amount integer,
                       Bank_bal integer,
                       S_customer_id Integer
        )""")

        c.execute('''CREATE TABLE InsuranceType(
                            insurance_type_id INTEGER PRIMARY KEY, 
                            Insurance_NAME TEXT ,
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
                            insurance_type_id Int,
                            car_number_plate TEXT,
                            FOREIGN KEY (customer_id) REFERENCES Customer(customer_id),
                            FOREIGN KEY (insurance_type_id) REFERENCES InsuranceType(insurance_type_id)
                        )''')
        c.execute("""insert into Insurance values (1,2,3,'BJ69 HED'),(2,5,1,'HZ13 WWD')""")


        #
        con.commit()
        c.close()
if __name__=='__main__':
        CreateAccount()
