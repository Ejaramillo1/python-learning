"""
CS50 Python --Testing my twttr--

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/5/test_twttr/

---------------------DESCRIPTION--------------------------
In a file called twttr.py, reimplement twttr.py from problem set2, restructuring
your code per the below, wherein shorten expects a str as an input and returns
that same str but with vowels (A,E,I,O, and U) ommited, whether inputted in uppercase
or lowercase.
"""

def main():
    # Ask the user for input
    user_text = input("Insert the text here: ")
    print(shorten(user_text))


# Function to detect a vowel

def shorten(word):
    vowels = 'aeiou'
    for c in word:
        if c.lower() in vowels:
            word = word.replace(c, "")
    return word


if __name__ == "__main__":
    main()

