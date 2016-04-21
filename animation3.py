import pygame
import sys
from game3_ending import game3_ending
from pygame.locals import *

class animation3:
	def __init__(self,screen,direction,text,u1_,u2_,v1_,v2_):
		FPS = 30
		fpsClock = pygame.time.Clock()
		SCREEN_WIDTH = 600
		screen = pygame.display.set_mode((SCREEN_WIDTH,400), 0, 32)
		pygame.display.set_caption('Animation')
		WHITE = (255, 255, 255)
		RED = (255,0,0)
		background = pygame.image.load('Images/background.png')
		screen.blit(background,(0,0))
		objAImg = pygame.image.load('Images/game3/A.png')
		objBImg = pygame.image.load('Images/game3/B.png')
		fontObj = pygame.font.Font(None,16)
		objAImgx = 150
		objAImgy = 240
		objBImgx = 350
		objBImgy = 240
		Run1= True
		temp=1
		#case= 0
		font = pygame.font.SysFont("monospace", 15)
		#font = pygame.font.Font(None, 20)	
		texta = font.render("Final Velocity of A ="+str(v1_)+"m/sec. Final Velocity of B ="+str(v2_)+"m/sec", 1, (10, 10, 10)) 				
		textposa = texta.get_rect()
		textposa.centerx = background.get_rect().centerx
		textposa.y = 350				
		textb = font.render("The blocks wont collide !", 1, (10, 10, 10))
		textposb = textb.get_rect()
		textposb.centerx = background.get_rect().centerx
		textposb.y = 350
		noloop2 = False
			
		while Run1 :			#main game loop
			screen.blit(background,(0,0))
			
			if u1_ > 0:
				if u2_ == 0:
					#case =1
					background.blit(texta, textposa)
				
					if objAImgx <290 :
						objAImgx += 3
				
					if objAImgx >= 290:
						Run1= False

				elif u2_ < 0:
					#case = 2
					background.blit(texta, textposa)

					if objAImgx >= objBImgx:
						Run1= False

					else :
						objAImgx += 3
						objBImgx -= 3

				else :
		
					if u2_ <u1_:
						objAImgx += 4
						objBImgx += 2
						#case = 3
						background.blit(texta, textposa)

					if objAImgx >= (objBImgx-60):
						Run1= False
						background.blit(texta, textposa)
								
					if (u2_ > u1_) :
						#case = 4
						objAImgx += 2
						objBImgx += 4
						background.blit(textb, textposb)
					
					if (u2_ == u1_) :
						#case = 5
						objAImgx += 3
						objBImgx += 3
						background.blit(textb, textposb)

					if objAImgx >= 620:
						game3_ending(screen,"The blocks wont collide !")

			elif u1_ == 0:
				
				if u2_ == 0:
					#case = 6
					background.blit(textb, textposb)
					pygame.display.update()
					fpsClock.tick(FPS)
					Run1 = False
					noloop2 = True
				
				if u2_ > 0:
					#case = 7
					background.blit(textb, textposb)
					objBImgx += 3

				if objBImgx >= 620:
					game3_ending(screen,"The blocks wont collide !")

				if u2_ < 0:
					#case = 8
					background.blit(texta, textposa)
					
					if objAImgx >= (objBImgx-60):
						Run1= False

					else :
						objBImgx -= 3

			else :
						
				if u2_ > 0 :
					#case =9
					background.blit(textb, textposb)
					objAImgx -= 3
					objBImgx += 3
				if objBImgx >= 620:
					game3_ending(screen,"The blocks wont collide !")
										
				if u2_ == 0:
					#case = 10
					background.blit(textb, textposb)
					objAImgx -= 3
				if objAImgx < 0:
					game3_ending(screen,"The blocks wont collide !")
								
				if u2_<0 :
					if u2_ <u1_:
						objAImgx -= 2
						objBImgx -= 4
						#case = 11
						background.blit(texta, textposa)

					if objAImgx >= (objBImgx-60):
						Run1= False		
						background.blit(texta, textposa)
			
					if (u2_ >u1_) :
						#case = 12
						objAImgx -= 4
						objBImgx -= 2
						background.blit(textb, textposb)
					if objBImgx < 0:
						game3_ending(screen,"The blocks wont collide !")
					
					if (u2_ ==u1_) :
						#case = 13
						objAImgx -= 3
						objBImgx -= 3
						background.blit(textb, textposb)
					if objBImgx < 0:
						game3_ending(screen,"The blocks wont collide !")
								
			screen.blit(objAImg, (objAImgx,objAImgy))
			screen.blit(objBImg, (objBImgx,objBImgy))
					
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()

			pygame.display.update()
			fpsClock.tick(FPS)
		if noloop2 :
			screen.blit(textb, textposb)
			pygame.display.update()
			fpsClock.tick(FPS)
			game3_ending(screen,"The blocks wont collide !")
		Run2= True
		collison = pygame.image.load('Images/game3/collison.jpg')
		screen.blit(collison,(0,0))
		pygame.display.update()
		fpsClock.tick(FPS)
		pygame.time.wait(3000)
		objAImgx = 200
		objAImgy = 240
		objBImgx = 260
		objBImgy = 240
		screen.blit(background,(0,0))
		screen.blit(objAImg, (objAImgx,objAImgy))
		screen.blit(objBImg, (objBImgx,objBImgy))
		pygame.display.update()
		fpsClock.tick(FPS)
		while Run2:
			screen.blit(background,(0,0))
			
			if v1_ >0 and v2_ > 0 :
				if v1_ > v2_ :
					objAImgx += 4
					objBImgx += 2					

				elif v1_ == v2_ :
					objAImgx += 3
					objBImgx += 3
		
				elif v1_ < v2_ :
					objAImgx += 2
					objBImgx += 4

			elif v2_ > 0 and v1_ ==0:
				objBImgx += 3

			elif v2_ > 0 and v1_ <0:
				objAImgx -= 3
				objBImgx += 3

			elif v2_ == 0 and v1_ >0:
				objAImgx += 3				

		

			elif v2_ == 0 and v1_ <0:
				objAImgx -= 3
		
			elif v2_ < 0 and v1_ ==0:
				objBImgx -= 3

			elif v2_ < 0 and v1_ >0:
				objAImgx += 3
				objBImgx -= 3

			elif v2_ < 0 and v1_ <0:
				if v1_ > v2_ :
					objAImgx -= 2
					objBImgx -= 4
				
				elif v1_ == v2_ :
					objAImgx -= 3
					objBImgx -= 3
				
				elif v1_ < v2_ :
					objAImgx -= 4
					objBImgx -= 2

			
			else :
				Run2 = False
				
			if objAImgx < 0 or objAImgx > 600 :
				Run2 = False
			if objBImgx <0 or objBImgx > 600 :
				Run2 = False

			screen.blit(objAImg, (objAImgx,objAImgy))
			screen.blit(objBImg, (objBImgx,objBImgy))
			
			for event in pygame.event.get():
				if event.type == QUIT:
					pygame.quit()
					sys.exit()
			pygame.display.update()
			fpsClock.tick(FPS)

		game3_ending(screen,"The blocks wont collide !")

