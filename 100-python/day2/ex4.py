#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇.

def main():
    #First ask the amount of the total bill
    bill = float(input("Welcome to the tip calculator!\nWhat whas the total bill? $ "))
    #Second ask for the percentage of the total bill that the customer wants to give
    prc =  float(input("What percentage tip would you like to give? 10, 12, or 15? "))
    #Third ask the number of peple the account is going to be split
    ppl = float(input("How many people to split the bill? "))

    total = calculate_total(bill, prc, ppl)

    print(f"Each person should pay: {total:.2f}")

def calculate_total(bill, percent, people):
    percent = percent / 100
    total = (bill * (1 + percent)) / people
    return total
    


if __name__ == "__main__":
    main()
