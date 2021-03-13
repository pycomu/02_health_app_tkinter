import re
      
def v_email1(email):
    regex = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
    
    # for custom mails use: '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w+$' 
    
    if(re.search(regex,email)):  
        print("Valid Email")            
    else:  
        print("Invalid Email")  


def v_email2(email):
    if len(email) > 7:
        if re.match("^.+@([?)[a-zA-Z0-9-.]+.([a-zA-Z]{2,3}|[0-9]{1,3})(]?)$", email) != None:
            return True
    return False

def v_email3(email):
    rule = r"^[A-Z0-9\._+ '\"-]+\@[A-Z0-9]+\.[A-Z0-9]+"
    inputu = input ("please enter your email:").upper()
    
    if re.search (rule, inputu):
        print ("Invalid")
    else:
        print ("Valid")


""" That will check that at the start of the string you have some substring made of letters, 
numbers, or periods, underscores, dashes, plus signs, spaces or single or double quotes. 
Then an @. Then another substring made of letters and numbers. Then a period. Then finally another 
substring made entirely of letters at the end of the string.

But note that this still doesn't mean that the address is valid. Only that it might be. 
If you really do need to validate an email address the only way is to send them an email, 
and get them to respond.
"""
if __name__ == '__main__' :  
      
    email = "ankitrai326@gmail.com"
    v_email1(email) 
  
    email = "my.ownsite@ourearth.org"
    v_email1(email) 
  
    email = "ankitrai326.com"
    v_email1(email) 
