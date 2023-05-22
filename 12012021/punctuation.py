''' Write a function that can remove punctuation marks from a string
    punctuations: "!()-[]{};:'"\,<>./?@#$%^&*_~"
'''


def punctuations_remover(string):
    punctuations = "!()-[]{};:\,<>./?@#$%^&*_~"

    fresh_word = ""

    for char in string:
        if char not in punctuations:
            fresh_word += char

    return fresh_word


print(punctuations_remover("He,ll.o>"))
