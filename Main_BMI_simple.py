
    

if __name__ == "__main__":

    weight_in = float(input("your weigt in Kg is ? "))
    height_in = float(input("your height in m is ? "))
    
    bmi = weight_in/(height_in*2)
    

    print("Your BMI is calculated to be ", "%.2f" % bmi)

    