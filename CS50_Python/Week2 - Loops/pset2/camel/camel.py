"""
CS50 Python --camelCase--

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/2/camel/

---------------------DESCRIPTION--------------------------
In a file called camel.py, implement a program that promts the user
for the name of a variable in camel case and outpus the corresponding
name in snake case. Assume that the user's input will indeed be in camel case
"""


def main():
    # Ask the user for input

    cam = input("camelCase: ")
    for i in range(len(cam)):
        if cam[i].isupper():
            print(f"_{cam[i].lower()}", end="")
        else:
            print(cam[i], end="")

if __name__ == "__main__":
    main()