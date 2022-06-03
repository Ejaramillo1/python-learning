"""
Write a program that works out wheter if a given number is odd or even number.

Even numbers can be divided by 2 with no remainder
"""

def main():
 # 🚨 Don't change the code below 👇
    number =  int(input("Which number do you want to check? "))

    if number % 2 != 0:
        print(f"The number {number} is odd")
    else:
        print(f"The number {number} is even") 


if __name__ == "__main__":
    main()