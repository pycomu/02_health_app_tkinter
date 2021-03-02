# Main code to be developed, principle in pseudo code:
# 1 Import dependencies
# 2 define global variables to refelct at any time which account, which user, which last log file entry
# 3 read out last log entry on current account, user and store in global variables
# 4 open windows (UI) and perform data entries to be stored, changed in database
# 5 switch on only relevant UI and focus for data manipulation

# import the Libraries
import tkinter as tk
from tkinter import *import mysql.connectorimport pandas as pd
from pandas import Series,DataFrame
from PIL import Image, ImageTk

# Global variables
account_id   
account_pin
account_email_id
child_id
log_id  

# other variables
child_first_name
child_last_name
child_dob
child_height
child_weight
child_age
child_genderchild_BMI
time_stamp



# functions
def get_input():
    weight_in = float(input("your weigt in Kg is ? "))
    height_in = float(input("your height in m is ? "))
    return (weight_in, height_in)
    
def calc_bmi(weight, height):
    return weight/(height*2)

def output(bmi):
    print("Your BMI is calculated to be ", "%.2f" % bmi)



if __name__ == "__main__":

    weight_ , height_ = get_input()
    
    bmi = calc_bmi(weight_, height_)
    
    output(bmi)

    