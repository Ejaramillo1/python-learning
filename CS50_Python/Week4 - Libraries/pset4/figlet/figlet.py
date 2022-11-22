"""
CS50 Python --Frank, Ian and Glen's Letters--

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/4/figlet/

---------------------DESCRIPTION--------------------------
In a file called figlet.py, implement a program that:
* Expects zero or two command-line arguments:
    * Zero if the user would like to output text in a random font.
    * Two if the user would like to output text in a specific font, in which case the first of the two
    should be -f or --font, and the second  of the two should be the name of the font.
* Prompts the user for a str of text.
* Outputs that text int he desired font
If the user provides two command-line arguments and the first is not -f or --font or the second is not the name of a font, the program
should exit via sys.exit with an error message
"""

import sys
from pyfiglet import Figlet

def main():
    if len(sys.argv) < 3:
        raw_text()
    elif sys.argv[1] != '-f':
        sys.exit("Invalid Argument")
    elif check_font(sys.argv[2]) == False:
        sys.exit("Font Not Listed")
    else:
        render_font(sys.argv[2])


def raw_text():
    text = input("Input: ")
    print(f"Output {text}")


def render_font(fontName):
    figlet = Figlet()
    fontName = figlet.setFont(font = fontName)
    text = input("Input: ")
    print(figlet.renderText(text))


def check_font(fontName):
    # get the list of all fonts
    figlet = Figlet()
    fonts = figlet.getFonts()
    for font in fonts:
        if fontName in fonts:
            return True
        else:
            return False

if __name__ == "__main__":
    main()

