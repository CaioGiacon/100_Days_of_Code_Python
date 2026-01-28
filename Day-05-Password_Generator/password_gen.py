import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print('Welcome to the PyPassword Generator!')
qtd_letters = int(input('How many letters would you like in your password?\n'))
qtd_symbols = int(input('How many symbols would you like?\n'))
qtd_numbers = int(input('How many numbers would you like?\n'))


password = []
for char in range(0, qtd_letters):
    password.append(random.choice(letters))
for char in range(0, qtd_symbols):
    password.append(random.choice(symbols))
for char in range(0, qtd_numbers):
    password.append(random.choice(numbers))
random.shuffle(password)

final_password = ''.join(password)
print(f'The final password is: {final_password}')

