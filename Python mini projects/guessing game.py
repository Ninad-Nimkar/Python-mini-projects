import random

num = random.randint(1, 10)

chances = 5
guess = 0
chances_left = 0

while chances_left == 0:
    guess = int(input("Enter your guess: "))

    if guess == num:
        print("Correct guess")
    
    elif guess > num:
        print("try a lower number")
        chances_left -= chances

    elif guess < num:
        print("try a higher number")
        chances_left -= chances

    else:
        break
