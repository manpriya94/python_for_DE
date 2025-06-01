""" 7- Number Type Checker : Ask the user to input a number.

Print whether it is:

Positive

Negative

Zero """

number = int(input("enter a number"))

if number > 0 :
    print("positive")
elif number < 0 :
    print("negavtive")
else:
    print("number is 0")