import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
from Button import Button
import sys
import game1
import inputbox
import teststart
import theory_game1

class game1_ending:
	def __init__(self, screen,text,path):
		print ("hi game1_ending")
		fontobject = pygame.font.Font(None,18)
		if pygame.mixer.music.get_busy():
			pygame.mixer.music.stop()
		pygame.mixer.music.load('Sound/bomb.ogg')
		pygame.mixer.music.play(-1, 0.0)
		if len(text) != 0:
			btn_replay = pygame.image.load('Images/buttons/playagain.png')
			btn_exit = pygame.image.load('Images/buttons/exitbutton.png')
			btn_learnmore = pygame.image.load('Images/buttons/learnbutton.png')
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
							game1.startGame1(screen)
						elif rect_exit.collidepoint(mouse):
							if pygame.mixer.music.get_busy():
								pygame.mixer.music.stop()
							print ("exit")
							run1 = False
							pygame.quit()
							sys.exit()
						elif rect_learnmore.collidepoint (mouse):
							theory_game1.theory_game1(screen,path)
													
							
				rect_replay = screen.blit(btn_replay ,(10,260))
				rect_exit = screen.blit(btn_exit,(210,260))
				rect_learnmore= screen.blit(btn_learnmore,(410,260))
				pygame.display.update()
				clock.tick(60)
