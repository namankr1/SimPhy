import pygame
import sys
from Button import Button
from pygame.locals import *
import VbyNLM
import TbyNLM
import UbyNLM
import AbyNLM
import SbyNLM

def startGame1(DISPLAYSURF):				# defining a fuction, this is how it is done in python
	btn = Button('Final Vel,v')
	btn2 = Button('Time, t')
	btn3 = Button('In. Vel, u')
	btn4 = Button('Accn., a')
	btn5 = Button('Disp, s')
	clock = pygame.time.Clock()
	background=pygame.image.load('Images/game1.jpg')
	run = True
	while run:
		DISPLAYSURF.blit(background,(0,0))
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if btn.obj.collidepoint(mouse):
					VbyNLM.compVbyNLM(DISPLAYSURF)
				elif btn2.obj.collidepoint(mouse):
					TbyNLM.compTbyNLM(DISPLAYSURF)
				elif btn3.obj.collidepoint(mouse):
					UbyNLM.compUbyNLM(DISPLAYSURF)
				elif btn4.obj.collidepoint(mouse):
					AbyNLM.compAbyNLM(DISPLAYSURF)
				elif btn5.obj.collidepoint(mouse):
					SbyNLM.compSbyNLM(DISPLAYSURF)
		btn.draw(DISPLAYSURF, mouse, (100,100,100,20), (125,103))
		btn2.draw(DISPLAYSURF, mouse, (100,130,100,20), (125,133))
		btn3.draw(DISPLAYSURF, mouse, (100,160,100,20), (125,163))
		btn4.draw(DISPLAYSURF, mouse, (100,190,100,20), (125,193))
		btn5.draw(DISPLAYSURF, mouse, (100,220,100,20), (125,223))
		pygame.display.update()
		clock.tick(60)
