import pygame
from pygame.locals import *
import sys
import pyganim
from Button import Button
import inputbox


def road_select(screen):
	print "inside road_select.py"
	background = pygame.image.load('Images/simphy.jpg')
	screen.blit(background,(0,0))
	pygame.display.update()
	road1 = pygame.image.load('Images/game1/road/r11.gif')
	road2 = pygame.image.load('Images/game1/road/r21.gif')
	road3 = pygame.image.load('Images/game1/road/r31.gif')
	road4 = pygame.image.load('Images/game1/road/r41.gif')
	run = True
	while run:
		screen.blit(background,(0,0))
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if rect1.collidepoint(mouse):
					return 1
				elif rect2.collidepoint(mouse):
					return 2
				elif rect3.collidepoint(mouse):
					return 3
				elif rect4.collidepoint(mouse):
					return 4
		rect1 = pygame.draw.rect(screen, (0,0,0), (30,180,120,80))
		rect2 = pygame.draw.rect(screen, (0,0,0), (180,180,120,80))
		rect3 = pygame.draw.rect(screen, (0,0,0), (330,180,120,80))
		rect4 = pygame.draw.rect(screen, (0,0,0), (470,180,120,80))
		screen.blit(road1,(30,180))
		screen.blit(road2,(180,180))
		screen.blit(road3,(330,180))
		screen.blit(road4,(470,180))
		pygame.display.update()
					
		

def car_select(screen):
	background = pygame.image.load('Images/simphy.jpg')
	screen.blit(background,(0,0))
	pygame.display.update()
	car1 = pygame.image.load('Images/game1/vehicle/v11.png')
	car2 = pygame.image.load('Images/game1/vehicle/v21.png')
	car3 = pygame.image.load('Images/game1/vehicle/v31.png')
	run = True
	while run:
		screen.blit(background,(0,0))
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if rect1.collidepoint(mouse):
					return 1
				elif rect2.collidepoint(mouse):
					return 2
				elif rect3.collidepoint(mouse):
					return 3
		rect1 = pygame.draw.rect(screen, (0,0,0), (30,180,100,100))
		rect2 = pygame.draw.rect(screen, (0,0,0), (180,180,100,100))
		rect3 = pygame.draw.rect(screen, (0,0,0), (330,180,100,100))			
		screen.blit(car1,(30,180))
		screen.blit(car2,(180,180))
		screen.blit(car3,(330,180))
		pygame.display.update()
	
def select_items(screen):
	car_val=car_select(screen)
	if(car_val==1):
		car1 = pygame.image.load('Images/game1/vehicle/car1.png')
		car2 = pygame.image.load('Images/game1/vehicle/car2.png')
	elif(car_val==2):
		car1 = pygame.image.load('Images/game1/vehicle/truck1.png')
		car2 = pygame.image.load('Images/game1/vehicle/truck2.png')
	elif(car_val==3):
		car1 = pygame.image.load('Images/game1/vehicle/matcycle1.png')
		car2 = pygame.image.load('Images/game1/vehicle/matcycle2.png')
	else:
		car1 = pygame.image.load('Images/game1/vehicle/car1.png')
		car2 = pygame.image.load('Images/game1/vehicle/car2.png')
		
	road_val= road_select(screen)
	
	if road_val == 1 :
		path1 = 'Images/game1/road/r1/'
		path2 = '.png'
		usr, boltAnim1,boltAnim2 = inputbox.ask_parallel(screen,"input :",road_val,46,path1,path2)
	elif road_val == 2 :
		path1 = 'Images/game1/road/r2/'
		path2 = '.gif'
		usr, boltAnim1,boltAnim2 = inputbox.ask_parallel(screen,"input :",road_val,31,path1,path2)	
	elif road_val == 3 :
		path1 = 'Images/game1/road/r3/'
		path2 = '.gif'
		usr, boltAnim1,boltAnim2 = inputbox.ask_parallel(screen,"input :",road_val,12,path1,path2)
	elif road_val == 4:
		path1 = 'Images/game1/road/r4/tmp-'
		path2 = '.gif'
		usr, boltAnim1,boltAnim2 = inputbox.ask_parallel(screen,"input:",road_val,20,path1,path2)
	else :
		path1 = 'Images/game1/road/r3/'
		path2 = '.gif'
		usr, boltAnim1,boltAnim2 = inputbox.ask_parallel(screen,"input :",road_val,12,path1,path2)
		
	return usr,car1,car2,boltAnim1,boltAnim2
