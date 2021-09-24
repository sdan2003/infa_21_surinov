def o2(r):
    for i in range (500):
        turtle.forward(0.25*r + 0.75)
        turtle.left(0.72)
    for i in range (500):
        turtle.forward(0.25*r + 0.75)
        turtle.right(0.72)

import turtle
turtle.shape('turtle')
turtle.speed(0)
turtle.left(90)
for i in range (1,6):
    o2(i)
