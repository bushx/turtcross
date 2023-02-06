from turtle import *
from frog import *
import time
from levels import *
from cars import *

screen = Screen()
level = Levels()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("TurterrX23")
screen.tracer(0)

frog = Frog()

screen.listen()
screen.onkey(frog.up, "Up")
screen.onkey(frog.down, "Down")
screen.onkey(frog.left, "Left")
screen.onkey(frog.right, "Right")


game_is_on = True

car = Cars()
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car.create_car()
    car.move()

    if frog.ycor() >= 280:
        level.add_level()
        frog.new_level()

    for cars in car.all_cars:
        if frog.distance(cars) < 20:
            level.game_over()
            game_is_on = False


screen.exitonclick()
