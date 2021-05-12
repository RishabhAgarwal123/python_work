import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from finishline import FinishLine

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()


finish = FinishLine()
player = Player()
screen.onkey(player.move_turtle, 'Up')
car_manager = CarManager()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_cars()

    # Detect Collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Detect Road Crossed
    if player.is_at_finish():
        scoreboard.increase_level()
        player.goto_start()
        car_manager.level_up()


screen.exitonclick()
