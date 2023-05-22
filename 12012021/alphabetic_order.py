'''Write a function that can take a sentence and print each word of that sentence in alphabetic order'''

def print_alphabetically(sentence):
  # Split the sentence into a list of words
  words = sentence.split()
  
  # Sort the list of words alphabetically
  words.sort()
  
  # Print each word
  for word in words:
    print(word)

print_alphabetically("The quick brown fox jumps over the lazy dog")

