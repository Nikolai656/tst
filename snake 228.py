import pygame
import random

pygame.init()  # запуск библиотеки

screen = pygame.display.set_mode((950, 950))  # создаем экран по имени screen габаритами 500 х 500
running = True


class Snake:
    def __init__(self):
        self.x = 475  # координаты змеи в простарнстве
        self.y = 475
        self.speed_y = 1# cкорость змеи
        self.speed_x = 1
        self.img = pygame.image.load('doggi.png')  # загрузка картинки в img
        self.img_rect = self.img.get_rect(center=(self.x, self.y))  # холст для картинки

    def move_up(self):
        self.y -= self.speed_y
        self.img_rect = self.img.get_rect(center=(self.x, self.y))

    def move_down(self):
        self.y += self.speed_y
        self.img_rect = self.img.get_rect(center=(self.x, self.y))

    def move_left(self):
        self.x -= self.speed_x
        self.img_rect = self.img.get_rect(center=(self.x, self.y))

    def move_right(self):
        self.x += self.speed_x
        self.img_rect = self.img.get_rect(center=(self.x, self.y))

    def show(self):
        screen.blit(self.img, self.img_rect)  # отрисовываем картинку на экране

class Gamover:
    def __init__(self):
        self.x = 475
        self.y = 475
        self.img = pygame.image.load('2015_01_17_c7d5131233596aff8c1e5a552587d747.jpg')
        self.img_rect = self.img.get_rect(center=(self.x, self.y))  # холст для картинки

    def gameover(self, x, y):
        if y < 0:
            self.show()
            self.img_rect = self.img.get_rect(center=(self.x, self.y))
        if y > 950:
            self.show()
            self.img_rect = self.img.get_rect(center=(self.x, self.y))
        if x < 0:
            self.show()
            self.img_rect = self.img.get_rect(center=(self.x, self.y))
        if x > 950:
            self.show()
            self.img_rect = self.img.get_rect(center=(self.x, self.y))

    def show(self):
        screen.blit(self.img, self.img_rect)  # отрисовываем картинку на экране

class Food:
    def __init__(self):
        self.x = random.randint(92, 858)
        self.y = random.randint(92, 858)
        self.img = pygame.image.load('3401.jpg')  # загрузка картинки в img
        self.img_rect = self.img.get_rect(center=(self.x, self.y))  # холст для картинки

    def crash(self, Snake):
        return self.img_rect.colliderect(Snake)

    def show(self):
        screen.blit(self.img, self.img_rect)  # отрисовываем картинку на экране

l = Gamover()
f = Food()
p = Snake()
score = 0
move = [1, 2, 3, 4]
mem = 0
hell = []

while running:  # главный игровой цикл
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if l.gameover(p.x, p.y):
        running = False
    screen.fill((7, 7, 7))  # заполняем экран черным цветом
    p.show()
    f.show()
    l.gameover(p.x, p.y)
    if f.crash(p.img_rect):
        f.__init__()
    if f.crash(p.img_rect):
        score += 1
    if mem != score:
        print(score)
    pressed = pygame.key.get_pressed()
    if move == 1:
        p.move_up()
    if move == 2:
        p.move_left()
    if move == 3:
        p.move_right()
    if move == 4:
        p.move_down()
    if pressed[pygame.K_s]:
        p.move_down()
        move = 4
    if pressed[pygame.K_w]:
        p.move_up()
        move = 1
    if pressed[pygame.K_a]:
        p.move_left()
        move = 2
    if pressed[pygame.K_d]:
        p.move_right()
        move = 3
    pygame.display.flip()  # зачищаем экран
    mem = score