# Write a function to find even or odd

def number_checker(number):
    if number % 2 == 0:
        print(f"{number} is even number")
    else:
        print(f"{number} is odd number")

number_checker(5)