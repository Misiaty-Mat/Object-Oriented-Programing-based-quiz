from data import questions_data
from question_model import Question
from quiz_brain import QuizBrain
from ui import QuizUserInterface

bank_questions = []

# Getting a list of question objects
for raw_question in questions_data:
    text_question = raw_question["question"]
    answear_question = raw_question["correct_answer"]
    question = Question(text_question, answear_question)
    bank_questions.append(question)

# Instantiate object 'quiz' to be the engine of the quiz
quiz = QuizBrain(bank_questions)

# Instantiate object 'user_interface' to give user interface
user_interface = QuizUserInterface(quiz)
