""" 4- write a function to take a positive number as input from user. if the user enters negative number then keep prompting 
him to enter positive number until he enters the positive number and then print the same
 """

def positive() :
    number = int(input("input positive number"))
    if number > 0 : 
        print("postive number" , number)
        
    else :
        print("enter postive number")

positive()