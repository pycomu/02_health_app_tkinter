from tkinter import *
# imports every exposed object in Tkinter 
#Tkinter is the standard GUI library for Python.

def calc_BMI ():
    pass

def input_value():
    #creating basic Tkinter window
    window= Tk()
    window.geometry("750x400")
    #setting the default window size using geometry function. size of the window width=750 and height =400

    window.resizable(0,0)
    #this prevents from resizing the window

    window.title("Child Health Monitor")
    #giving title for the window

    #**************************************************************
    # Age in years

    Agelabel=StringVar()
    #value holder for string variables

    Agelabel.set("Age")
    #set the variable to the VALUE

    Agetitle=Label(window, textvariable=Agelabel,bg="yellow",fg="green",font=("Calibri",20))

    Agetitle.grid(row=0, column=0)
    #grid uses the matrix row column concepts to organize the widgets

    Age= IntVar() 
    #value holder for integer variables

    spinlength= Spinbox(window, from_=1, to_=14, textvariable=Age, width=13,font=("Calibri",20))

    spinlength.grid(row=0,column=1)



    #*****************************************************************
    # Gender male, female, no say

    genderlabel=StringVar()
    #value holder for string variables

    genderlabel.set("Gender:")
    #set the variable to the VALUE

    gendertitle=Label(window, textvariable=genderlabel,bg="yellow",fg="green",font=("Calibri",20))

    gendertitle.grid(row=5, column=0)
    #grid uses the matrix row column concepts to organize the widgets

    Gender= IntVar() 
    #value holder for integer variables

    rad1= Radiobutton(window, text='Male', variable=Gender, value=1, font=("Calibri",20))
    rad2= Radiobutton(window, text='Female', variable=Gender, value=2, font=("Calibri",20))
    rad3= Radiobutton(window, text='No say', variable=Gender, value=3, font=("Calibri",20))

    rad1.grid(column=1, row=5)
    rad2.grid(column=2, row=5)
    rad3.grid(column=3, row=5)


    #********************************************************
    #Height in Meter, for user in cm
    #creating text label and input label


    heightlabel=StringVar()
    #value holder for string variables

    heightlabel.set("Height:")
    #set the variable to the VALUE

    heighttitle=Label(window, textvariable=heightlabel,bg="yellow",fg="green",font=("Calibri",20))

    heighttitle.grid(row=7, column=0)
    #grid uses the matrix row column concepts to organize the widgets

    Height= IntVar() 
    #value holder for integer variables

    height= Entry(window)
    height.grid(row=7, column=1)


    rad4= Radiobutton(window, text='cm', variable=Height, value=4, font=("Calibri",20))
    rad5= Radiobutton(window, text='Inch',variable=Height, value=5, font=("Calibri",20))
    rad6= Radiobutton(window, text='Feet', variable=Height, value=6, font=("Calibri",20))

    rad4.grid(column=2, row=7)
    rad5.grid(column=3, row=7)
    rad6.grid(column=4, row=7)


    #********************************************************
    #Weight in Kg
    #creating text label and input label

    weightlabel=StringVar()
    #value holder for string variables

    weightlabel.set("Weight:")
    #set the variable to the VALUE

    weighttitle=Label(window, textvariable=weightlabel,bg="yellow",fg="green",font=("Calibri",20))

    weighttitle.grid(row=8, column=0)
    #grid uses the matrix row column concepts to organize the widgets

    Weight= IntVar() 
    #value holder for integer variables

    weight= Entry(window)
    weight.grid(row=8, column=1)


    rad7= Radiobutton(window, text='Kg', variable=Weight, value=7, font=("Calibri",20))
    rad8= Radiobutton(window, text='Pound', variable=Weight, value=8, font=("Calibri",20))
   

    rad7.grid(column=2, row=8)
    rad8.grid(column=3, row=8)
    
    
    #***************************************************
    #BMI Generate


    btn=Button(window,text="BMI Generate",bg="orange",fg="red",command=calc_BMI ,font=("Calibri",20))
    #bg and fg changing the background and foreground colour

    btn.grid(row=9,column=0)

    bmi_label=Label(window,font=("Calibri",30))
    #setting the label font
    bmi_label.grid(row=9,column=1) 
    

    window.mainloop()

input_value()

