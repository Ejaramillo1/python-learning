"""
Multiplication Iterative solution

Multiply a * b is equivalent to "add" a to itself b times
"""

def mult_iter(a,b):
    result = 0
    while b > 0:
        result += a
        b -= 1
    return result