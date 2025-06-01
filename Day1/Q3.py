""" 3- Ask the user to enter their age. If age is:

less than 13 → print "Child"

between 13 and 19 → print "Teenager"

20 or more → print "Adult" """

age = int(input("Please enter your age"))

if age < 13 :
    print("clild")
elif age >= 13 and age <=19 :
    print("Teenager")
else:
    print("Adult")


