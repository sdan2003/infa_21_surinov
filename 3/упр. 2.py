def sootv(e):
    global k
    if e == 0:
        k = (1, 2, 4, 6, 8, 9)
    elif e == 1:
        k = (3, 4, 8)
    elif e == 2:
        k = (1, 4, 7, 9)
    elif e == 3:
        k = (1, 3, 5, 7)
    elif e == 4:
        k = (2, 4, 5, 8)
    elif e == 5:
        k = (1, 2, 5, 8, 9)
    elif e == 6:
        k = (2, 5, 6, 8, 9)
    elif e == 7:
        k = (1, 3, 6)
    elif e == 8:
        k = (1, 2, 4, 5, 6, 8, 9)
    elif e == 9:
        k = (1, 2, 4, 5, 7)
def prov(n):
    if n in k:
        turtle.pendown()
    else:
        turtle.penup()
def ris(k):
    turtle.left(180)
    prov(1)
    turtle.forward(30)
    turtle.left(90)
    prov(2)
    turtle.forward(30)
    turtle.left(135)
    prov(3)
    turtle.forward(1800**0.5)
    turtle.right(135)
    prov(4)
    turtle.forward(30)
    turtle.right(90)
    prov(5)
    turtle.forward(30)
    turtle.left(90)
    prov(6)
    turtle.forward(30)
    turtle.left(135)
    prov(7)
    turtle.forward(1800**0.5)
    turtle.right(135)
    prov(8)
    turtle.forward(30)
    turtle.right(90)
    prov(9)
    turtle.forward(30)
    turtle.penup()
    turtle.left(180)
    turtle.forward(90)
    turtle.left(90)
    turtle.forward(60)
    turtle.right(90)
    
import turtle
from random import *
k = ()
turtle.shape('turtle')
turtle.color('blue')
v = [1, 4, 1, 7, 0, 0]
for x in v:
    sootv(x)
    ris(k)
