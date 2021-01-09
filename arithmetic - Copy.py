'''This module contains Arithmetic operations'''
def Addition(*a):
    return sum(a)

def Subtract(*a):
    s=0
    for i in a:
        s=s-i
    return s

def Multiply(*a):
    mul=1
    for i in a:
        mul=mul*i
    return mul

def Division(a,b):
    if b==0:
        print("Zero Division Error! Division is not Possible")
    else:
        print("Division of {} and {} is {}".format(a,b,a/b))
      