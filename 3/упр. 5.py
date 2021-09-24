from random import randint
import turtle
from random import *


number_of_turtles = 100
steps_of_time_number = 100


pool = [turtle.Turtle(shape='turtle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.left(randint(1, 360))
        unit.forward(randint(-100, 100))
