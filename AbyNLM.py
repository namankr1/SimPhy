import pygame
import sys
import inputbox
from Button import Button
from anim1 import *
import errorScreen
from pygame.locals import *
from const_colors import *
import math

def compAbyNLM(DISPLAY_SURF):
	print ("INSIDE AbyNLM.py")

	btn_a1 = pygame.image.load('Images/buttons/parameters/a1.png') 	
	btn_a2 = pygame.image.load('Images/buttons/parameters/a2.png') 
	btn_a3 = pygame.image.load('Images/buttons/parameters/a3.png') 
	btn_a4 = pygame.image.load('Images/buttons/parameters/a4.png') 

	btn_back = Button('Back')
	btn_back.setColor(RED)
	btn_back.setHoverColor(LIME)
	btn_back.setFontColor(BLUE)
	clock = pygame.time.Clock()
	background=pygame.image.load('Images/game1/input_values.png')	
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
				if rect_a1.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					initial_velocity = inputbox.ask(DISPLAY_SURF, "Initial velocity, u",countInputs)
					initial_velocity = float (initial_velocity)
					countInputs = countInputs + 5;
					final_velocity = inputbox.ask(DISPLAY_SURF, "Final Velocity, v",countInputs)
					final_velocity = float (final_velocity)
					countInputs = countInputs + 5;
					time = inputbox.ask(DISPLAY_SURF, "Time, t",countInputs)
					time = float (time)
					if(time < 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Negative time entered")
						run = False
					if(time == 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Time cannot be zero in this case")
						run = False
					acceleration = (final_velocity - initial_velocity)/time
					displacement = initial_velocity*time+ acceleration*time*time/2
					
					font = pygame.font.Font(None, 36)
					text = font.render("Acceleration hence calculated is "+ str(acceleration) +"meter/sec/sec", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_A/G1/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif rect_a2.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					displacement = inputbox.ask(DISPLAY_SURF, "Displacement, s",countInputs)
					displacement = float (displacement)
					countInputs = countInputs + 5;
					final_velocity = inputbox.ask(DISPLAY_SURF, "Final Velocity, v",countInputs)
					final_velocity = float (final_velocity)
					countInputs = countInputs + 5;
					time = inputbox.ask(DISPLAY_SURF, "Time, t",countInputs)
					time = float (time)
					if(time < 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Negative time entered")
						run = False
					if(time == 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Time cannot be zero in this case")
						run = False
					acceleration = (final_velocity*time - displacement)*2/time/time
					
					initial_velocity = final_velocity - acceleration*time
					font = pygame.font.Font(None, 36)
					text = font.render("Acceleration hence calculated is "+ str(acceleration) +"meter/sec/sec", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_A/G2/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif rect_a3.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					initial_velocity = inputbox.ask(DISPLAY_SURF, "Initial velocity, u",countInputs)
					initial_velocity = float (initial_velocity)
					countInputs = countInputs + 5;
					displacement = inputbox.ask(DISPLAY_SURF, "Displacement, s",countInputs)
					displacement = float (displacement)
					countInputs = countInputs + 5;
					time = inputbox.ask(DISPLAY_SURF, "Time, t",countInputs)
					time = float (time)
					if(time < 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Negative time entered")
						run = False
					if(time == 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Time cannot be zero in this case")
						run = False
					acceleration = ((displacement-initial_velocity*time)/time/time)*2
					
					final_velocity = initial_velocity + acceleration*time
					font = pygame.font.Font(None, 36)
					text = font.render("Acceleration hence calculated is "+ str(acceleration) +"meter/sec/sec", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_A/G3/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif rect_a4.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					initial_velocity = inputbox.ask(DISPLAY_SURF, "Initial velocity, u",countInputs)
					initial_velocity = float (initial_velocity)
					countInputs = countInputs + 5;
					displacement = inputbox.ask(DISPLAY_SURF, "Displacement, s",countInputs)
					displacement = float (displacement)
					countInputs = countInputs + 5;
					final_velocity = inputbox.ask(DISPLAY_SURF, "Final Velocity, v",countInputs)
					final_velocity = float (final_velocity)
					if(displacement==0):
						errorScreen.errorScreen(DISPLAY_SURF,"Displacement cannot be zero in this case")
						run = False
					acceleration = (final_velocity*final_velocity - initial_velocity*initial_velocity )/2/displacement
					if (acceleration == 0):
						time =0
					else :
						time = (final_velocity - initial_velocity)/acceleration
					if(time < 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Inconsistent data entered.(results to Negative time)")
						run = False
					
					font = pygame.font.Font(None, 36)
					text = font.render("Acceleration hence calculated is "+ str(acceleration) +"meter/sec/sec", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_A/G4/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif btn_back.obj.collidepoint(mouse):
					run = False
		rect_a1 = DISPLAY_SURF.blit(btn_a1,(125, 103))
		rect_a2 = DISPLAY_SURF.blit(btn_a2,(125, 153))
		rect_a3 = DISPLAY_SURF.blit(btn_a3,(125, 203))
		rect_a4 = DISPLAY_SURF.blit(btn_a4,(125, 253))

		btn_back.draw(DISPLAY_SURF,mouse,(550,10,45,20),(560,13))
		pygame.display.update()
		clock.tick(60)
	print ("exit from AbyNLM")
