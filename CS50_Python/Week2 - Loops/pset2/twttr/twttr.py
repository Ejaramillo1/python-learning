"""
CS50 Python --Just setting up my twttr--

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/2/twttr/

---------------------DESCRIPTION--------------------------
In a file called twttr.py implement a program that prompts the user for
a str of text and then outputs that same text but with all vowels(AEIO and U)
omitted, whether inputted in uppercase or lowercase.
"""
# Main function

def main():
    # Ask the user for input

    user_text = input("Insert text here: ")
    print(vowel_detect(user_text))



# function to detect a vowel

def vowel_detect(word):
    vowels = 'aeiou'
    for vowel in word:
        if vowel.lower() in vowels:
            word = word.replace(vowel, "")
    return word

if __name__ == "__main__":
    main()


