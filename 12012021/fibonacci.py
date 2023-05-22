'''
The Fibonacci sequence is a sequence where the next term is the sum of the previous two terms. The first two terms of the Fibonacci sequence are 0 followed by 1. Now write a program to print fibonacci series up to a certain number
'''


def fibonacci_printer(end_number):
    a, b = 0, 1
    count = 0
    while count < end_number:
        a, b = b, a + b
        print(b)
        count += 1


fibonacci_printer(10)
