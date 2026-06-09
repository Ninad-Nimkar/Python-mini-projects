import random

ran_num = random.randint(1, 20)

print("wassup! guess what number i'm thinking between 1 and 20.")

while ran_num:
    guess = int(input("take a guess: "))

    if guess < ran_num:
        print("too low")

    elif guess > ran_num:
        print("too high")
    
    else:
        print("you got it!")
        break
    