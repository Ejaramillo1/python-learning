from ast import increment_lineno


# We want to guess the cube of the following number
cube = 29

# Epsilon is going to tell us how close do we want to get to the answer
epsilon = 0.01

guess = 0.0

# Size of which I am going to increase my guess
increment = 0.001

# Keep track of how many times do I go trough the loop while i do this
num_guesses = 0
while abs(guess**3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1
print('num_guesses =', num_guesses)
if abs(guess**3 - cube) >= epsilon:
    print('Failed on cube root of', cube)
else:
    print(guess, 'is close to the cube root of', cube)