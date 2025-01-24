import time
import turtle
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from screen_settings import SCREEN_WIDTH, SCREEN_HEIGHT, BGR_COLOR, GAME_TITLE, ANIMATION_SLEEP_TIME

#Constants
FOOD_COLLISION_DIST = 15
WALL_COLLISION_DIST_X = SCREEN_WIDTH / 2 - 20
WALL_COLLISION_DIST_Y = SCREEN_HEIGHT / 2 - 20

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

    if snake.head.distance(food) < FOOD_COLLISION_DIST:
        food.refresh()
        scoreboard.update_score()

    x_collision = snake.head.xcor() > WALL_COLLISION_DIST_X or snake.head.xcor() < -WALL_COLLISION_DIST_X
    y_collision = snake.head.ycor() > WALL_COLLISION_DIST_Y or snake.head.ycor() < -WALL_COLLISION_DIST_Y
    if x_collision or y_collision:
        game_over = True
        scoreboard.game_over()

screen.exitonclick()
