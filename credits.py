import pygame
import sys
from pygame.locals import *

def credits(DISPLAY_SURF):
	background1 = pygame.image.load('Images/credits.jpg')
	btn_home = pygame.image.load('Images/buttons/home.png')
	pygame.display.update()
	run = True
	while run:
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				inkey = event.key
				if inkey == K_ESCAPE :
					run = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if rect_home.collidepoint(mouse):
					run = False
		DISPLAY_SURF.blit(background1,(0,0))
		rect_home= DISPLAY_SURF.blit(btn_home,(550,10))
		pygame.display.update()
