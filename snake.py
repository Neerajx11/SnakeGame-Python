from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_list = []
        self.create_snake()
        self.head = self.snake_list[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segement(position)

    def add_segement(self, position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.goto(position)
        self.snake_list.append(new_segment)

    def extend(self):
        # add new segment
        self.add_segement(self.snake_list[-1].position())

    def move(self):
        for seg in range(len(self.snake_list)-1, 0, -1):
            new_x = self.snake_list[seg-1].xcor()
            new_y = self.snake_list[seg-1].ycor()
            self.snake_list[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # 0 (east), 90 (north), 180 (west), 270 (south)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
