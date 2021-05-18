import sqlite3
import random
conn = sqlite3.connect('test1.db')
print("Opened database successfully")
global new_name,new_password,new_address,new_pin,new_quantity,new_food,status
global choice1

def volunteer_list():
      conn.execute('''CREATE TABLE VOLUNTEERS
      (ID INT PRIMARY KEY  NOT NULL,
      NAME  TEXT  NOT NULL,
      PASSWORD TEXT NOT NULL,
      ADDRESS TEXT  NOT NULL,
      PIN INT NOT NULL,
      QUANTITY INT NOT NULL,
      FOOD TEXT NOT NULL,
      STATUS TEXT NOT NULL);''')
      print("Table created successfully")
      conn.execute("INSERT INTO VOLUNTEERS (ID,NAME,PASSWORD,ADDRESS,PIN,QUANTITY,FOOD,STATUS) \
      VALUES (2309, 'Charvi','CharPES','Rajarajeshwari Nagar', 560061, 2,'VEG','AVAILABLE' )")
      conn.execute("INSERT INTO VOLUNTEERS (ID,NAME,PASSWORD,ADDRESS,PIN,QUANTITY,FOOD,STATUS) \
      VALUES (1420, 'Shivani','ShivPES','Kattirguppe', 560061, 5,'NON-VEG','UNAVAILABLE' )")
      conn.execute("INSERT INTO VOLUNTEERS (ID,NAME,PASSWORD,ADDRESS,PIN,QUANTITY,FOOD,STATUS) \
      VALUES (5612, 'Shruthi','ShruPES','Chikkalasandra', 560061, 4,'VEG','AVAILABLE' )")

volunteer_list()

def patient_list():
    conn.execute('''CREATE TABLE PATIENTS
    (ID INT PRIMARY KEY  NOT NULL,
    NAME  TEXT  NOT NULL,
    ADDRESS TEXT  NOT NULL,
    PIN INT NOT NULL,
    QUANTITY INT NOT NULL,
    FOOD TEXT NOT NULL,
    STATUS TEXT NOT NULL);''')
    conn.execute("INSERT INTO PATIENTS (ID,NAME,ADDRESS,PIN,QUANTITY,FOOD,STATUS) \
          VALUES (1298, 'Kshama','Ramanjaneya Nagar', 560061, 4,'VEG','TAKEN' )")
    conn.execute("INSERT INTO PATIENTS (ID,NAME,ADDRESS,PIN,QUANTITY,FOOD,STATUS) \
              VALUES (1328, 'Akarsh','Vidyapeetha', 560061, 3,'NON VEG','NOT TAKEN' )")
    conn.execute("INSERT INTO PATIENTS (ID,NAME,ADDRESS,PIN,QUANTITY,FOOD,STATUS) \
              VALUES (4176, 'Suraj','JP NAGAR', 560061,6,'VEG','TAKEN' )")

patient_list()
'''
def allocate_volunteer():
    sql_select_query4 = """select * from VOLUNTEERS where NAME = ?"""
    cursor = conn.cursor()
    cursor.execute(sql_select_query4, (name,))
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[3])
        print("PIN = ", row[4])
        print("QUANTITY = ",row[5])
        print("FOOD = ",row[6])
        print("STATUS = ",row[7])'''

def sign_in(name,password):

        sql_select_query3 = """select * from VOLUNTEERS  where NAME = ? AND PASSWORD = ?"""
        cursor3 = conn.cursor()
        cursor3.execute(sql_select_query3, (name, password))
        print(name)
        '''if(name == name1 and password == password1):
            allocate_volunteer()
        else:
            print("Error! Invalid username or Password")
            sign_in()'''


def registration_volunteer():
    new_name = input("Enter your name: ")
    new_password = input("Enter your password: ")
    new_address = input("Enter your address: ")
    new_pin = int(input("Enter your pin code: "))
    new_food = input("Enter veg or non veg: ")
    new_quantity = int(input("Enter the number of ppl you're ready to cook for: "))
    id = random.randint(1000,9999)
    conn.execute("INSERT INTO VOLUNTEERS (ID,NAME,PASSWORD,ADDRESS,PIN,QUANTITY,FOOD,STATUS) \
          VALUES (id,new_name,new_password,new_address,new_pin,new_quantity,new_food,'AVAILABLE' )")
    sign_in()

def create_patient():
    global p_name, p_address, p_pin, p_quantity, p_status, p_food
    p_name = input("Enter your name: ")
    p_address = input("Enter your address: ")
    p_pin = input("Enter your pin: ")
    p_food = input("Veg or Non veg: ")
    p_quantity = input("Enter number of members: ")
    p_id = random.randint(1000,9999)
    conn.execute("INSERT INTO PATIENTS (ID,NAME,ADDRESS,PIN,QUANTITY,FOOD,STATUS) \
                  VALUES (p_id, p_name,p_address,p_pin,p_quantity,p_food,'NOT TAKEN' )")
    sql_select_query5 = """select * from PATIENTS where NAME = ?"""
    cursor = conn.cursor()
    cursor.execute(sql_select_query5, (p_name,))
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[2])
        print("PIN = ", row[3])
        print("QUANTITY = ", row[4])
        print("FOOD = ", row[5])
        print("STATUS = ", row[6])

