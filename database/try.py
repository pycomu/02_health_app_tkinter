import tkinter as tk

ws = tk.Tk()
ws.title("PythonGuides")
ws.geometry('400x300')
ws['bg'] = '#ffbf00'

def printValue():
    pname = player_name.get()
    print(pname)
    
player_name = tk.Entry(ws)
player_name.pack(pady=30)

tk.Button(ws,text="Register Player", padx=10, pady=5, command=printValue).pack()

ws.mainloop()