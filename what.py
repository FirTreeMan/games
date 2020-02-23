import random
import pygame

pygame.init()
win = pygame.display.set_mode((450, 450))
pygame.display.set_caption('1blocksnake')
choice1 = pygame.image.load('tetrisspriteblockred1.jpg')
choice2 = pygame.image.load('tetrisspriteblockgreen1.jpg')
choice3 = pygame.image.load('tetrisspriteblockblue1.jpg')
apple = pygame.image.load('tetrisspritepinkapple1.jpg')
clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.score = 0
        self.choosing = True
        self.chosen = 1
        self.char = apple
        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.leftLoop = 0
        self.rightLoop = 0
        self.upLoop = 0
        self.downLoop = 0
        self.hitbox = (self.x, self.y, 7, 7)

    def draw(self, win):
        win.blit(snake.char, (self.x, self.y))
        pygame.display.update()


class enemy(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.alive = True
        self.left = 0
        self.right = 443
        self.up = 0
        self.down = 443
        self.hitbox = (self.x, self.y, 7, 7)

    def draw(self, win):
        if self.alive is True:
            win.blit(apple, (self.x, self.y))
            pygame.display.update()
        else:
            self.x = (random.randrange(self.left, self.right, 7))
            self.y = (random.randrange(self.up, self.down, 7))
            self.alive = True
            pygame.display.update()


def redrawgamewindow():
    text = font.render('score' + str(snake.score), 1, (255, 0, 0))
    win.blit(text, (0, 0))
    snake.draw(win)
    food.draw(win)


# main loop
font = pygame.font.SysFont('comicsans', 30, True)
snake = player(218, 250, 7, 7)
food = enemy(random.randrange(0, 443, 7), (random.randrange(0, 443, 7)), 7, 7)
pygame.display.update()
run = True
while run:
    clock.tick(12)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if snake.leftLoop > 0:
        snake.leftLoop += 1
        snake.rightLoop = 0
        snake.upLoop = 0
        snake.downLoop = 0
    if snake.leftLoop > 6:
        snake.x -= 7
    if snake.rightLoop > 0:
        snake.leftLoop = 0
        snake.rightLoop += 1
        snake.upLoop = 0
        snake.downLoop = 0
    if snake.rightLoop > 6:
        snake.x += 7
    if snake.upLoop > 0:
        snake.leftLoop = 0
        snake.rightLoop = 0
        snake.upLoop += 1
        snake.downLoop = 0
    if snake.upLoop > 6:
        snake.y += 7
    if snake.downLoop > 0:
        snake.leftLoop = 0
        snake.rightLoop = 0
        snake.upLoop = 0
        snake.downLoop += 1
    if snake.leftLoop > 6:
        snake.y -= 7
    if snake.choosing is True:
        if snake.choosing < 1:
            snake.choosing = 3
        if snake.choosing > 3:
            snake.choosing = 1
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            snake.choosing -= 1
        if keys[pygame.K_RIGHT]:
            snake.choosing += 1
        if snake.choosing == 1:
            win.blit(choice1, (snake.x, snake.y))
            pygame.display.update()
        if snake.choosing == 2:
            win.blit(choice2, (snake.x, snake.y))
            pygame.display.update()
        if snake.choosing == 3:
            win.blit(choice3, (snake.x, snake.y))
            pygame.display.update()
        if keys[pygame.K_SPACE]:
            if snake.choosing == 1:
                snake.char = choice1
                snake.choosing = False
            if snake.choosing == 2:
                snake.char = choice2
                snake.choosing = False
            if snake.choosing == 3:
                snake.char = choice3
                snake.choosing = False
    else:
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and snake.right is False:
            if snake.left is not True:
                snake.x -= 7
                snake.left = True
                snake.right = False
                snake.up = False
                snake.down = False
                snake.leftLoop = 1
        if keys[pygame.K_RIGHT] and snake.left is False:
            if snake.right is not True:
                snake.x += 7
                snake.left = False
                snake.right = True
                snake.up = False
                snake.down = False
                snake.rightLoop = 1
        if keys[pygame.K_UP] and snake.down is False:
            if snake.up is not True:
                snake.y += 7
                snake.left = False
                snake.right = False
                snake.up = True
                snake.down = False
                snake.upLoop = 1
        if keys[pygame.K_DOWN] and snake.up is False:
            if snake.down is not True:
                snake.y -= 7
                snake.left = False
                snake.right = False
                snake.up = False
                snake.down = True
                snake.downLoop = 1
    win.fill((0, 0, 0))
    redrawgamewindow()
pygame.quit()
