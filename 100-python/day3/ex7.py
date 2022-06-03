
"""
Roller coaster with price calculation
"""
# Ask the user for his height
height = int(input("What's your height"))

def main():
    if height >= 120:
        # First print welcome message
        print("You can ride the rollercoaster!")
        # Ask the user for his/her age
        age = int(input("What is your age? "))
        if age <= 12:
            print("Please pay $5.")
        elif age <= 18:
            print("Please pay $7.")
        else:
            print("Please pay $12.")
    else:
        print("Sorry, you have to grow taller before you can ride.")  

if __name__ == "__main__":
    main()  

