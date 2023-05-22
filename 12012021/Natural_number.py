# If any natural number is greater than 1 and having no positive divisors other than 1 and the number itself then it's called a prime number. For example: 3, 7, 11 etc are prime numbers. Now write a function that can check if a number is prime number or not

def prime_checker(number):
    if number > 1:
        for i in range(2, number):
            if (number % i) == 0:
                print(f"{number} is not a prime number")
                break
        else: # NOTICE THIS ELSE BLOCK IS PART OF FOR STATEMENT NOT A PART OF IF STATEMENT
            print(f"{number} is a prime number")
    else:
        print(f"{number} is not a prime number")

prime_checker(10)