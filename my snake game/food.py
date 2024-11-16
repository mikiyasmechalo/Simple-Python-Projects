from turtle import Turtle
from random import randint


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('orange')
        self.penup()
        self.shapesize(stretch_wid=0.5)
        self.x_rand = 0
        self.y_rand = 0
        self.reset_position()

    def reset_position(self):
        self.x_rand = randint(-250, 250)
        self.y_rand = randint(-250, 250)
        self.goto(self.x_rand, self.y_rand)
