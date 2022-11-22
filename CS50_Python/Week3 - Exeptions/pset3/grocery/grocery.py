"""
CS50 Python --Grocery List--

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/3/grocery/

---------------------DESCRIPTION--------------------------
In a file called grocery.py, implement a program
that prompts the user for items, one per line,
until the user inputs control-d
(which is a common way of ending ones
input to a program). Then output the users
grocery list in all uppercase, sorted alphabetically
by item, prefixing each line with the number of
times the user inputted that item.
No need to pluralize the items.
Treat the users input case-insensitively.
"""

def main():
    items = get_grocery()
    u_items = get_uitems(items)
    for i in  u_items:
        print(f"{u_items[i]} {i}")


def get_uitems(grocery_list):
    u_grocery = {}
    count_a = 0

    for grocery in grocery_list:
        if grocery not in u_grocery:
            u_grocery[grocery] = 1
        else:
            u_grocery[grocery] += 1
    return u_grocery

def get_grocery():
    items = []
    while True:
        try:
            item = input("").upper()
            items.append(item)
            items.sort()
        except EOFError:
            print("")
            break
    return items

if __name__ == "__main__":
    main()