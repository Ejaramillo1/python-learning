"""
CS50 Python --Re-requesting a Vanity Plate
--

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/5/test_plates/

---------------------DESCRIPTION--------------------------
In a file called plates.py, reimplement Vanity Plates from Problem Set 2, 
restructuring your code per the below, wherein is_valid still expects a str as input 
and returns True if that str meets all requirements and False if it does not, 
but main is only called if the value of __name__ is "__main__"
"""

def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print('Valid')
    else:
        print('Invalid')



def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False

    if s[0].isalpha() == False or s[1].isalpha() == False:
        return False

    i = 0
    while i < len(s):
        if s[i].isalpha() == False:
            if s[i] == '0':
                return False
            else:
                break
        i += 1

    number_of_digits = len([char for char in s if char.isdigit()])
    if number_of_digits > 0:
        for i in range(len(s[-number_of_digits:])):
            if s[-number_of_digits:].isdigit() == False:
                return False

    for c in s:
        if c in ['.', ',', '!', '?']:
            return False
    else:
        return True




if __name__ == "__main__":
    main()