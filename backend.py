import sqlite3
import random

print("Opened database successfully")
global new_name, new_password, new_address, new_pin, new_quantity, new_food, status, new_no
global p_name, p_address, p_pin, p_quantity, p_status, p_food
global choice1
global id


def volunteer_list():
    conn = sqlite3.connect('test1.db')
    c = conn.cursor()
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='VOLUNTEERS' ''')

    # if the count is 1, then table exists
    if c.fetchone()[0] == 1:
        print('Table exists')
    else:
        conn.execute('''CREATE TABLE VOLUNTEERS
        (ID INT PRIMARY KEY  NOT NULL,
        NAME  TEXT  NOT NULL,
        PASSWORD TEXT NOT NULL,
        ADDRESS TEXT  NOT NULL,
        PIN INT NOT NULL,
        QUANTITY INT NOT NULL,
        FOOD TEXT NOT NULL,
        STATUS TEXT NOT NULL,
        NUMBER INT NOT NULL);''')
        print("Table created successfully")
        conn.execute("INSERT INTO VOLUNTEERS (ID,NAME,PASSWORD,ADDRESS,PIN,QUANTITY,FOOD,STATUS,NUMBER) \
                VALUES (2309, 'Charvi','CharPES','Rajarajeshwari Nagar', 560061, 2,'VEG','AVAILABLE',9876543210 )")
        conn.commit()
    conn.close()





def patient_list():
    conn = sqlite3.connect('test1.db')
    c = conn.cursor()
    c.execute(''' SELECT count(name) FROM sqlite_master WHERE type='table' AND name='PATIENTS' ''')

    # if the count is 1, then table exists
    if c.fetchone()[0] == 0:
        conn.execute('''CREATE TABLE PATIENTS
        (ID INT NOT NULL,
        NAME  TEXT  NOT NULL,
        ADDRESS TEXT  NOT NULL,
        PIN INT NOT NULL,
        QUANTITY INT NOT NULL,
        FOOD TEXT NOT NULL,
        STATUS TEXT NOT NULL,
        NUMBER INT NOT NULL);''')
        conn.execute("INSERT INTO PATIENTS (ID,NAME,ADDRESS,PIN,QUANTITY,FOOD,STATUS,NUMBER) \
          VALUES (2387,'Kshama','Ramanjaneya Nagar', 560061, 4,'VEG','NOT TAKEN',9876543210 )")
        conn.execute("INSERT INTO PATIENTS (ID,NAME,ADDRESS,PIN,QUANTITY,FOOD,STATUS,NUMBER) \
              VALUES (6348,'Akarsh','Vidyapeetha', 560063, 3,'NON VEG','NOT TAKEN',9876543210 )")
        conn.execute("INSERT INTO PATIENTS (ID,NAME,ADDRESS,PIN,QUANTITY,FOOD,STATUS,NUMBER) \
              VALUES (2075,'Suraj','JP NAGAR', 560061,6,'VEG','TAKEN',9876543210 )")
        conn.commit()
    conn.close()


patient_list()
'''
def allocate_volunteer():
    sql_select_query4 = """select * from VOLUNTEERS where NAME = ? and PASSWORD = ?"""
    cursor = conn.cursor()
    cursor.execute(sql_select_query4, (name,password))
    for row in cursor:
        print("ID = ", row[0])
        print("NAME = ", row[1])
        print("ADDRESS = ", row[3])
        print("PIN = ", row[4])
        print("QUANTITY = ",row[5])
        print("FOOD = ",row[6])
        print("STATUS = ",row[7])'''


def sign_in(name,password):
    conn = sqlite3.connect('test1.db')
    cursor3 = conn.cursor()
    cursor3.execute("SELECT * FROM VOLUNTEERS WHERE name = ? AND PASSWORD = ?", (name, password))
    data = cursor3.fetchall()
    if len(data) != 0:
            sql_select_query4 = """select * from VOLUNTEERS where NAME = ? and PASSWORD = ?"""
            cursor = conn.cursor()
            cursor.execute(sql_select_query4, (name, password))
            return True

    else:
        return False
        '''for row in cursor3:
            name1 = row[1]
            password1 = row[2]
        if(name == name1 and password == password1):
            allocate_volunteer()
        else:
            print("Error! Invalid username or Password")
            sign_in()'''



def registration_volunteer(new_name,new_password,new_no,new_address,new_pin,new_food,new_quantity):
    conn = sqlite3.connect('test1.db')
    id = random.randint(1000, 9999)
    conn.execute("INSERT OR IGNORE INTO VOLUNTEERS (ID,NAME,PASSWORD,ADDRESS,PIN,QUANTITY,FOOD,STATUS,NUMBER)\
                VALUES(?,?,?,?,?,?,?,?,?)",
                 [id, new_name, new_password, new_address, new_pin, new_quantity, new_food, 'AVAILABLE', new_no])
    conn.commit()
    print("Registered successfully")

    conn.close()


def create_patient(p_name,p_address,p_pin,p_food,p_quantity,p_no):
    conn = sqlite3.connect('test1.db')
    conn.execute("INSERT OR IGNORE INTO PATIENTS (ID,NAME,ADDRESS,PIN,QUANTITY,FOOD,STATUS,NUMBER)\
                    VALUES(?,?,?,?,?,?,?,?)",
                 [1, p_name, p_address, p_pin, p_quantity, p_food, 'NOT TAKEN', p_no])
    conn.commit()
    sql_select_query5 = """select * from PATIENTS where NAME = ?"""
    cursor = conn.cursor()
    cursor.execute(sql_select_query5, (p_name,))
    for row in cursor:
        print("NAME = ", row[0])
        print("ADDRESS = ", row[1])
        print("PIN = ", row[2])
        print("QUANTITY = ", row[3])
        print("FOOD = ", row[4])
        print("STATUS = ", row[5])
        print("NUMBER = ", row[6])
    conn.close()


'''
choice = input("Volunteer or Patient: ")
if(choice == "Volunteer"):
    sign_in()
else:
    create_patient()
'''

def get_patients(v_name):
    conn = sqlite3.connect('test1.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM VOLUNTEERS where NAME = ? ", (v_name,))

    for row in cursor:
        id = row[0]
    cursor2 = conn.cursor()
    cursor2.execute("SELECT * FROM PATIENTS where ID  = ?", (id,))
    data1 = cursor2.fetchall()
    l = []
    for names in data1:
        l.append(names)
    return l

def allocate_order(v_name):
    conn = sqlite3.connect('test1.db')
    global v_pin, v_food, v_id, p_no
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM VOLUNTEERS WHERE name = ?", (v_name,))
    #cursor.execute("""select * from VOLUNTEERS where NAME = ?""", (v_name))
    for row in cursor:
        v_id = row[0]
        v_pin = row[4]
        v_food = row[6]
    print(v_id)
    print(v_pin)
    print(v_food)
    cursor1 = conn.cursor()
    cursor1.execute("SELECT * FROM PATIENTS WHERE PIN = ? AND FOOD = ? AND STATUS = ?", (v_pin, v_food, 'NOT TAKEN'))
    data = cursor1.fetchall()
    if len(data) != 0:
        sql_select_query2 = """select * from PATIENTS where PIN = ? and FOOD = ? and STATUS = ?"""
        cursor2 = conn.cursor()
        cursor2.execute(sql_select_query2, (v_pin, v_food, 'NOT TAKEN'))
        for row in cursor2:
            p_no = row[7]
        sql_update_query1 = """Update PATIENTS set ID = ? where NUMBER = ?"""
        data1 = (v_id, p_no)
        cursor5 = conn.cursor()
        cursor5.execute(sql_update_query1, data1)
        conn.commit()
        sql_update_query = """Update VOLUNTEERS set STATUS = 'UNAVAILABLE' where NUMBER = ?"""
        cursor4 = conn.cursor()
        cursor4.execute(sql_update_query, (v_id,))
        conn.commit()
        sql_select_query3 = """select * from PATIENTS where PIN = ? and FOOD = ? and STATUS = ?"""
        cursor3 = conn.cursor()
        cursor3.execute(sql_select_query3, (v_pin, v_food, 'NOT TAKEN'))
        for row in cursor3:
            print("NAME = ", row[0])
            print("ADDRESS = ", row[1])
            print("PIN = ", row[2])
            print("QUANTITY = ", row[3])
            print("FOOD = ", row[4])
            print("STATUS = ", row[5])
            print("NUMBER = ", row[6])
        sql_update_query2 = """Update PATIENTS set STATUS = 'TAKEN' where NUMBER = ?"""
        cursor6 = conn.cursor()
        cursor6.execute(sql_update_query2, (p_no,))
        conn.commit()
    conn.close()


