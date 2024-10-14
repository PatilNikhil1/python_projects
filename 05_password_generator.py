import random

# Data
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# greeting
print('Welcome to the PyPassword Generator!')

# user input
letters_ip = int(input('How many letters would you like in your password?\n'))
symbols_ip = int(input('How many symbols would you like?\n'))
numbers_ip = int(input('How many numbers would you like?\n'))

# letters list as per user input
a = []
for char in range(letters_ip):
    a.append(random.choice(letters))

# symbols list as per user input
for char in range(symbols_ip):
    a.append(random.choice(symbols))

# numbers list as per user input
for char in range(numbers_ip):
    a.append(random.choice(numbers))

# print total list simple addition
print(a)

# random order of list 
random.shuffle(a)

# final output list 
print(a)

# final output password
b = ''.join(a)
print(f'Your password is : {b}')




