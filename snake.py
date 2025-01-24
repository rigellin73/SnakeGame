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
        self.head = self.snake[-1]

    def create_snake(self):
        """Create snake from segments at the start"""
        for snake_part_num in range(START_SNAKE_LEN):
            pos = (START_POS_X - TURTLE_SIDE_LEN * snake_part_num, START_POS_Y)
            new_snake_part = self.create_snake_part(pos)
            self.snake.insert(0, new_snake_part)

    def create_snake_part(self, position):
        """Create single snake segment with default settings and return it"""
        snake_part = Turtle(TURTLE_SHAPE)
        snake_part.color(TURTLE_COLOR)
        snake_part.penup()
        snake_part.goto(position)
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
        if not abs(self.head.heading() - DIRECTION_ANGLE[direction]) == 180:
            self.head.setheading(DIRECTION_ANGLE[direction])

    def add_new_segment(self):
        """Add new segment to the snake"""
        new_segment = self.create_snake_part(self.snake[0].position())
        self.snake.insert(0, new_segment)
