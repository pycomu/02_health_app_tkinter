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
        self.wm_title("Health Tracker")
        self.geometry("500x500")
        
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True) 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}  
        for F in (LoginPage,RegisterPage, MainPage, BMI_chart):  # define names of 2 frames
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
        
        label = ttk.Label(self, text ="Main Page", font="bold")        
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Login", command = lambda : controller.show_frame(MainPage))
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Register", command = lambda : controller.show_frame(RegisterPage))
        button2.grid(row = 3, column = 2, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text ="Import", command = lambda : controller.show_frame(Import))
        button3.grid(row = 3, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Export", command = lambda : controller.show_frame(Export))
        button4.grid(row = 3, column = 4, padx = 10, pady = 10)

        label1 = ttk.Label(self, text="PIN", font=("Arial Italic", 10))
        label1.grid(row=4, column=1)

        Entry1 = ttk.Entry(self,width=10, show="*")  # field entry for PIN
        Entry1.grid(row=4, column=2)

        
class RegisterPage(tk.Frame):       
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text ="Register Page",font="bold")        
        label.grid(row = 0, column = 0, padx = 10, pady = 10)

        label1 = ttk.Label(self, text="E-Mail", font=("Arial Italic", 10))
        label1.grid(row=1,column=1)

        label2 = ttk.Label(self, text="Account Name", font=("Arial Italic", 10))
        label2.grid(row=2,column=1)
        
        label3 = ttk.Label(self, text="Enter PIN", font=("Arial Italic", 10))
        label3.grid(row=3,column=1)

        label4 = ttk.Label(self, text="Re-enter PIN", font=("Arial Italic", 10))
        label4.grid(row=4,column=1)


        Entry1 = ttk.Entry(self,width=10) # field entry for account E-Mail
        Entry1.grid(row=1, column=2)
        
        Entry2 = ttk.Entry(self,width=10) # field entry for account Name
        Entry2.grid(row=2, column=2)

        Entry3 = ttk.Entry(self,width=10,show="*") # field entry for PIN
        Entry3.grid(row=3, column=2)

        Entry4 = ttk.Entry(self,width=10,show="*") # field entry for PIN
        Entry4.grid(row=4, column=2)

        button1 = ttk.Button(self, text ="Submit", command = lambda : controller.show_frame(LoginPage)) 
        button1.grid(row = 5, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Cancel", command = lambda : controller.show_frame(LoginPage)) 
        button2.grid(row = 5, column = 2, padx = 10, pady = 10) 

class MainPage(tk.Frame):      
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        label1 = ttk.Label(self, text ="USer Details - Main",font="bold")        
        label1.grid(row = 0, column = 0, padx = 10, pady = 10)

        label2 = ttk.Label(self, text="Height", font=("Arial Italic", 10))
        label2.grid(column=0, row=2)
        
        label3 = ttk.Label(self, text="Weight", font=("Arial Italic", 10))
        label3.grid(column=0, row=3)

        label4 = ttk.Label(self, text="Age", font=("Arial Italic", 10))
        label4.grid(column=0, row=4)
        
        height = ""
        weight =""
        Entry1 = ttk.Entry(self,width=10,textvariable = height)
        Entry1.grid(column=1, row=2)
        
        Entry2 = ttk.Entry(self,width=10,textvariable=weight) 
        Entry2.grid(column=1, row=3)
        
        resultAge = ttk.Label(self, text = "10")
        resultAge.grid(column=1, row=4)
        

        list_child = ("Max","Tom")

        self.list = tk.Listbox(self)  
        self.list.insert(0, *list_child) 
        self.list.grid(row=1,column=1)
                                   
        button2 = ttk.Button(self, text="BMI Chart", command=lambda: BMI_chart())
        button2.grid(row = 6, column = 1,padx = 10, pady = 10) 

        button5 = ttk.Button(self, text ="Close", command = lambda : controller.show_frame(LoginPage)) 
        button5.grid(row = 6, column = 2,padx = 10, pady = 10) 

        button1 = ttk.Button(self, text="Calculate BMI", command=lambda:  calc_bmi())
        button1.grid(row = 6, column = 0,padx = 10, pady = 10) 
        
        
        def calc_bmi(): # +++++++++++++++++++++++++++++++ calculation to be changed !
         height = Entry1.get()
         if height:
          height = int(height)
         weight = Entry2.get()
         if weight:
            weight = int(weight)
         BMI =  weight/(height*2)
         
         label5 = ttk.Label(self, text="BMI Index", font=("Arial Italic", 10))
         label5.grid(column=0, row=5)

         label6 = ttk.Label(self, text=BMI, font=("Arial Italic", 10))
         label6.grid(column=1, row=5)

class BMI_chart(tk.Frame):      
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)

        
        load = Image.open("./growthchart_example2.gif")
        #img = ImageTk.PhotoImage(Image.open("growthchart_example2.gif")) 
        render= ImageTk.PhotoImage(master=self,image = load) 
        #canvas.create_image(250, 250, image=img) 
        img = ttk.Label(self, image=render)
        img.image = render
        img.pack()

        button = Button (self, text="Close.", command = lambda:  controller.show_frame(MainPage))
        button.pack()
        button = Button (self, text="Export") # go to export page
        button.pack()
        

# ++++++ functions for database modifications e.g. insert data, delete data, update data

if __name__ == "__main__":

    app = health_app()
    app.mainloop()

    