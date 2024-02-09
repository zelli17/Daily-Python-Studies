import random

chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPPQRSTUVWXYZ0123456789!@#$%^&*().,?'

num =int(input("enter number of passwords you want to generate"))
len =int(input("enter the length of generated password"))

for pwd in range(num):
    passwords = ''
    for c in range(len):
        passwords += random.choice(chars)
    print(passwords)