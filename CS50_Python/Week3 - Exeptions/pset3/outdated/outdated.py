"""
CS50 Python --Grocery List--

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/3/outdated/

---------------------DESCRIPTION--------------------------
In a file called outdated.py, implement a program that promts the user for a date, anno Domini, in month-day-year order,
no matter the country, formatting years with four digits, and days with two digists, "padding" each with leading zeroes as needed.
"""

def main():
    get_month()

def get_month():
    # This while loop is handling exceptions, basically reprompts when the user enters incorrect values
    while True:
        try:
            #This section runs if the user enters a date with the format mmmm dd, yyyy
            # get input from the user
            user_date = input("Date: ")
            # use the function called long_date to transform the date the user inputed
            transformed_date = long_date(user_date)
            # This is handling the specific erors when the user enters a month bigger than 12 or a day bigger than 31

            if transformed_date == 'error':
                    raise ValueError("Month bigger than 12")

        except (ValueError):
            # This section runs if the user enters a date with the format mm-dd-yyyy
            try:
                transformed_date = short_date(user_date)
                 # This is handling the specific erors when the user enters a month bigger than 12 or a day bigger than 31
                if transformed_date == 'error':
                    raise ValueError("Month bigger than 12")
            except (ValueError):
                pass
            else:
                break
            pass
        else:
            break
    return transformed_date
    # print(f"The year is {year} and month {month} and day {day}")
    #  month, day, year = input("Date: ").split("/")
    # print(f"{year}-{month:02}-{day:02}")


# This is the function that converts long dates into short dates with the mmmm dd, yyyy format to yyy-mm-dd
def long_date(date):

    months = {
        "January": 1,
        "February": 2,
        "March": 3,
        "April": 4,
        "May": 5,
        "June":6,
        "July":7,
        "August":8,
        "September":9,
        "October":10,
        "November":11,
        "December":12}


    month_day, year = date.split(",")
    month, day = month_day.split(" ")
    for mth in months:
        if mth == month:
            month = int(months[mth])
    day = int(day)
    year = int(year)
    if month > 12:
        return 'error'
    elif day > 31:
        return 'error'
    else:
        return print(f"{year}-{month:02}-{day:02}")


# This is the function that converts short dates into short dates with the mmm-yy-dd format to yyyy-mm-dd
def short_date(date):
    month, day, year = date.split("/")
    month = int(month)
    year = int(year)
    day = int(day)
    if month > 12:
        return 'error'
    elif day > 31:
        return 'error'
    else:
        return print(f"{year}-{month:02}-{day:02}")

if __name__ == "__main__":
    main()