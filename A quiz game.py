questions = ("Whats the speed of light?",
            "whats the speed of sound?",
            "which is the First planet in solat system?")

options = (("A.3*10^8", "B.7*10^5", "C.3*10^4", "D.9*10^2"),
           ("A.345 m/s", "B.343 m/s", "C.343 k/s", "D.34 m/s"), 
           ("A.earth", "B.mars", "C.jupiter", "D.mercury"))

answers = ("A", "B", "D")

guesses = []
score = 0
question_num = 0


for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    print()

    
    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer   ")
    question_num += 1

print("-------------------------")
print("---------RESULTS---------")
print("-------------------------")

print("Answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
   
print()

print("Your guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")

print()

score = int(score / len(questions) * 100)
print(f"Your score: {score}%")