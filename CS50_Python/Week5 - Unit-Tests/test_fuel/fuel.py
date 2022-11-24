"""
CS50 Python --Refueling--

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/5/test_fuel/

---------------------DESCRIPTION--------------------------
In a file called fuel.py, reimplement Fuel Gauge from Problem Set 3, restructuring your code per the below, wherein:

convert expects a str in X/Y format as input, wherein each of X and Y is an integer, and returns that fraction as a percentage rounded to the nearest int between 0 and 100, inclusive. If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError. If Y is 0, then convert should raise a ZeroDivisionError.
gauge expects an int and returns a str that is:
"E" if that int is less than or equal to 1,
"F" if that int is greater than or equal to 99,
and "Z%" otherwise, wherein Z is that same int.
"""

def main():
    fuel = input("Fraction: ")
    z = convert(fuel)
    print(gauge(z))


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f"{percentage:.0f}%"





def convert(fraction):
    while True:
        try:
            x,y = fraction.split("/")
            y = int(y)
            x = int(x)
            z = x / y
            if z <= 1:
                p = int(z * 100)
                return p
            else:
                fraction = input("Fraction: ")
                pass
        except (ValueError, ZeroDivisionError):
            raise





if __name__ == "__main__":
    main()