from tkinter import * #type: ignore
THEME_COLOR = "#375362"

class QuizIterface:
    def __init__(self, quiz, score):
        self.quiz = quiz
        self.score = score

        self.window = Tk()
        self.window.title("Quiz")
        self.window.config(padx = 20, pady = 20, bg = THEME_COLOR)

        # Score
        self.score = Label(text = f"Score: {self.score}", bg = THEME_COLOR, font=("Arial", 20), fg = "white")
        self.score.grid(column = 2, row = 1)

        # Quiz
        self.quiz_canvas = Canvas(height=250, width = 300)
        self.quiz_canvas.create_text(150, 125, text = f"{self.quiz}", font = ("Arial", 10, "italic"), width = 280)
        self.quiz_canvas.grid(column = 1, columnspan=2, row = 2, padx = 20, pady = 20)

        # Button
        self.true_image = PhotoImage(file = "Day-27-Python/images/true.png")
        self.false_image = PhotoImage(file = "Day-27-Python/images/false.png")
        Button(image = self.true_image).grid(column = 1, row = 3, )
        Button(image = self.false_image).grid(column = 2, row = 3, )

        self.window.mainloop()