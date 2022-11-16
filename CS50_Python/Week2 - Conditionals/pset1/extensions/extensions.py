"""
CS50 Python --File Extensions--

This is the first set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/1/bank/

---------------------DESCRIPTION--------------------------
In a file called extensions.py, implement a program that prompts the user 
for the name of a file and then outputs that file’s media type if the file’s 
name ends, case-insensitively, in any of these suffixes:

.gif
.jpg
.jpeg
.png
.pdf
.txt
.zip
If the file’s name ends with some other suffix or has no suffix at all, 
output application/octet-stream instead, which is a common default.
"""

file = input("File name: ").lower()

# Check GIF extension
if '.gif' in file:
    print('image/gif', end)
# Check JPG extension
elif '.jpg' in file:
    print('image/jpg', end="")
# Check for JPEG extension
elif '.jpeg' in file:
    print('image/jpeg', end="")
# Check PNG extension
elif '.png' in file:
    print('image/png', end="")
# Check PDF extension
elif '.pdf' in file:
    print('application/pdf', end="")
# Check TXT extension
elif '.txt' in file:
    print('text/plain', end="")
# Check ZIP extension
elif '.zip' in file:
    print('application/zip', end="")
# Disregard everything else
else:
    print('application/octed-stream')





    