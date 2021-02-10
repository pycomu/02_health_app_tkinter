# simple code to have functions and test parameters

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

    