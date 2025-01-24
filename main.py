import time
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = SCREEN_WIDTH
BGR_COLOR = "black"
GAME_TITLE = "Snake Game"
ANIMATION_SLEEP_TIME = 0.1

screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(BGR_COLOR)
screen.title(GAME_TITLE)
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
game_over = False

def turn_right():
    snake.turn("EAST")

def turn_left():
    snake.turn("WEST")

def move_up():
    snake.turn("NORTH")

def move_down():
    snake.turn("SOUTH")

turtle.onkey(turn_right, "d")
turtle.onkey(turn_left, "a")
turtle.onkey(move_up, "w")
turtle.onkey(move_down, "s")
turtle.listen()

while not game_over:
    screen.update()
    time.sleep(ANIMATION_SLEEP_TIME)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.update_score()

screen.exitonclick()
