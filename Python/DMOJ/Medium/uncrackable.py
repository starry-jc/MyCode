# Problem: wc17c3j3

# Defining password
password = input()

# Defining uppercase, lowercase, numbers
uppercase = 0
lowercase = 0
numbers = 0

# Testing for loop
for char in password:
    if char.isupper():
        uppercase += 1
    elif char.islower():
        lowercase += 1
    elif char.isnumeric():
        numbers += 1

# Checking to see if they meet the min / max character count
# Defining password - password length
length = uppercase + lowercase + numbers

# Defining checklength
checklength = length >= 8 and length <= 12

# Defining checkcase
checkcase = lowercase >= 3 and uppercase >=2 and numbers >= 1

if checklength and checkcase:
    print('Valid')
else:
    print('Invalid')