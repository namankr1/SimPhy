import pygame
from pygame.locals import *
import sys
import time
from endScreen import endScreen
from game1_ending import game1_ending
import road_select
from const_colors import *
from constants import *


class anim1:
	def __init__(self,DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path):
		print ("INSIDE anim1.py")
		
		s_in =0
		s_f = displacement
		if s_f <=40:
			s_f = 40
		if s_f >= 100:
			s_f = 100
		
		DISPLAY_SURF = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT), 0, 32)
		pygame.display.set_caption('Animation')
		# create the animation objects   ('filename of image',    duration_in_seconds)
		
		usr_input,car_move_forward,car_move_backward,boltAnim1,boltAnim2,carx,mincary,maxcary,scalex,scaley,scalew,scalez,multiplier_scale_big,multiplier_scale_small,sound_path = road_select.select_items(DISPLAY_SURF)
		print ("INSIDE anim1.py")
		if pygame.mixer.music.get_busy():
			pygame.mixer.music.stop()
		pygame.mixer.music.load(sound_path)
		pygame.mixer.music.play(-1, 0.0)
		
		print ("INSIDE anim1.py")
		if initial_velocity > 0 :
			boltAnim = boltAnim1
			car = car_move_forward
		elif initial_velocity == 0 and displacement >= 0:
			boltAnim = boltAnim1
			car = car_move_forward
		else :
			boltAnim = boltAnim2
			car = car_move_backward
		print ("INSIDE anim1.py")
		if acceleration>0 and initial_velocity >=0:
			cary = 300
		elif acceleration==0 and initial_velocity >=0:
			cary = 320
		elif acceleration <0 and initial_velocity >=0:
			cary = 200
		elif acceleration>0 and initial_velocity<0:
			cary = 250
		elif acceleration ==0 and initial_velocity<0:
			cary = 130
		else :
			cary=130
		print ("INSIDE anim1.py")
		boltAnim.play();
		mainClock = pygame.time.Clock()
		BGCOLOR = (100, 50, 50)

		textpos = text.get_rect()
		textpos.centerx =300
		textpos.y = 10
		font = pygame.font.Font(None, 36)
		text_usr = font.render("You Guessed : "+str(usr_input), 1, WHITE)
		text_usrpos = text_usr.get_rect()
		text_usrpos.centerx = 300
		text_usrpos.y = 40
		DISPLAY_SURF.blit(text, textpos)
		DISPLAY_SURF.blit(text_usr,text_usrpos)
		Run = True
		noLoop = 40
		reverseTime = 60
		print ("INSIDE anim1.py")
		while Run:
		#windowSurface.fill(BGCOLOR)
			if initial_velocity > 0 and acceleration < 0:
				noLoop -= 1
			elif initial_velocity < 0 and acceleration > 0:
				noLoop -= 1
			else :
				noLoop+=1
				
			if noLoop < 0:
				while reverseTime>1:
					if pygame.mixer.music.get_busy():
						pygame.mixer.music.stop()
					reverseTime-=1
					image_reverse=pygame.image.load('Images/reverse_direction.jpg')
					DISPLAY_SURF.blit(image_reverse,SCREEN_TOPLEFT)
					pygame.display.update()
					mainClock.tick(30)
					s_in = 0
				if reverseTime == 1:
					pygame.mixer.music.load(sound_path)
					pygame.mixer.music.play(-1, 0.0)
					reverseTime-=1
				if acceleration > 0:
					boltAnim.pause();
					boltAnim = boltAnim1
					boltAnim.play();
					car = car_move_forward
				else:
					boltAnim.pause();
					boltAnim = boltAnim2
					boltAnim.play();
					car = car_move_backward

			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
				if event.type == KEYDOWN and event.key == K_ESCAPE:
				# press "Esc" key to stop looping
					if pygame.mixer.music.get_busy():
						pygame.mixer.music.stop()
					Run = False
					boltAnim.loop = False
			if s_in > s_f :
				if acceleration>=0 :
					cary -= 1
					scalex = multiplier_scale_small * scalex
					scaley = multiplier_scale_small* scaley
					if cary< (mincary):
						game1_ending(DISPLAY_SURF,"The block will move forever",path)
				elif acceleration < 0:
					cary += 1
					scalex = multiplier_scale_big * scalex
					scaley = multiplier_scale_big* scaley
					if cary > maxcary :
						game1_ending(DISPLAY_SURF,"The block will move forever",path) 
			else:
				s_in += 1
			boltAnim.blit(DISPLAY_SURF, (0, 0))
			carN = pygame.transform.scale(car,(int(scalex*car.get_width()),int(scaley*car.get_height())))
			DISPLAY_SURF.blit(carN,(carx,cary))
			DISPLAY_SURF.blit(text, textpos)
			DISPLAY_SURF.blit(text_usr,text_usrpos)
			pygame.display.update()
			mainClock.tick(30) # Feel free to experiment with any FPS setting.
		print ("exit from anim1.py")
	
