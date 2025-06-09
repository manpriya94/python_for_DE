""" 2- from a list of numbers create 2 list , one containing only the even numbers and other only the odd numbers """

numbers = [1,4,5,3,7,8,20,15,17,100]

even = []
odd = []

[ even.append(nm) if nm%2 == 0  else odd.append(nm) for nm in numbers ]

print(even)
print(odd)