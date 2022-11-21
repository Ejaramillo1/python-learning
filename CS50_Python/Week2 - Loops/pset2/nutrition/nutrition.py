"""
CS50 Python --Nutrition Facts--

This is the set of assignments from CS50 Python course on Edx: the link to the full description of this
problemset is in the following link.

https://cs50.harvard.edu/python/2022/psets/2/nutrition/

---------------------DESCRIPTION--------------------------
In a file called nutrition.py, implement a program that prompts
consumers to input a frut and then outputs the number of calories
in one portion of that fruit.
"""

# Create a dictionary with the fruits

fruit_user = input("Item: ").lower()


fruits = [
    {"name":"Apple", "calories":"130"},
    {"name":"Avocado", "calories":"50"},
    {"name":"Banana", "calories":"110"},
    {"name":"Cantaloupe", "calories":"50"},
    {"name":"Grapefruit", "calories":"60"},
    {"name":"Grapes", "calories":"90"},
    {"name":"Honeydew Melon", "calories":"50"},
    {"name":"Kiwifruit", "calories":"90"},
    {"name":"Lemon", "calories":"15"},
    {"name":"Lime", "calories":"20"},
    {"name":"Nectarine", "calories":"60"},
    {"name":"Orange", "calories":"80"},
    {"name":"Peach", "calories":"60"},
    {"name":"Pear", "calories":"100"},
    {"name":"Pineapple", "calories":"50"},
    {"name":"Plums", "calories":"70"},
    {"name":"Strawberries", "calories":"50"},
    {"name":"Sweet Cherries", "calories":"100"},
    {"name":"Tangerine", "calories":"50"},
    {"name":"Watermelon", "calories":"80"}
    ]


for row in fruits:
    fruit = row["name"].lower()
    if fruit == fruit_user:
        cal = row["calories"]
        print(f"Calories: {cal}")

