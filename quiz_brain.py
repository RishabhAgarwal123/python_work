class QuizBrain:

    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer.lower():
            self.score += 1
            print(f"You got it correct. ")
        else:
            print("Wrong answer")
        print(f"The correct answer was {correct_answer}")
        print(f"Your score is {self.score}/{self.question_number}")
        print("\n")

    def next_question(self):
        question = self.question_list[self.question_number].question_name
        correct_answer = self.question_list[self.question_number].answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number} - {question} (True/False) : ").lower()
        self.check_answer(user_answer, correct_answer)

    def still_has_questions(self):
        if self.question_number < len(self.question_list):
            self.score
            return True
        else:
            return False

