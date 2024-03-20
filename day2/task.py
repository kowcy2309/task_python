
'''Modulus contain add,su,mul,div,percentage'''
def addition(a,b):
    "addition"
    return a+b

def subtraction(a,b):
    "subtraction"
    # c=a-b
    # if c>=0:
    #     return c
    # else:
    #     return -(c)
    if a>=0 and b>=0:
        if a>b:
            return a-b
        else:
            return b-a
    
def multiply(a,b):

    "multiplication"
    return a*b

def division(a,b):
    "division"
    if a>0 and b>0:
        return a/b
    else:
        return "denominator is not zero"
    
    
def percentage(a,b):
    "percentage"
    return ((a+b)/2)*100
