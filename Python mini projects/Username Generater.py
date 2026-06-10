import random

names = ['John', 'Jane', 'Doe', 'Alice', 'Bob', 'Charlie', 'Diana', 'Eve'] #you can add more names to the list if you want 
print("Welcome to the Username Generator!")
username = random.choice(names) + str(random.randint(100, 999))
print(f"Username: {username}")

