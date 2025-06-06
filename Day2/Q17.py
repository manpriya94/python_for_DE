""" 17- ipl= ['CSK','MI','KKR','LSG','PBKS']
take ipl team name as user input. display True if the team exists else display False. """

ipl= ['CSK','MI','KKR','LSG','PBKS']

team = input("team name : ")

if team in ipl :   #sol1
    print("true")
else : 
    print("false")

print(team in ipl)  # sol2