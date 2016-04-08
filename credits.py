import pygame
import sys
from pygame.locals import *

def credits(screen):
	file_name = open("dev_credits.txt")
	screen.fill((15,15,15))
	pygame.display.update()
	string =  file_name.read()
	array = string.splitlines();
	fontObj =pygame.font.SysFont("monospace", 15)
	textSurfaceObj=["a" for i in range(26)]
	for i in range(26):
		textSurfaceObj[i] = fontObj.render(array[i],True,(255,255,255))
	run = True
	while run:
		for i in range(26):
			textSurfaceObj[i] = fontObj.render(array[i],True,(255,255,255))
			screen.blit(textSurfaceObj[i],(10,i*18+10))
			pygame.display.update()
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			if event.type == KEYDOWN:
				inkey = event.key
				if inkey == K_ESCAPE :
					run = False
