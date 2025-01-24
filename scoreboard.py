from turtle import Turtle
from screen_settings import SCREEN_HEIGHT

# Constants
TEXT_POSITION = (0, SCREEN_HEIGHT / 2 - 30)
TEXT_COLOR = "white"
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')
SCORE_TEXT = "Score:"
GAME_OVER_TEXT = "GAME OVER"

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
        """Update scoreboard text to show current score"""
        self.clear()
        self.write(f"{SCORE_TEXT} {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        """Increase score and update text on the screen"""
        self.score += 1
        self.update_text()

    def game_over(self):
        """Show game over text"""
        self.goto(0, 0)
        self.write(GAME_OVER_TEXT, align=ALIGNMENT, font=FONT)
