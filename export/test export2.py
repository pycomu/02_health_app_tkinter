# https://www.geeksforgeeks.org/python-asksaveasfile-function-in-tkinter/
# https://stackoverflow.com/questions/19476232/save-file-dialog-in-tkinter

from tkinter import * 
from tkinter import ttk 
  
# import only asksaveasfile from filedialog 
# which is used to save file in any extension 
from tkinter.filedialog import asksaveasfile 
from tkinter import filedialog

root = Tk() 
root.geometry('200x300') 
  
# function to call when user press 
# the save button, a filedialog will 
# open and ask to save file 
def save1(): 
    files = [('All Files', '*.*'),  
             ('Python Files', '*.db'), 
             ('Text Document', '*.pdf')] 
    file = asksaveasfile(filetypes = files, defaultextension = files) 

def save2():
    
    files = [('db file', '*.db')] 
    f = filedialog.askopenfilename(initialdir = "./", title = "Select the db File",filetypes = files)
    print("you have choosen :",f)

# save as file dialog - how to not allow overwrite
# https://stackoverflow.com/questions/29492832/save-as-file-dialog-how-to-not-allow-overwrite

import os

def save3():
        file = "./text.txt"
        if os.path.exists(file):
            if os.path.isdir(file):
                # self.master.bell()
                return
            d = Dialog(self.top,
                       title="Overwrite Existing File",
                       text="You can't overwrite an existing file %r. Please select a new name." % (file,),
                       bitmap='error',
                       default=0,
                       strings=("OK",))
            return
        else:
            head, tail = os.path.split(file)
            if not os.path.isdir(head):
                self.master.bell()
                return
        quit(file)



btn1 = ttk.Button(root, text = 'Save 1', command = lambda : save1()) 
btn1.pack(side = TOP, pady = 20) 

btn2 = ttk.Button(root, text = 'Save 2', command = lambda : save2()) 
btn2.pack(side = TOP, pady = 20) 

btn3 = ttk.Button(root, text = 'Save 3', command = lambda : save3()) 
btn3.pack(side = TOP, pady = 20) 
  
mainloop() 