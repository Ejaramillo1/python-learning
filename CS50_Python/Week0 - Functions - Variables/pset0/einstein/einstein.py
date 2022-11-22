"""
CS50 Python --Einstein--

This is the first set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/0/einstein/

---------------------DESCRIPTION--------------------------
Implement a program in python that prompts the user of mass as an integer
in KG and then outputs the equivalent number of joules as an integer
"""

# Define speed of ligth

LIGHT = int(300000000)

c2 = LIGHT * LIGHT

m = int(input("Please enter the mass of the object in kg here: "))

e = m*c2

print(f"E:{e:.0f}")