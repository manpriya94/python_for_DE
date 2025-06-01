""" 10 - Bill Splitter with Tip: Ask the user to input:

Total bill amount

Tip percentage (e.g., 10 for 10%)

Number of people

Calculate:

Tip amount = (bill × tip %) / 100

Total amount = bill + tip

Per person share = total amount / number of people

Print all three values clearly.

example output :

Tip: ₹100.0
Total Bill (with tip): ₹1100.0
Each person should pay: ₹275.0 """

bill = float(input("enter total bill amount"))
tipperct = int(input("enter tip amount"))
noofpeople = int(input("enter number of people"))

tip_amount = ((bill * tipperct) / 100)
tot_bill_with_tip = tip_amount + bill
share = tot_bill_with_tip / noofpeople

print("tip :",tip_amount)
print("bill amont tot ",tot_bill_with_tip)
print("share :", share)
