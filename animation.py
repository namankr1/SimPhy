import pygame
import os
import sys
import inputbox
import errorScreen
from pygame.locals import *
from const_colors import *


class animation:
	def __init__(self,DISPLAY_SURF,direction,text):
		FPS = 30
		fpsClock = pygame.time.Clock()
		SCREEN_WIDTH = 600
		DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH,400), 0, 32)
		pygame.display.set_caption('Animation')
		WHITE = WHITE
		RED = RED
		catImg = pygame.image.load('Images/game4/block.png')
		cloud = pygame.image.load('Images/game4/cloudf.png')
		tree = pygame.image.load('Images/game4/tree.png')
		background = pygame.image.load('Images/game4/background.png')
		DISPLAY_SURF.blit(background,SCREEN_TOPLEFT)
		treex=370
		treey = 0
		catx = 0
		caty = 240
		textpos = text.get_rect()
		textpos.centerx = background.get_rect().centerx
		textpos.y = 350
		countTrees = 0
		background.blit(text, textpos)


		cloudx = SCREEN_WIDTH + 5
		cloudy = 60
		centerx = SCREEN_WIDTH
		fontObj = pygame.font.Font(None,16)
		textSurfaceObj = fontObj.render('Block is going to infinity!!',True,RED)
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.center = (centerx,50)


		while True :			#main game loop
			DISPLAY_SURF.blit(background,SCREEN_TOPLEFT)
			textRectObj.center = (centerx,cloudy)
			

			if direction == 'right':
				if catx < SCREEN_WIDTH/2 :
					catx += 5
				else:
					treex -= 5

				if countTrees>1 :
					cloudx -= 5
					centerx -= 5
					textRectObj.center = (centerx,50)
					DISPLAY_SURF.blit(textSurfaceObj,textRectObj)		
					DISPLAY_SURF.blit(cloud,(cloudx,cloudy))
					catx += 5
					treex += 5
					if catx > 580:
						errorScreen.errorScreen(DISPLAY_SURF,"Block went to Infinity")
				DISPLAY_SURF.blit(catImg, (catx,caty))
				DISPLAY_SURF.blit(tree, (treex,treey))
				if treex < -tree.get_width() - 10:
					treex = SCREEN_WIDTH + 20
					countTrees += 1
			if direction == 'left' :
				catx += 5		
				if catx > 500 :
					catx = 0
					pygame.time.wait(700)			# pause for 700 mili seconds
					errorScreen.errorScreen(DISPLAY_SURF,"Block went to -ve infinfity")
				DISPLAY_SURF.blit(catImg, (catx,caty))
				DISPLAY_SURF.blit(tree, (treex,treey))
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			pygame.display.update()
			fpsClock.tick(FPS)
