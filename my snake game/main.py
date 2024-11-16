from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


def restart_game():
    choice = str(screen.textinput("choose", "Do to want to play again? (yes/ no)"))
    choice.lower()
    if choice == 'yes':
        snake.reset_game()
        scoreboard.reset_score()
        food.reset_position()
        screen.listen()
        return True
    else:
        return False


screen = Screen()
screen.bgcolor('black')
screen.setup(height=600, width=600)
screen.tracer(0)
food = Food()
snake = Snake()
scoreboard = Scoreboard()

boarder = Turtle()
boarder.pencolor('red')
boarder.pensize(width=20)
# boarder.teleport(300, 300)
boarder.penup()
boarder.goto(300, 300)
boarder.pendown()
boarder.goto(300, -300)
boarder.goto(-300, -300)
boarder.goto(-300, 300)
boarder.goto(300, 300)
boarder.hideturtle()

screen.listen()
screen.onkeypress(snake.up, 'w')
screen.onkeypress(snake.down, 's')
screen.onkeypress(snake.left, 'a')
screen.onkeypress(snake.right, 'd')

game_is_on = True
while game_is_on:
    time.sleep(0.08)
    snake.move_snake()
    screen.update()

    # collision with food
    if food.distance(snake.head) < 15:
        scoreboard.score += 1
        scoreboard.update_score()
        food.reset_position()
        snake.create_segments(snake.all_segments[len(snake.all_segments)-1].position())

    # collision with wall
    if snake.head.xcor() >= 280 or snake.head.xcor() <= -280 or snake.head.ycor() >= 280 or snake.head.ycor() <= -280:
        scoreboard.game_over()
        game_is_on = restart_game()

screen.exitonclick()
