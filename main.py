import random
import string

chrvalues = string.ascii_letters + string.digits + string.punctuation

password_len = int(input("Enter the password lenth:- "))

password = ""
for i in range(password_len):
    password += random.choice(chrvalues)

print("your random password is:- ",password)