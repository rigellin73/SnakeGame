from turtle import Turtle
from screen_settings import SCREEN_HEIGHT

# Constants
TEXT_POSITION = (0, SCREEN_HEIGHT / 2 - 30)
TEXT_COLOR = "white"
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')
HIGHSCORE_FILENAME = "highscore.txt"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(TEXT_POSITION)
        self.color(TEXT_COLOR)
        self.hideturtle()
        self.score = 0
        self.highscore = 0
        self.read_highscore()
        self.update_text()

    def update_text(self):
        """Update scoreboard text to show current score"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        """Increase score and update text on the screen"""
        self.score += 1
        self.update_text()

    def reset_score(self):
        if self.score > self.highscore:
            self.highscore = self.score
            self.write_highscore(self.highscore)
        self.score = 0
        self.update_text()

    def read_highscore(self):
        try:
            with open(HIGHSCORE_FILENAME) as hs_file:
                self.highscore = int(hs_file.read())
        except IOError:
            print("Highscore file does not exist, creating new file")
            self.write_highscore(0)
        except ValueError:
            print("Highscore file is corrupted, creating new")
            self.write_highscore(0)

    def write_highscore(self, new_highscore):
        with open(HIGHSCORE_FILENAME, "w") as hs_file:
            hs_file.write(str(new_highscore))
