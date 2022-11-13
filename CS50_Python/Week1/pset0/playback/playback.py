"""
CS50 Python 

--Playback Speed--

This is the first set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/0/indoor/

---------------------DESCRIPTION--------------------------

Implement a program in python that prompts the user for input and then
outputs that same input, replacing each space with ...
"""


message = input("Hello please write your message here: ")

message = message.replace(" ", "...")

print(f"Your message is: {message}")