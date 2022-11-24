"""
CS50 Python --Back to the Bank--

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/5/test_bank/

---------------------DESCRIPTION--------------------------
n a file called bank.py, reimplement Home Federal Savings Bank from Problem Set 1, 
restructuring your code per the below, wherein value expects a str as input and returns 0 
if that str starts with “hello”, 20 if that str starts with an “h” (but not “hello”), 
or 100 otherwise, treating the str case-insensitively. Only main should call print.
"""

def main():
    user_text = input("Enter your greeting word here: ")
    print(value(user_text))




def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith("hello"):
        tip = 0
    elif greeting.startswith("h") and greeting != "hello":
        tip =20
    else:
        tip = 100
    return tip




if __name__ == "__main__":
    main()
