import pygame as pg
import random

pg.init()

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

size = [800, 400]
screen = pg.display.set_mode(size)

done = True
clock = pg.time.Clock()

xcoor = 75
ycoor = size[1]*0.8
crouchSize = -50

xcact = 600
ycact = size[1]*0.8

jumpSpd = 12
fallSpd = 7
cactSpd = 5

fall = False
jump = False
crouch = False
moveRight = False
moveLeft = False
cactus1 = False
cactus2 = False

while done:
    clock.tick(30)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = False

    screen.fill(WHITE)

    pg.draw.line(screen, BLACK, [0, size[1]*0.8], [size[0], size[1]*0.8], 5 )

    if event.type == pg.KEYDOWN:
        if event.key == pg.K_UP:
            if not fall:
                jump = True
        if event.key == pg.K_DOWN:
            crouch = True
        #if event.key == pg.K_RIGHT:
        #    moveRight = True
        #if event.key == pg.K_LEFT:
        #    moveLeft = True

    crouchSize = -50

    if jump:
        ycoor -= jumpSpd
        if ycoor <= 240:
            ycoor = 240
            jump = False
            fall = True

    if fall:
        ycoor += fallSpd
        if ycoor >= size[1]*0.8:
            ycoor = size[1]*0.8
            fall = False

    if crouch:
        crouchSize = -30
        crouch = False

    #if moveRight:
    #    xcoor += 0.1
    #    moveRight = False

    #if moveLeft:
    #    xcoor -= 0.1
    #    moveLeft = False

    if cactus1 == False:
        cactSpawn = random.randint(0, 1000)
        print(cactSpawn)
        if cactSpawn < 12:
            cactus1 = True
    
    if cactus1:
        xcact -= cactSpd
        pg.draw.rect(screen, GREEN, [xcact, ycact, -10, -40], 5)
        #print(xcact)
        if xcact <= 20:
            xcact = 700
            cactus1 = False

    if cactus2 == False:
        cactSpawn = random.randint(0, 1000)
        print(cactSpawn)
        if cactSpawn < 12:
            cactus2 = True
    
    if cactus2:
        xcact -= cactSpd
        pg.draw.rect(screen, GREEN, [xcact, ycact, -10, -40], 5)
        #print(xcact)
        if xcact <= 20:
            xcact = 700
            cactus2 = False

    pg.draw.rect(screen, BLACK, [xcoor, ycoor, -20, crouchSize], 5)

    pg.display.update()

