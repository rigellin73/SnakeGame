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
ANIMATION_SLEEP_TIME = 0.5
EAST_ANGLE = 0
NORTH_ANGLE = 90
WEST_ANGLE = 180
SOUTH_ANGLE = 270


screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor(BGR_COLOR)
screen.title(GAME_TITLE)
screen.tracer(0)

snake = []
game_over = False

def create_snake_part():
    snake_part = Turtle(TURTLE_SHAPE)
    snake_part.color(TURTLE_COLOR)
    snake_part.penup()
    return snake_part

def turn_right():
    snake[-1].setheading(EAST_ANGLE)

def turn_left():
    snake[-1].setheading(WEST_ANGLE)

def move_up():
    snake[-1].setheading(NORTH_ANGLE)

def move_down():
    snake[-1].setheading(SOUTH_ANGLE)

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
    time.sleep(ANIMATION_SLEEP_TIME)
    for index, segment in enumerate(snake):
        if index < len(snake) - 1:
            next_segment = snake[index + 1]
            next_segment_pos = (next_segment.xcor(), next_segment.ycor())
            segment.goto(next_segment_pos)
        else:
            segment.forward(SNAKE_STEP)

screen.exitonclick()