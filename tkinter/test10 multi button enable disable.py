from tkinter import *
 
root = Tk() 
root.geometry("300x200")


def enable_all():
    for x in windows:           # loop through the button list
        x.config(state="normal") # enable again all buttons
                            
  
def disable_button(number):
        for x in windows:               # loop through the button list
            x.config(state="disabled") # disable all buttons
                    
        windows[number].config(state="normal") # enable again button defined in "number"
        
# Button widgets 
B1 = Button(root, text="Button 1", command=lambda: disable_button(0)) 
B1.pack() 
    
B2 = Button(root, text="Button 2", command=lambda: disable_button(1)) 
B2.pack() 
  
B3 = Button(root, text="Button 3", command=lambda: disable_button(2)) 
B3.pack()

B4 = Button(root, text="Reset", command=lambda: enable_all()) 
B4.pack()
  
windows = [B1,B2,B3] # list of buttons

root.mainloop() 