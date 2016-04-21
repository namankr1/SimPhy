import pygame
import sys
import inputbox
from Button import Button
from anim1 import *
import errorScreen
from pygame.locals import *
from const_colors import *
import math

def compVbyNLM(DISPLAY_SURF):
	btn_v1 = pygame.image.load('Images/buttons/parameters/v1.png') 	
	btn_v2 = pygame.image.load('Images/buttons/parameters/v2.png') 
	btn_v3 = pygame.image.load('Images/buttons/parameters/v3.png') 
	btn_v4 = pygame.image.load('Images/buttons/parameters/v4.png') 


	btn_back = Button('Back')
	btn_back.setColor(RED)
	btn_back.setHoverColor(LIME)
	btn_back.setFontColor(BLUE)
	clock = pygame.time.Clock()
	background=pygame.image.load('Images/game1/input_values.png')
	
	run = True
	Zero = 0
	while run:
		DISPLAY_SURF.blit(background,SCREEN_TOPLEFT)
		mouse = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
				pygame.quit()
				sys.exit()
			elif event.type == pygame.MOUSEBUTTONDOWN:
				if rect_v1.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					initial_velocity = inputbox.ask(DISPLAY_SURF, "Initial velocity, u",countInputs)
					initial_velocity = float (initial_velocity)
					countInputs = countInputs + 5;
					acceleration = inputbox.ask(DISPLAY_SURF, "Acceleration, a",countInputs)
					acceleration = float (acceleration)
					countInputs = countInputs + 5;
					time = inputbox.ask(DISPLAY_SURF, "Time, t",countInputs)
					time = float (time)
					if (time < 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Negative time entered")
						run = False
					final_velocity = initial_velocity + acceleration * time
					displacement = initial_velocity*time + acceleration*time*time/2
					final_velocity = str (final_velocity)
					font = pygame.font.Font(None, 36)
					text = font.render("The Final Velocity hence calculated is "+ str(final_velocity) +" metre/sec", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_V/G1/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False

				elif rect_v2.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					displacement = inputbox.ask(DISPLAY_SURF, "Displacement, s",countInputs)
					displacement = float (displacement)
					countInputs = countInputs + 5;
					acceleration = inputbox.ask(DISPLAY_SURF, "Acceleration, a",countInputs)
					acceleration = float (acceleration)
					countInputs = countInputs + 5;
					time = inputbox.ask(DISPLAY_SURF, "Time, t",countInputs)
					time = float (time)
					if(time < 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Negative time entered")
						run = False
					if(time == 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Time cannot be zero in this case")
						run = False
					initial_velocity = (displacement-acceleration*time*time/2)/time
					final_velocity = initial_velocity + acceleration * time
					final_velocity = str (final_velocity)
					font = pygame.font.Font(None, 36)
					text = font.render("The Final Velocity hence calculated is "+ str(final_velocity) +" metre/sec", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_V/G2/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif rect_v3.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					initial_velocity = inputbox.ask(DISPLAY_SURF, "Initial velocity, u",countInputs)
					initial_velocity = float (initial_velocity)
					countInputs = countInputs + 5;
					displacement = inputbox.ask(DISPLAY_SURF, "Displacement, s",countInputs)
					displacement = float (displacement)
					countInputs = countInputs + 5;
					time = inputbox.ask(DISPLAY_SURF, "Time, t",countInputs)
					time = float (time)
					print ("abcddfghj")
					if(time < 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Negative time entered")
						run = False
					if(time == 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Time cannot be zero in this case")
						run = False
					acceleration = ((displacement-initial_velocity*time)/time/time)*2
					print ("abcddfasdfghghj")
					final_velocity = initial_velocity + acceleration * time
					final_velocity = str (final_velocity)
					font = pygame.font.Font(None, 36)
					text = font.render("The Final Velocity hence calculated is "+ str(final_velocity) +" metre/sec", 1, WHITE)
					print ("abcddfghsdfghjdfghjkdfghjkj")
					path = "Images/game1/Explanation/Calculate_V/G3/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif rect_v4.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					initial_velocity = inputbox.ask(DISPLAY_SURF, "Initial velocity, u",countInputs)
					initial_velocity = float (initial_velocity)
					countInputs = countInputs + 5;
					displacement = inputbox.ask(DISPLAY_SURF, "Displacement, s",countInputs)
					displacement = float (displacement)
					countInputs = countInputs + 5;
					acceleration = inputbox.ask(DISPLAY_SURF, "Acceleration, a",countInputs)
					acceleration = float (acceleration)
					final_velocity = math.sqrt(initial_velocity*initial_velocity + 2*acceleration*displacement)
					final_velocity = str (final_velocity)
					if (acceleration == 0):
						time =0
					else :
						time = (final_velocity - initial_velocity)/acceleration
					if(time < 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Inconsistent data entered.(results to Negative time)")
						run = False
					font = pygame.font.Font(None, 36)
					text = font.render("The Final Velocity hence calculated is "+ str(final_velocity) +" metre/sec", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_V/G4/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif btn_back.obj.collidepoint(mouse):
					run = False


		rect_v1 = DISPLAY_SURF.blit(btn_v1,(125, 103))
		rect_v2 = DISPLAY_SURF.blit(btn_v2,(125, 153))
		rect_v3 = DISPLAY_SURF.blit(btn_v3,(125, 203))
		rect_v4 = DISPLAY_SURF.blit(btn_v4,(125, 253))
		
		btn_back.draw(DISPLAY_SURF,mouse,(550,10,45,20),(560,13))
		pygame.display.update()
		clock.tick(60)
	print ("exit from VbyNLM")
