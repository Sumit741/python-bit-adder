#code to convert the decimal number to binary number of 8 bits
"""Defining function that takes  a number as a parameter"""
def bin(num):
    """Initializing l as empty list,
       count as 0 and ans as empty
       string"""
    l=[]
    count=0
    ans=""
    """Using while loop to make binary number of 8 bits"""
    while count!=8:
        rem=num%2
        l.append(rem)#adding remainder i list
        num=num//2
        count+=1#increasing count by 1 time when each loop executes
        l1=l[::-1]#revering the list
    return l1




