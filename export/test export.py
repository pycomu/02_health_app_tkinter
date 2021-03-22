
import os
import shutil

from tkinter import * 
from tkinter import ttk 
  
from tkinter.filedialog import askdirectory
  
root = Tk() 
root.geometry('200x300') 
  
def save1(): 
    
    src = os.path.realpath(os.getcwd()) + "/export/text.txt"
    print("Source ", src)
        
    file = askdirectory()
    print("new dir ",file)
    dst = file + "/text_backup.txt"
    print("Destination ", dst)
    
    shutil.copy (src, dst) # copy and overwrite file
    

def save3(self):
        file = get_selection()
        if os.path.exists(file):
            if os.path.isdir(file):
                self.master.bell()
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
        self.quit(file)



btn1 = ttk.Button(root, text = 'Save 1', command = lambda : save1()) 
btn1.pack(side = TOP, pady = 20) 


btn3 = ttk.Button(root, text = 'Save 3', command = lambda : save3()) 
btn3.pack(side = TOP, pady = 20) 
  
mainloop() 