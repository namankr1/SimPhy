import pygame
import sys
import inputbox
from Button import Button
import errorScreen
from pygame.locals import *
from constants import *
import game1
import game2
import game3

def startGame(DISPLAY_SURF):
	background=pygame.image.load('Images/simphy.jpg')
	DISPLAY_SURF.blit(background,SCREEN_TOPLEFT)
	pygame.mixer.music.load('Sound/bill1.ogg')
	pygame.mixer.music.play(-1, 0.0)
	try:
		btn_linear_motion = pygame.image.load('Images/buttons/linear_motion_button.png')
		btn_vertical_motion = pygame.image.load('Images/buttons/vertical_motion_button.png')
		btn_momentum = pygame.image.load('Images/buttons/momentum_button.png')
		clock = pygame.time.Clock()
		run1= True;
		while run1:
			DISPLAY_SURF.blit(background,SCREEN_TOPLEFT)
			mouse = pygame.mouse.get_pos()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					if pygame.mixer.music.get_busy():
						pygame.mixer.music.stop()
					run1 = False
					pygame.quit()
					sys.exit()
				elif event.type == pygame.MOUSEBUTTONDOWN:
					if rect_linear_motion.collidepoint(mouse):
						game1.startGame1(DISPLAY_SURF)
					elif rect_vertical_motiond.collidepoint(mouse):
						game2.startGame2(DISPLAY_SURF)
					elif rect_momentum.collidepoint(mouse):
						print ("game 3")
						game3.startGame3(DISPLAY_SURF)
						
			rect_linear_motion = DISPLAY_SURF.blit(btn_linear_motion ,(100,210))
			rect_vertical_motiond = DISPLAY_SURF.blit(btn_vertical_motion,(300,210))
			rect_momentum= DISPLAY_SURF.blit(btn_momentum,(200,310))

			pygame.display.update()
			clock.tick(60)
	except Exception:							# except is the python equivalent of catch block
		print ("error in demo")
		errorScreen.errorScreen(DISPLAY_SURF,"Something went wrong")
	else:
		print ("all good")
