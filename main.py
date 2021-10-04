import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import math
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#Intialise player
player = Player()

#event listner
screen.listen()
screen.onkey(player.move, "Up")

car_manager = CarManager()
scoreboard = Scoreboard()
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #Has player reached the top?
    if player.is_finished():
        car_manager.all_cars.clear()
        spawn_new_cars = 0
        player.goto(0, -280)
        car_manager.increase_speed()
        car_manager.new_level()
    #car logic
    car_manager.create_car()
    car_manager.move()
    #Detect collisions with turtle and cars
    for cars in car_manager.all_cars:
        if cars.distance(player.position()) < 20:
            scoreboard.game_over()









