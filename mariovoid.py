import pygame

pygame.init()
win = pygame.display.set_mode((500, 500))
pygame.display.set_caption('fish poop')
walkRight = [pygame.image.load('mariospriteright1.png'), pygame.image.load('mariospriteright2.png'), pygame.image.load('mariospriteright3.png'), pygame.image.load('mariospriteright4.png')]
walkLeft = [pygame.image.load('mariospriteleft1.png'), pygame.image.load('mariospriteleft2.png'), pygame.image.load('mariospriteleft3.png'), pygame.image.load('mariospriteleft4.png')]
bg = pygame.image.load("black.jpg")
char = pygame.image.load('mariospritestand1.png')
char2 = pygame.image.load('mariospritestand2.png')
jump = pygame.image.load('mariospritejump1.png')
jump2 = pygame.image.load('mariospritejump2.png')


def redrawgamewindow():
    global walkCount
    win.blit(bg, (0, 0))
    if walkCount + 1 >= 12:
        walkCount = 0
    if isJump is True and right:
        win.blit(jump, (x, y))
    elif isJump is True and left:
        win.blit(jump2, (x, y))
    elif left:
        win.blit(walkLeft[walkCount//3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount//3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
    pygame.display.update()


screenWidth = 500
x = 50
y = 425
width = 40
height = 60
vel = 7
isJump = False
jumpCount = 10
left = False
right = False
walkCount = 0
run = True
while run:
    pygame.time.delay(100)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screenWidth - width - vel:
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walkCount = 0
    if not isJump:
        if keys[pygame.K_SPACE]:
            isJump = True
            left = False
            right = False
            walkCount = 0
            pygame.display.update()
    else:
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg
            jumpCount -= 1
        else:
            isJump = False
            jumpCount = 10
    win.fill((0, 0, 0))
    redrawgamewindow()
pygame.quit()
