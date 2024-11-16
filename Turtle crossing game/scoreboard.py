from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.penup()
        self.hideturtle()
        self.increase_level()

    def update_scoreboard(self):
        self.clear()
        self.goto(-220, 260)
        self.write(f"Level: {self.level}", False, font=FONT, align="center")

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.home()
        self.write("Game Over", font=("Courier", 50, "normal"), align="center")
