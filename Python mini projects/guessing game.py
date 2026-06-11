import random

num = random.randint(1, 10)

chances = 5
guess_counter = 0

print("Wassup, welcome to a simple number guessing game")

while chances > guess_counter:
    guess = int(input("Enter your guess: "))
    guess_counter +1

    if num < guess:
        print("pick a lower number")
    
    elif num > guess:
        print("pick a higher number")

    else:
        print("ggs, its Correct guess")
        break