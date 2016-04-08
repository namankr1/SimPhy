# test1_pyganim.py - A very very very basic pyganim test program.
#
# This program just runs a single animation. It shows you what you need to do to use Pyganim. Basically:
#   1) Import the pyganim module
#   2) Create a pyganim.PygAnimation object, passing the constructor a list of image filenames and durations.
#   3) Call the play() method.
#   4) Call the blit() method.
#
# The animation images come from POW Studios, and are available under an Attribution-only license.
# Check them out, they're really nice.
# http://powstudios.com/

import pygame
from pygame.locals import *
import sys
import time
from endScreen import endScreen
import road_select

#def __init__(self,screen,direction,text):
# set up the window

class anim1:
	def __init__(self,screen,text,v,u,a,t,s):
		
		s_in =0
		s_f = s
		if s_f <=40:
			s_f = 40
		if s_f >= 100:
			s_f = 100
		screen = pygame.display.set_mode((600, 400), 0, 32)
		pygame.display.set_caption('Animation')
		# create the animation objects   ('filename of image',    duration_in_seconds)
		
		usr_input,car1,car2,boltAnim1,boltAnim2 = road_select.select_items(screen)
		if u > 0 :
			boltAnim = boltAnim1
			car = car1
		elif u==0 and s>=0:
			boltAnim = boltAnim1
			car = car1
		else :
			boltAnim = boltAnim2
			car = car2
			
		scalex = 0.999
		scaley = 0.999
		if a>0 and u >=0:
			cary=300
		elif a==0 and u >=0:
			cary=320
		elif a <0 and u >=0:
			cary = 200
		elif a>0 and u<0:
			cary = 200
		elif a ==0 and u<0:
			cary = 130
		else :
			cary=130
		
		boltAnim.play();
		mainClock = pygame.time.Clock()
		BGCOLOR = (100, 50, 50)

		textpos = text.get_rect()
		textpos.centerx =300
		textpos.y = 10
		font = pygame.font.Font(None, 36)
		text_usr = font.render("your input is "+str(usr_input), 1, (255, 255, 255))
		text_usrpos = text_usr.get_rect()
		text_usrpos.centerx =300
		text_usrpos.y = 40
		screen.blit(text, textpos)
		screen.blit(text_usr,text_usrpos)
		Run =True
		noLoop =40
		reverseTime=40
		while Run:
		#windowSurface.fill(BGCOLOR)
			if u > 0 and a < 0:
				noLoop -= 1
			elif u < 0 and a > 0:
				noLoop -= 1
			else :
				noLoop+=1
				
			if noLoop < 0:
				while reverseTime>0:
					reverseTime-=1
					image_reverse=pygame.image.load('Images/simphy.jpg')
					screen.blit(image_reverse,(0,0))
					pygame.display.update()
					mainClock.tick(30)
					s_in = 0

				if a > 0:
					boltAnim.pause();
					boltAnim = boltAnim1
					boltAnim.play();
					car = car1
				else:
					boltAnim.pause();
					boltAnim = boltAnim2
					boltAnim.play();
					car = car2

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN and event.key == K_ESCAPE:
				# press "Esc" key to stop looping
					Run = False
					boltAnim.loop = False
			if s_in > s_f :
				if a>=0 :
					cary -= 1
					scalex = 0.992 * scalex
					scaley = 0.992* scaley
					if cary < 150 :
						endScreen(screen,"The block will move forever")
				elif a < 0:
					cary += 1
					scalex = 1.004 * scalex
					scaley = 1.004* scaley
					if cary > 300 :
						endScreen(screen,"The block will move forever") 
			else:
				s_in += 1
			boltAnim.blit(screen, (0, 0))
			carN = pygame.transform.scale(car,(int(scalex*car.get_width()),int(scaley*car.get_height())))
			screen.blit(carN,(280,cary))
			screen.blit(text, textpos)
			screen.blit(text_usr,text_usrpos)
			pygame.display.update()
			mainClock.tick(30) # Feel free to experiment with any FPS setting.
		print ("exit from anim1.py")
	
