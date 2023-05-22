#Write a function to find the largest number among three given input numbers

# def find_largest_number(number1, number2, number3):

#     largest = number1

#     if (number1 > number2) and (number1 > number3):
#         largest = number1
#     elif (number2 > number1) and (number2 > number3):
#         largest = number2
#     else:
#         largest = number3

#     print(f"The largest number is {largest}")


# find_largest_number(15, 23, 8)




def largest_number(num1,num2,num3):
    largest=num1
    if(num1>num2)and(num1>num3):
        largest=num1
    elif(num2>num1)and(num2>num3):
        largest=num2
    else:
        largest=num3

    print(f"largest number is {largest}")
largest_number(12,25,36)