from question import Question

question_prompt = [
    "What is my name? \n(a) Afua \n(b) Akua \n(c) Ama \n(d) Yaa \n\n",
    "How old am I? \n(a) 25 \n(b) 27 \n(c) 24 \n(d) 23 \n\n",
    "What is my program of study? \n(a) Cybersecurity \n(b) Information security \n(c) Computer Science \n(d) Software engineering \n\n"
]

questions = [
    Question(question_prompt[0], "a"),
    Question(question_prompt[1], "c"),
    Question(question_prompt[2], "b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " correct")

run_test(questions)