""" 15- ipl= ['CSK','MI','KKR','LSG','PBKS']

take a ipl team name as input from user and display a list of all elements except input one

example : input : KKR
output : ['CSK','MI','LSG','PBKS'] """

ipl= ['CSK','MI','KKR','LSG','PBKS']

team = input("input ipl team name : ")
ipl.remove(team)
print(ipl)
