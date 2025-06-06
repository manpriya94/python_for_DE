""" 
10- Mask Email ID : Ask the user to enter their email address (ending with @gmail.com)

Mask everything except the first and last character of the username

Keep the total length of the username same

eg:
Input: ankitbansal@gmail.com
Output: a********l@gmail.com """

email = input("enter email ending with @gmail.com : ")
email_split = email.split('@',2)
domain = email_split[0]
masking = domain[0] +  '*' * (len(domain) - 2) + domain[-1]
print(masking + '@' + email_split[1])
