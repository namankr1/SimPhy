import pygame
import sys
import inputbox
from Button import Button
from anim1 import *
from errorScreen import errorScreen
from pygame.locals import *
import math

def compVbyNLM(DISPLAYSURF):
	btn1 = Button('V by u,a,t')
	btn2 = Button('V by s,a,t')
	btn3 = Button('V by u,s,t')
	btn4 = Button('V by u,a,s')
	btn_back = Button('Back')
	btn_back.setColor((255,0,0))
	btn_back.setHoverColor((0,255,0))
	btn_back.setFontColor((0,0,255))
	clock = pygame.time.Clock()
	background=pygame.image.load('Images/game1.jpg')
	
	run = True
	Zero = 0
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
					if (t2<0):
						errorScreen(DISPLAYSURF,"Negative time entered")
						run = False
					v1 = u2 + a2 * t2
					s1 = u2*t2 + a2*t2*t2/2
					v2 = str (v1)
					font = pygame.font.Font(None, 36)
					text = font.render("The Final Velocity hence calculated is "+v2+" metre/sec", 1, (255, 255, 255))
					anim1(DISPLAYSURF,text,v1,u2,a2,t2,s1)
					run = False

				elif btn2.obj.collidepoint(mouse):
					countInputs=1;	# countInputs is related to the y coordinate of the input text boxes
					s1 = inputbox.ask(DISPLAYSURF, "Displacement, s",countInputs)
					s2 = float (s1)
					countInputs=countInputs+5;
					a1 = inputbox.ask(DISPLAYSURF, "Acceleration, a",countInputs)
					a2 = float (a1)
					countInputs=countInputs+5;
					t1 = inputbox.ask(DISPLAYSURF, "Time, t",countInputs)
					t2 = float (t1)
					if(t2<0):
						errorScreen(DISPLAYSURF,"Negative time entered")
						run = False
					if(t2==0):
						errorScreen(DISPLAYSURF,"Time cannot be zero in this case")
						run = False
					u1 = (s2-a2*t2*t2/2)/t2
					v1 = u1 + a2 * t2
					v2 = str (v1)
					font = pygame.font.Font(None, 36)
					text = font.render("The Final Velocity hence calculated is "+v2+" metre/sec", 1, (255, 255, 255))
					anim1(DISPLAYSURF,text,v1,u1,a2,t2,s2)
					run = False
				elif btn3.obj.collidepoint(mouse):
					countInputs=1;	# countInputs is related to the y coordinate of the input text boxes
					u1 = inputbox.ask(DISPLAYSURF, "Initial velocity, u",countInputs)
					u2 = float (u1)
					countInputs=countInputs+5;
					s1 = inputbox.ask(DISPLAYSURF, "Displacement, s",countInputs)
					s2 = float (s1)
					countInputs=countInputs+5;
					t1 = inputbox.ask(DISPLAYSURF, "Time, t",countInputs)
					t2 = float (t1)
					print ("abcddfghj")
					if(t2<0):
						errorScreen(DISPLAYSURF,"Negative time entered")
						run = False
					if(t2==0):
						errorScreen(DISPLAYSURF,"Time cannot be zero in this case")
						run = False
					a1 = ((s2-u2*t2)/t2/t2)*2
					print ("abcddfasdfghghj")
					v1 = u2 + a1 * t2
					v2 = str (v1)
					font = pygame.font.Font(None, 36)
					text = font.render("The Final Velocity hence calculated is "+v2+" metre/sec", 1, (255, 255, 255))
					print ("abcddfghsdfghjdfghjkdfghjkj")
					anim1(DISPLAYSURF,text,v1,u2,a1,t2,s2)
					run = False
				elif btn4.obj.collidepoint(mouse):
					countInputs=1;	# countInputs is related to the y coordinate of the input text boxes
					u1 = inputbox.ask(DISPLAYSURF, "Initial velocity, u",countInputs)
					u2 = float (u1)
					countInputs=countInputs+5;
					s1 = inputbox.ask(DISPLAYSURF, "Displacement, s",countInputs)
					s2 = float (s1)
					countInputs=countInputs+5;
					a1 = inputbox.ask(DISPLAYSURF, "Acceleration, a",countInputs)
					a2 = float (a1)
					v1 = math.sqrt(u2*u2 + 2*a2*s2)
					v2 = str (v1)
					if (a2 == 0):
						t1 =0
					else :
						t1 = (v1 - u2)/a2
					if(t1<0):
						errorScreen(DISPLAYSURF,"Inconsistent data entered.(results to Negative time)")
						run = False
					font = pygame.font.Font(None, 36)
					text = font.render("The Final Velocity hence calculated is "+v2+" metre/sec", 1, (255, 255, 255))
					anim1(DISPLAYSURF,text,v1,u2,a2,t1,s2)
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
	print ("exit from VbyNLM")
