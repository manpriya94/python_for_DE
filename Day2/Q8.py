""" 8-take 3 inputs from user : first name , last name and company name. create the email alias for the user and display it.  
Email alias is first 2 letters of first name , last 3 letters of last name and @company.com
example 
first name : MOhit
last name : sharma 
company : infosys

Display : morma@infosys.com 

note full email id should be in lower case """

f_name = input("first name")
l_name = input("last name")
company = input("company name")
email = f_name[:2] + l_name[-3:] + "@" + company + ".com"
print(email.lower())