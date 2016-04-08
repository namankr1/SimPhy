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

def start(DISPLAYSURF):

	background = pygame.image.load('Images/simphy.jpg')
	btn = Button('Start')
	btn.setColor((255,0,0))
	btn.setHoverColor((0,255,0))
	btn.setFontColor((0,0,255))
	btn2 = Button('Credits')
	btn2.setColor((255,0,0))
	btn2.setHoverColor((0,255,0))
	btn2.setFontColor((0,0,255))
	btn3 = Button('Manual')
	btn3.setColor((255,0,0))
	btn3.setHoverColor((0,255,0))
	btn3.setFontColor((0,0,255))
	clock = pygame.time.Clock()
# background=pygame.image.load('Images/simphy.jpg')
	run = True
	DISPLAYSURF = pygame.display.set_mode((600,400), 0, 32)
# create the animation objects   ('filename of image',    duration_in_seconds)
	boltAnim = pyganim.PygAnimation([('Images/simphyimages/s.jpg', 0.2),('Images/simphyimages/m.jpg', 0.2),('Images/simphyimages/p.jpg', 0.2),('Images/simphyimages/h.jpg', 0.2),('Images/simphyimages/y.jpg', 0.2),('Images/simphyimages/notzoom.jpg',0.2),('Images/simphyimages/allzoom.jpg', 0.2),])
	boltAnim.play();
	
	while run:
		DISPLAYSURF.blit(background,(0,0))
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit(0)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if btn.obj.collidepoint(mouse):
					demo.startGame(DISPLAYSURF)		
				elif btn2.obj.collidepoint(mouse):
					credits.credits(DISPLAYSURF)
				elif btn3.obj.collidepoint(mouse):
					manual.manual(DISPLAYSURF)	     
		boltAnim.blit(DISPLAYSURF, (0, 0))
		btn.draw(DISPLAYSURF, mouse, (200,200,200,40), (225,203),40)
		btn2.draw(DISPLAYSURF, mouse, (200,250,200,40), (225,253),40)
		btn3.draw(DISPLAYSURF, mouse, (200,300,200,40), (225,303),40)
		pygame.display.update()
		clock.tick(60)

