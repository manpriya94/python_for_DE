""" 7- take 1 input from user in comma separated format  : first name , last name and age . Display the information in below format:

exmaple input : MoHit,ShArma,32

Display : my name is Mohit Sharma and I am 32 years old.

note that first letter of first name and last name both should be in capital letters and rest in small. 
"""

user_input = input("enter your first name , last name and age")
name_age_list = user_input.split(',' , 3)

first_name = name_age_list[0].capitalize()
last_name = name_age_list[1].capitalize()
age = name_age_list[2]

print(f"my name is {first_name} {last_name} and my age is {age}")