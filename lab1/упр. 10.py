def o2():
    for i in range (500):
        turtle.forward(1.5)
        turtle.left(0.72)
    for i in range (500):
        turtle.forward(1.5)
        turtle.right(0.72)

import turtle
turtle.shape('turtle')
turtle.speed(0)
for i in range (3):
    o2()
    turtle.left(60)
