""" 2- write a program which takes the name of the user as input and replace all 
the occurence of character 'a' in the name to 'b' and print it. """

name = input("enter name ")

for letter in name :
    if letter == 'a' :
        name = name.replace('a','b')

print(name)