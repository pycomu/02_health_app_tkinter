import sqlite3
from tkinter import *

conn = sqlite3.connect ("bmi_memoona.db")
c = conn.cursor()
# Variable to store input from user-------------

def create_database():
      
   conn = sqlite3.connect ("bmi_memoona.db")
   c = conn.cursor()
   c.execute('''CREATE TABLE IF NOT EXISTS login_info (userid integer primary key autoincrement,
                                                            username TEXT, password TEXT, date_of_birth INT,
                                                            gender TEXT)''')
   
   c.execute('''CREATE TABLE IF NOT EXISTS bmi_info (records integer primary key autoincrement,
                                                        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                                                        age INT, weight INT, height INT, bmi TEXT)''')
   
def write_login():
    c.execute('INSERT INTO login_info (username, password, date_of_birth, gender) VALUES(?,?,?,?)',(name,pwd,u_dob,gender,))
    conn.commit()
    
def write_bmi_info():
    c.execute('INSERT INTO bmi_info (weight, height, bmi) VALUES(?,?,?)',(w, h,value,))
    conn.commit()
    #c.execute("INSERT INTO login_data (username, password) VALUES (?, ?)", user.get(), pswd.get())
   
def login():
    root.withdraw() # hiding root window
    login_window = Toplevel(root)
    login_window.geometry("300x300")
    login_window.title("Login Page")
    
    user_lbl= Label(login_window, text ="Username")
    user_lbl.place(x = 50, y = 20)
    
    pass_lbl = Label(login_window, text ="Password")
    pass_lbl.place(x = 50, y = 50)
    
    username = StringVar()
    Username = Entry(login_window, width = 35, textvariable = username )
    Username.place(x = 150, y = 20, width = 100) 
    
    password = StringVar()
    password = Entry(login_window, width = 35, textvariable = password, show= "*")
    password.place(x = 150, y = 50, width = 100)
 
    loginbtn = Button(login_window, text ="Login", command = check_login)
    loginbtn.place(x = 150, y = 135, width = 55)

    

def store_newuser():
    pass

def check_login():
    pass

def new_user():
    root.withdraw() # hiding root window
    reg_window = Toplevel(root) # ???? +++++++++++
    reg_window.geometry("600x600")
    reg_window.title("Login Page")

    # Create labels------------------
    
    user_lbl= Label(reg_window, text ="Username")
    user_lbl.place(x = 50, y = 20)
    
    pass_lbl = Label(reg_window, text ="Password")
    pass_lbl.place(x = 50, y = 50)
    
    dob_lbl = Label(reg_window, text ="Date of Birth")
    dob_lbl.place(x = 50, y = 50)
    
    gender_lbl = Label(reg_window, text ="Gender")
    gender_lbl.place(x = 50, y = 50)
    
    # Create Text boxes-----------------
    newuser = StringVar()
    newuser = Entry(reg_window, width = 35, textvariable = newuser )
    newuser.place(x = 150, y = 20, width = 100)
    
    npassword = StringVar()
    npassword = Entry(reg_window, width = 35, textvariable = npassword, show= "*")
    npassword.place(x = 150, y = 50, width = 100)
    
    dob = IntVar()
    dob= Entry(reg_window, width = 35, textvariable = dob)
    dob.place(x = 150, y = 50, width = 100)
    
    gender = StringVar()
    gender = Entry(reg_window, width = 35, textvariable = gender)
    gender.place(x = 150, y = 50, width = 100)
 
    register_btn = Button(reg_window, text ="Register", command = store_newuser)
    register_btn.place(x = 150, y = 135, width = 55)

    

# First window-----------------------------------
global root
root = Tk()
root.geometry("300x300")
root.title("Main window")

login_btn = Button(root, text ="Login", command = login)
login_btn.place(x = 150, y = 50, width = 80)

newuser_btn = Button(root, text ="New User", command = new_user)
newuser_btn.place(x = 150, y = 135, width = 80)

create_database()

root.mainloop()