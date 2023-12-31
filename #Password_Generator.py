#PassWord_Generator
import random

chars = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()"
length = int(input("Enter Desired Length: "))
password = ""

for a in range(length):
    password += random.choice(chars)
    
print(f"Passcode is {password}")
    