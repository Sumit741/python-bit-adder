#six different functions for AND, OR, XOR, NOT, NAND and NOR gate.

"""defining a function for AND gate with two values in parameter """
def AND(A, B):
    """Using if else satement for checking the condition of AND gate"""
    if A==1 and B==1:
        return 1
    else:
        return 0

"""defining a function for OR gate with two values in parameter """
def OR(A, B):
    """Using if else satement for checking the condition of OR gate"""
    if A==0 and B==0:
        return 0
    else:
        return 1

"""defining a function for XOR gate with two values in parameter """
def XOR(A, B):
    """Using if else satement for checking the condition of XOR gate"""
    if A!=B:
        return 1
    else:
        return 0

"""defining a function for NOT gate with two values in parameter """
def NOT(A):
    """Using if else satement for checking the condition of NOT gate"""
    if A==0:
        return 1
    else:
        return 0

"""defining a function for OR gate with two values in parameter """
def NAND(A, B):
    """Using if else satement for checking the condition of NAND gate"""
    if A==1 and B==1:
        return 0
    else:
        return 1

"""define a function for NOR gate with two values in parameter """
def NOR(A, B):
    """Using if else satement for checking the condition of NOR gate"""
    if A==0 and B==0:
        return 1
    else:
        return 0
