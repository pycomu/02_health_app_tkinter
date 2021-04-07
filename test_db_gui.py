

# import dependencies
import os
import shutil

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from tkcalendar import *
import tkcalendar
from tkcalendar import Calendar
import tkinter.messagebox
from tkcalendar import Calendar, DateEntry
import sqlite3

import pandas as pd
from pandas import Series,DataFrame
from PIL import Image, ImageTk

import database
from datetime import datetime
connection = database.connect()



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
        #setting window size
        width=600
        height=800
        screenwidth = self.winfo_screenwidth()
        screenheight = self.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.geometry(alignstr)
        self.resizable(width=False, height=False)
                
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True) 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        
        self.frames = {}  
        for F in (LoginPage,RegisterPage, MainPage, ChildPage, ChartPage):  # define names of all frames
            frame = F(container, self)  
            self.frames[F] = frame
            # label = ttk.Label(self, text ="x")
            # rows = 4
            # columns = 10
            # print(rows, columns, height, width)
            # for rows in range(height):
            #     frame.rowconfigure(rows, weight=1)
            #     for columns in range(width):
            #         frame.columnconfigure(columns, weight=1) 
            #         frame.Label(F, text='R%s/C%s'%(rows,columns), borderwidth=1 ).grid(row=rows,column=columns) # can be deleted
            
            frame.grid(row = 0, column = 0, sticky ="nsew") # each frame has the same grid parameters for layout
        
            

        self.show_frame(LoginPage)
  
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

    # read out database for gloabl variables, pointers for db navigation and array list for tkinter comboboxes
    def update_combo(self):
        pass
    
    #validate the numeirc field - Datatype and Length
    def validatePIN(self,P):
         
         if len(P) == 0 or len(P) <= 4 and P.isdigit():  # 4 characters
            return True
         else:
            return False

    #validate the string field - Datatype and Length
    def validateString(self,P):
        
         if len(P) == 0 or len(P) <= 10 and P.isalpha():  # 10 characters
            return True
         else:
            return False

class LoginPage(tk.Frame):       
    def __init__(self, parent, controller): # controller is "child" of class health_app to call its functions
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text ="Login Page", font="bold")        
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Login", command = lambda : controller.show_frame(MainPage))
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Register", command = lambda : controller.show_frame(RegisterPage))
        button2.grid(row = 3, column = 2, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text ="Import", command = lambda : controller.show_frame(Import))
        button3.grid(row = 3, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Export", command = lambda : controller.show_frame(LoginPage)) # not for pdf, for database export
        # button4 = ttk.Button(self, text ="Export", command = lambda : ChartPage.export_pdf(self))  # test for class of "ChartPage"      
        button4.grid(row = 3, column = 4, padx = 10, pady = 10)

        label1 = ttk.Label(self, text="PIN (4 digits)", font=("Arial Italic", 10))
        label1.grid(row=4, column=1)
        
        Entry1 = ttk.Entry(self,width=10, show="*",validate="key")
        Entry1['validatecommand'] = (Entry1.register(controller.validatePIN),'%P')
        Entry1.grid(row=4, column=2)

        # check if pin is matched with record
        
class RegisterPage(tk.Frame):       
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        #~~~~~~~~~~~~~~~~~ Labels ~~~~~~~~~~~~~~~~~~~        
        label = ttk.Label(self, text ="Register Page",font="bold")        
        label.grid(row = 0, column = 0, padx = 10, pady = 10)

        label1 = ttk.Label(self, text="E-Mail", font=("Arial Italic", 10))
        label1.grid(row=1,column=1)

        label2 = ttk.Label(self, text="Account Name", font=("Arial Italic", 10))
        label2.grid(row=2,column=1)
        
        label3 = ttk.Label(self, text="Enter PIN (4 digits)", font=("Arial Italic", 10))
        label3.grid(row=3,column=1)

        label4 = ttk.Label(self, text="Re-enter PIN", font=("Arial Italic", 10))
        label4.grid(row=4,column=1)
        
        label2 = ttk.Label(self, text="* Enter only 10 charecters",foreground='red', font=("Arial Italic", 10))
        label2.grid(row=2,column=3)

        # ~~~~~~~~~~~~~~~~~~~ Entries ~~~~~~~~~~~~~~~~~
        
        account_email = ttk.Entry(self, width=10) 
        account_email.grid(row=1, column=2)
          
        account_name = ttk.Entry(self, width=10,validate="key") 
        account_name['validatecommand'] = (account_name.register(controller.validateString),'%P')
        account_name.grid(row=2, column=2)
        
        account_pin = ttk.Entry(self,  width=10, show="*",validate="key") # PIN
        account_pin['validatecommand'] = (account_pin.register(controller.validatePIN),'%P')
        account_pin.grid(row=3, column=2)

        account_repin = ttk.Entry(self,width=10, show="*",validate="key") # Re enter PIN
        account_repin['validatecommand'] = (account_repin.register(controller.validatePIN),'%P')
        account_repin.grid(row=4, column=2)
        
        # ~~~~~~~~~~~~~~~~~~ Buttons ~~~~~~~~~~~~~~~~~~~~~~~
        button1 = ttk.Button(self, text ="Submit", command = lambda : [write_in_account(), controller.show_frame(LoginPage)]) # TODO: clear the entries here  
        button1.grid(row = 5, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Cancel", command = lambda : controller.show_frame(LoginPage)) 
        button2.grid(row = 5, column = 2, padx = 10, pady = 10) 
        
        # ~~~~~~~~~~~~~~~~~ Database Function ~~~~~~~~~~~~~~~~~~
        def write_in_account():
           
            database.store_account(connection, account_name.get(), account_pin.get(), account_email.get())
       
            ''' if account_pin == account_repin:
                    database.store_account(connection, account_name.get(), account_pin.get(), account_email.get())
                    else:
                    show a dialogbox or....
                    print(" PIN does not match")   #  we might clear the entryboxes here'''
                
        
class ChildPage(tk.Frame):       
    def __init__(self, parent, controller): # controller is "child" of class health_app to call its functions
        tk.Frame.__init__(self, parent)
    
        #********************************************************************************************
        child_bday = tk.StringVar()
        current_date = tk.StringVar()
        child_age = tk.StringVar()
        Days = tk.StringVar()
        Months = tk.StringVar()
        
        def Reset():
            
            current_date.set("")  
            Days.set("") 
            child_age.set("") 
            Months.set("")
            child_first_name.delete(0, tk.END)
            child_last_name.delete(0, tk.END)
            child_birthday.delete(0, tk.END)
            child_age.delete(0, tk.END)
        
        
        def iExit():
            iExit =tkinter.messagebox.askyesno("User Registration", "Confirm if you want to Exit")
            if iExit>=0:
                self.destroy()
                return
            
        def Results():
            Ent_current_date = DateEntry(self, font=("arial", 10, 'bold'), width=43, borderwidth=2, date_pattern='dd/mm/yyyy')
            CurrentDate =(Ent_current_date.get_date())
            DOBDate = (child_birthday.get_date())

            Day =(abs((CurrentDate - DOBDate).days))
            Days.set(str(Day))

            Age = int(Days.get())
            Agess = (Age/365)
            child_age .set(str('%.1f'%(Agess)))
                
            
        # ~~~~~~~~~~~~~~ Labels ~~~~~~~~~~~~~~~~~
        label = ttk.Label(self, text ="Child Registration Page", font="bold")        
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
            
        lbl_child_first_name = ttk.Label(self, font=("arial", 10, 'bold'), text="child_first_name")
        lbl_child_first_name.grid(row=1, column=0,padx=5)
        
        lbl_child_last_name= ttk.Label(self, font=("arial", 10, 'bold'), text="child_last_name")
        lbl_child_last_name.grid(row=2, column=0,padx=5)
        
        lbl_child_bday= ttk.Label(self, font=("arial", 10, 'bold'), text="child_bday")
        lbl_child_bday.grid(row=3, column=0, padx=5)
        
        lbl_child_age= ttk.Label(self, font=("arial", 10, 'bold'), text="child_age")
        lbl_child_age.grid(row=6, column=0,  padx=5)
        
        lbl_child_gender= ttk.Label(self, font=("arial", 10, 'bold'), text="child_gender")
        lbl_child_gender.grid(row=7, column=0, padx=5)
        
        # ~~~~~~~~~~~~~~~~~~~~ Entries ~~~~~~~~~~~~~~~~~~~
        child_first_name = ttk.Entry(self, font=("arial", 10, 'bold'), width=44)
        child_first_name .grid(row=1, column=1)
        
        child_last_name = ttk.Entry(self, font=("arial", 10, 'bold'), width=44)
        child_last_name.grid(row=2, column=1)
        
        child_birthday = DateEntry(self, font=("arial", 10, 'bold'), width=43, borderwidth=2, date_pattern='dd/mm/yyyy')
        child_birthday.grid(row=3, column=1)
        
        child_age = ttk.Entry(self, font=("arial", 10, 'bold'), width=44, justify='left', textvariable=child_age)
        child_age.grid(row=6, column=1)

        #the variable 'var' mentioned here holds Integer Value, by deault 0
        child_gender = tk.StringVar()
        child_gender.set('Male')
        rb1 = tk.Radiobutton(self, text="Male",padx= 5, variable= child_gender, value="Male").grid(row=7, column=1)
        rb2 = tk.Radiobutton(self, text="Female",padx= 20, variable= child_gender, value="Female").grid(row=7, column=2)

        # ~~~~~~~~~~~~~~~~~~~ Buttons ~~~~~~~~~~~~~~~~~~~

        btnCalculate = ttk.Button(self, text="Calculate", command=lambda:  Results())
        btnCalculate.grid(row=9, column=0,padx=10,pady=2)
        
        btnReset = ttk.Button(self, text="Submit",command=lambda: [ Results(), write_in_child(), Reset()])
        btnReset.grid(row=9, column=1,padx=10,pady=2)
        
        btnExit = ttk.Button(self, text="Exit", command=lambda: iExit())
        btnExit.grid(row=9, column=2,padx=10,pady=2)
        
        button1 = ttk.Button(self, text ="Close", command = lambda : controller.show_frame(MainPage)) 
        button1.grid(row = 10, column = 1, padx = 10, pady = 10)    
            
        
        # ~~~~~~~~~~~~~~~~~ Database Function ~~~~~~~~~~~~~~~~~~
        
        def write_in_child():
            database.store_child(connection, child_first_name.get(), child_last_name.get(), child_gender.get(), child_birthday.get())
                
        
class MainPage(tk.Frame):      
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        # ~~~~~~~~~~~ Labels ~~~~~~~~~~~~~~~~~~~~~~~~~
        label1 = ttk.Label(self, text ="USer Details - Main Page",font="bold")        
        label1.grid(row = 0, column = 0, padx = 10, pady = 10)

        label2 = ttk.Label(self, text="Height in m", font=("Arial Italic", 10))
        label2.grid(column=0, row=2)
        
        label3 = ttk.Label(self, text="Weight in Kg", font=("Arial Italic", 10))
        label3.grid(column=0, row=3)

        label4 = ttk.Label(self, text="Age", font=("Arial Italic", 10))
        label4.grid(column=0, row=4)
        
        label5 = ttk.Label(self, text="BMI Index", font=("Arial Italic", 10))
        label5.grid(column=0, row=5)
               
        resultAge = ttk.Label(self, text = "10")
        resultAge.grid(column=1, row=4)
        
        resultbmi = ttk.Label(self, text = 'BMI')
        resultbmi.grid(column=1, row=4)
        
        #~~~~~~~~~~~~ Entries ~~~~~~~~~~~~~~~
       
        height = ttk.Entry(self,width=10)
        height.grid(column=1, row=2)
        
        weight = ttk.Entry(self,width=10) 
        weight.grid(column=1, row=3)
        
        #bmi = ttk.Entry(self, width=10)
        #bmi.grid(column=1, row=5)
        
        
                   
        # ~~~~~~~~~~~~~~ List ~~~~~~~~~~~~~~~

        list_child = ("Max","Tom")

        self.list = tk.Listbox(self)  
        self.list.insert(0, *list_child) 
        self.list.grid(row=1,column=1)
        
        # ~~~~~~~~~~~~ Buttons ~~~~~~~~~~~~~~~
                                   
        button2 = ttk.Button(self, text="BMI Chart", command = lambda: controller.show_frame(ChartPage))
        button2.grid(row = 6, column = 1,padx = 10, pady = 10) 

        button5 = ttk.Button(self, text ="Close", command = lambda : controller.show_frame(LoginPage)) 
        button5.grid(row = 6, column = 2,padx = 10, pady = 10) 

        button1 = ttk.Button(self, text="Calculate BMI", command=lambda:   write_in_logfile())
        button1.grid(row = 6, column = 0,padx = 10, pady = 10) 

        button3 = ttk.Button(self, text="Register Child", command = lambda: controller.show_frame(ChildPage))
        button3.grid(row = 2, column = 3,padx = 10, pady = 10) 
        
        
        def calc_bmi(height, weight): # +++++++++++++++++++++++++++++++ calculation to be changed !
            
            '''Formula: weight (kg) / [height (m)]2
               Calculation: [weight (kg) / height (cm) / height (cm)] x 10,000'''
            
            '''height = height.get()
            if height:
            height = float(height)
            weight = Entry2.get()
            if weight:
                weight = float(weight)'''
            BMI =  (weight/ (height)**2) * 10,000
            return BMI
         
         
         
        # ~~~~~~~~~~~~~~~~~ Database Function ~~~~~~~~~~~~~~~~~~
        def write_in_logfile():
            entry_date = datetime.now()
            database.store_logfile(connection, entry_date, height.get(), weight.get())
            #, bmi.get() , actual_age.get()

class ChartPage(tk.Frame):      
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)

        label1 = ttk.Label(self, text ="BMI Chart Page",font="bold")        
        label1.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        load = Image.open("./growthchart_example2.gif")
        #img = ImageTk.PhotoImage(Image.open("growthchart_example2.gif")) 
        render= ImageTk.PhotoImage(master=self,image = load) 
        #canvas.create_image(250, 250, image=img) 
        img = ttk.Label(self, image=render)
        img.image = render
        img.grid(column=1, row=1)
        
        button = ttk.Button (self, text="Close.", command = lambda:  controller.show_frame(MainPage))
        button.grid(column=1, row=3)
        
        button = ttk.Button (self, text="Export PdF Report", command = lambda : self.export_pdf())
        button.grid(column=1, row=6)

    def export_pdf(self): # by this that function can be called even outside that class by <class.function>
        
        # the pdf report must be created inside app and stored in specific folder ! ++++++++ open
        pdf_file = "/BMI_report_child_date.pdf" # could include name of child account ?
        pdf_source = os.path.realpath(os.getcwd()) + pdf_file # get working directory -> later from specific folder
        print("Source ", pdf_source) # to be deleted
            
        file = askdirectory() # ask user for folder to store(copy) pdf report; user can then use email to send away
        if file != "": # askdirectory() return "" if dialog closed with "cancel". -> nothing happens
            print("new dir ",file) # to be deleted
            pdf_destination = file + pdf_file
            print("Destination ", pdf_destination) # to be deleted
                
            shutil.copy (pdf_source, pdf_destination) # copy and overwrite file


# ++++++ functions for database modifications e.g. insert data, delete data, update data

if __name__ == "__main__":

    app = health_app()
    app.mainloop()