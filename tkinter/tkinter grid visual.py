import tkinter as tk
from tkinter import ttk

root = tk.Tk()

#setting window size
width=1200
height=800
screenwidth = root.winfo_screenwidth()
screenheight = root.winfo_screenheight()
alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
root.geometry(alignstr)
root.resizable(width=False, height=False)

# creates a defined grid in the main window and writes in row & column
def define_grid(width, height):
    for rows in range(height):
        root.rowconfigure(rows, weight=1)
        for columns in range(width):
            root.columnconfigure(columns, weight=1) 
            ttk.Label(root, text='R%s/C%s'%(rows,columns), borderwidth=1 ).grid(row=rows,column=columns) # can be deleted


define_grid(4,7) 
print("grid size is width/height columns/rows :",root.grid_size())

root.mainloop()