# https://www.geeksforgeeks.org/how-to-hide-recover-and-delete-tkinter-widgets/

from tkinter import *
 
# toplevel window 
root = Tk() 
  
# Method to make Button(Widget) invisible from toplevel 
  
  
def hide_button(widget): 
    # This will remove the widget from toplevel 
    widget.pack_forget() 
  
  
# Method to make Button(widget) visible 
def show_button(widget): 
    # This will recover the widget from toplevel 
    widget.pack() 
  
  
# Button widgets 
B1 = Button(root, text="Button 1", command=lambda: show_button(B3)) 
B1.pack() 
  
  
# See, in command hide_button() function is passed to hide Button B3
B2 = Button(root, text="Button 2", command=lambda: hide_button(B3)) 
B2.pack() 
  

B3 = Button(root, text="Button 3") 
B3.pack() 
  
root.mainloop() 