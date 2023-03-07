from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain) -> None:
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title('Quizzlets')
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        self.canvas = Canvas(width=300, height=250, bg='white')

        #Labels
        self.question_text = self.canvas.create_text(
            150, 
            125,
            width=280,
            text="Kanye Quote Goes HERE", 
            font=("Arial", 20, "italic"), 
            fill="black"
        )
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.score_text = Label(text='Score: 0', fg='white', bg=THEME_COLOR, font=("Arial", 20, "italic"))
        self.score_text.grid(column=1, row=0)
        # self.score_text = self.canvas.create_text(0, 0, text="Score: 0", font=, fill="black")

        #Buttons
        img_false = PhotoImage(file="images/false.png")
        self.btn_false = Button(image=img_false, highlightthickness=0, command=self.false_pressed)
        self.btn_false.grid(column=1, row=2)

        img_true = PhotoImage(file="images/true.png")
        self.btn_true = Button(image=img_true, highlightthickness=0, command=self.true_pressed)
        self.btn_true.grid(column=0, row=2)

        self.get_next_question()

        self.window.mainloop()


    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score_text.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='You have reached the end of the quiz')
            self.btn_false.config(state='disabled')
            self.btn_true.config(state='disabled')


    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('True'))
        # print('ehllo')


    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)
        # print('false')


    def give_feedback(self, is_right):
        print(is_right)
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')

        self.window.after(1000, self.get_next_question)
        # self.canvas.config(bg='white')