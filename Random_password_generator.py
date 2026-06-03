#========================================================================

#                    RANDOM PASSWORD GENERATOR                           

#========================================================================

import random
import string

print("\n==============================================\n")
print("           RANDOM PASSWORD GENERATOR           ")
print("\n==============================================\n")

# User input
length = int(input("Enter password length: "))

if(length <= 0):
    print("Password must be greater than 0\n")

else:
#chararters
    letters = string.ascii_letters
    numbers = string.digits
    symbols = string.punctuation


all_characters = letters + numbers + symbols


password = ""

for i in range(length):
    password += random.choice(all_characters)

#generate the password
print(f'Genearate Password : {password}')

print("\nThanks for using the password generator\n\n\n")
