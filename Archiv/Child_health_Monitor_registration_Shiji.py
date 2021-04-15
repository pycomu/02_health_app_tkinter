from tkinter import *
from tkcalendar import *
from tkcalendar import Calendar
import tkinter.messagebox
#from tkcalendar import Calendar, DateEntry

root = Tk()
space = " "
root.title(185 * space + "User Registration")
root.geometry("1245x700+56+0")

MainFrame = Frame(root, bd = 10, width =1245, height=700, relief = RIDGE, bg="cadet blue")
MainFrame.grid()

TitleFrame = Frame(MainFrame, bd = 7, width =1245, height=70, relief = RIDGE)
TitleFrame.grid(row=0, column=0)

TopFrame3 = Frame(MainFrame, bd = 5, width =1245, height=500, relief = RIDGE)
TopFrame3.grid(row=1, column=0)

LeftFrame = Frame(TopFrame3, bd = 5, width =1245, height=400, padx=2, bg= "cadet blue", relief = RIDGE)
LeftFrame.pack(side=TOP, padx=10, pady=12)
LeftFrame1 = Frame(LeftFrame, bd = 5, width =600, height=180, padx=2, pady=4, relief = RIDGE)
LeftFrame1.pack(side=TOP, padx=10, pady=12)

RightFrame1 = Frame(TopFrame3, bd = 5, width =320, height=400, padx=2, bg= "cadet blue", relief=RIDGE)
RightFrame1.pack(side=RIGHT, padx=2)
RightFrame1a = Frame(RightFrame1, bd=5, width =310, height=300, padx=2, pady=2, relief=RIDGE)
RightFrame1a.pack(side=TOP, padx=5, pady=6)

lblTitle = Label(TitleFrame, font=("arial", 10, 'bold'), text="User Registration", bd=7)
lblTitle.grid(row=0, column=0, padx=30)

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
    child_age .set(str('%.0f'%(Agess)))

cal= Calendar(RightFrame1a,selectmode="day", year=2021, month=10, day=10, date_pattern='dd/mm/y', font=('arial', 10, 'bold'))
cal.grid(row=0, column=0, padx=10)

#********************************************************************************************

child_first_name = Label(LeftFrame1, font=("arial", 10, 'bold'), text="child_first_name", bd=7, anchor='w', justify=LEFT)
child_first_name.grid(row=0, column=0, sticky= W, padx=5)
Ent_child_first_name = Entry(LeftFrame1, font=("arial", 10, 'bold'), bd=5, width=44, justify=LEFT)
Ent_child_first_name .grid(row=0, column=1)

lbl_child_last_name= Label(LeftFrame1, font=("arial", 10, 'bold'), text="child_last_name", bd=7, anchor='w', justify=LEFT)
lbl_child_last_name.grid(row=1, column=0, sticky= W, padx=5)
Ent_child_last_name = Entry(LeftFrame1, font=("arial", 10, 'bold'), bd=5, width=44, justify=LEFT)
Ent_child_last_name.grid(row=1, column=1)

lbl_child_bday= Label(LeftFrame1, font=("arial", 10, 'bold'), text="child_bday", bd=7, anchor='w', justify=LEFT)
lbl_child_bday.grid(row=2, column=0, sticky= W, padx=5)
Ent_child_bday = DateEntry(LeftFrame1, font=("arial", 10, 'bold'), bd=5, width=43, borderwidth=2, date_pattern='dd/mm/yyyy')
Ent_child_bday.grid(row=2, column=1)

lbl_current_date= Label(LeftFrame1, font=("arial", 10, 'bold'), text="current_date", bd=7, anchor='w', justify=LEFT)
lbl_current_date.grid(row=3, column=0, sticky= W, padx=5)
Ent_current_date = DateEntry(LeftFrame1, font=("arial", 10, 'bold'), bd=5, width=43, borderwidth=2, date_pattern='dd/mm/yyyy')
Ent_current_date.grid(row=3, column=1)

lbl_days= Label(LeftFrame1, font=("arial", 10, 'bold'), text="Days", bd=7, anchor='w', justify=LEFT)
lbl_days.grid(row=4, column=0, sticky= W, padx=5)
Ent_days = Entry(LeftFrame1, font=("arial", 10, 'bold'), bd=5, width=44, justify='left', textvariable=Days)
Ent_days.grid(row=4, column=1)


lbl_child_age= Label(LeftFrame1, font=("arial", 10, 'bold'), text="child_age", bd=7, anchor='w', justify=LEFT)
lbl_child_age.grid(row=5, column=0, sticky= W, padx=5)
Ent_child_age = Entry(LeftFrame1, font=("arial", 10, 'bold'), bd=5, width=44, justify='left', textvariable=child_age)
Ent_child_age.grid(row=5, column=1)

lbl_child_gender= Label(LeftFrame1, font=("arial", 10, 'bold'), text="child_gender", bd=7, anchor='w', justify=LEFT)
lbl_child_gender.grid(row=6, column=0, sticky= W, padx=5)

#the variable 'var' mentioned here holds Integer Value, by deault 0
var=IntVar()
#this creates 'Radio button' widget and uses place() method
Radiobutton(LeftFrame1,justify='left', text="Male",padx= 5, variable= var, value=1).place(x=235,y=200)
Radiobutton(LeftFrame1,justify='left', text="Female",padx= 20, variable= var, value=2).place(x=290,y=200)

#********************************************************************************************

btnCalculate = Button(RightFrame1a, padx=10, bd=7,font =('Helvetical', 10, 'bold'), width=23, text="Calculate", bg='cadetblue',command=Results)
btnCalculate.grid(row=1, column=0,padx=10,pady=2)

btnReset = Button(RightFrame1a, padx=10, bd=7,font =('Helvetical', 10, 'bold'), width=23, text="Reset", bg='cadetblue',command=Reset)
btnReset.grid(row=2, column=0,padx=10,pady=2)

btnExit = Button(RightFrame1a, padx=10, bd=7,font =('Helvetical', 10, 'bold'), width=23, text="Exit", bg='cadetblue', command=iExit)
btnExit.grid(row=3, column=0,padx=10,pady=2)

root.mainloop()
