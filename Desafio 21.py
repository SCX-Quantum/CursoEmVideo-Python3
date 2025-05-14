import pygame

pygame.init()

pygame.mixer.music.load('Desafio 21 - lofi.mp3')
pygame.mixer.music.play()
input('Aperte ENTER para PARAR.')
pygame.mixer.music.stop()


