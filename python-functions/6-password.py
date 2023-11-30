def validate_password(password):
    # Check minimum length
    if len(password) < 8:
         return False
    elif ' ' in password:
         return False
    else:
        for char in password:
             if char.isupper(): 
                 return True
             elif char.islower():
                 return True
             elif char.isdigit():
                 return True
    return False       
   

    

