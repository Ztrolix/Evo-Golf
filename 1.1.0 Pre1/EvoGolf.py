from pickle import FALSE, TRUE
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
            text = font.render('', True, textColor)
            fx = random.randint(100,1000)
            fy = random.randint(700,800)
            telNumFake = 10
            telNum = 5
            carImg = pygame.image.load('flag_pole.png')



    if (loading == True) :
        bg_img = pygame.image.load('black.jpg')

        
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
            fx = 475
            fy = 550
            x = 650
            y = 400
            vel = 2
            loading = False
            gameStart = False
        else :
            loadPercent = loadPercent + loadNum
            loadNum = random.randint(1,2)
            print("Loading: ",loadPercent,"%")
            
    if (start == True) :
        print(" Hole: ",holeNumber)
        bg_img = pygame.image.load('background.png')
        if (x == fxhole) :
            if (y == fyhole) :
                fx = random.randint(100,1000)
                fy = random.randint(700,800)
                fx = 600
                fy = 400
                fxhole = fx * 1.1
                fyhole = fy * 1.1
                x = 650
                y = 400
                TextX = X // 2
                TextY = Y // 4
                holeNumber = holeNumber + 1
                mixer.music.play()

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




   