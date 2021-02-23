from tkinter import *

top_window = Tk()

def new_window():
    new_window = Toplevel()
    new_window.geometry("300x300")
    new_window.title("Sub level window")

    close_btn = Button(new_window, text ="close sub window", command = new_window.destroy)
    close_btn.pack()

    new_window.mainloop()


top_window.geometry("500x500")
top_window.title("Main window")

login_btn = Button(top_window, text ="open new window", command = new_window)
login_btn.pack()

quit_btn = Button(top_window, text ="Quit", command = top_window.destroy)
quit_btn.pack()

top_window.mainloop()