import turtle

n = int(input('Введите кол-во лап '))
turtle.shape('turtle')
turtle.speed(0)
for i in range (n):
    turtle.forward(100)
    turtle.stamp()
    turtle.left(180)
    turtle.penup()
    turtle.forward(100)
    turtle.left(360/n + 180)
    turtle.pendown()
