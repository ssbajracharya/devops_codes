# Password generator       
import random
import string

pass_len = int(input("Enter password length: "))
spec_len = int(input("Enter how many special characters"))

diff_len = pass_len - spec_len

password = []


lower = string.ascii_lowercase
upper = string.ascii_uppercase
number = string.digits

char_num = lower + upper + number

symbols = string.punctuation

for i in range(diff_len):
    password.append(random.choice(char_num))
    
for j in range(spec_len):
    password.append(random.choice(symbols))
random.shuffle(password)

    
print("".join(password))