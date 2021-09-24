def m(n):
    turtle.left(180 - 90*(n-2)/n)
    for k in range (n):
        turtle.forward(n*10)
        turtle.left(180 - 180*(n-2)/n)
    turtle.right(180 - 90*(n-2)/n)

import turtle

a = [17.320508075689, 28.284271247462, 42.532540417602, 60, 80.666770483687, 104.52503719011, 131.57119800734, 161.80339887499, 195.22060430863, 231.82219830938]
turtle.shape('turtle')
turtle.speed(0)
for i in range (3, 13):
    m(i)
    if i < 12:
        turtle.penup()
        turtle.forward(a[i-2]-a[i-3])
        turtle.pendown()
