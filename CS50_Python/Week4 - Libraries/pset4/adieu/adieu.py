"""
CS50 Python --Adieu- Adieu --

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/4/adieu/

---------------------DESCRIPTION--------------------------
In a file called adieu.py, implementa a program that prompts the user for names, one per line,
until the user inputs control-d. Assume that the user will input at least one name.
Then bit adieu to those names, separating two names with one and,
tree names with two commas and one and, and n names with n - 1 commas and
one and, as in the below
"""

import inflect

def main():
    print(f"Adieu, adieu, to {loop_names(get_names())}")


# Define a function to loop trough the names in a list

def loop_names(names):
    p = inflect.engine()
    for n in range(len(names)):
        return p.join(names)


# Define a funciton to get a list of the names an break when the user clicks ctrl + C


def get_names():
    names = []
    while True:
        try:
            name = input("Name: ")
            names.append(name)
        except EOFError:
            print("")
            break
        return names

if __name__ == "__main__":
    main()