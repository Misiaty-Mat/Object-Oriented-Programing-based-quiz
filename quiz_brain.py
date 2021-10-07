class QuizBrain:
    def __init__(self, question_bank):
        self.question_number = 0
        self.score = 0
        self.question_bank = question_bank

    def still_has_questions(self):
        return self.question_number < len(self.question_bank)

    def next_question(self):
        question = self.question_bank[self.question_number]
        self.question_number += 1
        user_answear = input(
            f"Q.{self.question_number}: {question.text} (True/False)?: ")
        self.check_answear(user_answear, question.answear)

    def check_answear(self, user_answear, correct_answear):
        if user_answear.lower() == correct_answear.lower():
            print("You got it!")
            self.score += 1
        else:
            print("You got it wrong!")
        print(f"The correct answear was {correct_answear}")
        print(f"Your current score is {self.score}/{self.question_number}")
        print("\n")
