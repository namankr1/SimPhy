import pygame
import sys
import inputbox
from Button import Button
from anim1 import *
from errorScreen import errorScreen
from pygame.locals import *
import math

def compSbyNLM(DISPLAYSURF):
	btn1 = Button('S by u,a,t')
	btn2 = Button('S by v,a,t')
	btn3 = Button('S by u,v,t')
	btn4 = Button('S by u,a,v')
	btn_back = Button('Back')
	btn_back.setColor((255,0,0))
	btn_back.setHoverColor((0,255,0))
	btn_back.setFontColor((0,0,255))
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
				if btn1.obj.collidepoint(mouse):
					countInputs=1;	# countInputs is related to the y coordinate of the input text boxes
					u1 = inputbox.ask(DISPLAYSURF, "Initial velocity, u",countInputs)
					u2 = float (u1)
					countInputs=countInputs+5;
					a1 = inputbox.ask(DISPLAYSURF, "Acceleration, a",countInputs)
					a2 = float (a1)
					countInputs=countInputs+5;
					t1 = inputbox.ask(DISPLAYSURF, "Time, t",countInputs)
					t2 = float (t1)
					if(t2<0):
						errorScreen(DISPLAYSURF,"Negative time entered")
						run = False
					s1 = u2*t2 + a2 * t2*t2/2
					v1 = u2 + a2*t2
					s2 = str (s1)
					font = pygame.font.Font(None, 36)
					text = font.render("The Displacement hence calculated is "+s2+"metre", 1, (255, 255, 255))
					anim1(DISPLAYSURF,text,v1,u2,a2,t2,s1)
					run = False
				elif btn2.obj.collidepoint(mouse):
					countInputs=1;	# countInputs is related to the y coordinate of the input text boxes
					v1 = inputbox.ask(DISPLAYSURF, "Final velocity, v",countInputs)
					v2 = float (v1)
					countInputs=countInputs+5;
					a1 = inputbox.ask(DISPLAYSURF, "Acceleration, a",countInputs)
					a2 = float (a1)
					countInputs=countInputs+5;
					t1 = inputbox.ask(DISPLAYSURF, "Time, t",countInputs)
					t2 = float (t1)
					if(t2<0):
						errorScreen(DISPLAYSURF,"Negative time entered")
						run = False
					s1 = v2*t2 - a2 * t2*t2/2
					u1 = v2 - a2*t2
					s2 = str (s1)
					font = pygame.font.Font(None, 36)
					text = font.render("The Displacement hence calculated is "+s2+"metre", 1, (255, 255, 255))
					anim1(DISPLAYSURF,text,v2,u1,a2,t2,s1)
					run = False
				elif btn3.obj.collidepoint(mouse):
					countInputs=1;	# countInputs is related to the y coordinate of the input text boxes
					u1 = inputbox.ask(DISPLAYSURF, "Initial velocity, u",countInputs)
					u2 = float (u1)
					countInputs=countInputs+5;
					v1 = inputbox.ask(DISPLAYSURF, "Final velocity, v",countInputs)
					v2 = float (v1)
					countInputs=countInputs+5;
					t1 = inputbox.ask(DISPLAYSURF, "Time, t",countInputs)
					t2 = float (t1)
					if(t2<0):
						errorScreen(DISPLAYSURF,"Negative time entered")
						run = False
					if(t2==0):
						s1 = 0
						a1 = 0
					else:
						a1 = (v2 - u2)/t2
						if(a1==0):
							s1 = u2*t2
						else :
							s1 = (v2*v2 - u2*u2)/2/a1
					s2 = str (s1)
					font = pygame.font.Font(None, 36)
					text = font.render("The Displacement hence calculated is "+s2+"metre", 1, (255, 255, 255))
					anim1(DISPLAYSURF,text,v2,u2,a1,t2,s1)
					run = False
				elif btn4.obj.collidepoint(mouse):
					countInputs=1;	# countInputs is related to the y coordinate of the input text boxes
					u1 = inputbox.ask(DISPLAYSURF, "Initial velocity, u",countInputs)
					u2 = float (u1)
					countInputs=countInputs+5;
					v1 = inputbox.ask(DISPLAYSURF, "Final Velocity, v",countInputs)
					v2 = float (v1)
					countInputs=countInputs+5;
					a1 = inputbox.ask(DISPLAYSURF, "Acceleration, a",countInputs)
					a2 = float (a1)
					if (a2==0):
						s1 = 0
						t1 = 0
					else:
						s1 = (v2*v2 - u2*u2)/2/a2
						t1 = (v2 - u2)/a2
						if(t1<0):
							errorScreen(DISPLAYSURF,"Inconsistent data entered.(results to Negative time)")
							run = False
					s2 = str (s1)
					font = pygame.font.Font(None, 36)
					text = font.render("The Displacement hence calculated is "+s2+"metre", 1, (255, 255, 255))
					anim1(DISPLAYSURF,text,v2,u2,a2,t1,s1)
					run = False
				elif btn_back.obj.collidepoint(mouse):
					run = False
		btn1.draw(DISPLAYSURF, mouse, (100,100,100,20), (125,103))
		btn2.draw(DISPLAYSURF, mouse, (100,130,100,20), (125,133))
		btn3.draw(DISPLAYSURF, mouse, (100,160,100,20), (125,163))
		btn4.draw(DISPLAYSURF, mouse, (100,190,100,20), (125,193))
		btn_back.draw(DISPLAYSURF,mouse,(550,10,45,20),(560,13))
		pygame.display.update()
		clock.tick(60)
	print ("Exit from SbyNLM")
