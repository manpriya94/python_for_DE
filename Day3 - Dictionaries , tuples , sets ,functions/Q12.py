""" 12- You're given a dictionary like:
{
  'Ankit': ('Python',),
  'Riya': ('Python', 'Tableau'),
  'Soham': ('SQL', 'Power BI'),
  'Neha': ('Python', 'SQL', 'Power BI')
}
Write a function that returns:
a set of all unique courses and names of students enrolled in exactly 2 courses """

dict = {
  'Ankit': ('Python',),
  'Riya': ('Python', 'Tableau'),
  'Soham': ('SQL', 'Power BI'),
  'Neha': ('Python', 'SQL', 'Power BI')
}

courses = dict.values()
courseset = set()
def courses() :
    for i in courses :
        i.add(courseset)
    return courseset

result = courses()

print(result)
