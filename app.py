#Python Quiz Game

questions = ("What is the largest ocean on Earth?",
             "What is the capital of India?",
             "Who painted the Mona Lisa painting?",
             "What is the chemical symbol for water?",
             "what is the largest continent in the world?")

options = (("A.The Atlantic Ocean","B.The Pacific Ocean","C.The Indian Ocean","D.The Arctic Ocean"),
           ("A.Chennai","B.Hyderabad","C.Raipur","D.New Delhi"),
           ("A.Leonardo da Vinci","B.Pablo Picasso","C.Claude Monet","D.Raphel"),
           ("A.CO2","B.NAOH","C.H2O","D.NACL"),
           ("A.North America","B.Asia","C.Antarctica","D.Europe"))

answers = ("B","D","A","C","B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("---------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1    

print("---------------------------")
print("          RESULTS          ")
print("---------------------------")

print("answers:", end="")
for answer in answers:
    print(answer , end="")
print()

print("guesses:", end="")
for guess in guesses:
    print(guess , end="")
print()


score = int(score / len(questions) * 100)
print(f"Your score is: { score }%")