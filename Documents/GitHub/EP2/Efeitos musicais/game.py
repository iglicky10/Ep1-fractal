import pygame
pygame.mixer.init()
pygame.mixer.music.load("casino.wav")
pygame.mixer.music.play()
if pygame.mixer:
        pygame.mixer.music.fadeout(1000)
    pygame.time.wait(1000)
    pygame.quit()
while pygame.mixer.music.get_busy() == True:
    continue

