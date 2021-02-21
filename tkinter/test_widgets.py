import tkinter as tk
from tkinter import ttk
from tkinter import filedialog


class Counter_program():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("tk Examples")
        self.create_widgets()

        self.radio_variable = tk.StringVar()
        self.combobox_value = tk.StringVar()

    def create_widgets(self):
        # Create some room around all the internal frames
        self.window['padx'] = 5
        self.window['pady'] = 5

        # The Data entry frame
        entry_frame = ttk.LabelFrame(self.window, text="Data Entry for age, height, weight made easy",
                                     relief=tk.RIDGE)
        entry_frame.grid(row=0, column=1, sticky=tk.E + tk.W + tk.N + tk.S)

        

        
        my_spin_label = ttk.Label(entry_frame, text="Select your age from 1 to max 16")
        my_spin_label.grid(row=1, column=1, sticky=tk.W + tk.N)
        my_spinbox = tk.Spinbox(entry_frame, from_=1, to=16, width=5, justify=tk.RIGHT)
        my_spinbox.grid(row=1, column=2, sticky=tk.E, pady=3)

        my_scale_label = ttk.Label(entry_frame, text="Select the measured weight in full Kg")
        my_scale_label.grid(row=2, column=1, sticky=tk.W + tk.N)
        my_scale = tk.Scale(entry_frame, from_=0, to=60, orient=tk.HORIZONTAL, width=8, length=200)
        my_scale.grid(row=2, column=2, sticky=tk.W)

        my_scale2_label = ttk.Label(entry_frame, text="Select the measured weight after comma")
        my_scale2_label.grid(row=3, column=1, sticky=tk.W + tk.N)
        my_scale2 = tk.Scale(entry_frame, from_=0, to=9, orient=tk.HORIZONTAL, width=8, length=200)
        my_scale2.grid(row=3, column=2, sticky=tk.W)

        my_spin2_label = ttk.Label(entry_frame, text="Select your weight from 1 to max 60: (previous weight was)")
        my_spin2_label.grid(row=4, column=1, sticky=tk.W + tk.N)
        my_spinbox2 = tk.Spinbox(entry_frame, from_=1, to=60, width=5, justify=tk.RIGHT)
        my_spinbox2.grid(row=4, column=2, sticky=tk.E, pady=3)
        

        # - - - - - - - - - - - - - - - - - - - - -
        # Quit button in the lower right corner
        quit_button = ttk.Button(self.window, text="Quit", command=self.window.destroy)
        quit_button.grid(row=5, column=1)

# Create the entire GUI program
program = Counter_program()

# Start the GUI event loop
program.window.mainloop()
