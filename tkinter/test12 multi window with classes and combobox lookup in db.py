import tkinter as tk
from tkinter import ttk

import sqlite3 

conn = sqlite3.connect("./experiment12.db")
c = conn.cursor()

# read out database for gloabl variables, pointers for db navigation and array list for tkinter comboboxes
c.execute("select account_id, account_name from account")
account_names =[]
for row in c.fetchall():
    print("Id: ", row[0])
    print("Acc. Name: ", row[1])
    account_names.append(row[1])
print(account_names)
no_account = False


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
        
        for F in (MainPage,LoginPage,RegisterPage):  # iterating through a tuple consisting of the different page layouts
            frame = F(container, self)  
            self.frames[F] = frame  # initializing frame of that object from different frames/screens respectively with for loop
            frame.grid(row = 0, column = 0, sticky ="nsew") # each frame has the same grid parameters for layout
         
        self.show_frame(LoginPage) # first show Main page
  
    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class MainPage(tk.Frame):       # defining main page with nicer layout design using ttk of tkinter
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         
        label = ttk.Label(self, text ="Main Page", font="bold")        
        label.grid(row = 0, column = 0, padx = 10, pady = 10) # putting the grid in its place by using grid
  
        button1 = ttk.Button(self, text ="to login", command = lambda : controller.show_frame(LoginPage))
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)

        button2 = ttk.Button(self, text ="to register", command = lambda : controller.show_frame(RegisterPage))
        button2.grid(row = 3, column = 2, padx = 10, pady = 10)

        
class LoginPage(tk.Frame):       # defining Login page with nicer layout design using ttk of tkinter
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         
        label1 = ttk.Label(self, text ="Login Page",font="bold")        
        label1.grid(row = 0, column = 0, padx = 10, pady = 10) # putting the grid in its place by using grid

        label2 = ttk.Label(self, text="Chose Account", font=("Arial Italic", 10))
        label2.grid(column=0, row=1)
        label3 = ttk.Label(self, text="Enter PIN", font=("Arial Italic", 10))
        label3.grid(column=1, row=1)

        # this callback to use to change the global variable account_id according the choice in combobox
        def callbackFunc(event): 
            print("New Element Selected :",my_combobox.get())

        self.combobox_value = tk.StringVar()
        my_combobox = ttk.Combobox(self, height=4, width=10, textvariable=self.combobox_value)
        my_combobox.grid(row=2, column=0)
        my_combobox['values'] = account_names
        my_combobox.current(0)
        my_combobox.bind("<<ComboboxSelected>>", callbackFunc) # callback action whenever an item is selected

    
        Entry1 = ttk.Entry(self,width=10, show="*") # field entry for account PIN
        Entry1.grid(column=1, row=2)

        button1 = ttk.Button(self, text="Login", command=lambda: controller.show_frame(MainPage))
        button1.grid(column=2, row=2)

        button2 = ttk.Button(self, text="Register")
        button2.grid(column=0, row=3)

        button3 = ttk.Button(self, text="Import")
        button3.grid(column=1, row=3)

        button4 = ttk.Button(self, text="Export")
        button4.grid(column=2, row=3)

        button5 = ttk.Button(self, text ="to main", command = lambda : controller.show_frame(MainPage)) 
        button5.grid(row = 4, column = 1, padx = 10, pady = 10)    
        # manually block login button
        button6 = ttk.Button(self, text="Test block login", command=lambda:button1.config(state="disabled"))
        button6.grid(column=2, row=4)

        print(no_account)
        if no_account == True:      # if global var no_account is True, then disable buttons like login, etc
            button1.config(state="disabled")

        def store_sql(*value_in): # can take more than on argument
            with conn: 
                c.execute("INSERT INTO user VALUES (?)", (value_in))
            controller.show_frame(MainPage) # switch to main page

class RegisterPage(tk.Frame):       # defining Login page with nicer layout design using ttk of tkinter
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         
        label1 = ttk.Label(self, text ="Register Page",font="bold")        
        label1.grid(row = 0, column = 0, padx = 10, pady = 10)

        label2 = ttk.Label(self, text="Account Name", font=("Arial Italic", 10))
        label2.grid(column=0, row=1)
        
        label3 = ttk.Label(self, text="Enter PIN", font=("Arial Italic", 10))
        label3.grid(column=1, row=1)

        Entry1 = ttk.Entry(self,width=10) # field entry for account name
        Entry1.grid(column=0, row=2)
        
        Entry2 = ttk.Entry(self,width=10,show="*") # field entry for account PIN
        Entry2.grid(column=1, row=2)

        button1 = ttk.Button(self, text="Submit", command=lambda: store_sql(txt_box.get()))
        button1.grid(column=2, row=2)

        button5 = ttk.Button(self, text ="to main", command = lambda : controller.show_frame(MainPage)) 
        button5.grid(row = 4, column = 1, padx = 10, pady = 10)    
        
        def store_sql(*value_in): # can take more than on argument
            with conn: 
                c.execute("INSERT INTO user VALUES (?)", (value_in))
            controller.show_frame(MainPage) # switch to main page




""" 

conn.close() """

if __name__ == "__main__":
    app = health_app()
    app.mainloop()
    
