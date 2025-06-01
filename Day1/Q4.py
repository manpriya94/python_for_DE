""" 4- Create two variables: username = "admin" and password = "1234".

Ask the user to input username and password.

If both match, print “Login successful”, else “Invalid credentials”. """

username = "admin"
password = "1234"

uname = input("enter username")
pwd = input("enter password")

if username == uname and password == pwd:
    print("Login successfull")
else:
    print("invalid credentials")