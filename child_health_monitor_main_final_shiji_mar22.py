#importing tkinter module for GUI application
import tkinter as tk
from tkinter import *
import tkcalendar
from tkinter import ttk
from tkcalendar import Calendar, DateEntry
import tkinter.messagebox


def user_registration():

    #Creating object 'root' of Tk()
    root = Tk()
    #Providing Geometry to the form
    root.geometry("900x400")

    #Providing title to the form
    root.title('User Information')

    #this creates 'Label' widget for User Information and uses place() method.
    label_0 =Label(root,text="User Information", width=15,font=("bold",20))
    label_0.grid(row=0,column=1)

    #********************************************************************************************
    child_bday = StringVar()
    current_date = StringVar()
    Days = StringVar()
    child_age = StringVar()
    Months = StringVar()
    child_gender = StringVar()

    def Reset():
        child_bday.set("") 
        current_date.set("")  
        Days.set("") 
        child_age.set("") 
        Months.set("")
        child_gender.set("")
        Ent_child_first_name.delete(0, END)
        Ent_child_last_name.delete(0, END)

    def iExit():
        iExit =tkinter.messagebox.askyesno("User Registration", "Confirm if you want to Exit")
        if iExit>=0:
            root.destroy()
            return
        

    def Results():
        CurrentDate =(Ent_current_date.get_date())
        DOBDate = (Ent_child_bday.get_date())

        Day =(abs((CurrentDate - DOBDate).days))
        Days.set(str(Day))

        Age = int(Days.get())
        Agess = (Age/365)
        child_age .set(str('%.1f'%(Agess)))

    child_first_name = Label(root, font=("arial", 10, 'bold'), text="child_first_name", bd=7, anchor='w', justify=LEFT)
    child_first_name.grid(row=1, column=0, sticky= W, padx=5)
    Ent_child_first_name = Entry(root, font=("arial", 10, 'bold'), bd=5, width=44, justify=LEFT)
    Ent_child_first_name .grid(row=1, column=1)

    lbl_child_last_name= Label(root, font=("arial", 10, 'bold'), text="child_last_name", bd=7, anchor='w', justify=LEFT)
    lbl_child_last_name.grid(row=2, column=0, sticky= W, padx=5)
    Ent_child_last_name = Entry(root, font=("arial", 10, 'bold'), bd=5, width=44, justify=LEFT)
    Ent_child_last_name.grid(row=2, column=1)

    lbl_child_bday= Label(root, font=("arial", 10, 'bold'), text="child_bday", bd=7, anchor='w', justify=LEFT)
    lbl_child_bday.grid(row=3, column=0, sticky= W, padx=5)
    Ent_child_bday = DateEntry(root, font=("arial", 10, 'bold'), bd=5, width=43, borderwidth=2, date_pattern='dd/mm/yyyy')
    Ent_child_bday.grid(row=3, column=1)

    lbl_current_date= Label(root, font=("arial", 10, 'bold'), text="current_date", bd=7, anchor='w', justify=LEFT)
    lbl_current_date.grid(row=4, column=0, sticky= W, padx=5)
    Ent_current_date = DateEntry(root, font=("arial", 10, 'bold'), bd=5, width=43, borderwidth=2, date_pattern='dd/mm/yyyy')
    Ent_current_date.grid(row=4, column=1)

    lbl_child_age= Label(root, font=("arial", 10, 'bold'), text="child_age", bd=7, anchor='w', justify=LEFT)
    lbl_child_age.grid(row=6, column=0, sticky= W, padx=5)
    Ent_child_age = Entry(root, font=("arial", 10, 'bold'), bd=5, width=44, justify='left', textvariable=child_age)
    Ent_child_age.grid(row=6, column=1)

    lbl_child_gender= Label(root, font=("arial", 10, 'bold'), text="child_gender", bd=7, anchor='w', justify=LEFT)
    lbl_child_gender.grid(row=7, column=0, sticky= W, padx=5)

    #the variable 'var' mentioned here holds Integer Value, by deault 0
    var=IntVar()
    #this creates 'Radio button' widget and uses place() method
    Radiobutton(root,justify='left', text="Male",padx= 5, variable= var, value=1).grid(row=7, column=1)
    Radiobutton(root,justify='left', text="Female",padx= 20, variable= var, value=2).grid(row=7, column=2)

    btnCalculate = Button(root, padx=10, bd=7,font =('Helvetical', 10, 'bold'), width=23, text="Calculate", bg='cadetblue',command=Results)
    btnCalculate.grid(row=9, column=0,padx=10,pady=2)

    btnReset = Button(root, padx=10, bd=7,font =('Helvetical', 10, 'bold'), width=23, text="Reset", bg='cadetblue',command=Reset)
    btnReset.grid(row=9, column=1,padx=10,pady=2)

    btnExit = Button(root, padx=10, bd=7,font =('Helvetical', 10, 'bold'), width=23, text="Exit", bg='cadetblue', command=iExit)
    btnExit.grid(row=9, column=2,padx=10,pady=2)

    root.mainloop()
user_registration()

