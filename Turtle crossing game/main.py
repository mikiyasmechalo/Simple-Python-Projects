import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from random import randint

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
scoreboard = Scoreboard()
player = Player()
car_manager = CarManager()

screen.onkeypress(player.move, "w")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move()

    # detect car collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # detect crossing
    if player.is_at_finish_line():
        car_manager.increase_level()
        player.go_to_start()
        scoreboard.increase_level()

screen.exitonclick()
