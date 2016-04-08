import pygame
import inputbox
from pygame.locals import *
from animation3 import animation3
from Button import Button
         
def startGame3(DISPLAYSURF):
			
	FPS = 30
	fpsClock = pygame.time.Clock()
	SCREEN_WIDTH = 600
	#DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH,400), 0, 32)
	pygame.display.set_caption('Animation')
	WHITE = (255, 255, 255)
	RED = (255,0,0)

	btn = Button('Input the values')
	
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
					countInputs=1;
					u1 = inputbox.ask(DISPLAYSURF, "Initial velocity of object 1, u1",countInputs)
					u1_ = float (u1)
					countInputs=countInputs+5;
					u2 = inputbox.ask(DISPLAYSURF, "Initial velocity of object 2, u2",countInputs)
					u2_ = float (u2)
					countInputs=countInputs+5;
					m1 = inputbox.ask(DISPLAYSURF, "Mass of object 1, m1",countInputs)
					m1_ = float (m1)
					countInputs=countInputs+5;
					m2 = inputbox.ask(DISPLAYSURF, "Mass of object 2, m2",countInputs)
					m2_ = float (m2)
					if(m1_<0 or m2_<0):
						errorScreen(DISPLAYSURF,"Invalid Mass entered")
					v1 = (((m1_ - m2_)*u1_) + (2*m2_*u2_))/(m1_+m2_)
					v1_ = round (v1,2)		# round to 2 decimal places
					v2 = ((2*m1_*u1_) - (( m1_ - m2_)* u2_))/(m1_+m2_)
					v2_ = round (v2,2)
					background = pygame.image.load('Images/game3/background.png')
					DISPLAYSURF.blit(background,(0,0))
					font = pygame.font.Font(None, 20)
					text = font.render("Final Velocity of object A ="+str(v1_)+"metre/sec and Final Velocity of object B ="+str(v2_)+"metre/sec", 1, (10, 10, 10))
					animation3(DISPLAYSURF,'right',text,u1_,u2_,v1_,v2_)
					run = False	
				
		btn.draw(DISPLAYSURF, mouse, (185,80,200,20), (225,83))
		pygame.display.update()
		clock.tick(60)

