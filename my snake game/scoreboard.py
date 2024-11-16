from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.create_score()
        self.update_score()

    def create_score(self):
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 250)

    def update_score(self):
        self.clear()
        self.write(f'Score: {self.score}', align='center', font=('Courier', 25, 'normal'))

    def game_over(self):
        self.home()
        self.write(f'Game over', align='center', font=('Courier', 50, 'normal'))

    def reset_score(self):
        self.clear()
        self.score = 0
        self.create_score()
        self.update_score()

