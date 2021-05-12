from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question_data in question_data:
    question_text = question_data['question']
    answer = question_data['correct_answer']
    question = Question(question_text, answer)
    question_bank.append(question)


quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is :: {quiz.score}/{quiz.question_number}")
