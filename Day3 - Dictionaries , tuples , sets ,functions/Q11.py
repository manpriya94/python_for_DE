""" 11- Write a function that counts word frequency in a paragraph and 
ignores common stopwords like 'is', 'the', 'a', 'an', 'and'. """


paragraph = """Hello Hi My name is priyanka , I am from lucknow. My husbands name is Prabodh. I live in the bangalore."""
stop_words = ['is', 'the', 'a', 'an', 'and']

def word_count() :
    count = 0
    for word in paragraph.split() :
        
        if word.lower() in stop_words :
            count = count
        else :
            count = count + 1

    return count

result =  word_count()

print(result)
