import math as m
from random import choice, randint
import pygame


FPS = 30

RED = 0xFF0000
BLUE = 0x0000FF
YELLOW = 0xFFC91F
GREEN = 0x00FF00
MAGENTA = 0xFF03B8
CYAN = 0x00FFCC
BLACK = (0, 0, 0)
WHITE = 0xFFFFFF
GREY = 0x7D7D7D
GAME_COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]

WIDTH = 800
HEIGHT = 600
g = m.exp(0.05)


class Ball:
    def __init__(self, screen: pygame.Surface, x=40, y=450):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.screen = screen
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(GAME_COLORS)
        self.live = 30

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        if self.x + self.vx > WIDTH:
            self.vx = - self.vx
        if self.y - self.vy - g > HEIGHT or self.y - self.vy - g < 0:
            self.vy = - self.vy
        self.x += self.vx
        self.y -= self.vy
        self.vy -= g

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj (для целей 1-го типа).

        Args:
            obj: Обьект, с которым проверяется столкновение (цель 1-го типа).
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if (self.x - obj.x) ** 2 + (self.y - obj.y) ** 2 <= (self.r + obj.r) ** 2:
            return True
        else:
            return False

    def hittest_2(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj (для целей 2-го типа).

        Args:
            obj: Обьект, с которым проверяется столкновение (цель 2-го типа).
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        if ((self.x + self.r >= obj.x1) and (self.x - self.r <= obj.x2) and
        (self.y + self.r >= obj.y1) and (self.y - self.r <= obj.y2)):
            return True
        else:
            return False


class Gun:
    def __init__(self, screen):
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = GREY

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        global balls, bullet
        bullet += 1
        new_ball = Ball(self.screen)
        new_ball.r += 5
        self.an = m.atan2((event.pos[1]-new_ball.y), (event.pos[0]-new_ball.x))
        new_ball.vx = self.f2_power * m.cos(self.an)
        new_ball.vy = - self.f2_power * m.sin(self.an)
        balls.append(new_ball)
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = m.atan((event.pos[1]-450) / (event.pos[0]-20))
        if self.f2_on:
            self.color = RED
        else:
            self.color = GREY

    def draw(self):
        pygame.draw.line(screen, BLACK, (10, 3 * HEIGHT / 4), (35, 3 * HEIGHT / 4), 4)
        # FIXIT don't know how to do it

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1
            self.color = RED
        else:
            self.color = GREY


class Target:
    def new_target(self):
        """ Инициализация новой цели. """
        x = self.x = randint(600, 780)
        y = self.y = randint(300, 550)
        r = self.r = randint(2, 50)
        self.points = 0
        self.live = 1
        color = self.color = RED

    def hit(self, points=1):
        """Попадание шарика в цель."""
        self.points += points

    def draw(self):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.r)

class Target_2:
    def new_target(self):
        """ Инициализация новой цели 2-го типа."""
        x1 = self.x1 = randint(600, 780)
        y1 = self.y1 = randint(300, 550)
        x2 = self.x2 = randint(x1 + 30, WIDTH - 10)
        y2 = self.y2 = randint(y1 + 30, HEIGHT - 10)
        self.points = 0
        self.live = 1
        color = self.color = BLUE

    def hit(self, points=1):
        """Попадание шарика в цель 2-го типа."""
        self.points += points

    def draw(self):
        pygame.draw.polygon(screen, self.color, ((self.x1, self.y1), (self.x1, self.y2), (self.x2, self.y2), (self.x2, self.y1), (self.x1, self.y1)))
        

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
bullet = 0
balls = []

clock = pygame.time.Clock()
gun = Gun(screen)
target = Target()
Target.new_target(target)
target_2 = Target_2()
Target_2.new_target(target_2)
finished = False

while not finished:
    screen.fill(WHITE)
    gun.draw()
    target.draw()
    target_2.draw()
    for b in balls:
        b.draw()
    pygame.display.update()

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            gun.fire2_start(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            gun.fire2_end(event)
        elif event.type == pygame.MOUSEMOTION:
            gun.targetting(event)

    for b in balls:
        b.move()
        if b.hittest(target) and target.live:
            target.live = 0
            target.hit()
            target.new_target()
        if b.hittest_2(target_2) and target_2.live:
            target_2.live = 0
            target_2.hit()
            target_2.new_target()
    gun.power_up()

pygame.quit()
