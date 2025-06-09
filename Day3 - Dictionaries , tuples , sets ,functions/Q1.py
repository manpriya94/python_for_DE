""" 1- write a function to find the median of the numbers in a list of numbers unsorted.  """

numbers = [1,2,4,5]
def num_median() :
    numbers.sort()
    l = len(numbers)
    if l % 2 == 0:
        return (numbers[l // 2] + numbers[l // 2 - 1]) / 2
    else :
        return numbers[l // 2]

a = num_median()
print(a)



