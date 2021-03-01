

# import libraries
import tkinter as tk
from tkinter import Button, Canvas
from PIL import Image, ImageTk
root = tk.Tk()

def BMI_chart():
    canvas = Canvas(root, width = 600, height = 600)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("growthchart_example2.gif"))  
    canvas.create_image(250, 250, image=img) 
    #root.mainloop() 
    button = Button (root, text="Close.", command = lambda: close_window(root))
    button.pack()
    button = Button (root, text="Export_PDF", command = lambda: close_window(root))
    button.pack()
    button = Button (root, text="Export_DB", command = lambda: close_window(root))
    button.pack()
    tk.mainloop()

def close_window (root): 
    root.destroy() 
if __name__ == "__main__":
    BMI_chart()
