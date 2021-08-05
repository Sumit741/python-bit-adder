#code to check for thee valid entry

"""defining a function with a number as a parameter"""
def validation(num):
    a = 0#initializing a as 0
    """Defining a while loop"""
    while a==0:
        if num<0 or num>=255:#if else statement to check for valid entry
            """printing the error message is invalid input is given"""
            print("The given value "+str(num) +" is out of range! Please enter a number between 0 and 255")
        break#breaking the continuation of loop
    return num

