from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.all_segments = []
        self.old_segments = []
        for position in STARTING_POSITIONS:
            self.create_segments(position)
        self.head = self.all_segments[0]

    def create_segments(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        new_segment.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.all_segments.append(new_segment)

    def move_snake(self):
        for i in range(len(self.all_segments) - 1, 0, -1):
            self.all_segments[i].goto(self.all_segments[i-1].position())
        self.head.forward(20)
        self.head.color('blue')

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def reset_game(self):
        for segment in self.all_segments[3:]:
            self.all_segments.remove(segment)

        for i in range(3):
            self.all_segments[i].goto(STARTING_POSITIONS[i])
            self.all_segments[i].setheading(0)
