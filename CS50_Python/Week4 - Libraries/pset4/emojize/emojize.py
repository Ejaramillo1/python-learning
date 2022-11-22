"""
CS50 Python --Emojize--

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/4/emojize/

---------------------DESCRIPTION--------------------------
In a file calle emojize.py, implement a program that prompts the use for a str in English
and then outputs the 'emojized' version of that str, converting any codes (or aliases) therein
to their corresponding emoji.
"""

import sys
import emoji

text = input("Input: ")
print("Output: " + emoji.emojize(text))