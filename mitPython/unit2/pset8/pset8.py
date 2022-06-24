"""
Write an iterative function iterPower(base, exp) that calculates the exponential base by simply using sucessive
multiplication.

This function should take in two values base can be a float or an integer; exp will be an integer >= 0
It should return numberical value. Your code must be iterative

"""

def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Base case is when exp = 0
    if exp <= 0:
        return 1

    # Otherwise, exp must be > 0, so return 
    #  base* base^(exp-1). This is the recursive case.
    return base * recurPower(base, exp - 1)



    

print(recurPower(-3.8, 0))