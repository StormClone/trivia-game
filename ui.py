import time
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ('Arial', 20, 'italic')


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        """initialize ui"""
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzer")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        # -- SCORE LABEL -- #
        self.score = Label(self.window, text=f"Score: 0", bg=THEME_COLOR, fg='white', pady=20, font=("Arial", 10))
        self.score.grid(column=1, row=0)

        # -- CANVAS -- #
        self.canvas = Canvas(self.window, width=300, height=250)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        self.question_text = self.canvas.create_text(150, 125, width=280, font=FONT, text="Question", fill=THEME_COLOR)

        # -- BUTTONS -- #
        self.img_check = PhotoImage(file="images/true.png")
        self.b_correct = Button(self.window, image=self.img_check, highlightthickness=0, command=self.answer_true)
        self.b_correct.grid(column=0, row=2)

        self.img_cross = PhotoImage(file="images/false.png")
        self.b_wrong = Button(self.window, image=self.img_cross, highlightthickness=0, command=self.answer_false)
        self.b_wrong.grid(column=1, row=2)

        # -- INITIALIZE QUESTION -- #
        self.get_next_question()

        self.window.mainloop()

# ----------------- METHODS -------------------- #
    def get_next_question(self):
        """gets next question and shows it on the canvas"""
        self.canvas.config(bg='white')
        self.canvas.itemconfig(self.question_text, fill=THEME_COLOR)
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the question list.")
            self.b_wrong.config(state='disabled')
            self.b_correct.config(state='disabled')

    def answer_true(self):
        """user inputs true as their answer and gets feedback"""
        if self.quiz.check_answer('True'):
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.score.config(text=f"Score: {self.quiz.score}")
        self.canvas.itemconfig(self.question_text, fill='white')
        self.window.after(1000, self.get_next_question)

    def answer_false(self):
        """user inputs false as their answer and gets feedback"""
        if self.quiz.check_answer('False'):
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.score.config(text=f"Score: {self.quiz.score}")
        self.canvas.itemconfig(self.question_text, fill='white')
        self.window.after(1000, self.get_next_question)
