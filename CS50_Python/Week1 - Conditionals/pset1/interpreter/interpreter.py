"""
CS50 Python -- Math Interpreter--

This is the first set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/1/interpreter/

---------------------DESCRIPTION--------------------------
In a file called interpreter.py, impement a program that promts the user for an arithmetic expression
and then calculates and outputs the result as a floating point value
formatted to one decimal place. Assume that the user's input will be formatter as x y z, with one space
between x and y and one space between y and z, wherein:
"""

user_input = input("Expression: ")

x, y, z = user_input.split(" ")

n_x = float(x)
n_z = float(z)

if '+' in y:
    a = n_x + n_z
    print(f"{a:.1f}")
elif '-' in y:
    a = n_x - n_z
    print(f"{a:.1f}")
elif '/' in y:
    a = n_x / n_z
    print(f"{a:.1f}")
elif '*' in y:
    a = n_x * n_z
    print(f"{a:.1f}")