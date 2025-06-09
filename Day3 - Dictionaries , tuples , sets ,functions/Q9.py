""" 9- Write a function that takes a string and returns the number of unique words (case-insensitive).
eg:
# Input: "Python is great and python is fun"
# Output: 5 """

#string = "Python is great and python is fun"

def unique_word(string) :
    unique_word = set()
    word_split = string.split()
    for word in word_split :
        unique_word.add(word.lower())
    return len(unique_word)

output = unique_word(input("enter a sentence : "))
print(output)