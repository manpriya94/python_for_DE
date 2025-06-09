""" 5- consider the below list of list conatins following information :

1. The name of a university 
2. The total number of enrolled students
3. The annual tuition fees

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

write a function to print follwoing information :
1- a list of all the universitites  : ['California Institute of Technology','Harvard',..so on]
2- total number of student entrolled in all the unversities together 
3- mean of tuition fees """

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

def university() :
    uni_list = []
    tot_stu = 0
    fees_tot = 0
    count = 0 
    for record in universities :
        uni_list.append(record[0])
        tot_stu = tot_stu + record[1]
        fees_tot =  fees_tot + record[2] 
        count = count + 1  
    return uni_list , tot_stu , fees_tot / count

uni_list , tot_stu , mean = university()
print(f"university list : {uni_list}\ntotal students : {tot_stu}\nmean of tution fees : {mean}")




