import tkinter as tk
from tkinter import StringVar, ttk
from numpy import var

class health_app(tk.Tk): # this is running any time and defining basic properties of an UI screen
     
    # __init__ function for class health_app 
    def __init__(self, *args, **kwargs): 
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)        
        self.wm_title("Child Health App") # Adding a title to the window
        self.geometry("400x400")
        
        # creating a container with command Frame ++++++++++++ how to set geometry ?
        container = tk.Frame(self, height=800, width=800) 
        container.pack(side = "top", fill = "both", expand = True) 
        
        # configuring the location of the container using grid  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
          
        self.frames = {}  # initializing frames to an empty array to store different names of frames (screens of UI)
        
        for F in (MainPage,RegisterPage,UserMainScreen):  # iterating through a tuple consisting of the different page layouts
            frame = F(container, self)  
            self.frames[F] = frame  # initializing frame of that object from different frames/screens respectively with for loop
            frame.grid(row = 0, column = 0, sticky ="nsew") # each frame has the same grid parameters for layout
         
        self.show_frame(MainPage) # first show Main page
  
    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class MainPage(tk.Frame):       # defining main page with nicer layout design using ttk of tkinter
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         
        label = ttk.Label(self, text ="Main Page", font="bold")        
        label.grid(row = 0, column = 1, padx = 10, pady = 10)
  
        button1 = ttk.Button(self, text ="Login", command = lambda : controller.show_frame(UserMainScreen))
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Register", command = lambda : controller.show_frame(RegisterPage))
        button2.grid(row = 3, column = 2, padx = 10, pady = 10)
        
        button3 = ttk.Button(self, text ="Import", command = lambda : controller.show_frame(RegisterPage))
        button3.grid(row = 3, column = 3, padx = 10, pady = 10)

        button4 = ttk.Button(self, text ="Export", command = lambda : controller.show_frame(RegisterPage))
        button4.grid(row = 3, column = 4, padx = 10, pady = 10)

        label1 = ttk.Label(self, text="PIN", font=("Arial Italic", 10))
        label1.grid(row=4, column=1)

        Entry1 = ttk.Entry(self,width=10, show="*")  # field entry for PIN
        Entry1.grid(row=4, column=2)


class RegisterPage(tk.Frame):       # defining Login page with nicer layout design using ttk of tkinter
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

        button1 = ttk.Button(self, text ="Submit", command = lambda : controller.show_frame(MainPage)) 
        button1.grid(row = 5, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="Cancel", command = lambda : controller.show_frame(MainPage)) 
        button2.grid(row = 5, column = 2, padx = 10, pady = 10) 


class UserMainScreen(tk.Frame):      
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        label1 = ttk.Label(self, text ="USer Details - Main",font="bold")        
        label1.grid(row = 0, column = 0, padx = 10, pady = 10)

        label2 = ttk.Label(self, text="Height", font=("Arial Italic", 10))
        label2.grid(column=1, row=1)
        
        label3 = ttk.Label(self, text="Weight", font=("Arial Italic", 10))
        label3.grid(column=1, row=2)

        label4 = ttk.Label(self, text="Age", font=("Arial Italic", 10))
        label4.grid(column=1, row=3)
        
        label5 = ttk.Label(self, text="BMI Index", font=("Arial Italic", 10))
        label5.grid(column=1, row=4)

        Entry1 = ttk.Entry(self,width=10) 
        Entry1.grid(column=2, row=1)
        
        Entry2 = ttk.Entry(self,width=10) 
        Entry2.grid(column=2, row=2)
        
        resultAge = ttk.Label(self, text = "10")
        resultAge.grid(column=2, row=3)
        
        Entry4 = ttk.Entry(self,width=10,show="22.1") 
        Entry4.grid(column=2, row=4)

        list_child = ("Max","Tom")
        var = 0

        for child in list_child:
         btn = tk.Button(self, text=child)
         btn.grid(row=5,column=var)
         var += 1
       
        button1 = ttk.Button(self, text="Calculate BMI", command=lambda:  calc_bmi(124, 10))
        button1.grid(row = 6, column = 0,padx = 10, pady = 10) 

        button2 = ttk.Button(self, text="BMI Chart", command=lambda: calc_bmi(124, 50))
        button2.grid(row = 6, column = 1,padx = 10, pady = 10) 

        button5 = ttk.Button(self, text ="Close", command = lambda : controller.show_frame(MainPage)) 
        button5.grid(row = 6, column = 2,padx = 10, pady = 10) 

        def calc_bmi(weight, height):
         return weight/(height*2)
        

if __name__ == "__main__":
    app = health_app()
    app.mainloop()
    