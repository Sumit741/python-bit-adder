#code for main module that performs the whole calculation

"""importing modules addition, comnversion, validation and new"""
import addition as m
import conversion as c
import validation as v
import new as nn

"""initializing decimal_num as 0"""
decimal_num=0
"""Printing the welcome message to user"""
print("********Hello!! Welcome to My software********")

state = True#initializing state as True
"""Defining while loop"""
while state==True:
    try:#defining try function
        """taking two decimal number as user inputs"""
        decimal1=int(input("Enter first decimal number between 0 and 255: "))
        decimal2=int(input("Enter second decimal number between 0 and 255: "))
        First_decimal=v.validation(decimal1)#Calling validation() function and passing 1st user input to it
        Second_decimal=v.validation(decimal2)#Calling validation() function and passing 2nd user input to it
        First_decimal1=c.bin(First_decimal)#Calling bin() function and passing 1st validated value to it
        Second_decimal1=c.bin(Second_decimal)#Calling bin() function and passing 2nd validated value to it
        New1 = m.add(First_decimal1,Second_decimal1, 0)#Calling add() function and passing value to its parameter for addition
        decimal_num=First_decimal+Second_decimal
        
        """Using if else statement to check out of range values"""
        if First_decimal<0 or First_decimal>255 and Second_decimal<0 or Second_decimal>255:
            print("")
        else:    
            print("The decimal to binary conversion of " +str(First_decimal)+" is ", nn.string(First_decimal1))#printing binary of first decimal number
            print("The decimal to binary conversion of " +str(Second_decimal)+" is ", nn.string(Second_decimal1))#printing binary of second decimal number
            print("The binary addition of " +str(nn.string(First_decimal1))+" and "+str(nn.string(Second_decimal1))+" is ", New1)#printing the addition of two binary numbers
            print("The decimal conversion of given added output "+str(New1) + " is ",str(decimal_num))#printing the decimal of binary addition
        
    except:#defining except function
        """Printing error message for invalid values"""
        print("Please enter valid value!!")

    """Asking user to continue the program"""
    conti = input("Do You want to continue?").lower()
    """If the answer is no chaninging the state to false and stopping the program"""
    if conti=="no":
        state=False
        print("********Thank You For choosing us for your work!!*********")
        break #breaking the continuation of loop in the program
