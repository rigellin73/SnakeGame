from turtle import Turtle
from screen_settings import SCREEN_WIDTH, SCREEN_HEIGHT
from random import randint

MAX_FOOD_POS_X = SCREEN_WIDTH / 2 - 20
MAX_FOOD_POS_Y = SCREEN_HEIGHT / 2 - 20
SIZE_STRETCH = 0.5
SHAPE = "circle"
COLOR = "purple"
ANIM_SPEED = "fastest"

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_wid=SIZE_STRETCH, stretch_len=SIZE_STRETCH)
        self.color(COLOR)
        self.speed(ANIM_SPEED)
        self.refresh()

    def refresh(self):
        rand_x = randint(-MAX_FOOD_POS_X, MAX_FOOD_POS_X)
        rand_y = randint(-MAX_FOOD_POS_Y, MAX_FOOD_POS_Y)
        self.goto(rand_x, rand_y)
