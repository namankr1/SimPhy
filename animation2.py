import pygame
import sys
import inputbox
from endScreen import endScreen
from pygame.locals import *

class animation2:
	def __init__(self,screen,direction,text):
		FPS = 30
		fpsClock = pygame.time.Clock()
		screen = pygame.display.set_mode((600,400), 0, 32)
		pygame.display.set_caption('Animation')
		WHITE = (255, 255, 255)
		block = pygame.image.load('Images/game2/3.png')
		background = pygame.image.load('Images/game2/4.png')
		screen.blit(background,(0,0))
		blockx = 267
		blocky = 0
		textpos = text.get_rect()
		textpos.x = 0
		textpos.y = 350
		background.blit(text, textpos)
		while True :			#main game loop
			screen.blit(background,(0,0))
			if direction == 'down':
				blocky += 5
			if blocky>450 :
				endScreen(screen,"Oops.. The block fell down !")
			screen.blit(block, (blockx,blocky))
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
			fpsClock.tick(FPS)
