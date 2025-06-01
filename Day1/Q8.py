""" 8- Password Strength Checker (Basic): Ask the user to enter a password.

If the password is:

Less than 6 characters → print "Weak Password"

6–10 characters → print "Moderate Password"

More than 10 characters → print "Strong Password"
 
ps: you can use len function to check the string length ex len(password) """

password = input("enter password")
plength = len(password)
if plength < 6 :
    print("weak password")
elif plength >=6 and plength <=10 :
    print("Moderate password")
else :
    print("strong password")