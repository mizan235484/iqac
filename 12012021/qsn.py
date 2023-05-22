'''1. Write a Python program that takes two numbers as input and prints their sum.'''

# num1 = float(input("Enter the first number: "))
# num2 = float(input("Enter the second number: "))
# sum_result = num1 + num2

# print("The sum of", num1, "and", num2, "is:", sum_result)


'''2. Write a Python program that takes a list of integers as input and prints the sum all of'''
# def sum_even_numbers(numbers):
#     return sum([number for number in numbers if number % 2 == 0])

# numbers = [1, 2, 3, 4, 5, 6,]
# print(sum_even_numbers(numbers))


'''3. Write a Python program to check if a given string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward sequence of charact and backward.'''

# def is_palindrome(s):
#     return s == s[::-1]

# string = "racecar"
# if is_palindrome(string):
#     print("Yes, it's a palindrome")
# else:
#     print("No, it's not a palindrome")
# print(is_palindrome("201"))





''' 4. Write a Python program that reads a text file and counts the frequency of each word in the file. Display the top three most frequent words along with their frequencies.'''

# from collections import Counter

# def count_words(filename):
#     try:
#         with open(filename, 'r') as file:
#             # Read the file and split into words
#             words = file.read().lower().split()

#             # Count the frequency of each word
#             word_counts = Counter(words)

#             # Get the top three most frequent words
#             top_words = word_counts.most_common(3)

#             # Display the results
#             print("Top 3 most frequent words:")
#             for word, count in top_words:
#                 print(f"{word}: {count}")
#     except FileNotFoundError:
#         print("File not found.")

# # Replace 'filename.txt' with the path to your text file
# count_words('all.txt')


'''or'''

# from collections import Counter
# import re

# # Prompt the user to enter the file name
# file_name = input("Enter the file name: ")

# # Read the contents of the file
# with open(file_name, 'r') as file:
#     # Read the file content and split it into words
#     content = file.read()
    
#     # Remove punctuation and convert to lowercase
#     content = re.sub(r'[^\w\s]', '', content.lower())

# # Split the content into words
# words = content.split()

# # Count the frequency of each word
# word_counts = Counter(words)

# # Get the top three most frequent words
# top_words = word_counts.most_common(3)

# # Display the top three words with their frequencies
# print("Top Three Most Frequent Words:")
# for word, count in top_words:
#     print(f"{word}: {count} occurrences")


