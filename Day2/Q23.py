""" 23 - you are given a sorted list . Ask user for an input integer value.

insert that element in the list so that list still remian sorted . dont use sort method.
a) solve it using insert method 
b) solve without insert and sort method 

my_list = [10,30,40,65,90]
eg : input = 35
output: [10,30,35,40,65,90] """

my_list = [10,30,40,65,90]

value = int(input("input interger value : "))
for i in range(len(my_list)) :
    if value < my_list[i] :
        my_list.insert(i,value)
        break

print(my_list)
