""" 14- ipl= ['CSK','MI','KKR','LSG','PBKS']

take a ipl team name as input from user and display a list of all elements from that name.

example : input : KKR
output : ['KKR','LSG','PBKS'] """

ipl= ['CSK','MI','KKR','LSG','PBKS']

team = input("input ipl team name : ")

print(ipl[ipl.index(team) : ])  #solution 1

for t in range(len(ipl)) :    #solution 2
    if ipl[t] == team :
        print(ipl[t:])