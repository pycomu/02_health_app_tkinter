from tkinter import *
import mysql.connector


root = Tk()
root.title('BMI Calculator')
root.geometry("300x300")


# Create Calculate function for database
def calculate(h_text,w_text):
    # Create a database connection
    connection = mysql.connector.connect(host="localhost", user="root", password="pass123", database= "BMI_db")
    c = connection.cursor()

    # Create table 
    #c.execute("CREATE TABLE user_data (height float, weight float, bmi float)")

    h_user = h_text.get()
    w_user = w_text.get()

    # Insert into Table
    query = "INSERT INTO user_data (height, weight) VALUES (%s, %s)"
    val = (h_user, w_user)
    c.execute(query, val)
    

    connection.commit()
    connection.close()

 
 
# Create entry boxes 
h_text= Entry(root, width=30)
h_text.grid(row=0, column=1, padx=20)


w_text = Entry(root, width=30)
w_text.grid(row=1, column=1, padx=20)

bmi = Entry(root, width=30)
bmi.grid(row=2, column=1, padx=20)

calculate(h_text,w_text)

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





root.mainloop()
