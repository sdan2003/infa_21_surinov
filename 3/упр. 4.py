import turtle
turtle.shape('turtle')
turtle.speed(0)
Vx = 10
Vy = -70
ay = -10
x = 0
y = 0
dt = 0.01
for i in range (6):
    Vy = - 10 - Vy
    k = 2*Vy/0.1
    for i in range(int(k)):
        x += Vx*dt
        y += Vy*dt + ay*dt**2/2
        Vy += ay*dt
        turtle.goto(x, y)

