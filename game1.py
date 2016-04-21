import pygame
import sys
from Button import Button
from pygame.locals import *
from constants import *
import VbyNLM
import TbyNLM
import UbyNLM
import AbyNLM
import SbyNLM

def startGame1(DISPLAY_SURF):				# defining a fuction, this is how it is done in python

	btn_final_velocity =  pygame.image.load('Images/buttons/final_velocity.png') 
	btn_time =  pygame.image.load('Images/buttons/time.png') 
	btn_initial_velocity =  pygame.image.load('Images/buttons/initial_velocity.png') 
	btn_acceleration =  pygame.image.load('Images/buttons/acceleration.png') 
	btn_displacement =  pygame.image.load('Images/buttons/displacement.png') 
	clock = pygame.time.Clock()
	#background=pygame.image.load('Images/game1/physics.png')
	background=pygame.image.load('Images/game1Back.png')
	run = True
	while run:
		DISPLAY_SURF.blit(background,SCREEN_TOPLEFT)
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if rect_final_velocity.collidepoint(mouse):
					VbyNLM.compVbyNLM(DISPLAY_SURF)
				elif rect_time.collidepoint(mouse):
					TbyNLM.compTbyNLM(DISPLAY_SURF)
				elif rect_initial_velocity.collidepoint(mouse):
					UbyNLM.compUbyNLM(DISPLAY_SURF)
				elif rect_acceleration.collidepoint(mouse):
					AbyNLM.compAbyNLM(DISPLAY_SURF)
				elif rect_displacement.collidepoint(mouse):
					SbyNLM.compSbyNLM(DISPLAY_SURF)

		rect_final_velocity = DISPLAY_SURF.blit(btn_final_velocity,(125,103))
		rect_initial_velocity = DISPLAY_SURF.blit(btn_initial_velocity,(125,143))
		rect_time = DISPLAY_SURF.blit(btn_time,(125,183))
		rect_acceleration = DISPLAY_SURF.blit(btn_acceleration,(125,223))
		rect_displacement = DISPLAY_SURF.blit(btn_displacement,(125,263))
		
		pygame.display.update()
		clock.tick(60)
