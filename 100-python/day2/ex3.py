"""
I was reading this article by Tim Urban - 
Your life in Weeks and realized just how little time
we actually have
"""
# 🚨 Don't change the code below 👇
from cgi import print_form


age = input("What's your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_left = 90 - int(age)

days = years_left * 365
weeks = years_left * 52
months = years_left * 12

print(f"You have {days} days, {weeks} weeks, and {months} months left.")
