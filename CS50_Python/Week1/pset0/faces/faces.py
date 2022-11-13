"""
CS50 Python 
--Making Faces--

This is the first set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/0/faces/


---------------------DESCRIPTION--------------------------
Implement a function called convert that accepts a str as input and 
returns the same input with any :) converted to slightly smiling face.

Also implement a function called main that prompts the user for inputs,
calls convert on that input, and prints the results.

"""

def main():
    message = input("Please enter your message with emoji here: ")
    faces(message)

def faces(m = 'message'):
    if ":)" in m:
        m = m.replace(":)", "🙂")
    if ":(" in m:
        m = m.replace(":(", "🙁")
    print(m)
main()