import turtle
from random import *
turtle.shape('turtle')
turtle.color('red')
for i in range (200):
    turtle.forward(randint(1,40))
    turtle.left(360*random())
