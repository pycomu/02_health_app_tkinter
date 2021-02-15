import tkinter as tk

root = tk.Tk() 

def reg_mask():
    # window of input mask
    canvas = tk.Canvas(root, width=500, height=300)
    canvas.grid(columnspan=3, rowspan=3)

    # label and entry fields
    user_name = tk.Entry(root, width = 30)
    user_name.grid(column=2, row=0)
    

    print(user_name.get())  
    
      
    
    #register button
    reg_text = tk.StringVar()
    reg_text.set("Push")
    reg_btn = tk.Button(root, textvariable=reg_text, command=lambda:print(user_name.get()), font="Raleway", bg="#20bebe", fg="white", height=2, width=15)
    
    reg_btn.grid(column=2, row=2)
    
    root.mainloop()


if __name__ == "__main__":
    reg_mask()
