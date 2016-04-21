import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
from Button import Button
import sys
import inputbox
import teststart
from constants import *
from const_colors import *

class errorScreen:
	def __init__(self, DISPLAY_SURF,text):
	    # set up music
		pygame.mixer.music.load('Sound/error.ogg')
		pygame.mixer.music.play(-1, 0.0)
		fontobject = pygame.font.Font(None,18)
		bckgd = pygame.image.load('Images/error.jpg')
		DISPLAY_SURF.blit(bckgd,SCREEN_TOPLEFT)
		pygame.draw.rect(DISPLAY_SURF, (75,100,25),((DISPLAY_SURF.get_width() / 2) - 100,100,200,20), 0)
		pygame.draw.rect(DISPLAY_SURF, WHITE,((DISPLAY_SURF.get_width() / 2) - 102,98,204,24), 1)
		
		if len(text) != 0:
			DISPLAY_SURF.blit(fontobject.render(text, 1, WHITE),((DISPLAY_SURF.get_width() / 2) - 100, 100))
			pygame.display.flip()
			btn_replay = pygame.image.load('Images/buttons/playagain.png')
			btn_exit = pygame.image.load('Images/buttons/exitbutton.png')

			#btnReplay = Button('  Play Again ?')
			#btnExit = Button('          Exit' )
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
							print ("exit")
							if pygame.mixer.music.get_busy():
								pygame.mixer.music.stop()
							run1= False;
							pygame.quit()
							sys.exit()
							
				rect_replay = DISPLAY_SURF.blit(btn_replay ,(130,(DISPLAY_SURF.get_height()-100)))
				rect_exit = DISPLAY_SURF.blit(btn_exit,(320,(DISPLAY_SURF.get_height()-100)))
				#btnReplay.draw(DISPLAY_SURF, mouse, (150,(DISPLAY_SURF.get_height()-100),100,20), (150,(DISPLAY_SURF.get_height()-100)))
				#btnExit.draw(DISPLAY_SURF, mouse, (300,(DISPLAY_SURF.get_height()-100),100,20), (300,(DISPLAY_SURF.get_height()-100)))
				pygame.display.update()
				clock.tick(60)
