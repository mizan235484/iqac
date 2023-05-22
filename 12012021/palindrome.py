'''
If a word remains the same after reversing it then it's a palindrome. Now define a function to detect if a word is palindrome or not

'''



def is_palindrome(word):
    reversed_word = ""

    for char in word:
        reversed_word = char + reversed_word

    return word == reversed_word


print(is_palindrome("mim"))





