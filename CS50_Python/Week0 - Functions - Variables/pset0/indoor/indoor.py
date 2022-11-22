"""
CS50 Python 
--Indoor Voice--

This is the first set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link. 

https://cs50.harvard.edu/python/2022/psets/0/indoor/

---------------------DESCRIPTION--------------------------

In a file called indoor.py, implement a program in Python that prompts the user 
for input and then outputs that same input in lowercase. Punctuation and whitespace 
should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, 
as by passing a str of your own as an argument to input.e
"""


message = input("Hello please write your message here: ").lower()
print(f"Your message is: {message}")
