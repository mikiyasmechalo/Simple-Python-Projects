import html
from random import randint


class QuizBrain:
    def __init__(self, question_list, number_of_questions):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0
        self.number_of_questions = number_of_questions

    def next_question(self):
        q_no = self.question_number
        self.question_number += 1
        num = randint(0, len(self.question_list))
        print(len(self.question_list))
        question = self.question_list[num]
        # q = question.text.replace("&quot;", "'")
        # q = q.replace("&eacute;", "")
        q = html.unescape(question.text)
        self.question_list.remove(question)
        user_answer = input(f"Q.{q_no + 1}: {q} (True/False): ").lower()
        self.check_answer(user_answer, question.answer)

    def is_question_available(self):
        return self.question_number < self.number_of_questions

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You are right!")
            self.score += 1
        else:
            print("You are wrong!")
        print(f"The correct answer is {correct_answer}")
        print(f"Your current score is {self.score}/{self.question_number}\n")
