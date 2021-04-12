# import dependencies
import os
import shutil

import tkinter as tk
from tkinter import ttk
from tkinter.filedialog import askdirectory
from tkinter import filedialog, messagebox

from tkcalendar import *
import tkcalendar
from tkcalendar import Calendar
import tkinter.messagebox
from tkcalendar import Calendar, DateEntry

import sqlite3

import pandas as pd
from pandas import Series,DataFrame
from PIL import Image, ImageTk

conn = sqlite3.connect("./health_app.db")
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

def read_terms():
    c.execute("select date_terms, terms_version from terms")
    date_terms =[]
    for row in c.fetchall():
        # date_terms.append(row[0])
        print(date_terms)
        return TRUE if date_terms != "" # True if terms were confirmed



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
        
        button3 = ttk.Button(self, text ="Import", command = lambda : self.import_db())
        button3.grid(row = 3, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Export", command = lambda : self.export_db()) # for database export
        # button4 = ttk.Button(self, text ="Export", command = lambda : ChartPage.export_pdf(self))  # test for class of "ChartPage"      
        button4.grid(row = 3, column = 4, padx = 10, pady = 10)

        label1 = ttk.Label(self, text="PIN (4 digits)", font=("Arial Italic", 10))
        label1.grid(row=4, column=1)
      
        Entry1 = ttk.Entry(self,width=10, show="*",validate="key")
        Entry1['validatecommand'] = (Entry1.register(controller.validatePIN),'%P')
        Entry1.grid(row=4, column=2)

    def export_db(self): # by this that function can be called even outside that class by <class.function>
        db_file = "/health_app.db" # complete sqlite database
        db_source = os.path.realpath(os.getcwd()) + db_file # get working directory -> later from specific folder
                    
        file = askdirectory() # ask user for folder to store(copy) sqlite db - user can then use email to send away
        if file != "": # askdirectory() return "" if dialog closed with "cancel". -> nothing happens
            db_destination = file + db_file     
            shutil.copy (db_source, db_destination) # copy and overwrite file
            messagebox.showinfo("Notice !","Export of db-file done")

    def import_db(self):
        files = [('db file', '*.db')] 
        db_import = filedialog.askopenfilename(initialdir = "./", title = "Select the db File",filetypes = files)
        if db_import != "": # askopenfilename() return "" if dialog closed with "cancel". -> nothing happens
            db_file = "/health_app.db"
            db_destination = os.path.realpath(os.getcwd()) + db_file    
            shutil.copy (db_import, db_destination) # copy and overwrite file, but name stays health_app.db !
            messagebox.showinfo("Notice !","Import of db-file done, existing file overwritten !")
        # if imported db-file is corrupted or unable to read, then app new install with empty database !
        
class RegisterPage(tk.Frame):       
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
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


        Entry1 = ttk.Entry(self,width=10) # field entry for account E-Mail
        Entry1.grid(row=1, column=2)
        
        Entry2 = ttk.Entry(self,width=10, show="*",validate="key") # Account Name
        Entry2['validatecommand'] = (Entry2.register(controller.validateString),'%P')
        Entry2.grid(row=2, column=2)
        label2 = ttk.Label(self, text="* Enter only 10 charecters",foreground='red', font=("Arial Italic", 10))
        
        label2.grid(row=2,column=3)

        Entry3 = ttk.Entry(self,width=10, show="*",validate="key") # PIN
        Entry3['validatecommand'] = (Entry3.register(controller.validatePIN),'%P')
        Entry3.grid(row=3, column=2)

        Entry4 = ttk.Entry(self,width=10, show="*",validate="key") # Re enter PIN
        Entry4['validatecommand'] = (Entry4.register(controller.validatePIN),'%P')
        Entry4.grid(row=4, column=2)

        button1 = ttk.Button(self, text ="Submit", command = lambda : controller.show_frame(LoginPage)) 
        button1.grid(row = 5, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Cancel", command = lambda : controller.show_frame(LoginPage)) 
        button2.grid(row = 5, column = 2, padx = 10, pady = 10) 

class ChildPage(tk.Frame):       
    def __init__(self, parent, controller): # controller is "child" of class health_app to call its functions
        tk.Frame.__init__(self, parent)
    
        label = ttk.Label(self, text ="Child Registration Page", font="bold")        
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        button1 = ttk.Button(self, text ="Close", command = lambda : controller.show_frame(MainPage)) 
        button1.grid(row = 10, column = 1, padx = 10, pady = 10)

        #********************************************************************************************

        child_bday = tk.StringVar()
        current_date = tk.StringVar()
        Days = tk.StringVar()
        child_age = tk.StringVar()
        Months = tk.StringVar()
        child_gender = tk.StringVar()
        
        def Reset():
            child_bday.set("") 
            current_date.set("")  
            Days.set("") 
            child_age.set("") 
            Months.set("")
            child_gender.set("")
            Ent_child_first_name.delete(0, tk.END)
            Ent_child_last_name.delete(0, tk.END)
        
        def iExit():
            iExit =tkinter.messagebox.askyesno("User Registration", "Confirm if you want to Exit")
            if iExit>=0:
                self.destroy()
                return
        

        def Results():
            Ent_current_date = DateEntry(self, font=("arial", 10, 'bold'), width=43, borderwidth=2, date_pattern='dd/mm/yyyy')
            CurrentDate =(Ent_current_date.get_date())
            DOBDate = (Ent_child_bday.get_date())

            Day =(abs((CurrentDate - DOBDate).days))
            Days.set(str(Day))

            Age = int(Days.get())
            Agess = (Age/365)
            child_age .set(str('%.1f'%(Agess)))

        child_first_name = ttk.Label(self, font=("arial", 10, 'bold'), text="child_first_name")
        child_first_name.grid(row=1, column=0,padx=5)
        Ent_child_first_name = ttk.Entry(self, font=("arial", 10, 'bold'), width=44)
        Ent_child_first_name .grid(row=1, column=1)

        lbl_child_last_name= ttk.Label(self, font=("arial", 10, 'bold'), text="child_last_name")
        lbl_child_last_name.grid(row=2, column=0,padx=5)
        Ent_child_last_name = ttk.Entry(self, font=("arial", 10, 'bold'), width=44)
        Ent_child_last_name.grid(row=2, column=1)

        lbl_child_bday= ttk.Label(self, font=("arial", 10, 'bold'), text="child_bday")
        lbl_child_bday.grid(row=3, column=0, padx=5)
        Ent_child_bday = DateEntry(self, font=("arial", 10, 'bold'), width=43, borderwidth=2, date_pattern='dd/mm/yyyy')
        Ent_child_bday.grid(row=3, column=1)

        lbl_child_age= ttk.Label(self, font=("arial", 10, 'bold'), text="child_age")
        lbl_child_age.grid(row=6, column=0,  padx=5)
        Ent_child_age = ttk.Entry(self, font=("arial", 10, 'bold'), width=44, justify='left', textvariable=child_age)
        Ent_child_age.grid(row=6, column=1)

        lbl_child_gender= ttk.Label(self, font=("arial", 10, 'bold'), text="child_gender")
        lbl_child_gender.grid(row=7, column=0, padx=5)

        #the variable 'var' mentioned here holds Integer Value, by deault 0
        var=tk.IntVar()
        tk.Radiobutton(self, text="Male",padx= 5, variable= var, value=1).grid(row=7, column=1)
        tk.Radiobutton(self, text="Female",padx= 20, variable= var, value=2).grid(row=7, column=2)

        btnCalculate = ttk.Button(self, text="Calculate", command=lambda:  Results())
        btnCalculate.grid(row=9, column=0,padx=10,pady=2)
        
        btnReset = ttk.Button(self, text="Reset",command=lambda: Reset())
        btnReset.grid(row=9, column=1,padx=10,pady=2)
        
        btnExit = ttk.Button(self, text="Exit", command=lambda: iExit())
        btnExit.grid(row=9, column=2,padx=10,pady=2)

class MainPage(tk.Frame):      
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        label1 = ttk.Label(self, text ="USer Details - Main Page",font="bold")        
        label1.grid(row = 0, column = 0, padx = 10, pady = 10)

        label2 = ttk.Label(self, text="Height in m", font=("Arial Italic", 10))
        label2.grid(column=0, row=2)
        
        label3 = ttk.Label(self, text="Weight in Kg", font=("Arial Italic", 10))
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
                                   
        button2 = ttk.Button(self, text="BMI Chart", command = lambda: controller.show_frame(ChartPage))
        button2.grid(row = 6, column = 1,padx = 10, pady = 10) 

        button5 = ttk.Button(self, text ="Close", command = lambda : controller.show_frame(LoginPage)) 
        button5.grid(row = 6, column = 2,padx = 10, pady = 10) 

        button1 = ttk.Button(self, text="Calculate BMI", command=lambda:  calc_bmi())
        button1.grid(row = 6, column = 0,padx = 10, pady = 10) 

        button3 = ttk.Button(self, text="Register Child", command = lambda: controller.show_frame(ChildPage))
        button3.grid(row = 2, column = 3,padx = 10, pady = 10) 
        
        
        def calc_bmi(): # +++++++++++++++++++++++++++++++ calculation to be changed !
         height = Entry1.get()
         if height:
          height = float(height)
         weight = Entry2.get()
         if weight:
            weight = float(weight)
         BMI =  weight/(height*2)
         
         label5 = ttk.Label(self, text="BMI Index", font=("Arial Italic", 10))
         label5.grid(column=0, row=5)

         label6 = ttk.Label(self, text=BMI, font=("Arial Italic", 10))
         label6.grid(column=1, row=5)

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
        
        button = ttk.Button (self, text="Close", command = lambda:  controller.show_frame(MainPage))
        button.grid(column=1, row=3)
        
        button = ttk.Button (self, text="Export Pdf Report", command = lambda : self.export_pdf())
        button.grid(column=1, row=6)

    def export_pdf(self): # by this that function can be called even outside that class by <class.function>
        
        # the pdf report must be created inside app and stored in specific folder ! ++++++++ open
        pdf_file = "/BMI_report_child_date.pdf" # could include name of child account ?
        pdf_source = os.path.realpath(os.getcwd()) + pdf_file # get working directory -> later from specific folder
                    
        file = askdirectory() # ask user for folder to store(copy) pdf report; user can then use email to send away
        if file != "": # askdirectory() return "" if dialog closed with "cancel". -> nothing happens
            pdf_destination = file + pdf_file     
            shutil.copy (pdf_source, pdf_destination) # copy and overwrite file
            messagebox.showinfo("Notice !","Export of pdf report done")

# ++++++ functions for database modifications e.g. insert data, delete data, update data

if __name__ == "__main__":

    app = health_app()
    
    if read_terms == False:
        controller.show_frame(RegisterPage)
    else:
        controller.show_frame(LoginPage)

    app.mainloop()

    