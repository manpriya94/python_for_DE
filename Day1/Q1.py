""" 1- write a program which takes 3 inputs from user as principle amount (int) and rate of annual interest (float) and total tenure (in years). 
write a program to print total amount value at the end fo the tenure

example : principle : 100 , interest percent 8 , tenure = 2  then amount will be : 100*1.08*1.08 = 116.64 """


PAmount = int(input("Enter principal Amount"))
Irate = float(input("Enter annual rate of interest"))
Tenure = int(input("Enter tenure"))

Amount = PAmount * ((1 + Irate/100) ** Tenure)

print("Total amount is : ",Amount)

