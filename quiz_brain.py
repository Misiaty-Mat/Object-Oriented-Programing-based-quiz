import html

# Class made up to handle most of functionality of the quiz


class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_bank = question_bank

    def still_has_questions(self):
        return self.question_number < len(self.question_bank)

    def next_question(self):
        self.question = self.question_bank[self.question_number]
        self.question_number += 1
        self.question_text = html.unescape(self.question.text)
        return f"Q.{self.question_number}: {self.question_text} (True/False)?: "

    def check_answear(self, user_answear, correct_answear):
        if user_answear.lower() == correct_answear.lower():
            return True
            self.score += 1
        else:
            return False
