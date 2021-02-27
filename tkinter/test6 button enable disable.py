# https://www.delftstack.com/howto/python-tkinter/how-to-change-tkinter-button-state/
# 

from tkinter import *
 
# toplevel window 
root = Tk() 
root.geometry("300x200")
  
  
def disable_button(widget): 
    # widget.config(state=root.DISABLED)
    widget.config(state="disabled")
  
  
def enable_button(widget): 
    widget.config(state="normal")
  
  
# Button widgets 
B1 = Button(root, text="Button 1 to disable Quit", command=lambda: disable_button(B3)) 
B1.pack() 
  
  
B2 = Button(root, text="Button 2 to enable Quit", command=lambda: enable_button(B3)) 
B2.pack() 
  

B3 = Button(root, text="Button 3 to quit", command=lambda: root.destroy()) 
B3.pack() 
  
root.mainloop() 