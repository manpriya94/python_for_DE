""" 15- Write a function that takes a list of numbers and returns a dictionary with keys "min" and "max".
eg:
# Input: [5, 2, 8, 1, 9]
# Output: {'min': 1, 'max': 9} """

numbers = [1,5,9,8,6,2,11]
ndict = {}
length = len(numbers)
def min_max(numbers) :
    numbers.sort()
    ndict = { "min" : numbers[0] ,
          "max" : numbers[length - 1 ]}
    return ndict

result = min_max(numbers)
print(result)
    
