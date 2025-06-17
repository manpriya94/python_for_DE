""" 6- write a function to convert above universities list to a dictionary. the keys should be the name of the university

eg : {'California Institute of Technology': {"entrolled_students" : 2175 , "fees": 37704} , and so on } 

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]"""

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

def uni_dict() : 
    university_dict = {}
    for univ, students, fees in universities :
        university_dict[univ] = { 
            "enrolled_student" : students ,
            "fees" : fees
        }
    return university_dict

result = uni_dict()
print(result)
        
        



