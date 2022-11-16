"""
CS50 Python -- Meal Time --

This is the first set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/1/meal/

---------------------DESCRIPTION--------------------------
In a file called interpreter.py, impement a program that promts the user for an arithmetic expression
and then calculates and outputs the result as a floating point value
formatted to one decimal place. Assume that the user's input will be formatter as x y z, with one space
between x and y and one space between y and z, wherein:
"""

def main():
    tm = input("Input the time in the following format ##:## : ")
    hrs, mins = tm.split(":")
    hrs = int(hrs)
    if 7 <= hrs <= 8:
        print("breakfast time")
    elif 12 <= hrs <= 13:
        print("lunch time")
    elif 18 <= 19:
        print("dinner time")
    else:
        print("")



# def convert(time):



if __name__ == "__main__":
    main()
