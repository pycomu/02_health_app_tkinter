# import dependencies
import tkinter as tk
from tkinter import ttk
import sqlite3

import pandas as pd
from pandas import Series,DataFrame
from PIL import Image, ImageTk

conn = sqlite3.connect("./database/health_app.db")
c = conn.cursor()

# Global variables along database structure - if required ?

# +++++ pointers for status/position in database
# Account_id or account_name
# Child_id or child_name
# Logfile_id

# ++++++ parameters to show in label or preset entrybox
# Last_weight
# Last_height
# etc.
"""
"account_id"	INTEGER,
"account_name"	TEXT,
"account_pin"	INTEGER,
"account_email"	TEXT,
"account_create_date" TEXT,

"child_id"	INTEGER,
"child_first_name"	TEXT,
"child_last_name"	TEXT,
"child_bday"	TEXT,
"child_gender"	TEXT,
"child_country"	TEXT,
"child_create_date"	TEXT,
"account_id"	INTEGER,

"logfile_id"	integer,
"logfile_timestamp"	TEXT,
"logfile_weight"	REAL,
"logfile_height"	REAL,
"logfile_bmi"	REAL,
"logfile_age_act"	REAL,
"child_id"	INTEGER,


"""
# ++++++ functions for GUI, layout window and its different frames
class health_app(tk.Tk):    
    def __init__(self, *args, **kwargs): 
                
        tk.Tk.__init__(self, *args, **kwargs)        
        self.wm_title("Test App")
        self.geometry("400x300")
        
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True) 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}  
        for F in (LoginPage,RegisterPage):  # define names of 2 frames
            frame = F(container, self)  
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew") # each frame has the same grid parameters for layout
            
        self.show_frame(LoginPage)
  
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # read out database for gloabl variables, pointers for db navigation and array list for tkinter comboboxes
    def update_combo(self):
        pass

class LoginPage(tk.Frame):       
    def __init__(self, parent, controller): # controller is "child" of class health_app to call its functions
        tk.Frame.__init__(self, parent)
        
        label1 = ttk.Label(self, text ="Login Page",font="bold")        
        label1.grid(row = 0, column = 0, padx = 10, pady = 10) # putting the grid in its place by using grid

        button1 = ttk.Button(self, text="go to register", command=lambda: controller.show_frame(RegisterPage))
        button1.grid(column=1, row=1)

        
class RegisterPage(tk.Frame):       
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        label1 = ttk.Label(self, text ="Register Page",font="bold")        
        label1.grid(row = 0, column = 0, padx = 10, pady = 10)

        button5 = ttk.Button(self, text ="go to login", command = lambda : controller.show_frame(LoginPage)) 
        button5.grid(row = 1, column = 1, padx = 10, pady = 10) 


# ++++++ functions for database modifications e.g. insert data, delete data, update data

if __name__ == "__main__":

    app = health_app()
    app.mainloop()

    