import turtle

turtle.shape('turtle')
turtle.speed(0)
for i in range (10):
    turtle.forward(i * 20 + 25)
    turtle.left(90)
    turtle.forward(i * 20 + 25)
    turtle.left(90)
    turtle.forward(i * 20 + 25)
    turtle.left(90)
    turtle.forward(i * 20 + 25)
    if i < 9:
        turtle.penup()
        turtle.forward(10)
        turtle.right(90)
        turtle.forward(10)
        turtle.left(180)
        turtle.pendown()
        
