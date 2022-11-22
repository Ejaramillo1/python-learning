"""
CS50 Python --Fuel Gauge--

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/3/fuel/

---------------------DESCRIPTION--------------------------
In a file called taqueria.py implement a program that enables a user to place
an order, prompting them for items, one per line, until the user inputs control-d
(which is a common way of ending one's input to a program). After each inputted item,
display the total cost of all items inputted thus far,  prefixed with a dollar sign($)
and formatted to two decimal places
"""

def main():
    z = calculate_fraction()
    if z <= 1:
        print('E')
    elif z >= 99:
        print('F')
    else:
        print(f'{z:.0f}%')


def calculate_fraction():
    while True:
        try:
            x, y = input("Fraction: ").split('/')
            y = int(y)
            x = int(x)
            if x < 0:
                raise ValueError('This must be greater than zero')
            elif x > y:
                raise ValueError('x should not be greater than y')
            z = round((x / y) * 100)
        except(ValueError, ZeroDivisionError):
            pass
        else:
            break
    return z


if __name__ =="__main__":
    main()