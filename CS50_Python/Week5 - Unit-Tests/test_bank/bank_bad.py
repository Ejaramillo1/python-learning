def main():
    user_text = input("Enter your greeting word here: ")
    print(value(user_text))


def value(greeting):
    greeting = greeting.strip().lower()
    if greeting.startswith('hello') :
        tip = 0
    elif greeting.startswith('h') and greeting != 'hello' :
        tip = 20
    else:
        tip = 100
    return tip


if __name__ == "__main__":
    main()