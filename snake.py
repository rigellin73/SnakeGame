from turtle import Turtle

class Snake:

    def __init__(self):

        # Constants
        self.START_SNAKE_LEN = 3
        self.START_POS_X = 0
        self.START_POS_Y = self.START_POS_X
        self.TURTLE_SIDE_LEN = 20
        self.TURTLE_SHAPE = "square"
        self.TURTLE_COLOR = "white"
        self.SNAKE_STEP = 20
        self.DIRECTION_ANGLE = {
            "EAST": 0,
            "NORTH": 90,
            "WEST": 180,
            "SOUTH": 270
        }

        self.snake = []

        # Create default snake
        for snake_part_num in range(self.START_SNAKE_LEN):
            new_snake_part = self.create_snake_part()
            new_snake_part.goto(self.START_POS_X - self.TURTLE_SIDE_LEN * snake_part_num, self.START_POS_Y)
            self.snake.insert(0, new_snake_part)

    def create_snake_part(self):
        """Create single snake segment with default settings and return it"""
        snake_part = Turtle(self.TURTLE_SHAPE)
        snake_part.color(self.TURTLE_COLOR)
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
                segment.forward(self.SNAKE_STEP)

    def turn(self, direction):
        """Turn the snake's head in one of the directions: EAST, NORTH, WEST or SOUTH"""
        self.snake[-1].setheading(self.DIRECTION_ANGLE[direction])
