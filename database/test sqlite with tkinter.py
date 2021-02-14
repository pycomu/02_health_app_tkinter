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

# def store_sql(value_in): # something wrong here
#     with conn:
#         c.execute("INSERT INTO user VALUES (:name, :weight, :height, :gender)", {'name':value_in.name, 'weight':value_in.weight, 'height':value_in.height, 'gender':value_in.gender})

def store_sql(value_in):
    print(value_in)
    with conn:
        c.execute("INSERT INTO user VALUES (?, ?)", (value_in))
        # conn.commit() 
         

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

    dataset = (user_name, user_dateofbirth)
    print(dataset)

    #register button
    reg_text = tk.StringVar()
    reg_btn = tk.Button(root, textvariable=reg_text, command=lambda:store_sql(dataset), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
    reg_text.set("Register")
    reg_btn.grid(column=2, row=3)
    
    # conn.close()

    root.mainloop()


if __name__ == "__main__":
    reg_mask()

    

    # https://www.pythoncentral.io/introduction-to-sqlite-in-python/
    # check content of db here https://sqliteonline.com/
