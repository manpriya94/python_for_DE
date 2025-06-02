""" 3- Ask the user to input a word.
Check if the word is a palindrome (same forward and backward) eg : madam 
Print appropriate message"""

word = input("enter a word")

reverse = word[::-1]

if word == reverse :
    print("word is palindrome")
else :
    print("word not palindrome")
    