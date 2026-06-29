
score = 0


answer1 = input("1. What is the capital of France? ")

if answer1.lower() == "paris":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is Paris.")


answer2 = input("\n2. What is 5 + 3? ")

if answer2 == "8":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is 8.")


answer3 = input("\n3. Which planet is known as the Red Planet? ")

if answer3.lower() == "mars":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is Mars.")

# Final Score
print("\nQuiz Finished!")
print("Your final score is:", score, "out of 3")