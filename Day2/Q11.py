""" 11 - Password Analyzer : Ask the user to enter a password.
Your program should print:

Total number of characters
Number of uppercase letters
Number of lowercase letters
Number of digits
Number of special characters (anything that is not letter or digit)

eg:
Input: Ankit@123
Output:

Total characters: 9
Uppercase letters: 1
Lowercase letters: 4
Digits: 3
Special characters: 1 """

password = input("Please enter system password")
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