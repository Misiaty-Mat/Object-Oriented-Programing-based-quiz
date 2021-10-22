from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

# Graphical User Interface
class QuizUserInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz = quiz

        self.window = Tk()
        self.window.title("Quiz time!")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_banner = Label(
            text="Score: 0", bg=THEME_COLOR, fg="white", font=("Arial", 12)
        )
        self.score_banner.grid(column=1, row=0, padx=20, pady=20)

        self.canvas = Canvas(width=300, height=250, bg="white")
        self.canvas.grid(column=0, row=1, columnspan=2, padx=20, pady=20)
        self.question_txt = self.canvas.create_text(
            150,
            125,
            width=280,
            text="Answear them all!",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"),
        )

        true_img = PhotoImage(file="images/true.png")
        self.true_btn = Button(
            image=true_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.btn_press_true,
        )
        self.true_btn.grid(column=0, row=2, padx=20, pady=20)

        false_img = PhotoImage(file="images/false.png")
        self.false_btn = Button(
            image=false_img,
            highlightthickness=0,
            bg=THEME_COLOR,
            command=self.btn_press_false,
        )
        self.false_btn.grid(column=1, row=2, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            question_txt = self.quiz.next_question()
            self.canvas.itemconfig(self.question_txt, text=question_txt)
        else:
            self.canvas.itemconfig(
                self.question_txt, text="You have reached the end of the quiz!"
            )

            self.true_btn.config(state="disabled")
            self.false_btn.config(state="disabled")

    def btn_press_true(self):
        is_right = self.quiz.check_answear("True", self.quiz.question.answear)
        self.give_feedback(is_right)

    def btn_press_false(self):
        is_right = self.quiz.check_answear("False", self.quiz.question.answear)
        self.give_feedback(is_right)

    def give_feedback(self, is_right: bool):
        if is_right:
            self.canvas.config(bg="green")
            self.quiz.score += 1
        else:
            self.canvas.config(bg="red")

        self.score_banner.config(text=f"Score: {self.quiz.score}")
        self.window.after(1000, self.get_next_question)
