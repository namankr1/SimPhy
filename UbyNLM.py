import pygame
import sys
import inputbox
from Button import Button
from anim1 import *
import errorScreen
from pygame.locals import *
from const_colors import *
import math

def compUbyNLM(DISPLAY_SURF):
	btn_u1 = pygame.image.load('Images/buttons/parameters/u1.png') 	
	btn_u2 = pygame.image.load('Images/buttons/parameters/u2.png') 
	btn_u3 = pygame.image.load('Images/buttons/parameters/u3.png') 
	btn_u4 = pygame.image.load('Images/buttons/parameters/u4.png') 

	
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
				if rect_u1.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					final_velocity = inputbox.ask(DISPLAY_SURF, "Final Velocity, v",countInputs)
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
					initial_velocity = final_velocity - acceleration*time
					
					displacement = initial_velocity*time + acceleration*time*time/2
					font = pygame.font.Font(None, 36)
					text = font.render("The Initial Velocity hence calculated is "+ str(initial_velocity) +"metre/sec", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_U/G1/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif rect_u2.collidepoint(mouse):
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
					
					final_velocity = initial_velocity + acceleration*time
					font = pygame.font.Font(None, 36)
					text = font.render("The Initial Velocity hence calculated is "+ str(initial_velocity) +"metre/sec", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_U/G2/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif rect_u3.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					final_velocity = inputbox.ask(DISPLAY_SURF, "Final Velocity, v",countInputs)
					final_velocity = float (final_velocity)
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
					initial_velocity = 2*displacement/time - final_velocity
					acceleration = (final_velocity -initial_velocity)/time
					
					font = pygame.font.Font(None, 36)
					text = font.render("The Initial Velocity hence calculated is "+ str(initial_velocity) +"metre/sec", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_U/G3/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif rect_u4.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					final_velocity = inputbox.ask(DISPLAY_SURF, "Final Velocity, v",countInputs)
					final_velocity = float (final_velocity)
					countInputs = countInputs + 5;
					displacement = inputbox.ask(DISPLAY_SURF, "Displacement, s",countInputs)
					displacement = float (displacement)
					countInputs = countInputs + 5;
					acceleration = inputbox.ask(DISPLAY_SURF, "Acceleration, a",countInputs)
					acceleration = float (acceleration)
					initial_velocity = math.sqrt(final_velocity*final_velocity - 2*acceleration*displacement)
					
					if (acceleration == 0):
						time =0
					else :
						time = (final_velocity - initial_velocity)/acceleration
					if(time < 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Inconsistent data entered.(results to Negative time)")
						run = False
					font = pygame.font.Font(None, 36)
					text = font.render("The Initial Velocity hence calculated is "+ str(initial_velocity) +"metre/sec", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_U/G4/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif btn_back.obj.collidepoint(mouse):
					run = False

		rect_u1 = DISPLAY_SURF.blit(btn_u1,(125, 103))
		rect_u2 = DISPLAY_SURF.blit(btn_u2,(125, 153))
		rect_u3 = DISPLAY_SURF.blit(btn_u3,(125, 203))
		rect_u4 = DISPLAY_SURF.blit(btn_u4,(125, 253))
		
		btn_back.draw(DISPLAY_SURF,mouse,(550,10,45,20),(560,13))
		pygame.display.update()
		clock.tick(60)
	print ("exit from UbyNLM")
