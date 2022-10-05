import pygame

pygame.init()

pygame.mixer.music.load('arquivo musica')
pygame.mixer.music.play()
pygame.event.wait()

