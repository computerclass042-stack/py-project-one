# Quiz game.

score = 0

print("Quiz Game")

answer = input("Q1: What is the capital of India? ")
if answer.lower() == "delhi":
    score += 1

answer = input("Q2: 5 * 6 = ? ")
if answer == "30":
    score += 1

print("Your Score:", score)
print("You won")