import pygame
from pygame.draw import *
from random import randint
from math import sin, cos
from tkinter import *
from tkinter import messagebox

name = input('Hello! Write your name : ')

pygame.init()

FPS = 2

screen = pygame.display.set_mode((1200, 900))

RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

def ball(n):
    '''двигает шарик, отражает шарик от стены и создает новый шарик по прошествии времени'''
    global iter_balls, x_balls, y_balls, vx_balls, vy_balls
    if iter_balls[n] < 10:
        if (x_balls[n] + vx_balls[n] < 0 or x_balls[n] + vx_balls[n] > 1200):
            vx_balls[n] = randint(0, 100) * (-1) * vx_balls[n] / abs(vx_balls[n])
        if (y_balls[n] + vy_balls[n] < 0 or y_balls[n] + vy_balls[n] > 900):
            vy_balls[n] = randint(0, 100) * (-1) * vy_balls[n] / abs(vy_balls[n])
        circle(screen, color_balls[n], (x_balls[n]+vx_balls[n], y_balls[n]+vy_balls[n]), r_balls[n])
        x_balls[n] = vx_balls[n] + x_balls[n]
        y_balls[n] = vy_balls[n] + y_balls[n]
        iter_balls[n] += 1
    else:
        new_ball(n)

def new_ball(n):
    '''рисует новый шарик '''
    global x_balls, y_balls, r_balls, color_balls
    x_balls[n] = randint(100, 1100)
    y_balls[n] = randint(100, 900)
    r_balls[n] = randint(10, 100)
    color_balls[n] = COLORS[randint(0, 5)]
    vx_balls[n] = randint(-100, 100)
    vy_balls[n] = randint(-100, 100)
    iter_balls[n] = 0
    circle(screen, color_balls[n], (x_balls[n], y_balls[n]), r_balls[n])

def hexagon(n):
    '''двигает в плоскости и вращает шестиугольник, отражает его от стены и создает новый шестиугольник по прошествии времени'''
    global x0_hexagons, y0_hexagons, x1_hexagons, y1_hexagons, x2_hexagons, y2_hexagons, x3_hexagons, y3_hexagons
    global x4_hexagons, y4_hexagons, x5_hexagons, y5_hexagons, x6_hexagons, y6_hexagons, vx_hexagons, vy_hexagons
    global ax_hexagons, ay_hexagons, iter_hexagons, r_hexagons
    a = (2 * (r_hexagons[n] ** 2) - 2 * (r_hexagons[n] ** 2) * cos(3.14159/18)) ** 0.5
    if iter_hexagons[n] < 12:
        if (x0_hexagons[n] + vx_hexagons[n] < 0 or x0_hexagons[n] + vx_hexagons[n] > 1200):
            vx_hexagons[n] = randint(0, 100) * (-1) * vx_hexagons[n] / abs(vx_hexagons[n])
        if (y0_hexagons[n] + vy_hexagons[n] < 0 or y0_hexagons[n] + vy_hexagons[n] > 900):
            vy_hexagons[n] = randint(0, 100) * (-1) * vy_hexagons[n] / abs(vy_hexagons[n])
        ost = iter_hexagons[n] % 6                                                                       
        if ost < 3:
            x0_hexagons[n] = int(x0_hexagons[n] + vx_hexagons[n])
            y0_hexagons[n] = int(y0_hexagons[n] + vy_hexagons[n])
            x1_hexagons[n] = int(x1_hexagons[n] + vx_hexagons[n] + a * sin(3.14159 * ((17 - 2 * ost) / 36)))
            y1_hexagons[n] = int(y1_hexagons[n] + vy_hexagons[n] + a * cos(3.14159 * ((17 + 2 * ost) / 36)))
            x2_hexagons[n] = int(x2_hexagons[n] + vx_hexagons[n] + a * sin(3.14159 * ((5 - 2 * ost) / 36)))
            y2_hexagons[n] = int(y2_hexagons[n] + vy_hexagons[n] + a * cos(3.14159 * ((5 - 2 * ost) / 36)))
            x3_hexagons[n] = int(x3_hexagons[n] + vx_hexagons[n] - a * sin(3.14159 * ((7 + 2 * ost) / 36)))
            y3_hexagons[n] = int(y3_hexagons[n] + vy_hexagons[n] + a * cos(3.14159 * ((7 + 2 * ost) / 36)))
            x4_hexagons[n] = int(x4_hexagons[n] + vx_hexagons[n] - a * sin(3.14159 * ((17 + 2 * ost) / 36)))
            y4_hexagons[n] = int(y4_hexagons[n] + vy_hexagons[n] - a * cos(3.14159 * ((17 - 2 * ost) / 36)))
            x5_hexagons[n] = int(x5_hexagons[n] + vx_hexagons[n] - a * sin(3.14159 * ((5 - 2 * ost) / 36)))
            y5_hexagons[n] = int(y5_hexagons[n] + vy_hexagons[n] - a * cos(3.14159 * ((5 - 2 * ost) / 36)))
            x6_hexagons[n] = int(x6_hexagons[n] + vx_hexagons[n] + a * sin(3.14159 * ((7 + 2 * ost) / 36)))
            y6_hexagons[n] = int(y6_hexagons[n] + vy_hexagons[n] - a * cos(3.14159 * ((7 + 2 * ost) / 36)))
        elif ost < 5:
            x0_hexagons[n] = x0_hexagons[n] + vx_hexagons[n]
            y0_hexagons[n] = y0_hexagons[n] + vy_hexagons[n]
            x1_hexagons[n] = x1_hexagons[n] + vx_hexagons[n] + a * cos(3.14159 * ((1 + 2 * ost) / 36))
            y1_hexagons[n] = y1_hexagons[n] + vy_hexagons[n] + a * sin(3.14159 * ((1 + 2 * ost) / 36))
            x2_hexagons[n] = x2_hexagons[n] + vx_hexagons[n] - a * cos(3.14159 * ((13 + 2 * ost) / 36))
            y2_hexagons[n] = y2_hexagons[n] + vy_hexagons[n] + a * sin(3.14159 * ((13 + 2 * ost) / 36))
            x3_hexagons[n] = x3_hexagons[n] + vx_hexagons[n] - a * cos(3.14159 * ((11 - 2 * ost) / 36))
            y3_hexagons[n] = y3_hexagons[n] + vy_hexagons[n] + a * sin(3.14159 * ((11 - 2 * ost) / 36))
            x4_hexagons[n] = x4_hexagons[n] + vx_hexagons[n] - a * cos(3.14159 * ((1 + 2 * ost) / 36))
            y4_hexagons[n] = y4_hexagons[n] + vy_hexagons[n] - a * sin(3.14159 * ((1 + 2 * ost) / 36))
            x5_hexagons[n] = x5_hexagons[n] + vx_hexagons[n] + a * cos(3.14159 * ((13 + 2 * ost) / 36))
            y5_hexagons[n] = y5_hexagons[n] + vy_hexagons[n] - a * sin(3.14159 * ((13 + 2 * ost) / 36))
            x6_hexagons[n] = x6_hexagons[n] + vx_hexagons[n] + a * cos(3.14159 * ((11 - 2 * ost) / 36))
            y6_hexagons[n] = y6_hexagons[n] + vy_hexagons[n] - a * sin(3.14159 * ((11 - 2 * ost) / 36))
        else:
            r = r_hexagons[n]
            x0_hexagons[n] = x0_hexagons[n] + vx_hexagons[n]
            y0_hexagons[n] = y0_hexagons[n] + vy_hexagons[n]
            x1_hexagons[n] = x0_hexagons[n]
            y1_hexagons[n] = y0_hexagons[n] - r
            x2_hexagons[n] = x0_hexagons[n] + 0.5 * r * (3 ** 0.5)
            y2_hexagons[n] = y0_hexagons[n] - 0.5 * r
            x3_hexagons[n] = x0_hexagons[n] + 0.5 * r * (3 ** 0.5)
            y3_hexagons[n] = y0_hexagons[n] + 0.5 * r
            x4_hexagons[n] = x0_hexagons[n]
            y4_hexagons[n] = y0_hexagons[n] + r
            x5_hexagons[n] = x0_hexagons[n] - 0.5 * r * (3 ** 0.5)
            y5_hexagons[n] = y0_hexagons[n] + 0.5 * r
            x6_hexagons[n] = x0_hexagons[n] - 0.5 * r * (3 ** 0.5)
            y6_hexagons[n] = y0_hexagons[n] - 0.5 * r
        iter_hexagons[n] += 1
        polygon(screen, color_hexagons[n], ((x1_hexagons[n], y1_hexagons[n]), (x2_hexagons[n], y2_hexagons[n]),
                                           (x3_hexagons[n], y3_hexagons[n]), (x4_hexagons[n], y4_hexagons[n]),
                                           (x5_hexagons[n], y5_hexagons[n]), (x6_hexagons[n], y6_hexagons[n])))
        vx_hexagons[n] += ax_hexagons[n]
        vy_hexagons[n] += ay_hexagons[n]
    else:
        new_hexagon(n)           
        

def new_hexagon(n):
    '''рисует новый шестиугольник'''
    global x0_hexagons, y0_hexagons, x1_hexagons, y1_hexagons, x2_hexagons, y2_hexagons, x3_hexagons, y3_hexagons
    global x4_hexagons, y4_hexagons, x5_hexagons, y5_hexagons, x6_hexagons, y6_hexagons, r_hexagons, color_hexagons
    x0_hexagons[n] = randint(100, 1100)
    y0_hexagons[n] = randint(100, 900)
    r_hexagons[n] = randint(10, 100)
    r = r_hexagons[n]
    x1_hexagons[n] = x0_hexagons[n]
    y1_hexagons[n] = y0_hexagons[n] - r
    x2_hexagons[n] = x0_hexagons[n] + 0.5 * r * (3 ** 0.5)
    y2_hexagons[n] = y0_hexagons[n] - 0.5 * r
    x3_hexagons[n] = x0_hexagons[n] + 0.5 * r * (3 ** 0.5)
    y3_hexagons[n] = y0_hexagons[n] + 0.5 * r
    x4_hexagons[n] = x0_hexagons[n]
    y4_hexagons[n] = y0_hexagons[n] + r
    x5_hexagons[n] = x0_hexagons[n] - 0.5 * r * (3 ** 0.5)
    y5_hexagons[n] = y0_hexagons[n] + 0.5 * r
    x6_hexagons[n] = x0_hexagons[n] - 0.5 * r * (3 ** 0.5)
    y6_hexagons[n] = y0_hexagons[n] - 0.5 * r
    color_hexagons[n] = COLORS[randint(0, 5)]
    vx_hexagons[n] = randint (-40, 40)
    vy_hexagons[n] = randint (-40, 40)
    ax_hexagons[n] = randint (-15, 15)
    ay_hexagons[n] = randint (-15, 15)
    iter_hexagons[n] = 0
    polygon(screen, color_hexagons[n], ((x1_hexagons[n], y1_hexagons[n]), (x2_hexagons[n], y2_hexagons[n]),
                                       (x3_hexagons[n], y3_hexagons[n]), (x4_hexagons[n], y4_hexagons[n]),
                                       (x5_hexagons[n], y5_hexagons[n]), (x6_hexagons[n], y6_hexagons[n])))

def click(event):
    '''проверяет попадание в мишень, считает очки'''
    global k, p, n_balls, x_balls, y_balls, r_balls, n_hexations, iter_balls, iter_gexagons
    global x1_hexagons, y1_hexagons, x2_hexagons, y2_hexagons, x3_hexagons, y3_hexagons, x4_hexagons, y4_hexagons
    global x5_hexagons, y5_hexagons, x6_hexagons, y6_hexagons
    indicator = 0
    i = 0
    for i in range (n_balls):
        if (event.pos[0] - x_balls[i])**2 + (event.pos[1] - y_balls[i])**2 <= r_balls[i]**2:
            k += 1
            print('Очков: ', k, '  Промахов: ', p)
            indicator = 1
            new_ball(i)
            iter_balls[i] = 0
    for i in range (n_hexagons):
        x = event.pos[0]
        y = event.pos[1]
        x1 = x1_hexagons[i]
        x2 = x2_hexagons[i]
        x3 = x3_hexagons[i]
        x4 = x4_hexagons[i]
        x5 = x5_hexagons[i]
        x6 = x6_hexagons[i]
        y1 = y1_hexagons[i]
        y2 = y2_hexagons[i]
        y3 = y3_hexagons[i]
        y4 = y4_hexagons[i]
        y5 = y5_hexagons[i]
        y6 = y6_hexagons[i]
        if (line_x_from_y (x1, y1, x2, y2, y) > x and line_x_from_y (x2, y2, x3, y3, y) > x
        and line_y_from_x (x3, y3, x4, y4, x) > y and line_x_from_y (x4, y4, x5, y5, y) < x
        and line_x_from_y (x5, y5, x6, y6, y) < x and line_y_from_x (x6, y6, x1, y1, x) < y):
            k += 2
            print('Очков: ', k, '  Промахов: ', p)
            number_of_hexagon = i
            indicator = 1
            new_hexagon(i)
            iter_hexagons[i] = 0
    if indicator == 0:
        p += 1
        print('Очков: ', k, '  Промахов: ', p)

def line_y_from_x (x1, y1, x2, y2, x):
    '''рассматривает прямую, проходящую через две точки (x1, y1) и (x2, y2), как функцию от абсциссы
       и нахаходит ее значение в точке x'''
    k = (y1 - y2) / (x1 - x2)
    b = y1 - (k * x1)
    return k * x + b

def line_x_from_y (x1, y1, x2, y2, y):
    '''рассматривает прямую, проходящую через две точки (x1, y1) и (x2, y2), как функцию от ординаты
       и нахаходит ее значение в точке y'''
    k = (x1 - x2) / (y1 - y2)
    b = x1 - (k * y1)
    return k * y + b

pygame.display.update()
clock = pygame.time.Clock()
finished = False
number_of_ball = -1
n_balls = 4
k = 0
p = 0
vx_balls = n_balls * [0]
vy_balls = n_balls * [0]
x_balls = n_balls * [0]
y_balls = n_balls * [0]
r_balls = n_balls * [0]
color_balls = n_balls * [0]
iter_balls = n_balls * [0]

number_of_hexagon = -1
n_hexagons = 2
ax_hexagons = n_hexagons * [0]
ay_hexagons = n_hexagons * [0]
vx_hexagons = n_hexagons * [0]
vy_hexagons = n_hexagons * [0]
x0_hexagons = n_hexagons * [0]
y0_hexagons = n_hexagons * [0]
x1_hexagons = n_hexagons * [0]
y1_hexagons = n_hexagons * [0]
x2_hexagons = n_hexagons * [0]
y2_hexagons = n_hexagons * [0]
x3_hexagons = n_hexagons * [0]
y3_hexagons = n_hexagons * [0]
x4_hexagons = n_hexagons * [0]
y4_hexagons = n_hexagons * [0]
x5_hexagons = n_hexagons * [0]
y5_hexagons = n_hexagons * [0]
x6_hexagons = n_hexagons * [0]
y6_hexagons = n_hexagons * [0]
r_hexagons = n_hexagons * [0]
color_hexagons = n_hexagons * [0]
iter_hexagons = n_hexagons * [0]

for i in range (n_balls):
    new_ball(i)

for i in range (n_hexagons):
    new_hexagon(i)
    
while not finished:
    pygame.display.update()
    screen.fill(BLACK)
    clock.tick(FPS)
    for event in pygame.event.get():
        if p == 10:
            finished = True
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print('Click!')
            click(event)
    for i in range (n_balls):
        ball(i)
    for i in range (n_hexagons):
        hexagon(i)

pygame.quit()

f = open('results.txt')
list = f.readlines()
results = []
for x in list:
    results.append(x.split())
f.close()
f = open('results.txt', 'w')
i = 0
if i < len(results):
    while k < int(results[i][0]):
        f.write(results[i][0] + ' ' + results[i][1] + '\n')
        i += 1
        if i == len(results):
            break
f.write(str(k) + ' ' + name + '\n')
s = Entry().get()
if k % 10 == 1 and k % 100 != 11:
    o = 'очко'
elif k % 10 == 0:
    o = 'очков'
elif k % 10 < 5 and k % 100 != 12 and k % 100 != 13 and k % 100 != 14:
    o = 'очка'
else:
    o = 'очков'
messagebox.showinfo(
    "Your result", 
    'Эта игра окончена. Вы заработали ' + str(k) + ' ' + o +' и идете на ' + str(i+1) + '-м месте')
for u in range (i + 1, len(results) + 1):
    f.write(results[u-1][0] + ' ' + results[u-1][1] + '\n')
f.close()

"Комментарий создается ради возможности сделать новый коммит, чтобы исправить название лабораторной работы"
