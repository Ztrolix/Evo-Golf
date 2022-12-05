import pygame
from pathlib import Path
background_colour = (255,255,255)
(width, height) = (400, 0)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Evo Golf - Settings [DO NOT CLOSE]')
Icon = pygame.image.load('settings_logo.png')
pygame.display.set_icon(Icon)
screen.fill(background_colour)
pygame.display.flip()
running = True
print(" ")
path_to_file = 'settings.txt'
path = Path(path_to_file)

FPS_lim = 60
Speed_lim = 1
Brightness = 100

if path.is_file():
    f = open('settings.txt', 'r')
    content = f.read()
    print(content)
else:
    file = open("settings.txt","w")
    L = ["Evo Golf Settings\n"," \n","FPS Limit: _____ [Do not change over 120!]\n","Speed Limit: _____ [Do not change over 3!]\n","Brightness: _____ [Do not change over 100!]\n"]
    file.writelines(L)
    file.close()



while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False