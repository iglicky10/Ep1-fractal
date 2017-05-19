import pygame, sys
from pygame.locals import *
pygame.init()
DISPLAYSURF = pygame.display.set_mode((500, 400), 0, 32)




soundObj = pygame.mixer.Sound('casino.wav')
soundObj.play()
pygame.mixer.music.stop()