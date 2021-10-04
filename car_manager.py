from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):

        super().__init__()
        self.all_cars = []
        self.STARTING_MOVE_DISTANCE = STARTING_MOVE_DISTANCE
        self.MOVE_INCREMENT = MOVE_INCREMENT
        self.speed = STARTING_MOVE_DISTANCE
        self.penup()

    def create_car(self):
        random_change = random.randint(1,6)
        if random_change == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.goto(280, random.randrange(-250, 250, 50))

            self.all_cars.append(new_car)


    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def new_level(self):
        self.speed += self.MOVE_INCREMENT
        # for car in self.all_cars:
        #     car.backward(self.speed)