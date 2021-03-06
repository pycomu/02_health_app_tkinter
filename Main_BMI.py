# Main code to be developed, principle in pseudo code:
# 1 Import dependencies
# 2 define global variables to refelct at any time which account, which user, which last log file entry
# 3 read out last log entry on current account, user and store in global variables
# 4 open windows (UI) and perform data entries to be stored, changed in database
# 5 switch on only relevant UI and focus for data manipulation

# import dependencies
import tkinter as tk
from tkinter import *
import mysql.connector
import pandas as pd
from pandas import Series,DataFrame
from PIL import Image, ImageTk

""" # Global variables along database structure

# +++++ pointers for status/position in database
Account_id
Child_id
Logfile_id

# +++++ arrays to show content in comboboxes
Account_name
User name

# ++++++ parameters to show in label or preset entrybox
Last_weight
Last_height
etc.

"account_id"	INTEGER,
"account_name"	TEXT,
"account_pin"	INTEGER,
"account_email"	TEXT,
"account_create_date" TEXT,

"child_id"	INTEGER,
"child_first_name"	TEXT,
"child_last_name"	TEXT,
"child_bday"	TEXT,
"child_gender"	TEXT,
"child_country"	TEXT,
"child_create_date"	TEXT,
"account_id"	INTEGER,

"logfile_id"	integer,
"logfile_timestamp"	TEXT,
"logfile_weight"	REAL,
"logfile_height"	REAL,
"logfile_bmi"	REAL,
"logfile_age_act"	REAL,
"child_id"	INTEGER,


"""
def update_global_variables(): # read out all account names, user name, set pointers
    pass

# ++++++ functions for GUI, layout window and its different frames

# ++++++ functions for database modifications e.g. insert data, delete data, update data

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

    