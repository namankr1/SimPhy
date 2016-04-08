import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
from Button import Button
import sys
import inputbox
import teststart

class errorScreen:
	def __init__(self, screen,text):
	    # set up music
		pygame.mixer.music.load('Sound/error.ogg')
		pygame.mixer.music.play(-1, 0.0)
		fontobject = pygame.font.Font(None,18)
		bckgd = pygame.image.load('Images/error.jpg')
		screen.blit(bckgd,(0,0))
		pygame.draw.rect(screen, (75,100,25),((screen.get_width() / 2) - 100,100,200,20), 0)
		pygame.draw.rect(screen, (255,255,255),((screen.get_width() / 2) - 102,98,204,24), 1)
		
		if len(text) != 0:
			screen.blit(fontobject.render(text, 1, (255,255,255)),((screen.get_width() / 2) - 100, 100))
			pygame.display.flip()
			btnReplay = Button('  Play Again ?')
			btnExit = Button('          Exit' )
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
						if btnReplay.obj.collidepoint(mouse):
							if pygame.mixer.music.get_busy():
								pygame.mixer.music.stop()
							print ("restart")
							teststart.start(screen)
						elif btnExit.obj.collidepoint(mouse):
							print ("exit")
							if pygame.mixer.music.get_busy():
								pygame.mixer.music.stop()
							run1= False;
							pygame.quit()
							sys.exit()
							
				btnReplay.draw(screen, mouse, (150,(screen.get_height()-100),100,20), (150,(screen.get_height()-100)))
				btnExit.draw(screen, mouse, (300,(screen.get_height()-100),100,20), (300,(screen.get_height()-100)))
				pygame.display.update()
				clock.tick(60)
