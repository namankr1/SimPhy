import pygame
import sys
from Button import Button
from pygame.locals import *

def manual(DISPLAY_SURF):
	file_name = open("man_game1.txt")
	btn_home = pygame.image.load('Images/buttons/home.png')
	btn_up = pygame.image.load('Images/buttons/up.png')
	btn_down = pygame.image.load('Images/buttons/down.png')
	btn_top1 = pygame.image.load('Images/buttons/top.png')
	DISPLAY_SURF.fill((0,0,200))
	pygame.display.update()
	btn_top = Button('Top')
	pos=[0 for i in range(40)]
	for i in range(40):
		pos[i] = i*15 + 40
		if pos[i]>350 :
			pos[i] = 400
		if pos[i] < 30:
			pos[i] = -30
	string = file_name.read()
	array = string.splitlines();
	fontObj =pygame.font.SysFont("monospace", 15)
	textSurfaceObj=["a" for i in range(30)]
	for i in range(30):
		textSurfaceObj[i] = fontObj.render(array[i],True,(255,255,255))
	run = True
	posCons=40
	while run:
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			elif event.type == KEYDOWN:
				inkey = event.key
				if inkey == K_ESCAPE :
					run = False
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if rect_up.collidepoint(mouse):
					posCons+=15
					if posCons >40:
						posCons = 40
					for i in range(40):
						pos[i] = i*15 +posCons
						if pos[i]>350 :
							pos[i] = 400
						if pos[i] < 30:
							pos[i] = -30
				elif rect_down.collidepoint(mouse):
					posCons-=15
					if posCons + 40*15 < 360:
						posCons +=15
					for i in range(40):
						pos[i] = i*15 +posCons
						if pos[i]>350 :
							pos[i] = 400
						if pos[i] < 30:
							pos[i] = -30
				elif rect_top1.collidepoint(mouse):
					posCons = 40
					for i in range(40):
						pos[i] = i*15 +posCons
						if pos[i]>350 :
							pos[i] = 400
						if pos[i] < 30:
							pos[i] = -30
				elif rect_home.collidepoint(mouse):
					run = False
				DISPLAY_SURF.fill((0,0,200))
				for i in range(30):
					textSurfaceObj[i] = fontObj.render(array[i],True,(255,255,255))
					DISPLAY_SURF.blit(textSurfaceObj[i],(10,pos[i]))

			else:
				for i in range(30):
					textSurfaceObj[i] = fontObj.render(array[i],True,(255,255,255))
					DISPLAY_SURF.blit(textSurfaceObj[i],(10,pos[i]))
		#btn_top.draw(DISPLAY_SURF,mouse,(200,5,40,20),(210,8))
		rect_home= DISPLAY_SURF.blit(btn_home,(550,10))
		rect_up = DISPLAY_SURF.blit(btn_up ,(10,10))
		rect_down = DISPLAY_SURF.blit(btn_down,(50,10))
		rect_top1 = DISPLAY_SURF.blit(btn_top1,(200,10))
		pygame.display.update()
		
