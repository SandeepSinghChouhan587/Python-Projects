email=input("Enter your email id:")
#username
username=email[:email.index("@")]
#print("User Name:",username)
#domain_name
domain_name=email[email.index("g"):]
#print("Domain Name:",domain_name)

output="Your user name is {} your Domain name is {}"
print(output.format(username,domain_name))