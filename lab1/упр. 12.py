def d(r):
    for i in range (250):
        turtle.forward(r)
        turtle.right(0.72)

import turtle
turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)
for i in range (4):
    d(0.5)
    d(0.1)
d(0.5)
