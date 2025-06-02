""" 9- Even Number Printer : Ask the user for a number n.

Print all even numbers from 1 to n 

eg : input 7
output 
2
4
6 """

num = int(input("enter a number"))

for i in range(1,num+1) : 
    if i % 2 == 0 :
        print(i)