import pygame
import sys
import inputbox
from Button import Button
from errorScreen import errorScreen
from pygame.locals import *
import game1
import game2
import game3

def startGame(DISPLAYSURF):
	background=pygame.image.load('Images/home.jpg')
	DISPLAYSURF.blit(background,(0,0))
	pygame.mixer.music.load('Sound/bill1.ogg')
	pygame.mixer.music.play(-1, 0.0)
	try:
		btngame1=Button('Linear Motion')
		btngame2=Button('Vertical Motion')	
		btngame3=Button('Momentum')	
		clock = pygame.time.Clock()
		run1= True;
		while run1:
			DISPLAYSURF.blit(background,(0,0))
			mouse = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					if pygame.mixer.music.get_busy():
						pygame.mixer.music.stop()
					run1 = False
					pygame.quit()
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if btngame1.obj.collidepoint(mouse):
						game1.startGame1(DISPLAYSURF)
					elif btngame2.obj.collidepoint(mouse):
						game2.startGame2(DISPLAYSURF)
					elif btngame3.obj.collidepoint(mouse):
						print ("game 3")
						game3.startGame3(DISPLAYSURF)
			btngame1.draw(DISPLAYSURF, mouse, (100,210,150,20), (100,210))				# draw linear motion button
			btngame2.draw(DISPLAYSURF, mouse, (300,210,150,20), (300,210))				# draw vertical motion button
			btngame3.draw(DISPLAYSURF, mouse, (200,310,150,20), (200,310))	
			pygame.display.update()
			clock.tick(60)
	except Exception:							# except is the python equivalent of catch block
		print ("error in demo")
		errorScreen(DISPLAYSURF,"Something went wrong")
	else:
		print ("all good")
