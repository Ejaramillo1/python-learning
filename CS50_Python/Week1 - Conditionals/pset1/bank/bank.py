"""
CS50 Python --Home Federal Savings Bank--

This is the first set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/1/bank/

---------------------DESCRIPTION--------------------------
In a file called bank.py, implement a program that prompts 
the user for a greeting. If the greeting starts with “hello”, 
output $0. If the greeting starts with an “h” (but not “hello”), 
output $20. Otherwise, output $100. Ignore any leading whitespace in 
the user’s greeting, and treat the user’s greeting case-insensitively.

"""

greet =  input("Enter you greeting word here: ").strip().lower()

if greet.startswith("hello"):
    print("$0")
elif greet.startswith("h") and greet != "hello":
    print("$20")
else:
    print("$100")
