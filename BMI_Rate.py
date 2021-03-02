

# import libraries
import tkinter as tk
from tkinter import Button


def output_result(BMIpercentile):
    #print("\n")
    #print(f'Your child BMI Percentile is - {BMIpercentile}')

    if BMIpercentile < 8:
        #print ("Your child is Underweight")
        BMIResult = "Your child BMI Percentile is - " + str(BMIpercentile) + "."
        BMIInference = "Your Child is Underweight"
    elif BMIpercentile > 8 and BMIpercentile < 84:
        print ("Your child is Healthy weight​​")
    elif BMIpercentile > 85 and BMIpercentile < 95:
        print ("Your child is Overweight")
    elif BMIpercentile > 95:
        print ("Your child is Obese")
    else:
        print ("Height and weight input is incorrect")

    root = tk.Tk()
    T = tk.Text(root, height=2, width=40)
    T.pack()
    T.insert(tk.END, BMIResult)
    T.insert(tk.END,'\n')
    T.insert(tk.END, BMIInference)
   # button = Button(root, text = "Close", command = close_window)
    
    button = Button (root, text="Close.", command = lambda: close_window(root))
    button.pack()
    tk.mainloop()
   
    
def close_window (root): 
    root.destroy()  

if __name__ == "__main__":
    output_result(5)
