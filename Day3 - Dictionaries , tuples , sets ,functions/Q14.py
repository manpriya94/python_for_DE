""" 14- Write a function most_frequent_char(s) that takes a string and returns the character that appears the most (excluding spaces).
eg:
# Input: "welcome to python"
# Output: 'o' """

s = "welcome to python"
fdict = {}
def most_frequent_char(s) :
    for letter in s.replace(" ","") :
        if letter in fdict :
            fdict[letter] = fdict[letter] + 1
        else :
            fdict[letter] = 1 
       
    return max(fdict , key = fdict.get)

result = most_frequent_char(s)
print(result)


    
