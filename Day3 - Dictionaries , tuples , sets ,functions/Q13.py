""" 13- Write a function that takes a list of words and groups them into anagrams using dictionary.

# Input: ['listen', 'silent', 'enlist', 'rat', 'tar', 'art']

# Output:
# {
#   'eilnst': ['listen', 'silent', 'enlist'],
#   'art': ['rat', 'tar', 'art']
# } """

words =  ['listen', 'silent', 'enlist', 'rat', 'tar', 'art']
anagram= {}
for word in words :
    key = ''.join(sorted(word))
    print(anagram)
    if key not in anagram:
        
        anagram[key] = []
        print(anagram)

    anagram[key].append(word)

print(anagram)



