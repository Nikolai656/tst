import pygame  # подключаем библиотеку
pygame.init()  # запуск библиотеки
screen = pygame.display.set_mode((500, 500))  # создаем экран по имени screen габаритами 500 х 500
running = True  # условие работы главного игрового цикла

class Mario:
    def __init__(self):
        self.x = 250  # координаты марио в простарнстве
        self.y = 250
        self.speed_y = 5  # cкорость марио
        self.speed_x = 5
        self.img = pygame.image.load('lol.jpg') # загрузка картинки в img
        self.img_rect = self.img.get_rect(center=(self.x, self.y))  # холст для картинки
    def move_up(self):
        if self.y > 50:
            self.y -= self.speed_y
            self.img_rect = self.img.get_rect(center=(self.x, self.y))
    def move_down(self):
        if self.y < 450:
            self.y += self.speed_y
            self.img_rect = self.img.get_rect(center=(self.x, self.y))
    def move_left(self):
        if self.x > 50:
            self.x -= self.speed_x
            self.img_rect = self.img.get_rect(center=(self.x, self.y))
    def move_right(self):
        if self.x < 450:
            self.x += self.speed_x
            self.img_rect = self.img.get_rect(center=(self.x, self.y))

    def show(self):
        screen.blit(self.img, self.img_rect)  # отрисовываем картинку на экране
          # холст для картинки
m = Mario()
x, y = 250, 250
while running:  # главный игровой цикл
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if pressed[pygame.K_s]:
            m.move_down()
        if pressed[pygame.K_w]:
            m.move_up()
        if pressed[pygame.K_a]:
            m.move_left()
        if pressed[pygame.K_d]:
            m.move_right()
        if event.type == pygame.QUIT:
            running = False
    screen.fill((7, 7, 7))  # заполняем экран черным цветом
    m.show()
    pygame.display.flip()  # зачищаем экран