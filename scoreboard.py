from turtle import Turtle

TEXT_POSITION = (0, 250)
TEXT_COLOR = "white"
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(TEXT_POSITION)
        self.color(TEXT_COLOR)
        self.hideturtle()
        self.score = 0
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.update_text()