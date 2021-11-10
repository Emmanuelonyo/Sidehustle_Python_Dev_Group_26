import random
chars = ("abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*_-+ABCDEFGHIJKLMNOPQRSTUVWXYZ")
lenght = 15
number = 1
for i in range(number):
    password = ''
    for x in range(lenght):
        password += random.choice(chars)
print(password)