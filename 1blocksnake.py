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
        self.hiscore = 0
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
    text = font.render('noms grabbd: ' + str(snake.score) + '   most noms grabbd: ' + str(snake.hiscore), 1, (255, 0, 0))
    win.blit(text, (0, 0))
    snake.draw(win)
    food.draw(win)


# main loop
# problem: character choosing kinda broken idk
font = pygame.font.SysFont('comicsans', 28, True)
snake = player(217, 280, 7, 7)
food = enemy(random.randrange(0, 443, 7), (random.randrange(0, 443, 7)), 7, 7)
pygame.display.update()
run = True
while run:
    clock.tick(12)
    if snake.clappa > 1:
        snake.clappa += 1
    if snake.clappa > 30:
        snake.clappa = 0
    if snake.score > snake.hiscore:
        snake.hiscore += 1
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        snake.choosing = False
    if snake.choosing is False:
        if snake.x == food.x:
            if snake.y == food.y:
                snake.score += 1
                food.x = (random.randrange(food.left, food.right, 7))
                food.y = (random.randrange(food.up, food.down, 7))
        if keys[pygame.K_LEFT] and snake.right is False:
            if snake.left is not True:
                snake.rightLoop = 0
                snake.upLoop = 0
                snake.downLoop = 0
                snake.left = True
                snake.x -= 7
                snake.left = True
                snake.right = False
                snake.up = False
                snake.down = False
                snake.leftLoop = 1
        elif keys[pygame.K_RIGHT] and snake.left is False:
            if snake.right is not True:
                snake.leftLoop = 0
                snake.upLoop = 0
                snake.downLoop = 0
                snake.right = True
                snake.x += 7
                snake.left = False
                snake.right = True
                snake.up = False
                snake.down = False
                snake.rightLoop = 1
        elif keys[pygame.K_UP] and snake.down is False:
            if snake.up is not True:
                snake.leftLoop = 0
                snake.rightLoop = 0
                snake.downLoop = 0
                snake.up = True
                snake.y -= 7
                snake.left = False
                snake.right = False
                snake.up = True
                snake.down = False
                snake.upLoop = 1
        elif keys[pygame.K_DOWN] and snake.up is False:
            if snake.down is not True:
                snake.leftLoop = 0
                snake.rightLoop = 0
                snake.upLoop = 0
                snake.down = True
                snake.y += 7
                snake.left = False
                snake.right = False
                snake.up = False
                snake.down = True
                snake.downLoop = 1
        if snake.leftLoop > 0:
            snake.leftLoop += 1
        if snake.leftLoop > 6:
            snake.x -= 7
            snake.leftLoop = 1
        elif snake.rightLoop > 0:
            snake.rightLoop += 1
        if snake.rightLoop > 6:
            snake.x += 7
            snake.rightLoop = 1
        elif snake.upLoop > 0:
            snake.upLoop += 1
        if snake.upLoop > 6:
            snake.y -= 7
            snake.upLoop = 1
        elif snake.downLoop > 0:
            snake.downLoop += 1
        if snake.downLoop > 6:
            snake.y += 7
            snake.downLoop = 1
    else:
        if keys[pygame.K_LEFT]:
            snake.choosing -= 1
        if keys[pygame.K_RIGHT]:
            snake.choosing += 1
        if snake.choosing < 1:
            snake.choosing = 3
        if snake.choosing > 3:
            snake.choosing = 1
        if snake.choosing == 1:
            snake.char = choice1
            pygame.display.update()
        if snake.choosing == 2:
            snake.char = choice2
            pygame.display.update()
        if snake.choosing == 3:
            snake.char = choice3
            pygame.display.update()
    if snake.x > 443 or snake.x < 0:
        snake.score = 0
        snake.choosing = True
        snake.x = 217
        snake.y = 280
    if snake.y > 443 or snake.y < 0:
        snake.score = 0
        snake.choosing = True
        snake.x = 217
        snake.y = 280
    win.fill((0, 0, 0))
    redrawgamewindow()
pygame.quit()
