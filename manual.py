import pygame
import sys
from Button import Button
from pygame.locals import *

def manual(screen):
	file_name = open("man_game1.txt")
	screen.fill((15,15,15))
	pygame.display.update()
	btn_up = Button('Up')
	btn_top = Button('Top')
	btn_down = Button('Down')
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
				if btn_up.obj.collidepoint(mouse):
					posCons+=15
					if posCons >40:
						posCons = 40
					for i in range(40):
						pos[i] = i*15 +posCons
						if pos[i]>350 :
							pos[i] = 400
						if pos[i] < 30:
							pos[i] = -30
				elif btn_down.obj.collidepoint(mouse):
					posCons-=15
					if posCons + 40*15 < 360:
						posCons +=15
					for i in range(40):
						pos[i] = i*15 +posCons
						if pos[i]>350 :
							pos[i] = 400
						if pos[i] < 30:
							pos[i] = -30
				elif btn_top.obj.collidepoint(mouse):
					posCons = 40
					for i in range(40):
						pos[i] = i*15 +posCons
						if pos[i]>350 :
							pos[i] = 400
						if pos[i] < 30:
							pos[i] = -30
				screen.fill((15,15,15))
				for i in range(30):
					textSurfaceObj[i] = fontObj.render(array[i],True,(255,255,255))
					screen.blit(textSurfaceObj[i],(10,pos[i]))

			else:
				for i in range(30):
					textSurfaceObj[i] = fontObj.render(array[i],True,(255,255,255))
					screen.blit(textSurfaceObj[i],(10,pos[i]))
		btn_up.draw(screen, mouse, (150,5,40,20), (160,8))
		btn_top.draw(screen,mouse,(200,5,40,20),(210,8))
		btn_down.draw(screen, mouse, (150,370,40,20), (153,373))
		pygame.display.update()
		
