import random
import string
length = int(input("Enter password length:"))

characters = string.ascii_letters 
numbers = input("include numbers?(yes/no):").lower()
symbols = input("incliude symbols?(yes/no):").lower()
if numbers == "yes":
    characters += string.digits
    if symbols == "yes":
        symbols += string.punctuation
password = " "
for i in range (length ):
    password += random.choice(characters)
print(" Your password is :" , password)

