""" 16- ipl= ['CSK','MI','KKR','LSG','PBKS']
take a user input contains 2 comma seprated values index,new_team . 
replace the index element of list with new value and display the same

example : input : 2,SRH
output : ['CSK','MI','SRH','LSG','PBKS'] """

ipl= ['CSK','MI','KKR','LSG','PBKS']

value = input("index and team name : ")
value1 = value.split(',')

ipl[int(value1[0])] = value1[1]

print(ipl)