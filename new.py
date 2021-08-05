#code to convert the numbers in list to string
"""impoting conversion module"""
import conversion as op

"""defining a function with a number in a parameter"""
def string(num):
    ss=""#initializing ss as empty string
    """defining a for loop"""
    for i in range(len(num)-1,-1,-1):
      ss=ss+str(num[i])#converting each binary digits to string
      ss1=ss[::-1]#reversing the string value
    return ss1#returing actual binary number as string


