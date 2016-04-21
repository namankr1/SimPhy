import pygame
import sys
import teststart
import pyganim
import string
from constants import *
from const_colors import *
from pygame.locals import *

def mainScreen():

	pygame.init()
	#BLACK = (0,0,0)
	#SCREEN_WIDTH = 600
	top_left = (10,10)
	clock = pygame.time.Clock()
	DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)
	#DISPLAY_SURF.fill(RED)
	DISPLAY_SURF.fill(WHITE)
	pygame.display.update()

	einstein = pygame.image.load('Images/einstein/1.jpg')
	einstein_Anim = pyganim.PygAnimation([('Images/einstein/1.jpg', 0.1),('Images/einstein/2.jpg', 0.1),('Images/einstein/3.jpg', 0.1),])              
	einstein_Anim.play()
	fontObj = pygame.font.Font(None,32)

	x = 10
	#file = open('SimPhy_Introduction.txt')
	with open('SimPhy_Introduction.txt') as file :
		for line in file :
			endIndex = len(line)
			string1 = line

			for curIndex in range(endIndex):
				############
				
				mouse = pygame.mouse.get_pos()
				for event in pygame.event.get():
					escapeText = fontObj.render("Press Escape to skip",True,BLACK)
					if event.type == pygame.QUIT:
						run = False
						pygame.quit()
						sys.exit()
					if event.type == KEYDOWN:
						inkey = event.key
						if inkey == K_ESCAPE :
							run = False
							teststart.start(DISPLAY_SURF)

				###########
				einstein_Anim.blit(DISPLAY_SURF, (SCREEN_WIDTH - einstein.get_width(),SCREEN_HEIGHT - einstein.get_height()))

				textSurfaceObj = fontObj.render(string1[0:curIndex],True,BLACK)
				textRectObj = textSurfaceObj.get_rect()
				textRectObj.topleft = top_left
				DISPLAY_SURF.blit(textSurfaceObj,textRectObj)
				DISPLAY_SURF.blit(escapeText,(50,300))

				pygame.display.update()
				clock.tick(10)

				
			x+=40
			top_left = (10,x)

		#### the Simphy-introduction file has last line with few spaces so that program waits for some milliseconds after printing text	
		teststart.start(DISPLAY_SURF)
				
	string1 = 'This is Simphy.'
	string2 = 'It is a Physics Simulation Game.'
	string3 = 'It helps in leaning Physics concepts.'
	endIndex1 = 1
	endIndex2 = 1
	endIndex3 = 1
	fontObj = pygame.font.Font(None,32)
	
	run = True

	while run:
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			escapeText = fontObj.render("Press Escape to skip",True,BLACK)
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				inkey = event.key
				if inkey == K_ESCAPE :
					run = False
					teststart.start(DISPLAY_SURF)

		pygame.display.update()	
		clock.tick(10)

#main starts
if __name__ == "__main__":
	mainScreen()
