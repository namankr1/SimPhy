import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
from Button import Button
import sys
import inputbox
import teststart
import theory_game2

class game2_ending:
	def __init__(self, DISPLAY_SURF,text):
		print ("hi game2_ending")
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
							teststart.start(DISPLAY_SURF)
						elif rect_exit.collidepoint(mouse):
							if pygame.mixer.music.get_busy():
								pygame.mixer.music.stop()
							print ("exit")
							run1 = False
							pygame.quit()
							sys.exit()
						elif rect_learnmore.collidepoint (mouse):
							theory_game2.theory_game2(DISPLAY_SURF)
															
				rect_replay = DISPLAY_SURF.blit(btn_replay ,(10,260))
				rect_exit = DISPLAY_SURF.blit(btn_exit,(210,260))
				rect_learnmore= DISPLAY_SURF.blit(btn_learnmore,(410,260))
				pygame.display.update()
				clock.tick(60)
