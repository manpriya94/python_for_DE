""" 5- write a program which takes the name of the user as input and print the index of character 'a' 
in the string. if 'a' is not there then return -1. """

name = input("enter ur name")

for i in range(len(name)) : 
    if name[i] == 'a' :
        print(name[i])
        break
else :
    print(-1)