# Main code to be developed, principle in pseudo code:
# 1 Import dependencies
# 2 define global variables to refelct at any time which account, which user, which last log file entry
# 3 read out last log entry on current account, user and store in global variables
# 4 open windows (UI) and perform data entries to be stored, changed in database
# 5 switch on only relevant UI and focus for data manipulation

# import the Libraries
#import tkinter as tk
#from tkinter import *
#import mysql.connector
import pandas as pd
from pandas import Series,DataFrame
from PIL import Image, ImageTk


""" # Global variables along database structure
"account_id"	INTEGER,
"account_name"	VARCHAR(20),
"account_email"	TEXT, or account_email_id
"account_pin"	text,
"user_id"	INTEGER, or child_id
"user_name"	VARCHAR(20), or child_first_name and child_last_name
"user_gender"	TEXT,
"user_dob"	INTEGER,or child_dob
"log_id"	INTEGER, or log_id  
"entry_time"	TIMESTAMP, or time_stamp
"height"	FLOAT, or child_height
"weight"	FLOAT, or child_weight
"age"	INTEGER, or child_age
"bmi"	FLOAT, or child_genderchild_BMI
"""
#importing tkinter module for GUI application
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
def user_registration():

    #Creating object 'root' of Tk()
    root = Tk()
    #Providing Geometry to the form
    root.geometry("500x500")

    #Providing title to the form
    root.title('User Information')

    #this creates 'Label' widget for User Information and uses place() method.
    label_0 =Label(root,text="User Information", width=20,font=("bold",20))
    #place method in tkinter is  geometry manager it is used to organize widgets by placing them in specific position
    label_0.place(x=90,y=60)

    #this creates 'Label' widget for child_first_name and uses place() method.
    child_first_name =Label(root,text="child_first_name", width=20,font=("bold",10))
    child_first_name.place(x=80,y=130)

    #this will accept the input string text from the user.
    child_first_name_entry_1=Entry(root)
    child_first_name_entry_1.place(x=240,y=130)

    #this creates 'Label' widget for child_last_name and uses place() method.
    child_last_name =Label(root,text="child_last_name", width=20,font=("bold",10))
    child_last_name.place(x=68,y=180)

    child_last_name_entry_3=Entry(root)
    child_last_name_entry_3.place(x=240,y=180)

    #this creates 'Label' widget for child Gender and uses place() method.
    child_gender =Label(root,text="child_gender", width=20,font=("bold",10))
    child_gender.place(x=70,y=230)


    #the variable 'var' mentioned here holds Integer Value, by deault 0
    var=IntVar()

    #this creates 'Radio button' widget and uses place() method
    Radiobutton(root,text="Male",padx= 5, variable= var, value=1).place(x=235,y=230)
    Radiobutton(root,text="Female",padx= 20, variable= var, value=2).place(x=290,y=230)

    ##this creates 'Label' widget for child date of birth and uses place() method.
    child_dob=Label(root,text="child_dob",width=20,font=('bold',10))
    child_dob.place(x=75,y=330)


    def example3():
        
        top = tk.Toplevel(root1)
        

        ttk.Label(top, text='Choose date').pack(padx=10, pady=10)

        cal = DateEntry(top, width=12, background='darkblue',
                            foreground='white', borderwidth=2, year=2010)
        cal.pack(padx=10, pady=10)


    ##this creates 'Label' widget for user country and uses place() method.
    user_Country=Label(root,text="Country",width=20,font=("bold",10))
    user_Country.place(x=70,y=280)

    #this creates list of countries available in the dropdownlist.
    list_of_country=[ 'India' ,'US' , 'UK' ,'Germany' ,'Austria']

    #the variable 'c' mentioned here holds String Value, by default ""
    c=StringVar()
    droplist=OptionMenu(root,c, *list_of_country)
    droplist.config(width=15)
    c.set('Select your Country')
    droplist.place(x=240,y=280)

    #this creates button for submitting the details provides by the user
    Button(root, text='Submit' , width=20,bg="black",fg='white').place(x=280,y=380)

    #this creates button for cancel the details provides by the user
    Button(root, text='Cancel' , width=20,bg="black",fg='white').place(x=100,y=380)


    #this will run the mainloop.
    root1 = tk.Tk()   
    Button(root, text='DateEntry' , command=example3, width=20,).place(x=240,y=320)
    #ttk.Button(root, text='DateEntry', command=example3).pack(padx=120, pady=210)
    root.mainloop()
user_registration()


def calc_BMI ():
    pass

def main_user_UI():
    #creating basic Tkinter window
    window= Tk()
    window.geometry("750x400")
    #setting the default window size using geometry function. size of the window width=750 and height =400

    window.resizable(0,0)
    #this prevents from resizing the window

    window.title("Main UI")
    #giving title for the window

    #**************************************************************
    # Age in years
    Agelabel=StringVar()
    #value holder for string variables

    Agelabel.set("child_age")
    #set the variable to the VALUE

    Agetitle=Label(window, textvariable=Agelabel,bg="yellow",fg="green",font=("Calibri",20))

    Agetitle.grid(row=0, column=0)
    #grid uses the matrix row column concepts to organize the widgets

    Age= IntVar() 
    #value holder for integer variables

    spinlength= Spinbox(window, from_=1, to_=14, textvariable=Age, width=13,font=("Calibri",20))

    spinlength.grid(row=0,column=1) 


    #********************************************************
    #Height in Meter, for user in cm
    #creating text label and input label

    heightlabel=StringVar()
    #value holder for string variables

    heightlabel.set("child_height")
    #set the variable to the VALUE

    heighttitle=Label(window, textvariable=heightlabel,bg="yellow",fg="green",font=("Calibri",20))

    heighttitle.grid(row=7, column=0)
    #grid uses the matrix row column concepts to organize the widgets

    Height= IntVar() 
    #value holder for integer variables

    spinlength= Spinbox(window, from_=15, to_=150, textvariable=heighttitle, width=13,font=("Calibri",20))

    spinlength.grid(row=7,column=1) 

    #********************************************************
    #Weight in Kg
    #creating text label and input label

    weightlabel=StringVar()
    #value holder for string variables

    weightlabel.set("child_weight")
    #set the variable to the VALUE

    weighttitle=Label(window, textvariable=weightlabel,bg="yellow",fg="green",font=("Calibri",20))

    weighttitle.grid(row=8, column=0)
    #grid uses the matrix row column concepts to organize the widgets

    Weight= IntVar() 
    #value holder for integer variables

    spinlength= Spinbox(window, from_=1, to_=100, increment_=0.1,textvariable=weighttitle, width=13,font=("Calibri",20))

    spinlength.grid(row=8,column=1) 

    
    #***************************************************
    #BMI Generate


    btn=Button(window,text="BMI Generate",bg="orange",fg="red",command=calc_BMI ,font=("Calibri",20))
    #bg and fg changing the background and foreground colour

    btn.grid(row=9,column=0)

    bmi_label=Label(window,font=("Calibri",30))
    #setting the label font
    bmi_label.grid(row=9,column=1) 
    

    window.mainloop()

main_user_UI()

#*********************************************************
#Age Calculator
from tkinter import *
from datetime import date
root = Tk()
root.geometry("700x500")
root.title("Age Calculator")

def calculateAge():
    today = date.today()
    birthDate = date(int(yearEntry.get()), int(monthEntry.get()), int(dayEntry.get()))
    age = today.year - birthDate.year - ((today.month, today.day) < (birthDate.month, birthDate.day))
    Label(text=f"{nameValue.get()} your age is {age}").grid(row=6, column=1)
    
Label(text="Name").grid(row=1, column=0, padx=90)
Label(text="Year").grid(row=2, column=0)
Label(text="Month").grid(row=3, column=0)
Label(text="Day").grid(row=4, column=0)

nameValue = StringVar()
yearValue = StringVar()
monthValue = StringVar()
dayValue = StringVar()

nameEntry = Entry(root, textvariable=nameValue)
yearEntry = Entry(root, textvariable=yearValue)
monthEntry = Entry(root, textvariable=monthValue)
dayEntry = Entry(root, textvariable=dayValue)

nameEntry.grid(row=1, column=1, pady=10)
yearEntry.grid(row=2, column=1, pady=10)
monthEntry.grid(row=3, column=1, pady=10)
dayEntry.grid(row=4, column=1, pady=10)

computeButton = Button(text="CalculateAge", command=calculateAge)
computeButton.grid(row=5, column=1, pady=10)
root.mainloop()
#**********************************************
#Age calculator using todays date
# import all functions from the tkinter 
from tkinter import *

# import messagebox class from tkinter
from tkinter import messagebox

# Function for clearing the 
# contents of all text entry boxes
def clearAll() :

	# deleting the content from the entry box
	dayField.delete(0, END)
	monthField.delete(0, END)
	yearField.delete(0, END)
	givenDayField.delete(0, END)
	givenMonthField.delete(0, END)
	givenYearField.delete(0, END)
	rsltDayField.delete(0, END)
	rsltMonthField.delete(0, END)
	rsltYearField.delete(0, END)

# function for checking error
def checkError() :

	# if any of the entry field is empty
	# then show an error message and clear 
	# all the entries
	if (dayField.get() == "" or monthField.get() == ""
		or yearField.get() == "" or givenDayField.get() == ""
		or givenMonthField.get() == "" or givenYearField.get() == "") :

		# show the error message
		messagebox.showerror("Input Error")

		# clearAll function calling
		clearAll()
		
		return -1

# function to calculate Age 
def calculateAge() :

	# check for error
	value = checkError()

	# if error is occur then return
	if value == -1 :
		return
	
	else :
		
		# take a value from the respective entry boxes
		# get method returns current text as string
		birth_day = int(dayField.get())
		birth_month = int(monthField.get())
		birth_year = int(yearField.get())

		given_day = int(givenDayField.get())
		given_month = int(givenMonthField.get())
		given_year = int(givenYearField.get())
		
		
		# if birth date is greater then given birth_month 
		# then donot count this month and add 30 to the date so 
		# as to subtract the date and get the remaining days 
		month =[31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
		
		if (birth_day > given_day):
			given_month = given_month - 1
			given_day = given_day + month[birth_month-1] 
					
					
		# if birth month exceeds given month, then 
		# donot count this year and add 12 to the 
		# month so that we can subtract and find out 
		# the difference 
		if (birth_month > given_month):
			given_year = given_year - 1
			given_month = given_month + 12
					
		# calculate day, month, year 
		calculated_day = given_day - birth_day; 
		calculated_month = given_month - birth_month; 
		calculated_year = given_year - birth_year;

		# calculated day, month, year write back
		# to the respective entry boxes

		# insert method inserting the 
		# value in the text entry box.
		
		rsltDayField.insert(10, str(calculated_day))
		rsltMonthField.insert(10, str(calculated_month))
		rsltYearField.insert(10, str(calculated_year))
	

# Driver Code
if __name__ == "__main__" :

	# Create a GUI window
	gui = Tk()

	# Set the background colour of GUI window 
	gui.configure(background = "light green")

	# set the name of tkinter GUI window 
	gui.title("Age Calculator")

	# Set the configuration of GUI window
	gui.geometry("525x260")

	# Create a Date Of Birth : label 
	dob = Label(gui, text = "Date Of Birth", bg = "blue")

	# Create a Given Date : label
	givenDate = Label(gui, text = "Given Date", bg = "blue")

	# Create a Day : label
	day = Label(gui, text = "Day", bg = "light green")

	# Create a Month : label
	month = Label(gui, text = "Month", bg = "light green")

	# Create a Year : label
	year = Label(gui, text = "Year", bg = "light green")

	# Create a Given Day : label
	givenDay = Label(gui, text = "Given Day", bg = "light green")

	# Create a Given Month : label
	givenMonth = Label(gui, text = "Given Month", bg = "light green")

	# Create a Given Year : label
	givenYear = Label(gui, text = "Given Year", bg = "light green")

	# Create a Years : label
	rsltYear = Label(gui, text = "Years", bg = "light green")

	# Create a Months : label
	rsltMonth = Label(gui, text = "Months", bg = "light green")

	# Create a Days : label
	rsltDay = Label(gui, text = "Days", bg = "light green")

	# Create a Resultant Age Button and attached to calculateAge function
	resultantAge = Button(gui, text = "Resultant Age", fg = "Black", bg = "Red", command = calculateAge)

	# Create a Clear All Button and attached to clearAll function
	clearAllEntry = Button(gui, text = "Clear All", fg = "Black", bg = "Red", command = clearAll)

	# Create a text entry box for filling or typing the information. 
	dayField = Entry(gui)
	monthField = Entry(gui)
	yearField = Entry(gui)
	
	givenDayField = Entry(gui)
	givenMonthField = Entry(gui)
	givenYearField = Entry(gui)
	
	rsltYearField = Entry(gui)
	rsltMonthField = Entry(gui)
	rsltDayField = Entry(gui)


	# grid method is used for placing 
	# the widgets at respective positions 
	# in table like structure .
	dob.grid(row = 0, column = 1)
	
	day.grid(row = 1, column = 0)
	dayField.grid(row = 1, column = 1)
	
	month.grid(row = 2, column = 0)
	monthField.grid(row = 2, column = 1)
	
	year.grid(row = 3, column = 0)
	yearField.grid(row = 3, column = 1)
	
	givenDate.grid(row = 0, column = 4)
	
	givenDay.grid(row = 1, column = 3)
	givenDayField.grid(row = 1, column = 4)
	
	givenMonth.grid(row = 2, column = 3)
	givenMonthField.grid(row = 2, column = 4)
	
	givenYear.grid(row = 3, column = 3)
	givenYearField.grid(row = 3, column = 4)
	
	resultantAge.grid(row = 4, column = 2)
	
	rsltYear.grid(row = 5, column = 2)
	rsltYearField.grid(row = 6, column = 2)
	
	rsltMonth.grid(row = 7, column = 2)
	rsltMonthField.grid(row = 8, column = 2)
	
	rsltDay.grid(row = 9, column = 2)
	rsltDayField.grid(row = 10, column = 2)

	clearAllEntry.grid(row = 12, column = 2)

	# Start the GUI
	gui.mainloop() 
