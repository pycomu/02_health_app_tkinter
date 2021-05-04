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
from datetime import date
import sqlite3

import pandas as pd
from pandas import Series,DataFrame
from PIL import Image, ImageTk

from fpdf import FPDF  # fpdf class

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
    c.execute("select date_confirm, terms_version from terms")
    content = c.fetchone()
    return False if content == None else True

def store_account(account_name, account_pin, account_email, account_create_date):
     with conn:
        c.execute("INSERT INTO account (account_name, account_pin, account_email, account_create_date) VALUES (?, ?, ?, ?)", (account_name, account_pin, account_email,account_create_date))

def store_confirm(date_confirm, terms_version):
     with conn:
        c.execute("INSERT INTO terms (date_confirm, terms_version) VALUES (?, ?)", (date_confirm, terms_version))




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
        for F in (ConfirmPage, LoginPage,RegisterPage, MainPage, ChildPage, ChartPage):  # define names of all frames
            frame = F(container, self)  
            self.frames[F] = frame
                        
            frame.grid(row = 0, column = 0, sticky ="nsew") # each frame has the same grid parameters for layout

        if read_terms() == False:
            self.show_frame(ConfirmPage)
        else:
            self.show_frame(LoginPage)
  
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

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

class ConfirmPage(tk.Frame):       
    def __init__(self, parent, controller): # controller is "child" of class health_app to call its functions
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text ="Terms & Confirmation Page", font="bold")        
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        confirmed=tk.IntVar()
        checkbutton = tk.Checkbutton(self, variable=confirmed,text="Agreed to our terms & conditions by checking this ckeck box",
         command = lambda : continue_check())
        # checkbutton = tk.Checkbutton(self, text="Agreed to our terms & conditions by checking this ckeck box",
        # command = continue_check())
        checkbutton.grid(row=1, column=1, columnspan = 2)
        # checkbutton.bind("<<ListboxSelect>>", lambda event: continue_check())

        button1 = ttk.Button(self, text ="Continue", command = lambda : controller.show_frame(RegisterPage))
        button1.grid(row = 2, column = 1, padx = 10, pady = 10)
        button1.configure(state="disabled")

        # placeholder for legal text content
        terms_text = """AGREEMENT TO TERMS, 
        These Terms and Conditions constitute a legally 
        binding agreement made between you, whether personally or on 
        behalf of an entity (“you”) and [business entity name] (“we,” “us” or “our”), 
        concerning your access to and use of the [website name.com] website as well as 
        any other media form, media channel, mobile website or mobile application related, 
        linked, or otherwise connected thereto (collectively, the “Site”). You agree that by
         accessing the Site, you have read, understood, and agree to be bound by all of these 
         Terms and Conditions Use. IF YOU DO NOT AGREE WITH ALL OF THESE TERMS and CONDITIONS, 
         THEN YOU ARE EXPRESSLY PROHIBITED FROM USING THE SITE AND YOU MUST DISCONTINUE USE IMMEDIATELY."""  

        text_box = tk.Text(self, height=20, width=40, padx=15, pady=15)
        text_box.grid(column=1, row=3, columnspan=4, rowspan=4)
        text_box.insert(1.0, terms_text)

        def continue_check():
            if confirmed.get() == 1:
                button1.configure(state="normal")
            else:
                button1.configure(state="disabled")


class LoginPage(tk.Frame):       
    def __init__(self, parent, controller): # controller is "child" of class health_app to call its functions
        tk.Frame.__init__(self, parent)
        
        label = ttk.Label(self, text ="Login Page", font="bold",style='My.TLabel')        
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Login",style='My.TButton', command = lambda : controller.show_frame(MainPage))
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Register", style='My.TButton', command = lambda : controller.show_frame(RegisterPage))
        button2.grid(row = 3, column = 2, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text ="Import", command = lambda : self.import_db())
        button3.grid(row = 3, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Export", command = lambda : self.export_db()) # for database export
        # button4 = ttk.Button(self, text ="Export", command = lambda : ChartPage.export_pdf(self))  # test for class of "ChartPage"      
        button4.grid(row = 3, column = 4, padx = 10, pady = 10)

        label1 = ttk.Label(self, text="PIN (4 digits)", font=("Arial Italic", 10),style='My.TLabel')
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
        
        label = ttk.Label(self, text ="Register Page",font="bold",style='My.TLabel')        
        label.grid(row = 0, column = 0, padx = 10, pady = 10)

        label1 = ttk.Label(self, text="E-Mail", font=("Arial Italic", 10),style='My.TLabel')
        label1.grid(row=1,column=1)

        label2 = ttk.Label(self, text="Account Name", font=("Arial Italic", 10),style='My.TLabel')
        label2.grid(row=2,column=1)
        
        label3 = ttk.Label(self, text="Enter PIN (4 digits)", font=("Arial Italic", 10),style='My.TLabel')
        label3.grid(row=3,column=1)

        label4 = ttk.Label(self, text="Re-enter PIN", font=("Arial Italic", 10),style='My.TLabel')
        label4.grid(row=4,column=1)


        Entry1 = ttk.Entry(self,width=20) # field entry for account E-Mail
        Entry1.grid(row=1, column=2)
        
        Entry2 = ttk.Entry(self,width=20, validate="key") # Account Name
        Entry2['validatecommand'] = (Entry2.register(controller.validateString),'%P')
        Entry2.grid(row=2, column=2)
        label2 = ttk.Label(self, text="* Enter only 20 charecters",foreground='red', font=("Arial Italic", 10))
        
        label2.grid(row=2,column=3)

        Entry3 = ttk.Entry(self,width=20, show="*",validate="key") # PIN
        Entry3['validatecommand'] = (Entry3.register(controller.validatePIN),'%P')
        Entry3.grid(row=3, column=2)

        Entry4 = ttk.Entry(self,width=20, show="*",validate="key") # Re enter PIN
        Entry4['validatecommand'] = (Entry4.register(controller.validatePIN),'%P')
        Entry4.grid(row=4, column=2)
    
        button1 = ttk.Button(self, text ="Submit", command = lambda : submit_account()) 
        button1.grid(row = 6, column = 1,  padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Cancel", command = lambda : controller.show_frame(LoginPage)) 
        button2.grid(row = 6, column = 2, padx = 10, pady = 10) 

        def submit_account():
            account_name = Entry2.get()
            account_pin = Entry4.get()
            account_email = Entry1.get()
            account_create_date = "2021-04-15"
            store_account(account_name, account_pin, account_email, account_create_date)
            store_confirm("2021-04-15", "1.0")
            print("Confirmed Value is :",confirmed.get())
            controller.show_frame(LoginPage)

class ChildPage(tk.Frame):       
    def __init__(self, parent, controller): # controller is "child" of class health_app to call its functions
        tk.Frame.__init__(self, parent)
    
        label = ttk.Label(self, text ="Child Registration Page", style='My.TLabel',font="bold")        
        label.grid(row = 0, column = 1, padx = 10, pady = 10)

        button1 = ttk.Button(self, text ="Close", style='My.TButton', command = lambda : controller.show_frame(MainPage)) 
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
            CurrentDate =date.today()
            DOBDate = (Ent_child_bday.get_date())
           
            Day =(abs((CurrentDate - DOBDate).days))
            Days.set(str(Day))

            Age = int(Days.get())
            Agess = (Age/365)
            child_age .set(str('%.1f'%(Agess)))

        child_first_name = ttk.Label(self, font=("arial", 10, 'bold'),style='My.TLabel', text="child_first_name")
        child_first_name.grid(row=1, column=0,padx=5)
        Ent_child_first_name = ttk.Entry(self, font=("arial", 10, 'bold'), width=44)
        Ent_child_first_name .grid(row=1, column=1)

        lbl_child_last_name= ttk.Label(self, font=("arial", 10, 'bold'),style='My.TLabel', text="child_last_name")
        lbl_child_last_name.grid(row=2, column=0,padx=5)
        Ent_child_last_name = ttk.Entry(self, font=("arial", 10, 'bold'), width=44)
        Ent_child_last_name.grid(row=2, column=1)

        lbl_child_bday= ttk.Label(self, font=("arial", 10, 'bold'), style='My.TLabel', text="child_bday")
        lbl_child_bday.grid(row=3, column=0, padx=5)
        Ent_child_bday = DateEntry(self, font=("arial", 10, 'bold'), width=43, borderwidth=2, date_pattern='dd/mm/yyyy')
        Ent_child_bday.grid(row=3, column=1)

        lbl_child_age= ttk.Label(self, font=("arial", 10, 'bold'), style='My.TLabel',  text="child_age")
        lbl_child_age.grid(row=6, column=0,  padx=5)
        Ent_child_age = ttk.Label(self, font=("arial", 10, 'bold'), width=44, justify='left', textvariable=child_age)
        Ent_child_age.grid(row=6, column=1)

        lbl_child_gender= ttk.Label(self, font=("arial", 10, 'bold'), style='My.TLabel', text="child_gender")
        lbl_child_gender.grid(row=7, column=0, padx=5)

        #the variable 'var' mentioned here holds Integer Value, by deault 0
        var=tk.IntVar()
        tk.Radiobutton(self, text="Male",padx= 5, variable= var, value=1).grid(row=7, column=1)
        tk.Radiobutton(self, text="Female",padx= 20, variable= var, value=2).grid(row=7, column=2)

        #https://www.color-hex.com/color/008000
        #gui_style = ttk.Style()
        #gui_style.configure('My.TButton', background='#FFFF00', foreground='#FF0000')
        #gui_style.configure('My.TLabel', background='#FFFF00', foreground='#FF0000')
        #gui_style.configure('My.TLabel', background='#0000FF', foreground='#FFFFFF')
        gui_style = ttk.Style()
        gui_style.configure('My.TButton', background='yellow', foreground='red')
        gui_style.configure('My.TLabel', background='blue', foreground='white')
        gui_style.configure('My.TFrame', background='#FF0000')

        btnCalculate = ttk.Button(self, text="Calculate", style='My.TButton', command=lambda:  Results())
        btnCalculate.grid(row=9, column=0,padx=10,pady=2)
        
        btnReset = ttk.Button(self, text="Reset", style='My.TButton', command=lambda: Reset())
        btnReset.grid(row=9, column=1,padx=10,pady=2)
        
        btnExit = ttk.Button(self, text="Exit", style='My.TButton', command=lambda: iExit())
        btnExit.grid(row=9, column=2,padx=10,pady=2)

class MainPage(tk.Frame):      
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        label1 = ttk.Label(self, text ="USer Details - Main Page",font="bold",style='My.TLabel')        
        label1.grid(row = 0, column = 0, padx = 10, pady = 10)

        label2 = ttk.Label(self, text="Height in m", font=("Arial Italic", 10),style='My.TLabel')
        label2.grid(column=0, row=2)
        
        label3 = ttk.Label(self, text="Weight in Kg", font=("Arial Italic", 10),style='My.TLabel')
        label3.grid(column=0, row=3)

        label4 = ttk.Label(self, text="Age", font=("Arial Italic", 10),style='My.TLabel')
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

                            
        button2 = ttk.Button(self, text="BMI Chart", style='My.TButton',command = lambda: controller.show_frame(ChartPage))
        button2.grid(row = 6, column = 1,padx = 10, pady = 10) 

        button5 = ttk.Button(self, text ="Close", style='My.TButton',command = lambda : controller.show_frame(LoginPage)) 
        button5.grid(row = 6, column = 2,padx = 10, pady = 10) 

        button1 = ttk.Button(self, text="Calculate BMI", style='My.TButton',command=lambda:  calc_bmi())
        button1.grid(row = 6, column = 0,padx = 10, pady = 10) 

        button3 = ttk.Button(self, text="Register Child", style='My.TButton',command = lambda: controller.show_frame(ChildPage))
        button3.grid(row = 2, column = 3,padx = 10, pady = 10) 
        
        
        def calc_bmi(): # +++++++++++++++++++++++++++++++ calculation to be changed !
         height = Entry1.get()
         if height:
          height = float(height)
         weight = Entry2.get()
         if weight:
            weight = float(weight)
         BMI =  weight/(height*2)
         
         label5 = ttk.Label(self, text="BMI Index", font=("Arial Italic", 10),style='My.TLabel')
         label5.grid(column=0, row=5)

         label6 = ttk.Label(self, text=BMI, font=("Arial Italic", 10),style='My.TLabel')
         label6.grid(column=1, row=5)

class ChartPage(tk.Frame):      
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)

        label1 = ttk.Label(self, text ="BMI Chart Page",font="bold",style='My.TLabel')        
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
        # create pdf first
        pdf_w=210
        pdf_h=297
        f = 0
        child_first ="Max"

        pdf = FPDF('P', 'mm', 'A4')
        pdf.add_page()
        pdf.set_xy(0.0,0.0)
        pdf.set_font('Arial', 'B', 20)
        pdf.cell(210, 20, "BMI History Report of " + child_first+ child_first+ child_first,f,1, "C") # always centered in middle of page
        pdf.set_font('Arial', '', 12)
        pdf.cell(210, 12, 'Please consider our legal terms and conditions you agreed on by using this app', f, 1, 'L')
        pdf.cell(210, 12, 'Creation date: <current_date>', f, 1, 'L')
        pdf.cell(210, 12, 'Child First Name :		<child_first_name>', f, 1, 'L')
        pdf.cell(210, 12, 'Child Last Name :		<child_last_name>', f, 1, 'L')
        pdf.cell(210, 12, 'Child Birthday :		    <child_bday>', f, 1, 'L')
        pdf.cell(210, 12, 'Child gender :		    <child_gender>', f, 1, 'L')

        pdf.set_font('Arial', 'B', 12)
        pdf.cell(210, 12, 'Last BMI measurement on <logfile_date>', f, 1, 'L')
        pdf.set_font('Arial', '', 12)
        pdf.cell(210, 12, 'Height in m:		<last logfile entry>', f, 1, 'L')
        pdf.cell(210, 12, 'Weight in Kg:	<last logfile entry>', f, 1, 'L')
        pdf.cell(210, 12, 'BMI calculated:	<last logfile entry>', f, 1, 'L')

        pdf.image("./growthchart_example2.png",60,140,100,155)
        pdf.output('BMI_report_child_date_V2.pdf', 'F')
        
        # now export created file
        pdf_file = "/BMI_report_child_date_V2.pdf" # could include name of child account ?
        pdf_source = os.path.realpath(os.getcwd()) + pdf_file # get working directory -> later from specific folder
                    
        file = askdirectory() # ask user for folder to store(copy) pdf report; user can then use email to send away
        if file != "": # askdirectory() return "" if dialog closed with "cancel". -> nothing happens
            pdf_destination = file + pdf_file     
            shutil.copy (pdf_source, pdf_destination) # copy and overwrite file
            messagebox.showinfo("Notice !","Export of pdf report done")

# ++++++ functions for database modifications e.g. insert data, delete data, update data

if __name__ == "__main__":

    app = health_app()
    
    
    app.mainloop()

    