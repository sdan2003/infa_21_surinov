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
turtle.shape('turtle')
input = open('индекс.txt')
s = input.readlines()
input.close()
for x in s:
    x = x.split()
    for i in range(len(x)):
        x[i] = int(x[i])
    k = tuple(x)
    ris(k)

