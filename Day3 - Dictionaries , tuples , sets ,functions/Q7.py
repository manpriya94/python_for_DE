""" 7- write a function that finds the largest number in a list(unsorted) of integers without using sort/sorted method. """

num_list = [1,2,37,6,8,9,4,100,55,200,90]

def largest_num() :
    largest = 1 
    for i in range(len(num_list) - 1 ) :
        if num_list[i] > num_list[i+1] :
            if num_list[i] > largest :
                largest = num_list[i]
        else :
            largest = num_list[i + 1]
    return largest

result = largest_num()
print(result)