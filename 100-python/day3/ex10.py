"""
Love Calculator:

You are going to write a program that tests the compatibility between
two people. To work out thelove score between two people:
    * Take both people's names and check for the number of times the letters
    in the word TRUE occurs.
    * Then ckeck for the number of times the letters in the word LOVE occurs
    * Then combine these numbers to make a 2 digit number
"""

def main():
# 🚨 Don't change the code below 👇
    print("Weocome to the Love Calculator!")
    name1 = input("What is your name? \n")
    name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

# Write your code below this line 
    combined_string = name1 + name2

    lower_case_string = combined_string.lower()

    love_score = int(count_letter(lower_case_string))

    if love_score < 10 or love_score > 90:
        print(f"Your score is {love_score}, you go together like coke and menthos")
    elif love_score >= 40 or love_score <= 50:
        print(f"Your score is {love_score}, you are alright together.")
    else:
        print(f"Your score is {love_score}")

   

def count_letter(names):
    cnt1 = 0
    cnt2 = 0
    for i in range(len(names)):
        if names[i] == 't' or names[i] == 'r' or names[i] == 'u' or names[i] == 'e':
            cnt1 += 1
        if names[i] == 'l' or names[i] == 'o' or names[i] == 'v' or names[i] == 'e':
            cnt2 += 1
    cnt1 = str(cnt1)
    cnt2 = str(cnt2)
    cnt = cnt1 + cnt2
    return cnt




if __name__ == "__main__":
    main()

