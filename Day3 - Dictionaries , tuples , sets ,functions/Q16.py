""" 16- You have a dictionary with student names and a list of their marks.
marks = {
    'Ankit': [80, 90, 85],
    'Riya': [70, 60, 75],
    'Soham': [88, 92, 90]
}

Write a function to return names of students whose average is above 80.

# Output: ['Ankit', 'Soham']
 """
marks = {
    'Ankit': [80, 90, 85],
    'Riya': [70, 60, 75],
    'Soham': [88, 92, 90]
}

stu_avg = {}
namelist = []
for a , b in marks.items() :
    stu_avg[a] = ( b[0] + b[1] + b[2] ) // 3
    if stu_avg[a] > 80 :
        namelist.append(a)

print(namelist)
