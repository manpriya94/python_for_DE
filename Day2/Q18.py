""" 18-ipl= ['CSK','MI','KKR','LSG','PBKS']
take a user input contains 2 comma seprated values index,new_team . Add the new value at that index in the list. 
Display the old list , new list,length of original and new list

example : input : 2,SRH
output : 
old list : ['CSK','MI','KKR','LSG','PBKS'] and length 5
new list : ['CSK','MI','SRH','KKR',LSG','PBKS'] and length 6 """

ipl= ['CSK','MI','KKR','LSG','PBKS']
ipl_old = ipl[:]
userinput = input("index and team name : ")
value = userinput.split(',')

ipl.insert(int(value[0]),value[1])

print(ipl_old , len(ipl_old))
print(ipl , len(ipl))