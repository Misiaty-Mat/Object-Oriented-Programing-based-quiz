from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

bank_questions = []

for raw_question in question_data:
    text_question = raw_question["question"]
    answear_question = raw_question["correct_answer"]
    question = Question(text_question, answear_question)
    bank_questions.append(question)

quiz = QuizBrain(bank_questions)

while quiz.still_has_questions():
    quiz.next_question()

print("That is the end of this quiz!")
print(f"Your score was {quiz.score} out of {quiz.question_number}")
