import pygame
from pygame.locals import *
import sys
import pyganim
from Button import Button
from constants import *
import inputbox


def road_select(DISPLAY_SURF):
	background = pygame.image.load('Images/road_sel.jpg')
	DISPLAY_SURF.blit(background,SCREEN_TOPLEFT)
	
	pygame.display.update()
	road1 = pygame.image.load('Images/game1/road/r11.gif')
	road2 = pygame.image.load('Images/game1/road/r21.gif')
	road3 = pygame.image.load('Images/game1/road/r31.gif')
	road4 = pygame.image.load('Images/game1/road/r41.gif')
	run = True
	while run:
		DISPLAY_SURF.blit(background,SCREEN_TOPLEFT)
		
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
		rect1 = DISPLAY_SURF.blit(road1,(30,180))
		rect2 = DISPLAY_SURF.blit(road2,(180,180))
		rect3 = DISPLAY_SURF.blit(road3,(330,180))
		rect4 = DISPLAY_SURF.blit(road4,(470,180))
		pygame.display.update()
					
		

def car_select(DISPLAY_SURF):
	background = pygame.image.load('Images/xyz.jpg')
	Imag = pygame.image.load('Images/selection.png')
	DISPLAY_SURF.blit(background,SCREEN_TOPLEFT)
	pygame.display.update()
	car1 = pygame.image.load('Images/game1/vehicle/car3.png')
	car2 = pygame.image.load('Images/game1/vehicle/truck3.png')
	car3 = pygame.image.load('Images/game1/vehicle/matcycle3.png')
	run = True
	while run:
		DISPLAY_SURF.blit(background,SCREEN_TOPLEFT)
		DISPLAY_SURF.blit(Imag,(30,10))
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
		rect1 = DISPLAY_SURF.blit(car1,(30,180))
		rect2 = DISPLAY_SURF.blit(car2,(230,193))
		rect3 = DISPLAY_SURF.blit(car3,(430,200))
		pygame.display.update()
	
def select_items(DISPLAY_SURF):
	car_val=car_select(DISPLAY_SURF)
	if(car_val==1):
		car1 = pygame.image.load('Images/game1/vehicle/car1.png')
		car2 = pygame.image.load('Images/game1/vehicle/car2.png')
		scalew = 0.995
		scalez = 0.995
		scalex = 0.999
		scaley = 0.999
		multiplier_scale_big = 1.004
		multiplier_scale_small = 0.992
		sound_path = 'Sound/car.ogg'
	elif(car_val==2):
		car1 = pygame.image.load('Images/game1/vehicle/truck1.png')
		car2 = pygame.image.load('Images/game1/vehicle/truck2.png')
		scalew = 0.800
		scalez = 0.800
		scalex = 0.999
		scaley = 0.999
		multiplier_scale_big = 1.004
		multiplier_scale_small = 0.992
		sound_path = 'Sound/truck.ogg'
	elif(car_val==3):
		car1 = pygame.image.load('Images/game1/vehicle/matcycle1.png')
		car2 = pygame.image.load('Images/game1/vehicle/matcycle2.png')
		scalew = 0.999
		scalez = 0.999
		scalex = 0.999
		scaley = 0.999
		multiplier_scale_big = 1.004
		multiplier_scale_small = 0.995
		sound_path = 'Sound/bike.ogg'
	else:
		car1 = pygame.image.load('Images/game1/vehicle/car1.png')
		car2 = pygame.image.load('Images/game1/vehicle/car2.png')
		scalew = 0.995
		scalez = 0.995
		scalex = 0.999
		scaley = 0.999
		multiplier_scale_big = 1.004
		multiplier_scale_small = 0.992
		sound_path = 'Sound/car.ogg'
		
	road_val= road_select(DISPLAY_SURF)
	
	background = pygame.image.load('Images/input.png')
	DISPLAY_SURF.blit(background,SCREEN_TOPLEFT)
	pygame.display.update()
	if road_val == 1 :
		path1 = 'Images/game1/road/r1/'
		path2 = '.png'
		usr, boltAnim1,boltAnim2 = inputbox.ask_parallel(DISPLAY_SURF,"Guess Answer ?? :",road_val,46,path1,path2)
		carx = 280
		mincary = 150
		maxcary = 300
	elif road_val == 2 :
		path1 = 'Images/game1/road/r2/'
		path2 = '.png'
		usr, boltAnim1,boltAnim2 = inputbox.ask_parallel(DISPLAY_SURF,"Guess Answer ?? :",road_val,30,path1,path2)
		carx = 280
		mincary = 188
		maxcary = 300
	elif road_val == 3 :
		path1 = 'Images/game1/road/r3/'
		path2 = '.gif'
		usr, boltAnim1,boltAnim2 = inputbox.ask_parallel(DISPLAY_SURF,"Guess Answer ?? :",road_val,13,path1,path2)
		carx = 310
		mincary = 180
		maxcary = 300
	elif road_val == 4:
		path1 = 'Images/game1/road/r4/tmp-'
		path2 = '.gif'
		usr, boltAnim1,boltAnim2 = inputbox.ask_parallel(DISPLAY_SURF,"Guess Answer ??:",road_val,20,path1,path2)
		carx = 280
		mincary = 180
		maxcary = 300
	else :
		path1 = 'Images/game1/road/r3/'
		path2 = '.gif'
		usr, boltAnim1,boltAnim2 = inputbox.ask_parallel(DISPLAY_SURF,"Guess Answer ?? :",road_val,13,path1,path2)
		carx = 280
		mincary = 170
		maxcary = 350
		
	return usr,car1,car2,boltAnim1,boltAnim2,carx,mincary,maxcary,scalex,scaley,scalew,scalez,multiplier_scale_big,multiplier_scale_small,sound_path
