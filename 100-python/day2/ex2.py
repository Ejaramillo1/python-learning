"""
Write a program that calculates the Body Mass Index
(BMI) from a user's weight and height.
"""

import math
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

bmi = int(weight) / (float(height) ** 2)

print(int(bmi))