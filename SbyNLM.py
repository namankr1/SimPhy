import pygame
import sys
import inputbox
from Button import Button
from anim1 import *
import errorScreen
from pygame.locals import *
from const_colors import *
import math

def compSbyNLM(DISPLAY_SURF):
	print ("INSIDE SbyNLM.py")

	btn_s1 = pygame.image.load('Images/buttons/parameters/s1.png') 	
	btn_s2 = pygame.image.load('Images/buttons/parameters/s2.png') 
	btn_s3 = pygame.image.load('Images/buttons/parameters/s3.png') 
	btn_s4 = pygame.image.load('Images/buttons/parameters/s4.png') 

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
				if rect_s1.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					initial_velocity = inputbox.ask(DISPLAY_SURF, "Initial velocity, u",countInputs)
					initial_velocity = float (initial_velocity)
					countInputs = countInputs + 5;
					acceleration = inputbox.ask(DISPLAY_SURF, "Acceleration, a",countInputs)
					acceleration = float (acceleration)
					countInputs = countInputs + 5;
					time = inputbox.ask(DISPLAY_SURF, "Time, t",countInputs)
					time = float (time)
					if(time < 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Negative time entered")
						run = False
					displacement = initial_velocity*time + acceleration * time*time/2
					final_velocity = initial_velocity + acceleration*time
					
					font = pygame.font.Font(None, 36)
					text = font.render("The Displacement hence calculated is "+ str(displacement) +"metre", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_S/G1/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif rect_s2.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					final_velocity = inputbox.ask(DISPLAY_SURF, "Final velocity, v",countInputs)
					final_velocity = float (final_velocity)
					countInputs = countInputs + 5;
					acceleration = inputbox.ask(DISPLAY_SURF, "Acceleration, a",countInputs)
					acceleration = float (acceleration)
					countInputs = countInputs + 5;
					time = inputbox.ask(DISPLAY_SURF, "Time, t",countInputs)
					time = float (time)
					if(time < 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Negative time entered")
						run = False
					displacement = final_velocity*time - acceleration * time*time/2
					initial_velocity = final_velocity - acceleration*time
					
					font = pygame.font.Font(None, 36)
					text = font.render("The Displacement hence calculated is "+ str(displacement) +"metre", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_S/G2/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif rect_s3.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					initial_velocity = inputbox.ask(DISPLAY_SURF, "Initial velocity, u",countInputs)
					initial_velocity = float (initial_velocity)
					countInputs = countInputs + 5;
					final_velocity = inputbox.ask(DISPLAY_SURF, "Final velocity, v",countInputs)
					final_velocity = float (final_velocity)
					countInputs = countInputs + 5;
					time = inputbox.ask(DISPLAY_SURF, "Time, t",countInputs)
					time = float (time)
					if(time < 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Negative time entered")
						run = False
					if(time == 0):
						displacement = 0
						acceleration = 0
					else:
						acceleration = (final_velocity - initial_velocity)/time
						if(acceleration == 0):
							displacement = initial_velocity*time
						else :
							displacement = (final_velocity*final_velocity - initial_velocity*initial_velocity)/2/acceleration
					
					font = pygame.font.Font(None, 36)
					text = font.render("The Displacement hence calculated is "+ str(displacement) +"metre", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_S/G3/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif rect_s4.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					initial_velocity = inputbox.ask(DISPLAY_SURF, "Initial velocity, u",countInputs)
					initial_velocity = float (initial_velocity)
					countInputs = countInputs + 5;
					final_velocity = inputbox.ask(DISPLAY_SURF, "Final Velocity, v",countInputs)
					final_velocity = float (final_velocity)
					countInputs = countInputs + 5;
					acceleration = inputbox.ask(DISPLAY_SURF, "Acceleration, a",countInputs)
					acceleration = float (acceleration)
					if (acceleration == 0):
						displacement = 0
						time = 0
					else:
						displacement = (final_velocity*final_velocity - initial_velocity*initial_velocity)/2/acceleration
						time = (final_velocity - initial_velocity)/acceleration
						if(time < 0):
							errorScreen.errorScreen(DISPLAY_SURF,"Inconsistent data entered.(results to Negative time)")
							run = False
					
					font = pygame.font.Font(None, 36)
					text = font.render("The Displacement hence calculated is "+ str(displacement) +"metre", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_S/G4/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif btn_back.obj.collidepoint(mouse):
					run = False
		rect_s1 = DISPLAY_SURF.blit(btn_s1,(125, 103))
		rect_s2 = DISPLAY_SURF.blit(btn_s2,(125, 153))
		rect_s3 = DISPLAY_SURF.blit(btn_s3,(125, 203))
		rect_s4 = DISPLAY_SURF.blit(btn_s4,(125, 253))

		btn_back.draw(DISPLAY_SURF,mouse,(550,10,45,20),(560,13))
		pygame.display.update()
		clock.tick(60)
	print ("Exit from SbyNLM")
