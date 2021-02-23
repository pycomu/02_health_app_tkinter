import sqlite3
from tkinter import *



# Variable to store input from user-------------
newuser = StringVar()
npassword = StringVar()
dob = IntVar()
gender = StringVar()
username = StringVar()
password = StringVar()
user_height = DoubleVar()
user_weight = DoubleVar()
user_bmi = DoubleVar()


# Create database-------------------------------

def database():
   name= newuser.get()
   pwd= npassword.get()
   u_dob= dob.get()
   gen = gender.get()
   w = user_weight.get()
   h = user_height.get()
   value = user_bmi.get()
   
   conn = sqlite3.connect ("bmi.db")
   c = conn.cursor()
   c.execute('''CREATE TABLE IF NOT EXISTS login_info (userid integer primary key autoincrement,
                                                            username TEXT, password TEXT, date_of_birth INT,
                                                            gender TEXT)''')
   
   c.execute('''CREATE TABLE IF NOT EXISTS bmi_info (records integer primary key autoincrement,
                                                        time TIMESTAMP DEFAULT CURRENT_TIMESTAMP NOT NULL,
                                                        age INT, weight INT, height INT, bmi TEXT)''')
   
   
   c.execute('INSERT INTO login_info (username, password, date_of_birth, gender) VALUES(?,?,?,?)',(name,pwd,u_dob,gender,))
   c.execute('INSERT INTO bmi_info (weight, height, bmi) VALUES(?,?,?)',(w, h,value,))

   conn.commit()
   #c.execute("INSERT INTO login_data (username, password) VALUES (?, ?)", user.get(), pswd.get())
   

# First window-----------------------------------
global root
root = Tk()
root.geometry("300x300")
root.title("Main window")

login_btn = Button(root, text ="Login", command = login)
login_btn.place(x = 150, y = 135, width = 55)

newuser_btn = Button(root, text ="New User", command = new_user)
newuser_btn.place(x = 150, y = 135, width = 55)



  
def new_user():
    
    reg_window = Toplevel(root)
    reg_window.geometry("600x600")
    reg_window.title("Login Page")
    
    # Create labels------------------
    
    user_lbl= Label(root, text ="Username")
    user_lbl.place(x = 50, y = 20)
    
    pass_lbl = Label(root, text ="Password")
    pass_lbl.place(x = 50, y = 50)
    
    dob_lbl = Label(root, text ="Date of Birth")
    dob_lbl.place(x = 50, y = 50)
    
    gender_lbl = Label(root, text ="Gender")
    gender_lbl.place(x = 50, y = 50)
    
    # Create Text boxes-----------------
    newuser = StringVar()
    newuser = Entry(root, width = 35, textvariable = newuser )
    newname.place(x = 150, y = 20, width = 100)
    
    npassword = StringVar()
    npassword = Entry(root, width = 35, textvariable = npassword, show= "*")
    npassword.place(x = 150, y = 50, width = 100)
    
    dob = IntVar()
    dob= Entry(root, width = 35, textvariable = dob)
    dob.place(x = 150, y = 50, width = 100)
    
    gender = StringVar()
    gender = Entry(root, width = 35, textvariable = gender)
    gender.place(x = 150, y = 50, width = 100)
 
    register_btn = Button(root, text ="Register", command = store_newuser)
    register_btn.place(x = 150, y = 135, width = 55)

def store_newuser():
   pass


def login():
        
    login_window = Toplevel(root)
    login_window.geometry("300x300")
    login_window.title("Login Page")
    
    user_lbl= Label(root, text ="Username")
    user_lbl.place(x = 50, y = 20)
    
    pass_lbl = Label(root, text ="Password")
    pass_lbl.place(x = 50, y = 50)
    
    username = StringVar()
    Username = Entry(root, width = 35, textvariable = username )
    Username.place(x = 150, y = 20, width = 100) 
    
    password = StringVar()
    password = Entry(root, width = 35, textvariable = password, show= "*")
    password.place(x = 150, y = 50, width = 100)
 
    loginbtn = Button(root, text ="Login", command = check_login)
    loginbtn.place(x = 150, y = 135, width = 55)
    
    
    
    
def check_login():
    
    # check if user exist 
    #   open bmi window
    # else
    # print message
    pass

def bmi_page():
    # Create the window

    bmi_window = Toplevel(root)
    bmi_window.title('BMI Calculator')
    bmi_window.geometry("300x300")

    # Create entry boxes 

    user_height = DoubleVar()
    user_height = Entry(root,textvariable= user_height, width=30)
    user_height.grid(row=0, column=1, padx=20)

    user_weight = DoubleVar()
    user_weight = Entry(root, width=30, textvariable=user_weight)
    user_weight.grid(row=1, column=1, padx=20)

    user_bmi = DoubleVar()
    user_bmi = Entry(root, width=30, textvariable=user_bmi)
    user_bmi.grid(row=2, column=1, padx=20)

    # Create Labels

    h_label = Label(root, text = "Height in cm")
    h_label.grid(row=0, column=0)

    w_label = Label()
    w_label = Label(root, text = "Weight in kg")
    w_label.grid(row=1, column=0)

    bmi_label = Label(root, text = "Your BMI is")
    bmi_label.grid(row=2, column=0)

    # Create calculte button

    cal_btn = Button(root, text = "Calculate",command = calculate)
    cal_btn.grid(row=3, column=0, columnspan=2, pady=10 , padx=10 )

def calculate():
    connection = sqlite3.connect ("bmi.db")
    c = connection.cursor()
    c.execute("INSERT INTO user_data (height, weight,) VALUES(?, ?)", (user_height.get(), user_weight.get()))
    bmi_result = user_weight /((user_height/100)^2)
    connection.commit()
    connection.close()
    return bmi_result
    
    
    
root.mainloop()
