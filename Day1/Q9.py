""" 9- Leap Year Checker : Ask the user to enter a year.

Print whether it is a leap year or not.

Rules:

A year is a leap year if:

It is divisible by 4 and

Not divisible by 100 unless it's also divisible by 400

Example: 2000 → Leap year  1900 → Not a leap year   2024 → Leap year
 """

year = int(input("enter year"))

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0 :
    print("Leap year")
else :
    print("not leap year")