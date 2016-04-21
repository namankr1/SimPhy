import pygame
import sys
import inputbox
from Button import Button
from animation2 import animation2
import errorScreen
from endScreen import endScreen
from constants import *
from pygame.locals import *

def startGame2(DISPLAY_SURF):
	print ("INSIDE GAME2.py")
	btn_start = pygame.image.load('Images/buttons/start.png')

	clock = pygame.time.Clock()
	background=pygame.image.load('Images/game2/1.png')
	run = True
	while run:
		DISPLAY_SURF.blit(background,SCREEN_TOPLEFT)
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if rect_start.collidepoint(mouse):
					countInputs = 1;
											
					mass = inputbox.ask(DISPLAY_SURF, "Mass, M",countInputs)
					mass = float (mass)
					if mass <= 0 :
						errorScreen.errorScreen(DISPLAY_SURF,"Mass must be Positve")
					countInputs = countInputs + 5;
					initial_velocity = inputbox.ask(DISPLAY_SURF, "Coeff. of Friction, u",countInputs)
					initial_velocity = float (initial_velocity)
					if initial_velocity > 1 :
						errorScreen.errorScreen(DISPLAY_SURF,"Invalid coeff. of friction")
					if initial_velocity < 0 :
						errorScreen.errorScreen(DISPLAY_SURF,"Invalid coeff. of friction")
					countInputs = countInputs + 5;
					force = inputbox.ask(DISPLAY_SURF, "Force, F",countInputs)
					force = float (force)
					final_velocity = initial_velocity * force
					weight = mass * 9.8
						
					if ( weight > final_velocity):
						font = pygame.font.Font(None, 36)
						text = font.render("The block will fall down.", 1, (10, 10, 10))
						animation2(DISPLAY_SURF,'down',text)
					else:
						res = pygame.image.load('Images/game2/5.png')
						DISPLAY_SURF.blit(res,SCREEN_TOPLEFT)
						endScreen(DISPLAY_SURF,":)")
					
		rect_start = DISPLAY_SURF.blit(btn_start ,(220,303))

		

		pygame.display.update()
		clock.tick(60)
