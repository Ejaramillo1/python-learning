# Demonstrates  how to define a function and this function performs a math operation

def main():
    x = int(input("What's x? "))
    print(f"{x} squared is", square(x))

def square(n):
    return n * n


if __name__ == "__main__":
    main()