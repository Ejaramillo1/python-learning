"""
CS50 Python --Deep Thought--

This is the first set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/1/deep/

---------------------DESCRIPTION--------------------------
In deep.py, implement a program that prompts the user for the 
answer to the Great Question of Life, the Universe and Everything, 
outputting Yes if the user inputs 42 or (case-insensitively) 
forty-two or forty two. Otherwise output No.

"""

# Ask the user fot the input

question = input("Enter the number: ").lower().strip()

match question:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")