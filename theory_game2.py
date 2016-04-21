import pygame
import sys
import inputbox
from Button import Button
import errorScreen
import teststart
from pygame.locals import *


def theory_game2(DISPLAYSURF):
	if pygame.mixer.music.get_busy():
		pygame.mixer.music.stop()
	btn_back = pygame.image.load('Images/buttons/back.png')
	btn_next = pygame.image.load('Images/buttons/next.png')
	btn_home = pygame.image.load('Images/buttons/home.png')

	clock = pygame.time.Clock()
	background1=pygame.image.load('Images/game2/Explanation/1.jpg')
	run = True
	image_no = 1
	while run:
		
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if rect_back.collidepoint(mouse):
					if image_no  <= 1:					
						image_no = 1
					else :
						image_no-=1
						image_name = "Images/game2/Explanation/"+str(image_no)+".jpg"
						background1=pygame.image.load(image_name)
						DISPLAYSURF.blit(background1,(0,0))						
						pygame.display.update()
						
				elif rect_next.collidepoint(mouse):
					if image_no >=7:
						image_no  = 7
					else :
						image_no+=1
						image_name = "Images/game2/Explanation/"+str(image_no)+".jpg"
						background1=pygame.image.load(image_name)
						DISPLAYSURF.blit(background1,(0,0))
						pygame.display.update()
				elif rect_home.collidepoint(mouse):
					run = False

		DISPLAYSURF.blit(background1,(0,0))
		rect_back = DISPLAYSURF.blit(btn_back ,(10,10))
		rect_next = DISPLAYSURF.blit(btn_next,(50,10))
		rect_home= DISPLAYSURF.blit(btn_home,(550,10))
		pygame.display.update()
		clock.tick(60)
	background_end=pygame.image.load('Images/simphy.jpg')
	DISPLAYSURF.blit(background_end,(0,0))
	pygame.display.update()
