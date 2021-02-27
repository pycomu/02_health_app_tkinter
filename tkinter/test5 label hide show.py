# https://www.delftstack.com/howto/python-tkinter/how-to-hide-recover-and-delete-tkinter-widgets/

# more examples there

# grid_forget() Method to Hide Tkinter Widgets if grid Layout Is Used
# If the widgets are placed with the grid layout manager, we should use grid_forget() method to make the Tkinter widgets invisible.

import tkinter as tk
 
class Test():
   def __init__(self):
       self.root = tk.Tk()
       self.label=tk.Label(self.root,
                           text = "Label")
       self.buttonForget = tk.Button(self.root,
                          text = 'Click to hide Label',
                          command=lambda: self.label.grid_forget())
       self.buttonRecover = tk.Button(self.root,
                          text = 'Click to show Label',
                          command=lambda: self.label.grid())       
       
       self.buttonForget.grid(column=0, row=0, padx=10, pady=10)
       self.buttonRecover.grid(column=0, row=1, padx=10,  pady=10)
       self.label.grid(column=0, row=2, padx=10, pady=10)
       self.root.mainloop()

   def quit(self):
       self.root.destroy()
        
app = Test()