from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo
question_bank = []

for data in question_data:
    question = Question(data["question"], data["correct_answer"])
    question_bank.append(question)

print(logo)
print("Welcome to the Quizz.")
number_of_questions = int(input("How many questions do you want?: "))
quiz = QuizBrain(question_bank, number_of_questions)

while quiz.is_question_available():
    quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
