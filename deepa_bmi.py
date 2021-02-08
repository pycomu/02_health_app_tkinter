# metric mode (Kg, Pound) (cm, inch, feet)
# Age in Years (later as dropdown list)
# Weight in Kg
# Height in Meter, for user in cm
# Gender male, female, no say
# BMI

# https://www.healthhub.sg/live-healthy/745/differencesbetweenchildandadultbmi

# https://www.indexmundi.com/blog/index.php/2013/04/11/body-mass-index-bmi-by-country/

# https://www.cdc.gov/growthcharts/percentile_data_files.htm

#BMI_low == 18.5
#BMI_up == 29.9

# import libraries
import tkinter as tk

# Shiji
def input_value():
    pass

# Memoona
def calc_BMI ():
    BMI = Weight/(Height*2)
    return BMI

# Deepa

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
    tk.mainloop()

if __name__ == "__main__":
    output_result(5)
