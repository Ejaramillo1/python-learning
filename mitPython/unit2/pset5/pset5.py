"""
Write a python function 'fourthPower', that takes one number and returns that value
raised to the fourth power.

You should use square procedure that you define in an earlier excercise 
"""



def fourthPower(x):
    z = square(square(x))
    return z 





def square(x):
    """
    x: int of float.    
    """
    # y = 0
    y = x**2
    return y

print(fourthPower(2))

