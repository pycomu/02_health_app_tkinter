# Main code to be developed, principle in pseudo code:
# 1 Import dependencies
# 2 define global variables to refelct at any time which account, which user, which last log file entry
# 3 read out last log entry on current account, user and store in global variables
# 4 open windows (UI) and perform data entries to be stored, changed in database
# 5 switch on only relevant UI and focus for data manipulation

# import the Libraries
import tkinter as tk
from tkinter import *
import mysql.connector
import pandas as pd
from pandas import Series,DataFrame
from PIL import Image, ImageTk

""" # Global variables along database structure
"account_id"	INTEGER,
"account_name"	VARCHAR(20),
"account_email"	TEXT, or account_email_id
"account_pin"	text,

"user_id"	INTEGER, or child_id
"user_name"	VARCHAR(20), or child_first_name and child_last_name
"user_gender"	TEXT,
"user_dob"	INTEGER,or child_dob

"log_id"	INTEGER, or log_id  
"entry_time"	TIMESTAMP, or time_stamp
"height"	FLOAT, or child_height
"weight"	FLOAT, or child_weight
"age"	INTEGER, or child_age
"bmi"	FLOAT, or child_genderchild_BMI


"""

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

    