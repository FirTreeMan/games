import random
import pygame

pygame.init()
win = pygame.display.set_mode((889, 650))
pygame.display.set_caption('senor fraug')
char1 = pygame.image.load('frogspritefront1.png')
char2 = pygame.image.load('frogspriteleft1.png')
char3 = pygame.image.load('frogspriteright1.png')
char4 = pygame.image.load('frogspriteback1.png')
frontLoop = [pygame.image.load('frogspritefront1.png'), pygame.image.load('frogspritefront2.png')]
leftLoop = [pygame.image.load('frogspriteleft1.png'), pygame.image.load('frogspriteleft2.png')]
rightLoop = [pygame.image.load('frogspriteright1.png'), pygame.image.load('frogspriteright2.png')]
backLoop = [pygame.image.load('frogspriteback1.png'), pygame.image.load('frogspriteback2.png')]
car1left = pygame.image.load('carsprite1left.png')
car1right = pygame.image.load('carsprite1right.png')
bg = pygame.image.load('roads.png')
bgnoise = pygame.mixer.music.load('carnoises.wav')
clock = pygame.time.Clock()
pygame.mixer.music.play(-1)


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.front = True
        self.walkCount = 0
        self.vel = 7
        self.win = 0
        self.rect = pygame.Rect(self.x + 5, self.y, 36, 40)

    def draw(self, win):
        if self.walkCount + 1 > 4:
            self.walkCount = 0
        win.blit(frontLoop[self.walkCount // 2], (self.x, self.y))
        self.walkCount += 1
        self.rect = pygame.Rect(self.x + 5, self.y, 36, 40)


class enemy(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, 0, 0)
        self.car = True

    def draw(self, win):
        if self.car:
            win.blit(car1left, (self.x, self.y))
        elif not self.car:
            win.blit(car1right, (self.x, self.y))
        self.rect = pygame.Rect(self.x, self.y, 0, 0)


def redrawgamewindow():
    win.blit(bg, (0, 0))
    if frog.win > 0:
        text = font.render('U WIN!!!111', 1, (255, 0, 0))
        win.blit(text, (0, 0))
    frog.draw(win)
    car1.draw(win)
    car2.draw(win)
    car3.draw(win)
    car4.draw(win)
    car5.draw(win)
    car6.draw(win)
    car7.draw(win)
    car8.draw(win)
    car9.draw(win)
    pygame.display.update()


# main loop
# problem: hitbox is only for bottom left point
font = pygame.font.SysFont('comicsans', 40, True)
frog = player(400, 610, 46, 40)
car1 = enemy(random.choice([-109, 889]), (random.randrange(430, 503)), 109, 35)
car2 = enemy(random.choice([-109, 889]), (random.randrange(230, 263)), 109, 35)
car3 = enemy(random.choice([-109, 889]), (random.randrange(40, 103)), 109, 35)
car4 = enemy(random.choice([-109, 889]), (random.randrange(430, 503)), 109, 35)
car5 = enemy(random.choice([-109, 889]), (random.randrange(230, 263)), 109, 35)
car6 = enemy(random.choice([-109, 889]), (random.randrange(40, 103)), 109, 35)
car7 = enemy(random.choice([-109, 889]), (random.randrange(430, 503)), 109, 35)
car8 = enemy(random.choice([-109, 889]), (random.randrange(230, 263)), 109, 35)
car9 = enemy(random.choice([-109, 889]), (random.randrange(40, 103)), 109, 35)
run = True
while run:
    clock.tick(12)
    if frog.rect.colliderect(car1.rect):
        run = False
    if frog.rect.colliderect(car2.rect):
        run = False
    if frog.rect.colliderect(car3.rect):
        run = False
    if frog.rect.colliderect(car4.rect):
        run = False
    if frog.rect.colliderect(car5.rect):
        run = False
    if frog.rect.colliderect(car6.rect):
        run = False
    if frog.rect.colliderect(car7.rect):
        run = False
    if frog.rect.colliderect(car8.rect):
        run = False
    if frog.rect.colliderect(car9.rect):
        run = False
    if frog.y <= 10:
        frog.win += 1
    if frog.win > 0:
        frog.win += 1
    if frog.win > 45:
        run = False
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if keys[pygame.K_UP] and frog.y >= 0:
        frog.front = True
        frog.y -= frog.vel
    elif keys[pygame.K_LEFT] and frog.x >= 0:
        frog.left = True
        frog.x -= frog.vel
    elif keys[pygame.K_RIGHT] and frog.x <= 849:
        frog.right = True
        frog.x += frog.vel
    elif keys[pygame.K_DOWN] and frog.y <= 604:
        frog.back = True
        frog.y += frog.vel
    if car1.x == 889:
        car1.car = True
    elif car1.x == -109:
        car1.car = False
    if car2.x == 889:
        car2.car = True
    elif car2.x == -109:
        car2.car = False
    if car3.x == 889:
        car3.car = True
    elif car3.x == -109:
        car3.car = False
    if car4.x == 889:
        car4.car = True
    elif car4.x == -109:
        car4.car = False
    if car5.x == 889:
        car5.car = True
    elif car5.x == -109:
        car5.car = False
    if car6.x == 889:
        car6.car = True
    elif car6.x == -109:
        car6.car = False
    if car7.x == 889:
        car7.car = True
    elif car7.x == -109:
        car7.car = False
    if car8.x == 889:
        car8.car = True
    elif car8.x == -109:
        car8.car = False
    if car9.x == 889:
        car9.car = True
    elif car9.x == -109:
        car9.car = False
    if car1.car is True:
        car1.x -= 40
        pygame.display.update()
    elif car1.car is False:
        car1.x += 40
        pygame.display.update()
    if car2.car is True:
        car2.x -= 40
        pygame.display.update()
    elif car2.car is False:
        car2.x += 40
        pygame.display.update()
    if car3.car is True:
        car3.x -= 40
        pygame.display.update()
    elif car3.car is False:
        car3.x += 40
        pygame.display.update()
    if car4.car is True:
        car4.x -= 40
        pygame.display.update()
    elif car4.car is False:
        car4.x += 40
        pygame.display.update()
    if car5.car is True:
        car5.x -= 40
        pygame.display.update()
    elif car5.car is False:
        car5.x += 40
        pygame.display.update()
    if car6.car is True:
        car6.x -= 40
        pygame.display.update()
    elif car6.car is False:
        car6.x += 40
        pygame.display.update()
    if car7.car is True:
        car7.x -= 40
        pygame.display.update()
    elif car7.car is False:
        car7.x += 40
        pygame.display.update()
    if car8.car is True:
        car8.x -= 40
        pygame.display.update()
    elif car8.car is False:
        car8.x += 40
        pygame.display.update()
    if car9.car is True:
        car9.x -= 40
        pygame.display.update()
    elif car9.car is False:
        car9.x += 40
        pygame.display.update()
    if car1.x > 899 or car1.x < -109:
        car1.x = (random.choice([-109, 899]))
    if car2.x > 899 or car2.x < -109:
        car2.x = (random.choice([899, -109]))
    if car3.x > 899 or car3.x < -109:
        car3.x = (random.choice([-109, 899]))
    if car4.x > 899 or car4.x < -109:
        car4.x = (random.choice([-109, 899]))
    if car5.x > 899 or car5.x < -109:
        car5.x = (random.choice([899, -109]))
    if car6.x > 899 or car6.x < -109:
        car6.x = (random.choice([-109, 899]))
    if car7.x > 899 or car7.x < -109:
        car7.x = (random.choice([-109, 899]))
    if car8.x > 899 or car8.x < -109:
        car8.x = (random.choice([899, -109]))
    if car9.x > 899 or car9.x < -109:
        car9.x = (random.choice([-109, 899]))
    win.fill((0, 0, 0))
    redrawgamewindow()
pygame.quit()
