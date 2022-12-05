from pickle import FALSE
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
 
x = 650
y = 400
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
textColor = (0, 0, 0)
display_surface = pygame.display.set_mode((X, Y))
font = pygame.font.Font('Toon Around.ttf', 100)
text = font.render('Evo Golf', True, textColor)
textRect = text.get_rect()
TextX = X // 2
TextY = Y // 4
textRect.center = (TextX, TextY)

display_width = 1300
display_height = 800
gameDisplay = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()
carImg = pygame.image.load('flag_pole.png')
def car(fx,fy):
    gameDisplay.blit(carImg, (fx,fy))

fx =  (display_width // 2)
fy = (display_height // 2)
gameStart = False

mixer.init()
mixer.music.load('hole.mp3')
mixer.music.set_volume(0.8)

loading = False
settings = False
start = False
loadPercent = 0

holeNumber = 1
randomX = random.randint(0,1200)
randomY = random.randint(400,800)
fps = 0

def update_fps():
	fps = str(int(clock.get_fps()))
	fps_text = font.render(fps, 1, pygame.Color("coral"))
	return fps_text

run = True
while run:
    if (gameStart == False) :
        print("X: ",x," Y: ",y)
        if (x == 762) :
            if (y == 754) :
                fx = 2000
                fy = 2000
                x = 2000
                y = 2000
                TextX = X // 2
                TextY = Y // 2
                vel = 0
                textColor = (255, 255, 255)
                text = font.render('Loading', True, textColor)
                gameStart = True
                print("Starting Game!")
                bg_img = pygame.image.load('black.jpg')
                loading = True

    if (loading == True) :
        bg_img = pygame.image.load('black.jpg')
        
        if (loadPercent == 100) :
            loadPercent = 100
            print("Done Loading!")
            bg_img = pygame.image.load('settings.jpg')
            TextX = X // 2.7
            TextY = Y // 4
            text = font.render('Edit Your Settings', True, textColor)
            print(" ")
            print("Current Settings")
            print(" ")
            print("Forward: W - UP")
            print("Left: A - LEFT")
            print("Backwards: S - DOWN")
            print("Right: D - RIGHT")
            print("Use: LMB")
            print(" ")
            print("You can change them below.")
            print(" ")
            print("Forward: _______")
            print("Left: _______")
            print("Backwards: _______")
            print("Right: _______")
            print("Use: _______")
            fx = 650
            fy = 400
            x = 650
            y = 400
            vel = 2
            settings = True
            loading = False
        else :
            loadPercent = loadPercent + 0.5
            print("Loading: ",loadPercent,"%")
            
    if (settings == True) :
        bg_img = pygame.image.load('settings.jpg')

        if (x == 762) :
            if (y == 754) :
                fx = random.randint(0,1200)
                fy = random.randint(400,800)
                fxhole = fx * 1.5
                fyhole = fy * 1.5
                x = 650
                y = 400
                TextX = X // 2
                TextY = Y // 4
                vel = 1
                textColor = (0, 0, 0)
                text = font.render('', True, textColor)
                print("Match Started")
                bg_img = pygame.image.load('background.png')
                start = True
                settings = False

    if (start == True) :
        print("X: ",x," Y: ",y," Hole: ",holeNumber," FX: ",fxhole," FY: ",fyhole)
        bg_img = pygame.image.load('background.png')
        if (x == fxhole) :
            if (y == fyhole) :
                #fx = random.randint(0,1200)
                #fy = random.randint(400,800)
                fx = 600
                fy = 400
                fxhole = fx * 0.5
                fyhole = fy * 0.5
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
      
    pygame.display.update() 
   