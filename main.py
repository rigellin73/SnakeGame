import time
import turtle
from turtle import Screen, Turtle

# Constants
SCREEN_WIDTH = 600
SCREEN_HEIGHT = SCREEN_WIDTH
BGR_COLOR = "black"
GAME_TITLE = "Snake Game"
START_SNAKE_LEN = 3
TURTLE_SHAPE = "square"
TURTLE_COLOR = "white"
START_POS_X = 0
START_POS_Y = START_POS_X
TURTLE_SIDE_LEN = 20
SNAKE_STEP = 20


screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(BGR_COLOR)
screen.title(GAME_TITLE)
screen.tracer(0)

snake = []
game_over = False
turn = ""

def create_snake_part():
    snake_part = Turtle(TURTLE_SHAPE)
    snake_part.color(TURTLE_COLOR)
    snake_part.penup()
    return snake_part

def turn_right():
    snake[-1].setheading(0)

def turn_left():
    snake[-1].setheading(180)

def move_up():
    snake[-1].setheading(90)

def move_down():
    snake[-1].setheading(270)

turtle.onkey(turn_right, "d")
turtle.onkey(turn_left, "a")
turtle.onkey(move_up, "w")
turtle.onkey(move_down, "s")
turtle.listen()

for snake_part_num in range(START_SNAKE_LEN):
    new_snake_part = create_snake_part()
    new_snake_part.goto(START_POS_X - TURTLE_SIDE_LEN * snake_part_num, START_POS_Y)
    snake.insert(0, new_snake_part)

while not game_over:
    screen.update()
    time.sleep(0.5)
    for index, segment in enumerate(snake):
        if index < len(snake) - 1:
            next_segment = snake[index + 1]
            next_segment_pos = (next_segment.xcor(), next_segment.ycor())
            segment.goto(next_segment_pos)
        else:
            segment.forward(SNAKE_STEP)

screen.exitonclick()