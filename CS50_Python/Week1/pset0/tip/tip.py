"""
CS50 Python --Tip Calculator--
This is the first problemset from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link. 

https://cs50.harvard.edu/python/2022/psets/0/tip/

---------------------DESCRIPTION--------------------------

Well, we’ve written most of a tip calculator for you. Unfortunately, we didn’t have time to implement two functions:
dollars_to_float, which should accept a str as input (formatted as $##.##, wherein each # is a decimal digit), 
remove the leading $, and return the amount as a float. For instance, given $50.00 as input, it should return 50.0.
percent_to_float, which should accept a str as input (formatted as ##%, wherein each # is a decimal digit), remove the 
trailing %, and return the percentage as a float. For instance, given 15% as input, it should return 0.15.
"""

def main():
    dollars = dollars_to_float(input("How much was the meal?: "))
    percent = percent_to_float(input("What percentage would you like to tip?: "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")

def dollars_to_float(d):
    dd = d.replace("$", "")
    return float(dd)


def percent_to_float(p):
    pp = p.replace("%", "")
    pp_conv = float(pp) / 100
    return pp_conv

if __name__ == "__main__":
    main()