from turtle import Turtle

class Snake:

    def __init__(self):
        for snake_part_num in range(self.START_SNAKE_LEN):
            new_snake_part = self.create_snake_part()
            new_snake_part.goto(self.START_POS_X - self.TURTLE_SIDE_LEN * snake_part_num, self.START_POS_Y)
            self.snake.insert(0, new_snake_part)

    START_SNAKE_LEN = 3
    START_POS_X = 0
    START_POS_Y = START_POS_X
    TURTLE_SIDE_LEN = 20
    TURTLE_SHAPE = "square"
    TURTLE_COLOR = "white"
    SNAKE_STEP = 20
    DIRECTION_ANGLE = {
        "EAST": 0,
        "NORTH": 90,
        "WEST": 180,
        "SOUTH": 270
    }

    snake = []

    def create_snake_part(self):
        snake_part = Turtle(self.TURTLE_SHAPE)
        snake_part.color(self.TURTLE_COLOR)
        snake_part.penup()
        return snake_part

    def move(self):
        for index, segment in enumerate(self.snake):
            if index < len(self.snake) - 1:
                next_segment = self.snake[index + 1]
                next_segment_pos = (next_segment.xcor(), next_segment.ycor())
                segment.goto(next_segment_pos)
            else:
                segment.forward(self.SNAKE_STEP)

    def turn(self, direction):
        self.snake[-1].setheading(self.DIRECTION_ANGLE[direction])
