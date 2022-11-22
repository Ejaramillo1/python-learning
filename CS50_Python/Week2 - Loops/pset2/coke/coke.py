"""
CS50 Python --Coke Machine--

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/2/coke/

---------------------DESCRIPTION--------------------------
In a file caled coke.py, implement a program that prompts the user to insert a coin,
one a a time, each time informing the user of the amount due. Once the user has inputted at least 50 cents,
output how many cents in change the user us owed. Assume that the user will only input integers, and ignoreany integer that isn't
an accepted denomination.
"""
def main():
    cost = 50
    while True:
        pay = get_coins()
        cost = cost - pay
        if cost > 0:
            print(f"Amount Due: {cost}")
            continue
        else:
            print(f"Change owed {abs(cost)}")
            break



def get_coins():
    valid = [5, 10,25,50]
    while True:
        n = int(input("Insert coin: "))
        if n in valid:
            return n
        else:
            return False


if __name__ == "__main__":
    main()