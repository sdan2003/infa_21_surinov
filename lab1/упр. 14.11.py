def z(n):
    u = 180/n
    for i in range (n):
        turtle.forward(200)
        turtle.right(180-u)

import turtle
turtle.shape('turtle')
turtle.speed(0)
z(11)
