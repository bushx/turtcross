from turtle import *
from random import *
COLORS = ["white", "pink", "yellow", "red", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
class Cars:

    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(1, 2)
            random_y = randint(-240, 240)
            new_car.goto(280, random_y)
            # new_car.x_move = -10
            # new_car.move_speed = 0.1
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def move_level(self):
        for car in self.all_cars:
            car.move_speed *= 0.9

