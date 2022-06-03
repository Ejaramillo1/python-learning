import random

# 🚨 Don't change the code below 👇
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# First create a random number between 0 and the length of the names
random_number = random.randint(0,len(names) - 1)

# Select who is going to pay for the bill

print(f"{names[random_number]} is going to buy the meal today")