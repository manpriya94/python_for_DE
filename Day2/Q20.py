""" 20- Word Length Filter : Ask the user to enter a sentence and a number n as 2 inputs

Your program should Split the sentence into words
Print all words with length greater than or equal to n

eg: 
Enter a sentence: Python is super fun and powerful
Enter minimum word length: 5

Output:
Python
super
powerful """

input1 = input("enter sentence : ")
input2 = input("number n : ")
str_split = input1.split(' ')

for word in str_split :
    if len(word) > int(input2) : 
        print(word)