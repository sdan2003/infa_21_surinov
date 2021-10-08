import pygame.font
from pygame.draw import *
from math import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((900, 1050))

white = (255, 255, 255)
black = (0, 0, 0)
gray = (125, 125, 125)
light_blue = (64, 128, 255)
green = (0, 200, 64)
yellow = (255, 255, 0)
blue = (50, 170, 205)
pink = (255, 50, 255)
red = (255, 0, 0)
blue_green = (0, 255, 100)
maroon = (115, 0, 0)
lime = (230, 255, 101)
purple = (240, 0, 255)
magenta = (255, 0, 230)
brown = (100, 40, 0)
forest_green = (5, 100, 5)
navy_blue = (0, 0, 100)
rust = (210, 150, 75)
light_yellow = (255, 200, 0)
highlighter = (255, 255, 100)
sky_blue = (0, 255, 255)
light_gray = (200, 200, 200)
dark_gray = (50, 50, 50)
tan = (230, 220, 170)
coffee_brown = (200, 190, 140)
moon_glow = (235, 245, 255)
c1 = [yellow, pink, magenta, rust, blue, pink, light_yellow,  yellow, red, red, pink, pink, light_yellow, red, pink, yellow, rust]
c2 = [(180, 180, 0), (190, 60, 0), (200, 0, 0), (190, 60, 0), (180, 0, 180), (60, 0, 180), (0, 60, 180), (0, 120, 180), (0, 180, 180), (0, 120, 120), (180, 180, 0),
      (0, 120, 180), (0, 60, 180), (60, 0, 180), (180, 0, 180), (190, 60, 0), (200, 0, 0)]
c3 = [red, yellow, green, blue, pink, blue, green, yellow, red, yellow, green, blue, pink, blue, green, yellow, red]
ct1 = [yellow, pink, magenta, rust, blue, pink, yellow, red, red, light_yellow, pink]
ct2 = [(180, 180, 0), (200, 0, 0), (180, 0, 180), (60, 0, 180), (0, 120, 180), (0, 180, 180), (180, 180, 0), (0, 120, 180), (0, 60, 180), (60, 0, 180), (180, 0, 180), (200, 0, 0)]
ct3 = [red, yellow, green, blue, pink, blue, green, yellow, red, yellow, green]

def alpha(a):
    return -a - pi


def sky():
    rect(screen, sky_blue, (0, 0, 900, 375))


def grass():
    rect(screen, blue_green, (0, 375, 900, 675))


def sun():
    circle(screen, yellow, (825, 90), 180)
    line(screen, yellow, (825, 90), (525, 90), 10)
    line(screen, yellow, (825, 90), (535, 168), 10)
    line(screen, yellow, (825, 90), (565, 240), 10)
    line(screen, yellow, (825, 90), (613, 302), 10)
    line(screen, yellow, (825, 90), (675, 350), 10)
    line(screen, yellow, (825, 90), (747, 380), 10)
    line(screen, yellow, (825, 90), (825, 390), 10)
    line(screen, yellow, (825, 90), (747, 380), 10)


def head(x, y, k):
    l = abs(k)
    ellipse(screen, white, (x-106*k, y + 47*l, 61*k, 115*l))
    circle(screen, white, (x-64*k, y + 37*l), 37*l)
    circle(screen, white, (x-19*k, y+49*l), 19*l)
    polygon(screen, white, [(x-51*k, y+l), (x-13*k, y+31*l), (x-19*k, y+48*l), (x-51*k, y+l)])


def body(x, y, k):
    l = abs(k)
    circle(screen, white, (x - 86*k, y + 158*l), 50*l)
    rect(screen, white, (min(x - 204*k, x - 86*k), y + 119*l, 118*l, 77*l))
    circle(screen, white, (x - 191*k, y + 163*l), 44*l)


def leg(x, y, k):
    l = abs(k)
    ellipse(screen, white, (x - 228*k, y + 166*l, 46*k, 86*l))
    circle(screen, white, (x - 213*k, y + 253*l), 16*l)
    rect(screen, white, (min(x - 227*k, x - 197*k), y + 255*l, 30*l, 44*l))
    rect(screen, light_yellow, (min(x - 228*k, x - 195*k), y + 277*l, 33*l, 24*l))
    ellipse(screen, white, (x - 95*k, y + 169*l, 40*k, 87*l))
    circle(screen, white, (x - 69*k, y + 256*l), 15*l)
    rect(screen, white, (min(x - 83*k, x - 55*k), y + 263*l, 28*l, 37*l))
    rect(screen, light_yellow, (min(x - 85*k, x - 53*k), y + 276*l, 32*l, 25*l))


def eye(x, y, k):
    l = abs(k)
    circle(screen, magenta, (x - 50*k, y + 26*l), 13*l)
    circle(screen, black, (x - 49*k, y + 26*l), 7*l)
    circle(screen, white, (x - 51*k, y + 23*l), 2*l)



def mane(x, y, k, c):
    l = abs(k)
    ellipse(screen, light_yellow, (x - 119*k, y + 17*l, 47*k, 25*l))
    ellipse(screen, light_yellow, (x - 131*k, y + 12*l, 35*k, 107*l))
    if k > 0:
        arc(screen, c[0], (x - 107*k, y + 4*l, 20*l, 70*l), 3 * pi / 10, 16.5 * pi / 10, 7)
        arc(screen, c[1], (x - 132*k, y + 15*l, 25*l, 70*l), pi / 2, 125 * pi / 100, 8)
        arc(screen, c[2], (x - 132*k, y + 20*l, 20*l, 73*l), pi / 2, 13.5 * pi / 10, 8)
        arc(screen, c[3], (x - 152*k, y + 42*l, 30*l, 59*l), -6*pi/10, 1*pi/10, 7)
        arc(screen, c[4], (x - 103*k, y + 51*l, 35*l, 59*l), 1.1 * pi, 1.58 * pi, 8)
        arc(screen, c[5], (x - 127*k, y + 65*l, 30*l, 59*l), -4. * pi / 10, 2 * pi / 10, 6)
        arc(screen, c[6], (x - 99*k, y + 6*l, 20*l, 50*l), 4.5*pi/10, 14*pi/10, 6)
        arc(screen, c[7], (x - 147*k, y +55*l, 30*l, 64*l), -7 * pi / 10, 2 * pi / 10, 10)
        arc(screen, c[8], (x - 135*k, y + 60*l, 30*l, 54*l), -7 * pi / 10, 2 * pi / 10, 9)
        arc(screen, c[9], (x - 118*k, y - 5*l, 35*l, 110*l), 3 * pi / 8, 12 * pi / 10, 10)
        arc(screen, c[10], (x - 125*k, y - 14*l, 46*l, 77*l), 5.6 * pi / 10, 1.13 * pi, 9)
        arc(screen, c[11], (x - 96*k, y - 19*l, 56*l, 32*l), 0.25 * pi, 1.2 * pi, 7)
        arc(screen, c[12], (x - 88*k, y - 5*l, 56*l, 26*l), 0.35 * pi, 1 * pi, 7)
        arc(screen, c[13], (x - 88*k, y - 14*l, 50*l, 26*l), 0.35 * pi, 0.9 * pi, 8)
        arc(screen, c[14], (x - 56*k, y - 31*l, 40*l, 26*l), 1.2 * pi, 1.91 * pi, 4)
        arc(screen, c[15], (x - 56*k, y - 26*l, 50*l, 26*l), 1.2 * pi, 1.81 * pi, 6)
        arc(screen, c[16], (x - 54*k, y - 18*l, 60*l, 26*l), 1.0 * pi, 1.5 * pi, 6)
    else:
        arc(screen, c[0], (x - 87*k, y + 4*l, 20*l, 70*l), alpha(16.5 * pi / 10), alpha(3 * pi / 10), 7)
        arc(screen, c[1], (x - 107*k, y + 15*l, 25*l, 70*l), alpha(125 * pi / 100), alpha(pi / 2), 8)
        arc(screen, c[2], (x - 112*k, y + 20*l, 20*l, 73*l), alpha(13.5 * pi / 10), alpha(pi / 2), 8)
        arc(screen, c[3], (x - 122*k, y + 42*l, 30*l, 59*l), alpha(1*pi/10), alpha(-6*pi/10), 7)
        arc(screen, c[4], (x - 68*k, y + 51*l, 35*l, 59*l), alpha(1.58 * pi), alpha(1.1 * pi), 8)
        arc(screen, c[5], (x - 97*k, y + 65*l, 30*l, 59*l), alpha(2 * pi / 10), alpha(-4. * pi / 10), 6)
        arc(screen, c[6], (x - 79*k, y + 6*l, 20*l, 50*l), alpha(14*pi/10), alpha(4.5*pi/10), 6)
        arc(screen, c[7], (x - 117*k, y + 55*l, 30*l, 64*l), alpha(2 * pi / 10), alpha(-7 * pi / 10), 10)
        arc(screen, c[8], (x - 105*k, y + 60*l, 30*l, 54*l), alpha(2 * pi / 10), alpha(-7 * pi / 10), 9)
        arc(screen, c[9], (x - 83*k, y - 5*l, 35*l, 110*l), alpha(12 * pi / 10), alpha(3 * pi / 8), 10)
        arc(screen, c[10], (x - 79*k, y - 14*l, 46*l, 77*l), alpha(1.13 * pi), alpha(5.6 * pi / 10), 9)
        arc(screen, c[11], (x - 40*k, y - 19*l, 56*l, 32*l), alpha(1.2 * pi), alpha(0.25 * pi), 7)
        arc(screen, c[12], (x - 32*k, y - 5*l, 56*l, 26*l), alpha(1 * pi), alpha(0.35 * pi), 7)
        arc(screen, c[13], (x - 38*k, y - 14*l, 50*l, 26*l), alpha(0.9 * pi), alpha(0.35 * pi), 8)
        arc(screen, c[14], (x - 16*k, y - 31*l, 40*l, 26*l), alpha(1.91 * pi), alpha(1.2 * pi), 4)
        arc(screen, c[15], (x - 6*k, y - 26*l, 50*l, 26*l), alpha(1.81 * pi), alpha(1.2 * pi), 6)
        arc(screen, c[16], (x + 6*k, y - 18*l, 60*l, 26*l), alpha(1.5 * pi), alpha(1.0 * pi), 6)


def ear(x, y, k):
    l = abs(k)
    polygon(screen, (20, 50, 70), [(x - 77*k, y + 6*l), (x - 98*k, y - 11*l), (x - 100*k, y - 8*l), (x - 91*k, y + 23*l), (x - 77*k, y + 6*l)])
    polygon(screen, (255, 255, 200), [(x - 77*k, y + 8*l), (x - 97*k, y - 9*l), (x - 99*k, y - 7*l), (x - 90*k, y + 22*l), (x - 77*k, y + 8*l)])


def horn(x, y, k):
    l = abs(k)
    polygon(screen, (50, 50, 0), [(x - 73*k, y - l), (x - 51*k, y - 59*l), (x - 52*k, y + 3*l), (x - 73*k, y - l)])
    polygon(screen, lime, [(x - 72*k, y + l), (x - 52*k, y - 52*l), (x - 53*k, y + 3*l), (x - 72*k, y + l)])


def tail(x, y, k, ct):
    l = abs(k)
    ellipse(screen, light_yellow, (x - 256*k, y + 128*l, 40*k, 25*l))
    ellipse(screen, blue, (x - 271*k, y + 151*l, 35*k, 107*l))

    if k > 0:
        arc(screen, ct[0], (x - 247*k, y + 149*l, 20*l, 70*l), 3 * pi / 10, 16.5 * pi / 10, 7)
        arc(screen, ct[1], (x - 272*k, y + 160*l, 25*l, 70*l), 0.5 * pi, 125 * pi / 100, 7)
        arc(screen, ct[2], (x - 272*k, y + 165*l, 20*l, 73*l), 0.1 * pi, 13.5 * pi / 10, 8)
        arc(screen, ct[3], (x - 292*k, y + 187*l, 30*l, 59*l), -6*pi/10, 1*pi/10, 7)
        arc(screen, ct[4], (x - 243*k, y + 196*l, 35*l, 59*l), 1.1 * pi, 1.58 * pi, 8)
        arc(screen, ct[5], (x - 267*k, y + 210*l, 30*l, 59*l), -4. * pi / 10, 2 * pi / 10, 6)
        arc(screen, ct[6], (x - 287*k, y + 200*l, 30*l, 64*l), -7 * pi / 10, 2 * pi / 10, 10)
        arc(screen, ct[7], (x - 275*k, y + 205*l, 30*l, 54*l), -7 * pi / 10, 4 * pi / 10, 9)
        arc(screen, ct[8], (x - 268*k, y + 140*l, 35*l, 110*l), 3 * pi / 8, 12 * pi / 10, 10)
        arc(screen, ct[9], (x - 260*k, y + 141*l, 38*l, 134*l), 0.6 * pi, 1.1 * pi, 9)
        arc(screen, ct[10], (x - 275*k, y + 131*l, 46*l, 77*l), 0.4 * pi, 1.13 * pi, 9)
    else:
        arc(screen, ct[0], (x - 227*k, y + 149*l, 20*l, 70*l), alpha(16.5 * pi / 10), alpha(3 * pi / 10), 7)
        arc(screen, ct[1], (x - 247*k, y + 160*l, 25*l, 70*l), alpha(125 * pi / 100), alpha(0.5 * pi), 7)
        arc(screen, ct[2], (x - 252*k, y + 165*l, 20*l, 73*l), alpha(13.5 * pi / 10), alpha(0.1 * pi), 8)
        arc(screen, ct[3], (x - 262*k, y + 187*l, 30*l, 59*l), alpha(1*pi/10), alpha(-6*pi/10), 7)
        arc(screen, ct[4], (x - 208*k, y + 196*l, 35*l, 59*l), alpha(1.58 * pi), alpha (1.1 * pi), 8)
        arc(screen, ct[5], (x - 237*k, y + 210*l, 30*l, 59*l), alpha(2 * pi / 10), alpha(-4. * pi / 10), 6)
        arc(screen, ct[6], (x - 257*k, y + 200*l, 30*l, 64*l), alpha(2 * pi / 10), alpha(-7 * pi / 10), 10)
        arc(screen, ct[7], (x - 245*k, y + 205*l, 30*l, 54*l), alpha(4 * pi / 10), alpha(-7 * pi / 10), 9)
        arc(screen, ct[8], (x - 233*k, y + 140*l, 35*l, 110*l), alpha(12 * pi / 10), alpha(3 * pi / 8), 10)
        arc(screen, ct[9], (x - 222*k, y + 141*l, 38*l, 134*l), alpha(1.1 * pi), alpha(0.6 * pi), 9)
        arc(screen, ct[10], (x - 229*k, y + 131*l, 46*l, 77*l), alpha(1.13 * pi), alpha(0.4 * pi), 9)


def tree(x, y, k):
    ellipse(screen, forest_green, (x+63*k, y+320*k, 100*k, 70*k))
    polygon(screen, coffee_brown, [(x+77*k, y+509*k), (x+127*k, y+504*k), (x+102*k, y+320*k), (x+89*k, y+320*k)])
    ellipse(screen, forest_green, (x, y+290*k, 120*k, 80*k))
    ellipse(screen, forest_green, (x+27*k, y+230*k, 180*k, 120*k))
    ellipse(screen, forest_green, (x+7*k, y+190*k, 100*k, 70*k))
    ellipse(screen, forest_green, (x+37*k, y+150*k, 150*k, 100*k))
    ellipse(screen, forest_green, (x+139*k, y+186*k, 67*k, 44*k))
    ellipse(screen, forest_green, (x+56*k, y+50*k, 98*k, 135*k))
    ellipse(screen, forest_green, (x+97*k, y+100*k, 80*k, 105*k))
    ellipse(screen, forest_green, (x+22*k, y+85*k, 70*k, 140*k))
    ellipse(screen, forest_green, (x+26*k, y+70*k, 50*k, 40*k))
    ellipse(screen, forest_green, (x+94*k, y+30*k, 80*k, 60*k))
    ellipse(screen, forest_green, (x+67*k, y, 70*k, 100*k))



def horse(x, y, k, c, ct):
    head(x, y, k)
    body(x, y, k)
    leg(x, y, k)
    eye(x, y, k)
    ear(x, y, k)
    mane(x, y, k, c)
    horn(x, y, k)
    tail(x, y, k, ct)
    

sky()
grass()
sun()
horse(500, 450, 1, c1, ct1)
horse(536, 315, -1, c2, ct2)
horse(510, 630, -0.7, c3, ct3)
tree(3, 75, 0.83)
tree(200, 82, 0.91)
tree(400, 60, 0.66)
circle(screen, red, (45, 200), 15)
circle(screen, red, (115, 350), 15)
circle(screen, red, (135, 240), 15)
circle(screen, red, (65, 310), 15)
circle(screen, blue, (445, 190), 8)
circle(screen, blue, (505, 160), 8)
circle(screen, blue, (460, 210), 8)
circle(screen, blue, (440, 250), 8)
circle(screen, blue, (485, 200), 8)
circle(screen, blue, (495, 255), 8)
circle(screen, blue, (465, 120), 8)
ellipse(screen, yellow, (280, 140, 16, 64))
ellipse(screen, yellow, (272, 176, 32, 32))
ellipse(screen, yellow, (326, 190, 16, 64))
ellipse(screen, yellow, (318, 226, 32, 32))
ellipse(screen, yellow, (266, 260, 16, 64))
ellipse(screen, yellow, (258, 296, 32, 32))

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()

