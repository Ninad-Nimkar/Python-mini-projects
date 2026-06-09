import random

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '0123456789'
symbols = '!@#$%^&*()_+-=[]|;:,.<>?/'

password = "".join(random.choice(letters + numbers + symbols) for x in range(14))

print(f"Password: {password} ")