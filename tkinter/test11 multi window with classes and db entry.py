import tkinter as tk
from tkinter import ttk

import sqlite3 

conn = sqlite3.connect("./experiment11.db")
c = conn.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS user ( 
            name text
            )""")

# conn.close()
# def store_sql(*value_in): # can take more than on argument # +++++++ problem of closed database when not in class
#             with conn:
#                 c.execute("INSERT INTO user VALUES (?)", (value_in))
#             conn.close()

class health_app(tk.Tk): # this is running any time and defining basic properties of an UI screen
     
    # __init__ function for class health_app 
    def __init__(self, *args, **kwargs): 
         
        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)
        # Adding a title to the window
        self.wm_title("Child Healt App")
        
        # creating a container with command Frame ++++++++++++ how to set geometry ?
        container = tk.Frame(self, height=400, width=600) 
        container.pack(side = "top", fill = "both", expand = True) 
        
        # configuring the location of the container using grid  
        container.grid_rowconfigure(0, weight = 1)
        container.grid_columnconfigure(0, weight = 1)
          
        # initializing frames to an empty array to store different names of frames (screens of UI)
        self.frames = {}  
        # iterating through a tuple consisting of the different page layouts
        for F in (MainPage,LoginPage):  
            frame = F(container, self)  
            # initializing frame of that object from different frames/screens respectively with for loop
            self.frames[F] = frame  
            frame.grid(row = 0, column = 0, sticky ="nsew") # each frame has the same grid parameters for layout
            
  
        self.show_frame(LoginPage) # first show Main page
  
    # to display the current frame passed as parameter
    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class MainPage(tk.Frame):       # defining main page with nicer layout design using ttk of tkinter
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         
        label = ttk.Label(self, text ="Main Page")        
        label.grid(row = 0, column = 0, padx = 10, pady = 10) # putting the grid in its place by using grid
  
        button1 = ttk.Button(self, text ="to login", command = lambda : controller.show_frame(LoginPage))
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)

        label_widget = ttk.Label(self, text="Please enter", font=("Arial Italic", 10))
        label_widget.grid(column=0, row=1)
        
        txt_box = ttk.Entry(self,width=10)
        txt_box.grid(column=1, row=1)
        fn_btn = ttk.Button(self, text="Submit", command= lambda: store_sql(txt_box.get()))
        fn_btn.grid(column=2, row=1)

        def store_sql(*value_in): # can take more than on argument
            with conn:
                c.execute("INSERT INTO user VALUES (?)", (value_in))
            controller.show_frame(LoginPage) # switch to login page


class LoginPage(tk.Frame):       # defining Login page with nicer layout design using ttk of tkinter
    def __init__(self, parent, controller): 
        tk.Frame.__init__(self, parent)
         
        label = ttk.Label(self, text ="Login Page")        
        label.grid(row = 0, column = 0, padx = 10, pady = 10) # putting the grid in its place by using grid

        button1 = ttk.Button(self, text ="to main", command = lambda : controller.show_frame(MainPage)) 
        button1.grid(row = 3, column = 1, padx = 10, pady = 10)    

        label_widget = ttk.Label(self, text="Please enter", font=("Arial Italic", 10))
        label_widget.grid(column=0, row=1)
        
        txt_box = ttk.Entry(self,width=10)
        txt_box.grid(column=1, row=1)
        fn_btn = ttk.Button(self, text="Submit", command=lambda: store_sql(txt_box.get()))
        fn_btn.grid(column=2, row=1)

        def store_sql(*value_in): # can take more than on argument
            with conn: 
                c.execute("INSERT INTO user VALUES (?)", (value_in))
            controller.show_frame(MainPage) # switch to main page


""" 

conn.close() """

if __name__ == "__main__":
    app = health_app()
    app.mainloop()
    
