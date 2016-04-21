import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
from Button import Button
import sys
import inputbox
import teststart

class endScreen:
	def __init__(self, DISPLAY_SURF,text):
		pygame.font.init()
		fontobject = pygame.font.Font(None,18)
		if pygame.mixer.music.get_busy():
			pygame.mixer.music.stop()
		pygame.mixer.music.load('Sound/bomb.ogg')
		pygame.mixer.music.play(-1, 0.0)
		if len(text) != 0:
			btn_replay = pygame.image.load('Images/buttons/playagain.png')
			btn_exit = pygame.image.load('Images/buttons/exitbutton.png')

			clock = pygame.time.Clock()
			run1= True;
			while run1:
				mouse = pygame.mouse.get_pos()
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						if pygame.mixer.music.get_busy():
							pygame.mixer.music.stop()
						run1 = False
						pygame.quit()
						sys.exit()
					elif event.type == pygame.MOUSEBUTTONDOWN:
						if rect_replay.collidepoint(mouse):
							if pygame.mixer.music.get_busy():
								pygame.mixer.music.stop()
							print ("restart")
							teststart.start(DISPLAY_SURF)
						elif rect_exit.collidepoint(mouse):
							if pygame.mixer.music.get_busy():
								pygame.mixer.music.stop()
							print ("exit")
							run1 = False
							pygame.quit()
							sys.exit()
				rect_replay = DISPLAY_SURF.blit(btn_replay ,(130,(DISPLAY_SURF.get_height()-100)))
				rect_exit = DISPLAY_SURF.blit(btn_exit,(320,(DISPLAY_SURF.get_height()-100)))
				pygame.display.update()
				clock.tick(60)
