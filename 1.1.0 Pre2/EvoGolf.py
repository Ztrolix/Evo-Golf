import pygame
import sys
import random
from pygame import mixer
from pygame.locals import *

pygame.init() 
win = pygame.display.set_mode((1300, 800))
pygame.display.set_caption("Evo Golf")
Icon = pygame.image.load('logo.jpg')
pygame.display.set_icon(Icon)
bg_img = pygame.image.load('background.png')
bg_img = pygame.transform.scale(bg_img,(1300,800))

fxhole = 0
fyhole = 0
 
x = 2000
y = 2000
width = 40
height = 40
vel = 1

radius = 10

bg_img = pygame.image.load('background.png')
bg_img = pygame.transform.scale(bg_img,(1300,800))
i = 0
runing = True

X = 1300
Y = 800
textColor = (255, 255, 255)
display_surface = pygame.display.set_mode((X, Y))
font = pygame.font.Font('Toon Around.ttf', 100)
text = font.render('Loading', True, textColor)
textRect = text.get_rect()
TextX = X // 2
TextY = Y // 2
textRect.center = (TextX, TextY)

display_width = 1300
display_height = 800
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
carImg = pygame.image.load('start_game.png')
def car(fx,fy):
    gameDisplay.blit(carImg, (fx,fy))

fx =  2000
fy = 2000
gameStart = True

mixer.init()
mixer.music.load('hole.mp3')
mixer.music.set_volume(0.8)

loading = True
settings = False
start = False
loadPercent = 0
buttonStart = False

holeNumber = 1
randomX = random.randint(0,1200)
randomY = random.randint(400,800)
fps = 0
loadNum = random.randint(1,2)
telNum = 5
telNumFake = 10
clickingButton = False
fxhole2 = 0
fyhole2 = 0
teleHole = 2000

loadWin = False
loadWin2 = False
printXY = False
teleHoleX = 2000
teleHoleY = 2000
teleHoleX2 = 2000
teleHoleY2 = 2000

MouseLocaX = 0
MouseLocaY = 0
gameStartRandX = random.randint(475,875)
gameStartRandY = random.randint(400,500)

def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text


run = True
while run:


    if (gameStart == False) :
        if (x == 650) :
            if (y == 399) :
                buttonStart = True
            if (y == 398) :
                buttonStart = True

        if (buttonStart == True) :
            gameStart = True
            start = True
            printXY = True
            text = font.render('', True, textColor)
            fx = 2000
            fy = 2000
            telNumFake = 10
            telNum = 5
            carImg = pygame.image.load('flag_pole_hole.png')



    if (loading == True) :
        bg_img = pygame.image.load('loading_screen.png')
        text = font.render('', True, textColor)
        printXY = False

        
        if (loadPercent > 99) :
            loadPercent = 100
            print("Loading: ",100,"%")
            print("Done Loading!")
            print(" ")
            print("Go down to start.")
            print(" ")
            bg_img = pygame.image.load('background.png')
            TextX = X // 2
            TextY = Y // 4
            textColor = (0, 0, 0)
            text = font.render('Evo Golf', True, textColor)
            fx = 2000
            fy = 2000
            x = 650
            y = 400
            vel = 1
            loading = False
            gameStart = False
        else :
            loadPercent = loadPercent + loadNum
            loadNum = random.randint(1,2)
            print("Loading: ",loadPercent,"%")

    if (loadWin2 == True) :
        printXY = False
        bg_img = pygame.image.load('loading_screen.png')
        text = font.render('', True, textColor)
        if (loadPercent > 99) :
            loadPercent = 100
            print("Loading: ",100,"%")
            print("Done Loading!")
            print(" ")
            bg_img = pygame.image.load('level_win_2.png')
            x = 570
            y = 722
            loadWin2 = False
            printXY = True
            teleHoleX = 2000
            teleHoleY = 2000
            teleHoleX2 = 568
            teleHoleY2 = 753
            loadPercent = 0
        else :
            loadPercent = loadPercent + loadNum
            loadNum = random.randint(2,4)
            print("Loading: ",loadPercent,"%")

    if (loadWin == True) :
        printXY = False
        bg_img = pygame.image.load('loading_screen.png')
        text = font.render('', True, textColor)
        if (loadPercent > 99) :
            loadPercent = 100
            print("Loading: ",100,"%")
            print("Done Loading!")
            print(" ")
            bg_img = pygame.image.load('level_win.png')
            x = 554
            y = 88
            loadWin = False
            printXY = True
            teleHoleX = 554
            teleHoleY = 51
            teleHoleX2 = 2000
            teleHoleY2 = 2000
            loadPercent = 0
        else :
            loadPercent = loadPercent + loadNum
            loadNum = random.randint(2,4)
            print("Loading: ",loadPercent,"%")

    if (printXY == True) :
        print(" Hole: ",holeNumber," X: ",x," Y: ",y)
            
    if (start == True) :
        
        if (holeNumber == 1) :
            bg_img = pygame.image.load('level_1.png')
            fxhole = 766
            fyhole = 638
            fxhole2 = 240
            fyhole2 = 369
        if (holeNumber == 2) :
            bg_img = pygame.image.load('level_2.png')
            fxhole = 470
            fyhole = 751
            fxhole2 = 2000
            fyhole2 = 2000
        if (holeNumber == 3) :
            bg_img = pygame.image.load('level_3.png')
            fxhole = 1134
            fyhole = 310
        if (holeNumber == 4) :
            bg_img = pygame.image.load('level_4.png')
            fxhole = 1133
            fyhole = 311
        if (holeNumber > 4) :
            bg_img = pygame.image.load('level_win.png')
            holeNumber = 0
            fxhole = 2000
            fyhole = 2000
            teleHoleX = 554
            teleHoleY = 51
            loadPercent = 0

        if (x == fxhole) :
            if (y == fyhole) :
                x = 650
                y = 400
                holeNumber = holeNumber + 1
                mixer.music.play()
        if (x == fxhole2) :
            if (y == fyhole2) :
                x = 650
                y = 400
                holeNumber = holeNumber + 1
                mixer.music.play()

        if (x == teleHoleX) :
            if (y == teleHoleY) :
                x = 650
                y = 400
                mixer.music.play()
                loadWin2 = True
        if (x == teleHoleX2) :
            if (y == teleHoleY2) :
                x = 650
                y = 400
                mixer.music.play()
                loadWin = True

    win.fill((0,0,0))
    win.blit(bg_img,(i,0))
    win.blit(bg_img,(width+i,0))
    if (i==-width):
        win.blit(bg_img,(width+i,0))
        i=0
    i-=0

    pygame.time.delay(10)

    keys = pygame.key.get_pressed()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    
    x += (keys[pygame.K_d] - keys[pygame.K_LEFT]) * vel
    y += (keys[pygame.K_s] - keys[pygame.K_UP]) * vel
    x -= (keys[pygame.K_a] - keys[pygame.K_RIGHT]) * vel
    y -= (keys[pygame.K_w] - keys[pygame.K_DOWN]) * vel

    textRect.center = (TextX, TextY)
    display_surface.blit(text, textRect)

    car(fx,fy)
    pygame.draw.circle(win,(255, 255, 255),(x,y),radius)
    
    MouseLocaX,MouseLocaY = pygame.mouse.get_pos()

    gameStartRandX = random.randint(475,875)
    gameStartRandY = random.randint(400,500)

    if (MouseLocaX == gameStartRandX) :
        if (MouseLocaY == gameStartRandY) :
            clickingButton = True
            print("Click To Play")
            textColor = (255, 255, 255)
            if event.type == pygame.MOUSEBUTTONDOWN :
                start = True
                buttonStart = True

    if event.type == pygame.MOUSEBUTTONDOWN :
        if (clickingButton == False) :
            if (telNumFake < 1) :
                print("Sorry You have No More Teleports")
            else :
                x,y = pygame.mouse.get_pos()
                print("Teleporting... ",telNumFake," Teleports Left")
                telNumFake = telNumFake - 1

      
    pygame.display.update() 




   