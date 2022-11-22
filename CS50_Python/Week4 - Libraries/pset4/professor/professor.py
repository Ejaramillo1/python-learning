"""
CS50 Python -- Little Professor --

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/4/professor/

---------------------DESCRIPTION--------------------------
In a file called profesor.py, implement a program that:
 * Prompts the user for a level, n. If the user does not input 1, 2 or 3, the program
 should prompt again.
 * Randomly generates ten (10) math problems formatted as X + Y =, wherein each
 of X and Y is a non-negative integer with n digits. No need to support operations other
 than addition (+).
 * Prompts the user to solve each of those problem. If an answer is not correct (or not even a number),
 the program should output EEE and prompt the user again, allowing the user up to three tries in total.
 If the user has still not answered correctly after three tries, the program should output the correct
 anser.
 The program should ultimately output the user's score, a number out of 10
"""

import random

def main():
    u_level = get_level()
    score = 0
    for i in range(0,10):
        # integer = generate_integer(u_level)
        sums = generate_integer(u_level)
        if simulate_round(sums) == 1:
            score += 1
    print(f"Score: {score}")


# Function to get the level
def get_level():
    while True:
        try:
            lvl = int(input("Level: "))
            if lvl > 3 or lvl < 1:
                raise ValueError("Level not supported")
        except ValueError:
            pass
        else:
            break
    return lvl

# Function to generate 10 random problems


def generate_integer(lvl):
    while True:
        try:
            if lvl == 1:
                X = random.randint(0,9)
                Y = random.randint(0,9)
            elif lvl == 2:
                X = random.randint(10,99)
                Y = random.randint(10,99)
            elif lvl == 3:
                X = random.randint(100,999)
                Y = random.randint(100,999)
            else:
                raise ValueError('Not accepted level')
        except ValueError:
            pass
        else:
            break
    return X, Y


def simulate_round(sum):
    f_dig = sum[0]
    s_dig = sum[1]
    result = f_dig + s_dig
    c_tries = 0
    correct = 0
    while c_tries <= 3:
        user_answer = int(input(f"{f_dig} + {s_dig} = "))
        if user_answer != result:
            c_tries += 1
            print('EEE')
            # print(f"number of tries {c_tries}")
            if c_tries == 3:
                print(f"{f_dig} + {s_dig} = {result}")
                break
        if user_answer == result:
            correct += 1
            break
    return correct

if __name__ == "__main__":
    main()