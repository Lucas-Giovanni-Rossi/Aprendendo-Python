# Tocar audio com py

import pygame #necessario importar pygam-ce

pygame.init() 
pygame.mixer.music.load('Desafios/21.desafio.mp3')
pygame.mixer.music.play()
pygame.event.wait

input()