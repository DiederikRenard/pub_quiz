from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzies")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score = Label()
        self.score.config(text=f"Score: {self.quiz.score}", bg=THEME_COLOR, fg="white")
        self.score.grid(column=1, row=1)

        self.canvas = Canvas()
        self.canvas.config(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text=f"Hello",
            fill=THEME_COLOR,
            font=("Ariel", 20, "italic")
        )
        self.canvas.grid(column=0, row=2, columnspan=2, pady=35)

        correct_image = PhotoImage(file="images/true.png")
        self.correct = Button(image=correct_image)
        self.correct.config(
            width=90,
            height=90,
            highlightthickness=0,
            borderwidth=0,
            command=self.correct_ans
        )
        self.correct.grid(column=0, row=4)

        false_image = PhotoImage(file="images/false.png")
        self.false = Button(image=false_image)
        self.false.config(
            width=90,
            height=90,
            highlightthickness=0,
            borderwidth=0,
            command=self.false_ans
        )
        self.false.grid(column=1, row=4)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        q_text = self.quiz.next_question()
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.question_text, text=q_text)
        self.score.config(text=f"Score: {self.quiz.score}")

    def correct_ans(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_ans(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
