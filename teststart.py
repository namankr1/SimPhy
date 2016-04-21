import pygame
import os
import sys
import inputbox
import demo
import manual
import pyganim
import credits
from Button import Button
from pygame.locals import *
from constants import *
from const_colors import *

def start(DISPLAY_SURF):

	background = pygame.image.load('Images/simphy.jpg')
	btn_start = pygame.image.load('Images/buttons/playbutton.png') 	
	btn_credits = pygame.image.load('Images/buttons/creditsbutton.png') 
	btn_manual = pygame.image.load('Images/buttons/manualbutton.png') 

	clock = pygame.time.Clock()
# background=pygame.image.load('Images/simphy.jpg')
	run = True
	DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)
# create the animation objects   ('filename of image',    duration_in_seconds)
	boltAnim = pyganim.PygAnimation([('Images/simphyimages/s.jpg', 0.2),('Images/simphyimages/m.jpg', 0.2),('Images/simphyimages/p.jpg', 0.2),('Images/simphyimages/h.jpg', 0.2),('Images/simphyimages/y.jpg', 0.2),('Images/simphyimages/notzoom.jpg',0.2),('Images/simphyimages/allzoom.jpg', 0.2),])
	boltAnim.play();
	
	while run:
		DISPLAY_SURF.blit(background,SCREEN_TOPLEFT)
		mouse = pygame.mouse.get_pos()
	

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit(0)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if rect_start.collidepoint(mouse):
					demo.startGame(DISPLAY_SURF)		
				elif rect_credits.collidepoint(mouse):
					credits.credits(DISPLAY_SURF)
				elif rect_manual.collidepoint(mouse):
					manual.manual(DISPLAY_SURF)	     
				#elif btn.obj.collidepoint(mouse):
				#	manual.manual(DISPLAY_SURF)	
		boltAnim.blit(DISPLAY_SURF, (0, 0))
		rect_start = DISPLAY_SURF.blit(btn_start,(210,185))
		rect_credits = DISPLAY_SURF.blit(btn_credits,(210,250))
		rect_manual = DISPLAY_SURF.blit(btn_manual,(210,315))
		
		pygame.display.update()
		clock.tick(60)

#main starts
if __name__ == "__main__":
	DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)
	pygame.init()
	
	start(DISPLAY_SURF)
