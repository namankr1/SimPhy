import pygame
import sys
import inputbox
from Button import Button
from anim1 import *
import errorScreen
from pygame.locals import *
from const_colors import *
import math

def compTbyNLM(DISPLAY_SURF):

	btn_t1 = pygame.image.load('Images/buttons/parameters/t1.png') 	
	btn_t2 = pygame.image.load('Images/buttons/parameters/t2.png') 
	btn_t3 = pygame.image.load('Images/buttons/parameters/t3.png') 
	btn_t4 = pygame.image.load('Images/buttons/parameters/t4.png') 

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
				if rect_t1.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					final_velocity = inputbox.ask(DISPLAY_SURF, "Final Velocity, v",countInputs)
					final_velocity = float (final_velocity)
					countInputs = countInputs + 5;
					acceleration = inputbox.ask(DISPLAY_SURF, "Acceleration, a",countInputs)
					acceleration = float (acceleration)
					countInputs = countInputs + 5;
					initial_velocity = inputbox.ask(DISPLAY_SURF, "Initial Velocity, u",countInputs)			
					initial_velocity = float (initial_velocity)
					if(acceleration==0):
						errorScreen.errorScreen(DISPLAY_SURF,"Acceleration cannot be zero in this case")
						run = False
					time = (final_velocity -initial_velocity)/acceleration
					if(time < 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Inconsistent data entered.(results to Negative time)")
						run = False
					displacement = initial_velocity*time + acceleration*time*time/2
					
					font = pygame.font.Font(None, 36)
					text = font.render("The Time hence calculated is "+ str(time) +" sec", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_T/G1/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif rect_t2.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					initial_velocity = inputbox.ask(DISPLAY_SURF, "Initial Velocity, u",countInputs)
					initial_velocity = float (initial_velocity)
					countInputs = countInputs + 5;
					displacement = inputbox.ask(DISPLAY_SURF, "Displacement, s",countInputs)
					displacement = float (displacement)
					countInputs = countInputs + 5;
					acceleration = inputbox.ask(DISPLAY_SURF, "Acceleration, a",countInputs)
					acceleration = float (acceleration)
					try :
						final_velocity = math.sqrt(initial_velocity*initial_velocity + 2*acceleration*displacement)
					except :
						errorScreen.errorScreen(DISPLAY_SURF,"Inconsistent data")
					if(acceleration==0):
						if (initial_velocity == 0):
							errorScreen.errorScreen(DISPLAY_SURF,"Inconsistent data")
							run = False
						else :
							time = displacement/initial_velocity
					else :
						time = (final_velocity - initial_velocity)/acceleration
					if(time < 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Inconsistent data entered.(results to Negative time)")
						run = False
					
					font = pygame.font.Font(None, 36)
					text = font.render("The Time hence calculated is "+ str(time) +" sec", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_T/G2/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif rect_t3.collidepoint(mouse):
					countInputs = 1;	# countInputs is related to the y coordinate of the input text boxes
					initial_velocity = inputbox.ask(DISPLAY_SURF, "Initiual Velocity, u",countInputs)
					initial_velocity = float (initial_velocity)
					countInputs = countInputs + 5;
					displacement = inputbox.ask(DISPLAY_SURF, "Displacement, s",countInputs)
					displacement = float (displacement)
					countInputs = countInputs + 5;
					final_velocity = inputbox.ask(DISPLAY_SURF, "Final Velocity, v",countInputs)
					final_velocity = float (final_velocity)
					if(displacement==0):
						acceleration = 0
						time = 0
					else :
						acceleration = (final_velocity*final_velocity - initial_velocity*initial_velocity)/2/displacement
						if(acceleration==0):
							errorScreen.errorScreen(DISPLAY_SURF,"Inconsistent data entered.(results to zero acceleration)")
							run = False
						time = (final_velocity - initial_velocity)/acceleration
						if(time < 0):
							errorScreen.errorScreen(DISPLAY_SURF,"Inconsistent data entered.(results to Negative time)")
							run = False
					
					font = pygame.font.Font(None, 36)
					text = font.render("The Time hence calculated is "+ str(time) +" sec", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_T/G3/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif rect_t4.collidepoint(mouse):
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
					if(acceleration==0):
						if (final_velocity == 0):
							errorScreen.errorScreen(DISPLAY_SURF,"Inconsistent data")
							run = False
						else :
							time = displacement/final_velocity
					else :
						time = (final_velocity - initial_velocity)/acceleration
					if(time < 0):
						errorScreen.errorScreen(DISPLAY_SURF,"Inconsistent data entered.(results to Negative time)")
						run = False
					
					font = pygame.font.Font(None, 36)
					text = font.render("The Time hence calculated is "+ str(time) +" sec", 1, WHITE)
					path = "Images/game1/Explanation/Calculate_T/G4/"
					anim1(DISPLAY_SURF,text,final_velocity,initial_velocity,acceleration,time,displacement,path)
					run = False
				elif btn_back.obj.collidepoint(mouse):
					run = False

		rect_t1 = DISPLAY_SURF.blit(btn_t1,(125, 103))
		rect_t2 = DISPLAY_SURF.blit(btn_t2,(125, 153))
		rect_t3 = DISPLAY_SURF.blit(btn_t3,(125, 203))
		rect_t4 = DISPLAY_SURF.blit(btn_t4,(125, 253))
		btn_back.draw(DISPLAY_SURF,mouse,(550,10,45,20),(560,13))
		pygame.display.update()
		clock.tick(60)
	print ("Exit from TbyNLM")
	
