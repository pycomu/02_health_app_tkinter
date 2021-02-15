import sqlite3 
import tkinter as tk

root = tk.Tk() 

conn = sqlite3.connect('./database/user.db')
c = conn.cursor()

# create table "user"
c.execute("""CREATE TABLE IF NOT EXISTS user ( 
            name text,
            dateofbirth text
            )""")

def store_sql(*value_in): # can take more than on argument
    with conn:
        c.execute("INSERT INTO user VALUES (?, ?)", (value_in))
        
         
def reg_mask():
    # window of input mask
    canvas = tk.Canvas(root, width=500, height=300)
    canvas.grid(columnspan=4, rowspan=4)

    # label and entry fields
    name_label = tk.Label(root, text = "Your Name here:")
    name_label.grid(column=1, row=0)
    
    user_name = tk.Entry(root, width = 30)
    user_name.grid(column=2, row=0)    
    
    dateofbirth_label = tk.Label(root, text = "Your date of birth (YYYY-MM-DD):")
    dateofbirth_label.grid(column=1, row=1)
    
    user_dateofbirth = tk.Entry(root, width = 30)
    user_dateofbirth.grid(column=2, row=1)

    #register button
    reg_text = tk.StringVar()
    
    # .get() gives value of entry fields for sql operation
    reg_btn = tk.Button(root, textvariable=reg_text, command=lambda:store_sql(user_name.get(), user_dateofbirth.get()), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
    
    reg_text.set("Register")
    reg_btn.grid(column=2, row=3)
    
    # conn.close()

    root.mainloop()


if __name__ == "__main__":
    reg_mask()

    

    # https://www.pythoncentral.io/introduction-to-sqlite-in-python/
    # check content of db here https://sqliteonline.com/
