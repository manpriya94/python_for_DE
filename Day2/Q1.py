""" 1- Vowel Counter : Ask the user to enter a sentence.

Count how many vowels (a, e, i, o, u) are in the sentence

Print the count
 """

userinput = input("enter a sentence")
count = 0 
for letter in userinput:
    if letter.lower() in ['a','e','i','o','u']:
        count = count + 1

print(count)