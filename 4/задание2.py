import pygame
from pygame.draw import *
from pygame.transform import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((800, 1130))
rect(screen, (0, 245, 255), (0, 0, 800, 565))
rect(screen, (220, 220, 220), (0, 565, 800, 565))
line(screen, (0, 0, 0), (0, 565), (800, 565), 1)
ellipse(screen, (80, 80, 80), (455, 647, 291, 121))
ellipse(screen, (40, 100, 80), (480, 687, 231, 81))
ellipse(screen, (0, 0, 0), (455, 647, 291, 121), 1)
ellipse(screen, (0, 0, 0), (480, 687, 231, 81), 1)
c = pygame.Surface((800, 1130), pygame.SRCALPHA)
d = pygame.Surface((800, 1130), pygame.SRCALPHA)
circle(c, (255, 255, 200, 140), (487, 240), 200, 39)
line(d, (255, 255, 200, 140), (282, 244), (687, 240), 31)
line(d, (255, 255, 200, 140), (500, 0), (474, 439), 31)
ellipse(d, (255, 255, 215, 240), (461, 222, 51, 42))
circle(d, (255, 255, 215, 240), (479, 427), 12)
ellipse(d, (255, 255, 215, 240), (285, 231, 30, 25))
ellipse(d, (255, 255, 215, 240), (657, 227, 30, 25))
screen.blit(c, (0, 0))
screen.blit(d, (0, 0))

line(screen, (0, 0, 0), (615, 322), (615, 735))
lines(screen, (0, 0, 0), False, ((615, 322), (512, 389), (419, 467), (336, 554), (261, 652)), 4)
ellipse(screen, (220, 220, 220), (139, 388, 174, 106))
ellipse(screen, (0, 0, 0), (139, 388, 174, 106), 1)
ellipse(screen, (220, 220, 220), (5, 460, 250, 400))
ellipse(screen, (0, 0, 0), (5, 460, 250, 400), 1)
ellipse(screen, (220, 220, 220), (130, 760, 160, 130))
ellipse(screen, (0, 0, 0), (130, 760, 160, 130), 1)
ellipse(screen, (220, 220, 220), (240, 845, 160, 60))
ellipse(screen, (0, 0, 0), (240, 845, 160, 60), 1)
ellipse(screen, (220, 220, 220), (210, 530, 140, 60))
ellipse(screen, (0, 0, 0), (210, 530, 140, 60), 1)
e = pygame.Surface((800, 1130), pygame.SRCALPHA)
ellipse(e, (200, 210, 210), (320, 730, 154, 54))
ellipse(e, (0, 0, 0), (320, 730, 154, 54), 1)
polygon(e, (200, 210, 210), ((320, 757), (293, 730), (293, 784)))
polygon(e, (0, 0, 0), ((320, 757), (293, 730), (293, 784)), 1)
e = pygame.transform.rotate(e, 15)
screen.blit(e, (0, 0))





pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()
