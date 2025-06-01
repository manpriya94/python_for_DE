""" 5- Find the Largest Number. Ask the user to enter three numbers a, b ,c with 3 inputs
Print the largest among them. """

a = input("enter number 1")
b = input("enter number 2")
c = input("enter number 3")


if a > b and b > c :
    print(a," is largest")
elif b > c :
    print(b," is larget")
else:
    print(c," is larget")