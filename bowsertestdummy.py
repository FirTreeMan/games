import pygame

pygame.init()
win = pygame.display.set_mode((300, 300))
pygame.display.set_caption('fish poop')
walkRight = [pygame.image.load('mariospriteright1.png'), pygame.image.load('mariospriteright2.png'),
             pygame.image.load('mariospriteright3.png'),
             pygame.image.load('mariospriteright4.png')]
walkLeft = [pygame.image.load('mariospriteleft1.png'), pygame.image.load('mariospriteleft2.png'),
            pygame.image.load('mariospriteleft3.png'),
            pygame.image.load('mariospriteleft4.png')]
bg = pygame.image.load('ground.jpg')
char = pygame.image.load('mariospritestand1.png')
char2 = pygame.image.load('mariospritestand2.png')
jump = pygame.image.load('mariospritejump1.png')
jump2 = pygame.image.load('mariospritejump2.png')
fireball1 = pygame.image.load('bowserspritefireball1.png')
fireball2 = pygame.image.load('bowserspritefireball2.png')
clock = pygame.time.Clock()
bowser_abuse = 0


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0
        self.screenWidth = 300
        self.standing = True
        self.hitbox = (self.x + 7, self.y - 2, 20, 32)

    def draw(self, win):
        if self.walkCount + 1 >= 9:
            self.walkCount = 0
        if not self.standing:
            if self.isJump is True and self.right:
                win.blit(jump, (self.x, self.y))
            elif self.isJump is True and self.left:
                win.blit(jump2, (self.x, self.y))
            elif self.left:
                win.blit(walkLeft[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            else:
                win.blit(walkRight[0], (self.x, self.y))
        self.hitbox = (self.x + 7, self.y - 2, 20, 32)
        # pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)


class projectile(object):
    def __init__(self, x, y, facing):
        self.x = x
        self.y = y
        self.facing = facing
        self.vel = 10 * facing

    def draw(self, win):
        win.blit(fireball1, (self.x, self.y))


class enemy(object):
    bowserWalkLeft = [pygame.image.load('bowserspriteleft1.png'), pygame.image.load('bowserspriteleft2.png'),
                      pygame.image.load('bowserspriteleft3.png'), pygame.image.load('bowserspriteleft4.png')]
    bowserWalkRight = [pygame.image.load('bowserspriteright1.png'), pygame.image.load('bowserspriteright2.png'),
                       pygame.image.load('bowserspriteright3.png'), pygame.image.load('bowserspriteright4.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 4
        self.hitbox = (self.x, self.y + 12, 27, 32)

    def draw(self, win):
        self.move()
        if self.walkCount + 1 >= 12:
            self.walkCount = 0
        if self.vel < 0:
            win.blit(self.bowserWalkLeft[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        else:
            win.blit(self.bowserWalkRight[self.walkCount // 3], (self.x, self.y))
            self.walkCount += 1
        self.hitbox = (self.x, self.y, 33, 39)
        # pygame.draw.rect(win, (0, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
    def hit(self):
        print('ow')
        pass


def redrawgamewindow():
    win.blit(bg, (0, 0))
    text = font.render('Times u abused bowser: ' + str(bowser_abuse), 1, (0, 0, 0))
    win.blit(text, (0, 0))
    mario.draw(win)
    bowser.draw(win)
    for fireball in fireballs:
        fireball.draw(win)
    pygame.display.update()


# main loop
font = pygame.font.SysFont('comicsans', 30, True)
mario = player(125, 226, 33, 33)
bowser = enemy(0, 219, 33, 40, 267)
shootLoop = 0
fireballs = []
run = True
while run:
    clock.tick(12)
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 25:
        shootLoop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for fireball in fireballs:
        if fireball.y - 10 < bowser.hitbox[1] + bowser.hitbox[3] and fireball.y + 10 > bowser.hitbox[1]:
            if fireball.x + 13 > bowser.hitbox[0] and fireball.x - 13 < bowser.hitbox[0] + bowser.hitbox[2]:
                bowser.hit()
                bowser_abuse += 1
                fireballs.pop(fireballs.index(fireball))
        if 300 > fireball.x > 0:
            fireball.x += fireball.vel
        else:
            fireballs.pop(fireballs.index(fireball))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE] and shootLoop == 0:
        if mario.left:
            facing = -1
        else:
            facing = 1
        if len(fireballs) < 2:
            fireballs.append(projectile(round(mario.x + mario.width // 2), round(mario.y + mario.height // 2), facing))
        shootLoop = 1
    if keys[pygame.K_LEFT] and mario.x > mario.vel:
        mario.x -= mario.vel
        mario.left = True
        mario.right = False
        mario.standing = False
    elif keys[pygame.K_RIGHT] and mario.x < mario.screenWidth - mario.width - mario.vel:
        mario.x += mario.vel
        mario.left = False
        mario.right = True
        mario.standing = False
    else:
        mario.standing = True
        walkCount = 0
    if not mario.isJump:
        if keys[pygame.K_UP]:
            mario.isJump = True
            mario.left = False
            mario.right = False
            mario.walkCount = 0
            pygame.display.update()
    else:
        if mario.jumpCount >= -10:
            mario.neg = 1
            if mario.jumpCount < 0:
                mario.neg = -1
            mario.y -= (mario.jumpCount ** 2) * 0.25 * mario.neg
            mario.jumpCount -= 1
        else:
            mario.isJump = False
            mario.jumpCount = 10
    win.fill((0, 0, 0))
    redrawgamewindow()
pygame.quit()
