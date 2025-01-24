from turtle import Turtle

# Constants
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

class Snake:

    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        """Create snake from segments at the start"""
        for snake_part_num in range(START_SNAKE_LEN):
            new_snake_part = self.create_snake_part()
            new_snake_part.goto(START_POS_X - TURTLE_SIDE_LEN * snake_part_num, START_POS_Y)
            self.snake.insert(0, new_snake_part)

    def create_snake_part(self):
        """Create single snake segment with default settings and return it"""
        snake_part = Turtle(TURTLE_SHAPE)
        snake_part.color(TURTLE_COLOR)
        snake_part.penup()
        return snake_part

    def move(self):
        """Move the snake one step"""
        for index, segment in enumerate(self.snake):
            if index < len(self.snake) - 1:
                next_segment = self.snake[index + 1]
                next_segment_pos = (next_segment.xcor(), next_segment.ycor())
                segment.goto(next_segment_pos)
            else:
                segment.forward(SNAKE_STEP)

    def turn(self, direction):
        """Turn the snake's head in one of the directions: EAST, NORTH, WEST or SOUTH"""
        self.snake[-1].setheading(DIRECTION_ANGLE[direction])
