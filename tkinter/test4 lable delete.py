# https://www.geeksforgeeks.org/how-to-hide-recover-and-delete-tkinter-widgets/

from tkinter import *
 
# toplevel window 
root = Tk() 
  
# label widget 
mylabel = Label(root, text="GeeksforGeeks") 
mylabel.pack() 
  
# delete_label() function  to delete Label(Widget) permanently 
  
  
def delete_label(): 
    mylabel.destroy() 
  
  
# Creating button. In this destroy method is passed 
# as command, so as soon as button is pressed 
# Label will be destroyed 
B1 = Button(root, text="DELETE", command=delete_label) 
B1.pack() 
  
# start the GUI 
root.mainloop() 