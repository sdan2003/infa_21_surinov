import pygame
from pygame.draw import *
from pygame.transform import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 1130))               #создал окно
rect(screen, (0, 245, 255), (0, 0, 800, 565))               #теперь небо будет голубым
rect(screen, (220, 220, 220), (0, 565, 800, 565))           #а лед будет светло-серым
line(screen, (0, 0, 0), (0, 565), (800, 565), 1)            #добавил линию горизонта
ellipse(screen, (80, 80, 80), (455, 647, 291, 121))         #прорубь: кромка льда (темно-серый эллипс большего диаметра)
ellipse(screen, (40, 100, 80), (480, 687, 231, 81))         #прорубь: вода (темно-зеленый эллипс)
ellipse(screen, (0, 0, 0), (455, 647, 291, 121), 1)         #внешняя граница проруби (лед-лед)
ellipse(screen, (0, 0, 0), (480, 687, 231, 81), 1)          #"внутренняя" граница проруби (вода-лед)
c = pygame.Surface((800, 1130), pygame.SRCALPHA)            #создал прозрачную поверхность (1)
d = pygame.Surface((800, 1130), pygame.SRCALPHA)            #создал прозрачную поверхность (2).

#<<<Начинаю работу с солнцем.
circle(c, (255, 255, 200, 140), (487, 240), 200, 39)        #солнечный круг на поверхности (1)
line(d, (255, 255, 200, 140), (282, 244), (687, 240), 31)   #горизонтальный отрезок в этом круге на поверхности (2)
line(d, (255, 255, 200, 140), (500, 0), (474, 439), 31)     #вертикальный отрезок в этом же круге на поверхности (2)
ellipse(d, (255, 255, 215, 240), (461, 222, 51, 42))        #"жирная точка" на пересечении отрезков (поверхность (2))
circle(d, (255, 255, 215, 240), (479, 427), 12)             #"жирная точка" внизу
ellipse(d, (255, 255, 215, 240), (285, 231, 30, 25))        #"жирная точка" слева
ellipse(d, (255, 255, 215, 240), (657, 227, 30, 25))        #"жирная точка" справа.
#Заканчиваю работу с солнцем.>>>

screen.blit(c, (0, 0))                                      #совмещаю поверхность (1) с окном
screen.blit(d, (0, 0))                                      #совмещаю поверхность (2) с окном

line(screen, (0, 0, 0), (615, 322), (615, 735))             #леска от спининга
lines(screen, (0, 0, 0), False, ((615, 322), (512, 389),
                (419, 467), (336, 554), (261, 652)), 4)     #сам спининг

#<<<Начинаю рисовать рыболова-любителя.
ellipse(screen, (220, 220, 220), (139, 388, 174, 106))      #с головы
ellipse(screen, (0, 0, 0), (139, 388, 174, 106), 1)         #граница головы
ellipse(screen, (220, 220, 220), (5, 460, 250, 400))        #тело
ellipse(screen, (0, 0, 0), (5, 460, 250, 400), 1)           #граница тела
ellipse(screen, (220, 220, 220), (130, 760, 160, 130))      #бедро
ellipse(screen, (0, 0, 0), (130, 760, 160, 130), 1)         #граница бедра
ellipse(screen, (220, 220, 220), (240, 845, 160, 60))       #голень
ellipse(screen, (0, 0, 0), (240, 845, 160, 60), 1)          #граница голени
ellipse(screen, (220, 220, 220), (210, 530, 140, 60))       #рука (по-русски это называется лапа)
ellipse(screen, (0, 0, 0), (210, 530, 140, 60), 1)          #граница лапы-руки.
ellipse(screen, (0, 0, 0), (210, 420, 10, 7))               #рыболов исключен из всероссийского общества слепых
ellipse(screen, (0, 0, 0), (307, 430, 10, 7))               #нос
arc(screen, (0, 0, 0), (0, 360, 400, 97), 4.71, 5.34)       #рот


#Заканчиваю рисовать рыболова, хотя неплохо было бы добавить ухо.>>>





e = pygame.Surface((800, 1130), pygame.SRCALPHA)            #как-то мало поверхностей, добавлю еще одну (3)

#<<<Начинаю рисовать рыбу. 
ellipse(e, (200, 210, 210), (320, 730, 154, 54))            #круглую
ellipse(e, (0, 0, 0), (320, 730, 154, 54), 1)               #и ее границы
polygon(e, (200, 210, 210), ((320, 757), (293, 730),
                             (293, 784)))                   #хвост рыбы
polygon(e, (0, 0, 0), ((320, 757), (293, 730),
                       (293, 784)), 1)                      #граница хвоста.
#Заканчиваю работу с рыбой.>>>

e = pygame.transform.rotate(e, 15)                          #поверну поверхность (4) 
screen.blit(e, (0, 0))                                      #и совмещу ее с окном





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
