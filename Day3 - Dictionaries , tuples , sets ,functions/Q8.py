""" 8- Write a function get_topper(student_marks) that takes a dictionary where keys are 
student names and values are their marks. 
Return the name(s) of the student(s) with the highest marks.
eg:
# Input:
# {'Ankit': 88, 'Shivansh': 92, 'Riya': 92, 'Soham': 85}
# Output: ['Shivansh', 'Riya'] """

student_marks = {'Ankit': 88
        , 'Shivansh': 92
        , 'Riya': 92
        , 'Soham': 85 }
def get_topper(student_marks) :
    high = max(student_marks.values())
    output = []
   
    for key1 in student_marks :
        if student_marks[key1] == high :
            output.append(key1)
    return output

result = get_topper(student_marks)
print(result)
