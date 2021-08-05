#a simple code for addition of two binary numbers
"""importing modules conversion and gates to use its function here"""
import conversion as c
import gates as g

"""Defining function with three values in parameter"""
def add(num1, num2, Cin):
    """Initializing Cin as o, l2 as empty list and final as empty string"""
    Cin=0
    l2=[]
    final=""

    """Using for loop for starting addition from the last indexed number"""
    for i in range(len(num1)-1,-1,-1):
        bit1=num1[i]#storing each indexed() value of num1 in bit1
        bit2=num2[i]#storing each indexed() value of num2 in bit2
        S1=g.XOR(bit1, bit2)#calling XOR() method of gates module and passing value in it.
        S2=g.NAND(S1, Cin)#calling NAND() method of gates module and passing value in it.
        S3=g.OR(S1, Cin)#calling OR() method of gates module and passing value in it.
        SUM=g.AND(S2, S3)#calling AND() method of gates module and passing value in it.
        C1=g.AND(bit1, bit2)#calling AND() method of gates module and passing value in it.
        C2=g.AND(S1, Cin)#calling AND() method of gates module and passing value in it.
        C3=g.NOR(C1, C2)#calling NOR() method of gates module and passing value in it.
        Cout=g.NOT(C3)#calling NOT() method of gates module and passing value in it.
        Cin=Cout#declaring cout as cin for next bit addition
        l2.append(SUM)#adding SUM to l2
        l3=l2[::-1]##reversing the value of l2
        final+=str(l2[-1])#converting the list value to string
        final1=final[::-1]#reversing string value
    return final1 #returning the binary addition as string
       
