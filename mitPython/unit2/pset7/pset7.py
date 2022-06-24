"""
Write an iterative function iterPower(base, exp) that calculates the exponential base by simply using sucessive
multiplication.

This function should take in two values base can be a float or an integer; exp will be an integer >= 0
It should return numberical value. Your code must be iterative

"""

def iterPower(base, exp):
    if exp == 0:
        result = 1
    else:
        result = base
    for _ in range(1, exp):
        result *= base
    return result
    
    

print(iterPower(-3.8, 0))
