from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 220)
        self.color("blue")
        self.write(self.l_score, align="center", font=("Courier", 40, "normal"))
        self.color("red")
        self.goto(100, 220)
        self.write(self.r_score, align="center", font=("Courier", 40, "normal"))
