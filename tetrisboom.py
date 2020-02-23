import random
import pygame

pygame.init()
win = pygame.display.set_mode((150, 200))
pygame.display.set_caption('Tetris Boom')
char = pygame.image.load('spaceshipsprite1small.jpg')
block = pygame.image.load('tetrisspriteline1.jpg')
bg = pygame.image.load('spacebackdrop.png')
bgnoise = pygame.mixer.music.load('lavendertown.wav')
music = pygame.mixer_music
clock = pygame.time.Clock()
pygame.mixer.music.play(-1)


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.kills = 0
        self.lazer = 0
        self.shootcool = 0
        self.left = True
        self.right = True
        self.leftStop = 3
        self.rightStop = 132
        self.shootSpeed = 6
        self.speed = 2

    def draw(self, win):
        win.blit(char, (self.x, self.y))
        pygame.display.update()


class enemy(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.alive = True
        self.moveLoop = 0
        self.jorg = True
        self.speed = 12
        self.spawnLeft = 3
        self.spawnRight = 142
        self.tengo = True

    def draw(self, win):
        if self.alive is True:
            win.blit(block, (self.x, self.y))
            pygame.display.update()
        else:
            self.x = (random.randrange(self.spawnLeft, self.spawnRight))
            self.y = -27
            if ship.kills < 60:
                ship.kills += 1
            if self.tengo:
                self.alive = True
            if ship.kills == 10:
                ship.leftStop += 1
                ship.rightStop -= 1
                ship.shootSpeed -= 0.5
                ship.speed += 1
                self.speed -= 5
                self.spawnLeft += 1
                self.spawnRight -= 1
            if ship.kills == 20:
                ship.leftStop += 1
                ship.rightStop -= 1
                ship.shootSpeed -= 0.5
                self.speed -= 1
                self.spawnLeft += 1
                self.spawnRight -= 1
            if ship.kills == 30:
                ship.leftStop += 1
                ship.rightStop -= 1
                ship.shootSpeed -= 0.5
                self.speed -= 1
                self.spawnLeft += 1
                self.spawnRight -= 1
            if ship.kills == 40:
                ship.leftStop += 1
                ship.rightStop -= 1
                ship.shootSpeed -= 0.5
                self.speed -= 1
                self.spawnLeft += 1
                self.spawnRight -= 1
            if ship.kills == 50:
                ship.leftStop += 1
                ship.rightStop -= 1
                ship.shootSpeed -= 0.5
                self.speed -= 1
                self.spawnLeft += 1
                self.spawnRight -= 1
            if ship.kills == 60:
                self.tengo = False
                self.alive = False
            pygame.display.update()

    def move(self):
        self.y += 28
        if self.y > 122:
            self.jorg = False
        pygame.display.update()


def redrawgamewindow():
    win.blit(bg, (0, 0))
    pygame.draw.rect(win, (255, 0, 0), [0, 150, 150, 1])
    text = font.render('MANIFESTATIONS KILLED : ' + str(ship.kills), 1, (255, 0, 0))
    if ship.kills == 60:
        text = gont.render(random.choice(['...YOU KILLED IT, SOMEHOW', "We're saved!*applause*"]), 1, (255, 0, 0))
    if tetris.jorg is False:
        text = bont.render(random.choice(["OH $HIT IT'S HERE RUN!", 'IT COMES FOR YOU', 'YOUR FATE IS SEALED', 'IT IS INEVITABLE', 'YOU HAD NO CHANCE', 'IT IS LIFE ITSELF', "YOU WERE DOOMED FROM THE BEGINNING", "YOU ARE NO MORE THAN IT'S TOY", 'YOU CANNOT COMPREHEND IT']), 1, (255, 0, 0))
    win.blit(text, (0, 0))
    if ship.lazer == 1:
        pygame.draw.rect(win, (255, 215, 0), [ship.x + 6, 0, 4, ship.y])
    ship.draw(win)
    tetris.draw(win)


# main loop
font = pygame.font.SysFont('comicsans', 13, True)
bont = pygame.font.SysFont('comicsans', 12, True)
gont = pygame.font.SysFont('comicsans', 14, True)
ship = player(60, 179, 15, 29)
tetris = enemy((random.randrange(3, 142)), -30, 8, 28)
pygame.display.update()
run = True
while run:
    clock.tick(12)
    tetris.moveLoop += 1
    if ship.shootcool > 0:
        ship.shootcool += 1
        ship.left = False
        ship.right = False
    if ship.shootcool > ship.shootSpeed:
        ship.shootcool = 0
        ship.lazer = 0
        ship.left = True
        ship.right = True
    if tetris.moveLoop > tetris.speed:
        tetris.moveLoop = 0
        tetris.move()
        pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and ship.left is True and ship.right is True:
        if tetris.y > 1:
            if ship.shootcool == 0:
                ship.shootcool += 1
                ship.lazer = 1
                pygame.display.update()
                if tetris.x == ship.x:
                    tetris.alive = False
                    pygame.display.update()
                if tetris.x == ship.x + 1:
                    tetris.alive = False
                    pygame.display.update()
                if tetris.x == ship.x + 2:
                    tetris.alive = False
                    pygame.display.update()
                if tetris.x == ship.x + 3:
                    tetris.alive = False
                    pygame.display.update()
                if tetris.x == ship.x + 4:
                    tetris.alive = False
                    pygame.display.update()
                if tetris.x == ship.x + 5:
                    tetris.alive = False
                    pygame.display.update()
                if tetris.x == ship.x + 6:
                    tetris.alive = False
                    pygame.display.update()
                if tetris.x == ship.x + 7:
                    tetris.alive = False
                    pygame.display.update()
                if tetris.x == ship.x + 8:
                    tetris.alive = False
                    pygame.display.update()
                if tetris.x == ship.x + 9:
                    tetris.alive = False
                    pygame.display.update()
                if tetris.x == ship.x + 10:
                    tetris.alive = False
                    pygame.display.update()
                if tetris.x == ship.x + 11:
                    tetris.alive = False
                    pygame.display.update()
                if tetris.x == ship.x + 13:
                    tetris.alive = False
                    pygame.display.update()
                if tetris.x == ship.x + 14:
                    tetris.alive = False
                    pygame.display.update()
                if tetris.x == ship.x + 15:
                    tetris.alive = False
                    pygame.display.update()
    if keys[pygame.K_LEFT] and ship.x > ship.leftStop and ship.left is True:
        ship.x -= ship.speed
        pygame.display.update()
    if keys[pygame.K_RIGHT] and ship.x < ship.rightStop and ship.right is True:
        ship.x += ship.speed
        pygame.display.update()
    if tetris.jorg is False:
        run = False
    win.fill((15, 15, 42))
    redrawgamewindow()
pygame.quit()
