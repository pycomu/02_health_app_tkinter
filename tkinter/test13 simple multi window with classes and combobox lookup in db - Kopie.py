# https://stackoverflow.com/questions/32385771/how-can-i-dynamically-update-ttk-combobox

import tkinter as tk
from tkinter import ttk

import sqlite3 

conn = sqlite3.connect("./tkinter/test frame sqlite combobox.db")
c = conn.cursor()

class health_app(tk.Tk):    
    def __init__(self, *args, **kwargs): 
                
        tk.Tk.__init__(self, *args, **kwargs)        
        self.wm_title("Test App")
        self.geometry("400x300")
        
        container = tk.Frame(self) 
        container.pack(side = "top", fill = "both", expand = True) 
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
        self.frames = {}  
        for F in (LoginPage,RegisterPage):  # define names of 2 frames
            frame = F(container, self)  
            self.frames[F] = frame
            frame.grid(row = 0, column = 0, sticky ="nsew") # each frame has the same grid parameters for layout
            
        self.show_frame(LoginPage)
  
    def show_frame(self, cont):
        frame = self.frames[cont]
        # frame.place(width=400, height=300, relx=0.5, rely=0.5) # anchor= CENTER ????
        frame.tkraise()

        # read out database for gloabl variables, pointers for db navigation and array list for tkinter comboboxes
    def update_combo(self):
        c.execute("select account_name from account")
        account_names =[]
        for row in c.fetchall():
            account_names.append(row[0])
        return account_names

         
class LoginPage(tk.Frame):       
    def __init__(self, parent, controller): # controller is "child" of class health_app to call its functions
        tk.Frame.__init__(self, parent)
        
        label1 = ttk.Label(self, text ="Login Page",font="bold")        
        label1.grid(row = 0, column = 0, padx = 10, pady = 10) # putting the grid in its place by using grid

        label2 = ttk.Label(self, text="Chose Account", font=("Arial Italic", 10))
        label2.grid(column=0, row=1)
        
        # this callback is for debugging and checking the combobox content - later to be used for db operations !
        def callbackFunc(event): 
            print("Element Selected :",my_combobox.get())
            print(my_combobox['values'])

        
        self.combobox_value = tk.StringVar() 
        my_combobox = ttk.Combobox(self, height=4, width=10, textvariable=self.combobox_value,
            postcommand=lambda: my_combobox.configure(values=controller.update_combo()))
        my_combobox.grid(row=2, column=0)
        my_combobox['values'] = controller.update_combo() # name reading out the db table
        my_combobox.current(0)
        my_combobox.bind("<<ComboboxSelected>>", callbackFunc) # callback action whenever an item is selected
    
        button1 = ttk.Button(self, text="Register", command=lambda: controller.show_frame(RegisterPage))
        button1.grid(column=2, row=2)

        
class RegisterPage(tk.Frame):       # defining Login page with nicer layout design using ttk of tkinter
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
        
        label1 = ttk.Label(self, text ="Register Page",font="bold")        
        label1.grid(row = 0, column = 0, padx = 10, pady = 10)

        label2 = ttk.Label(self, text="New Account", font=("Arial Italic", 10))
        label2.grid(column=0, row=1)
        
        Entry1 = ttk.Entry(self,width=10) # field entry for account name
        Entry1.grid(column=0, row=2)
   
        # pushing submit collect all entries into a tuple and call the function to add new record in data table
        button1 = ttk.Button(self, text="Submit", command=lambda: store_sql(Entry1.get()))
        button1.grid(column=2, row=2)

        button5 = ttk.Button(self, text ="to main", command = lambda : controller.show_frame(LoginPage)) 
        button5.grid(row = 5, column = 1, padx = 10, pady = 10) 

        
        def store_sql(*value_in):
            print(value_in)
            with conn: 
                c.execute("INSERT INTO account VALUES (?)", (value_in))
            controller.show_frame(LoginPage) # switch to main page
            account_names = controller.update_combo() # can be deleted
            print("New Account list is :", account_names) # can be deleted

if __name__ == "__main__":
    app = health_app()
    app.mainloop()
    
