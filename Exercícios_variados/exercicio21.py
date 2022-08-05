import pygame

pygame.mixer.init
pygame.init()
pygame.mixer.music.load('musical.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)
pygame.event.wait()

