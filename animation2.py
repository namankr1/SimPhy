import pygame
import sys
import inputbox
from game2_ending import game2_ending
from pygame.locals import *
from const_colors import *
from constants import *

class animation2:
	def __init__(self,DISPLAY_SURF,direction,text):
		FPS = 30
		fpsClock = pygame.time.Clock()
		DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)
		pygame.display.set_caption('Animation')
		block = pygame.image.load('Images/game2/3.png')
		background = pygame.image.load('Images/game2/4.png')
		DISPLAY_SURF.blit(background,SCREEN_TOPLEFT)
		blockx = 267
		blocky = 0
		textpos = text.get_rect()
		textpos.x = 0
		textpos.y = 350
		background.blit(text, textpos)
		while True :			#main game loop
			DISPLAY_SURF.blit(background,SCREEN_TOPLEFT)
			if direction == 'down':
				blocky += 5
			if blocky > 450 :
				game2_ending(DISPLAY_SURF,"Oops.. The block fell down !")
			DISPLAY_SURF.blit(block, (blockx,blocky))
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
			fpsClock.tick(FPS)
