import pygame
import sys
import teststart
import pyganim
import string
from pygame.locals import *

def mainScreen():

	pygame.init()
	Black = (0,0,0)
	SCREEN_WIDTH = 600
	top_left = (10,10)
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH,400), 0, 32)
	screen.fill((255,255,255))
	einstein = pygame.image.load('Images/einstein/1.jpg')
	string1 = 'This is Simphy.'
	string2 = 'It is a Physics Simulation Game.'
	string3 = 'It helps in leaning Physics concepts.'
	endIndex1 = 1
	endIndex2 = 1
	endIndex3 = 1
	fontObj = pygame.font.Font(None,32)
	einstein_Anim = pyganim.PygAnimation([('Images/einstein/1.jpg', 0.1),('Images/einstein/2.jpg', 0.1),('Images/einstein/3.jpg', 0.1),])              
	einstein_Anim.play()
	run = True

	while run:
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			escapeText = fontObj.render("Press Escape to skip",True,Black)
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				inkey = event.key
				if inkey == K_ESCAPE :
					run = False
					teststart.start(screen)

		if endIndex1 < 15 :
			endIndex1 += 1
			textSurfaceObj = fontObj.render(string1[0:endIndex1],True,Black)

		elif endIndex2 < 34:
			endIndex2 += 1
			textRectObj = textSurfaceObj.get_rect()
			textRectObj.topleft = top_left
			textSurfaceObj = fontObj.render(string1[0:endIndex1],True,Black)
			top_left = (10,60)
			textSurfaceObj = fontObj.render(string2[0:endIndex2],True,Black)

		elif endIndex3 < 40 :
			clock.tick(1000)
			endIndex3 += 1
			top_left = (10,10)
			textRectObj = textSurfaceObj.get_rect()
			textRectObj.topleft = top_left
			textSurfaceObj = fontObj.render(string1[0:endIndex1],True,Black)
			top_left = (10,60)
			textSurfaceObj = fontObj.render(string2[0:endIndex2],True,Black)
			top_left = (10,120)
			textSurfaceObj = fontObj.render(string3[0:endIndex3],True,Black)

		einstein_Anim.blit(screen, (SCREEN_WIDTH - einstein.get_width(),400 - einstein.get_height()))
		textRectObj = textSurfaceObj.get_rect()
		textRectObj.topleft = top_left
		screen.blit(escapeText,(50,300))
		screen.blit(textSurfaceObj,textRectObj)	
		pygame.display.update()	
		clock.tick(10)

#main starts
if __name__ == "__main__":
	mainScreen()
