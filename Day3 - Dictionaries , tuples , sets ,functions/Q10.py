""" 10- Given a list of tuples like [(101, 'Keyboard', 799), (102, 'Mouse', 499)], 
write a function that converts it into a dictionary with product name as key and price as value.

eg:
# Output:
# {'Keyboard': 799, 'Mouse': 499} """



list_of_tuples = [(101, 'Keyboard', 799), (102, 'Mouse', 499)]

def product(list_of_tuples) :
    dict1 = {}
    for item in list_of_tuples :
        dict1[item[1]] = item[2]
    return dict1

output = product(list_of_tuples)
print(output)