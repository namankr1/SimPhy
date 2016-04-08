import pygame
import sys
import inputbox
from Button import Button
from animation2 import animation2
from errorScreen import errorScreen
from endScreen import endScreen
from pygame.locals import *

def startGame2(DISPLAYSURF):
	btn = Button('Start')

	clock = pygame.time.Clock()
	background=pygame.image.load('Images/game2/1.png')
	run = True
	while run:
		DISPLAYSURF.blit(background,(0,0))
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if btn.obj.collidepoint(mouse):
					countInputs=1;
											
					m1 = inputbox.ask(DISPLAYSURF, "Mass, M",countInputs)
					m2 = float (m1)
					countInputs=countInputs+5;
					u1 = inputbox.ask(DISPLAYSURF, "Coefficient of Friction, u",countInputs)
					u2 = float (u1)
					if u2 > 1 :
						errorScreen(DISPLAYSURF,"Invalid coeff. of friction")
					if u2 < 0 :
						errorScreen(DISPLAYSURF,"Invalid coeff. of friction")
					countInputs=countInputs+5;
					f1 = inputbox.ask(DISPLAYSURF, "Force, F",countInputs)
					f2 = float (f1)
					v1 = u2 * f2
					W = m2 * 9.8
						
					if ( W > v1):
						font = pygame.font.Font(None, 36)
						text = font.render("The block will fall down.", 1, (10, 10, 10))
						animation2(DISPLAYSURF,'down',text)
					else:
						res=pygame.image.load('Images/game2/5.png')
						DISPLAYSURF.blit(res,(0,0))
						endScreen(DISPLAYSURF,":)")
					
		btn.draw(DISPLAYSURF, mouse, (200,300,100,20), (225,303))

		pygame.display.update()
		clock.tick(60)
