"""
Roller coaster with price calculation and asking for photo
"""
# Ask the user for his height
height = int(input("What's your height: "))
bill = 0

def main():
    if height >= 120:
        # First print welcome message
        print("You can ride the rollercoaster!")
        # Ask the user for his/her age
        age = int(input("What is your age? "))
        if age <= 12:
            bill = 5
            print("Please pay $5.")
        elif age <= 18:
            bill = 7
            print("Please pay $7.")
        else:
            bill = 12
            print("Please pay $12.")

        wants_photo = input("Do you want a photo taken? Y or N. ")
        if wants_photo == 'Y':
            bill += 3
        print(f"Your final bill is ${bill} ")

    else:
        print("Sorry, you have to grow taller before you can ride.")  

if __name__ == "__main__":
    main()  