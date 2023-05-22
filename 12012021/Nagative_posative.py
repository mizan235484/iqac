#Write a program to check if a number is positive, negative or zero

def number_checker(number):
    if number > 0:
        print("Number given by you is positive")
    elif number < 0:
        print("Number given by you is negative")
    else:
        print("Number given by you is zero")

number_checker(-9)
