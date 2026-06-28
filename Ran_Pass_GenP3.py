import random
import string

num = int(input("Enter password length: "))

all_char = string.ascii_letters + string.digits

password = ""

for i in range(num):
    x = random.choice(all_char)
    password = password + x

print("Your Password is:", password)
