"""
CS50 Python -- Guessing Game --

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/4/game/

---------------------DESCRIPTION--------------------------
In a file called game.py
Prompts the user for a level,.
* If the user does not input a positive integer, the program should prompt again.
* Randomly generates an integer between 1 and , inclusive, using the random module.
* Prompts the user to guess that integer. If the guess is not a positive integer, the program should prompt the user again.
* If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
* If the guess is larger than that integer, the program should output Too large! and prompt the user again.
* If the guess is the same as that integer, the program should output Just right! and exit.
"""

# We are using the random package to generate a random integer
import random


def main():

# Prompts the user for a level
    numero = get_level()
    # If the user does not input a positive integer, the program should prompt again.
    while True:
        try:
            # Prompts the user to guess that integer.
            guess = get_guess()
#* If the guess is larger than that integer, the program should output Too large! and prompt the user again.
            if guess > numero:
                print("Too large!")
                raise ValueError('Guess is too large')
# If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
            elif guess < numero:
                print('Too small!')
                raise ValueError('Guess is too small')
        except ValueError:
            pass
#* If the guess is the same as that integer, the program should output Just right! and exit.
        else:
            print('Just right!')
            break

 # If the guess is not a positive integer, the program should prompt the user again.
def get_guess():
    while True:
        try:
            guess = int(input("Guess: "))
            if guess <= 0:
                raise ValueError('Level must be positive integer')
        except ValueError:
            pass
        else:
            break
    return guess

# Randomly generates an integer between 1 and , inclusive, using the random module.
def get_level():
    numb = 0
    while True:
        try:
            level = int(input("Level: "))
            if level <= 0:
                raise ValueError('Level must be positive integer')
            else:
                numb = random.randint(1, level)
        except ValueError:
            pass
        else:
            break
    return numb


if __name__ == "__main__":
    main()