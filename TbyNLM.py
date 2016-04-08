import pygame
import sys
import inputbox
from Button import Button
from anim1 import *
from errorScreen import errorScreen
from pygame.locals import *
import math

def compTbyNLM(DISPLAYSURF):
	btn1 = Button('T by v,a,u')
	btn2 = Button('T by s,a,u')
	btn3 = Button('T by v,s,u')
	btn4 = Button('T by v,a,s')
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
					v1 = inputbox.ask(DISPLAYSURF, "Final Velocity, v",countInputs)
					v2 = float (v1)
					countInputs=countInputs+5;
					a1 = inputbox.ask(DISPLAYSURF, "Acceleration, a",countInputs)
					a2 = float (a1)
					countInputs=countInputs+5;
					u1 = inputbox.ask(DISPLAYSURF, "Initial Velocity, u",countInputs)			
					u2 = float (u1)
					if(a2==0):
						errorScreen(DISPLAYSURF,"Acceleration cannot be zero in this case")
						run = False
					t1 = (v2 -u2)/a2
					if(t1<0):
						errorScreen(DISPLAYSURF,"Inconsistent data entered.(results to Negative time)")
						run = False
					s1 = u2*t1 + a2*t1*t1/2
					t2 = str (t1)
					font = pygame.font.Font(None, 36)
					text = font.render("The Time hence calculated is "+t2+" sec", 1, (255, 255, 255))
					anim1(DISPLAYSURF,text,v2,u2,a2,t1,s1)
					run = False
				elif btn2.obj.collidepoint(mouse):
					countInputs=1;	# countInputs is related to the y coordinate of the input text boxes
					u1 = inputbox.ask(DISPLAYSURF, "Initial Velocity, u",countInputs)
					u2 = float (u1)
					countInputs=countInputs+5;
					s1 = inputbox.ask(DISPLAYSURF, "Displacement, s",countInputs)
					s2 = float (s1)
					countInputs=countInputs+5;
					a1 = inputbox.ask(DISPLAYSURF, "Acceleration, a",countInputs)
					a2 = float (a1)
					try :
						v1 = math.sqrt(u2*u2 + 2*a2*s2)
					except :
						errorScreen(DISPLAYSURF,"Inconsistent data")
					if(a2==0):
						if (u2 == 0):
							errorScreen(DISPLAYSURF,"Inconsistent data")
							run = False
						else :
							t1 = s2/u2
					else :
						t1 = (v1 - u2)/a2
					if(t1<0):
						errorScreen(DISPLAYSURF,"Inconsistent data entered.(results to Negative time)")
						run = False
					t2 = str (t1)
					font = pygame.font.Font(None, 36)
					text = font.render("The Time hence calculated is "+t2+" sec", 1, (255, 255, 255))
					anim1(DISPLAYSURF,text,v1,u2,a2,t1,s2)
					run = False
				elif btn3.obj.collidepoint(mouse):
					countInputs=1;	# countInputs is related to the y coordinate of the input text boxes
					u1 = inputbox.ask(DISPLAYSURF, "Initiual Velocity, u",countInputs)
					u2 = float (u1)
					countInputs=countInputs+5;
					s1 = inputbox.ask(DISPLAYSURF, "Displacement, s",countInputs)
					s2 = float (s1)
					countInputs=countInputs+5;
					v1 = inputbox.ask(DISPLAYSURF, "Final Velocity, v",countInputs)
					v2 = float (v1)
					if(s2==0):
						a1 = 0
						t1 = 0
					else :
						a1 = (v2*v2 - u2*u2)/2/s2
						if(a1==0):
							errorScreen(DISPLAYSURF,"Inconsistent data entered.(results to zero acceleration)")
							run = False
						t1 = (v2 - u2)/a1
						if(t1<0):
							errorScreen(DISPLAYSURF,"Inconsistent data entered.(results to Negative time)")
							run = False
					t2 = str (t1)
					font = pygame.font.Font(None, 36)
					text = font.render("The Time hence calculated is "+t2+" sec", 1, (255, 255, 255))
					anim1(DISPLAYSURF,text,v2,u2,a1,t1,s2)
					run = False
				elif btn4.obj.collidepoint(mouse):
					countInputs=1;	# countInputs is related to the y coordinate of the input text boxes
					v1 = inputbox.ask(DISPLAYSURF, "Final Velocity, v",countInputs)
					v2 = float (v1)
					countInputs=countInputs+5;
					s1 = inputbox.ask(DISPLAYSURF, "Displacement, s",countInputs)
					s2 = float (s1)
					countInputs=countInputs+5;
					a1 = inputbox.ask(DISPLAYSURF, "Acceleration, a",countInputs)
					a2 = float (a1)
					u1 = math.sqrt(v2*v2 - 2*a2*s2)
					if(a2==0):
						if (v2 == 0):
							errorScreen(DISPLAYSURF,"Inconsistent data")
							run = False
						else :
							t1 = s2/v2
					else :
						t1 = (v1 - u2)/a2
					if(t1<0):
						errorScreen(DISPLAYSURF,"Inconsistent data entered.(results to Negative time)")
						run = False
					t2 = str (t1)
					font = pygame.font.Font(None, 36)
					text = font.render("The Time hence calculated is "+t2+" sec", 1, (255, 255, 255))
					anim1(DISPLAYSURF,text,v2,u1,a2,t1,s2)
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
	print ("Exit from TbyNLM")
	
