"""
CS50 Python --Felipe's Taqueria--

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/3/taqueria/

---------------------DESCRIPTION--------------------------
In a file called taqueria.py implement a program that enables a user to place
an order, prompting them for items, one per line, until the user inputs control-d
(which is a common way of ending one's input to a program). After each inputted item,
display the total cost of all items inputted thus far,  prefixed with a dollar sign($)
and formatted to two decimal places
"""

def main():
    total = get_order()
    print(f"Total: ${total:.2f}")


def get_order():
    items = {
        "Baja Taco": 4.00,
        "Burrito": 7.50,
        "Bowl": 8.50,
        "Nachos": 11.00,
        "Quesadilla": 8.50,
        "Super Burrito": 8.50,
        "Super Quesadilla": 9.50,
        "Taco": 3.00,
        "Tortilla Salad": 8.00
        }
        
    total = 0

    while True:
        try:
            order = input("Item: ").lower()
            for item in items:
                product = item
                if order == product.lower():
                    total += items[item]
                    print(f"Total: ${total:.2f}")
        except EOFError:
            break
    return total

if __name__ == "__main__":
    main()
