""" 12 - Password Strength Checker: Ask the user to enter a password.
Check the password against the following rules:
Rules:
Must be at least 8 characters
Must contain at least one uppercase letter
Must contain at least one lowercase letter
Must contain at least one digit
Must contain at least one special character (!@#$%^&*()_+-=, etc.)((anything that is not letter or digit))

Output:
If all rules are satisfied → print "Strong Password"

If 3–4 rules are satisfied → print "Moderate Password"

If fewer than 3 rules are satisfied → print "Weak Password" """

password = input("Please enter system password : ")
tchar = 0
ucnt = 0
lcnt = 0
dgt = 0
spcl = 0
for letter in password :
    tchar = tchar + 1

    if letter.islower() and letter.isalpha() :
        lcnt = lcnt + 1
    elif letter.upper() and letter.isalpha(): 
        ucnt = ucnt + 1   
    elif letter.isdigit() :
        dgt = dgt + 1
    else :
        spcl = spcl + 1
print(tchar , lcnt , ucnt , dgt , spcl)

rules = 0
if tchar >=8 :
    rules = rules + 1
if lcnt >=1 :
    rules = rules + 1
if ucnt >=1 :
    rules = rules + 1
if dgt >=1 :
    rules = rules + 1
if spcl >=1 :
    rules = rules + 1
print(rules)
if rules == 5 :
    print("Strong password")
elif rules >=3 :
    print("Moderate password")
elif rules <3 :
    print("Weak Password")
