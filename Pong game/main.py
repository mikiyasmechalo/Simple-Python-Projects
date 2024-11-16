# 1. create screen
# 2. create and move a paddle
# 3. create another paddle
# 4. create and move a ball
# 5. detect collision with wall and bounce
# 6. detect collision with paddle
# 6. detect when paddle misses
# 7. keep score

from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
score = Scoreboard()
ball = Ball()
name = Turtle()
name.color("white")
name.penup()
name.hideturtle()
name.goto(0, 230)
name.write("Pong", font=("Courier", 40, "normal"), align="center")

screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.down, "s")

game_is_on = True

while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # collision with top and bottom
    if ball.ycor() > 280:
        ball.bounce_y()
    elif ball.ycor() < -280:
        ball.bounce_y()

    # collision with both paddle
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed = ball.speed()

    # detect R paddle misses
    if ball.xcor() > 380:
        ball.home()
        ball.reset_position()
        score.l_point()

    # detect L paddle misses
    if ball.xcor() < -380:
        ball.home()
        ball.reset_position()
        score.r_point()

screen.exitonclick()
