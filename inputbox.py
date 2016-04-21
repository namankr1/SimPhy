'''
 First multi-line comments
 function get_key() : 	because of this fuction we were unable to close the game on the DISPLAY_SURF where we enter data
 						as it contains an infinite loop which goes on till a key is pressed(not just mouse click)
 						and mouse click is not a key event so it is undetected .Adding pygame.QUIT part in this function
 						solves the problem
'''
import pygame, pygame.font, pygame.event, pygame.draw, string
from pygame.locals import *
import errorScreen
import pyganim
from const_colors import *


def get_key():
	while True:
		event = pygame.event.poll()
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		elif event.type == KEYDOWN:
			return event.key
		else:
			pass
			
def display_box(DISPLAY_SURF,countIn, message):
	"Print a message in a box in the middle of the DISPLAY_SURF"
	fontobject = pygame.font.Font("./fonts/comic.ttf",17)

	#pygame.draw.rect(DISPLAY_SURF, (75,100,200),(30,countIn*10,200,20), 0)
	#pygame.draw.rect(DISPLAY_SURF, (255,255,255),(28,countIn*10-2,204,24), 1)
	inputbox = pygame.image.load('Images/input_parameters.png') 	
	DISPLAY_SURF.blit(inputbox,(20,10 + countIn*15))

	if len(message) != 0:
		DISPLAY_SURF.blit(fontobject.render(message, 1, BLACK),(36,26 + countIn*15))
	pygame.display.flip()
	
def ask(DISPLAY_SURF, question,countIn):
	print "inside inputbox"
	try:
		"ask(DISPLAY_SURF, question) -> answer"
		pygame.font.init()
		current_string = []
		display_box(DISPLAY_SURF,countIn, question + ": " + "".join(current_string))
		#print "now enter"
		while True:
			mouse = pygame.mouse.get_pos()
			#	keeping pygame.QUIT part here is useless, because just in the first interation the control enters in get_key
			#	function and stays there till a key is pressed, so it doesnt check for pygame.QUIT part
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
			inkey = get_key()
			if inkey == K_BACKSPACE:
				current_string = current_string[0:-1]
			elif inkey == K_RETURN:
				break
			elif inkey == K_MINUS:
				if len(current_string) == 0:
					current_string.append("-")
			elif inkey <= 127:
				current_string.append(chr(inkey))
			display_box(DISPLAY_SURF, countIn,question + ": " + "".join(current_string))
		return "".join(current_string)
	except :
		print ("error in getting input")
		errorScreen.errorScreen(DISPLAY_SURF,"Error in getting "+question)
		return
		
def ask_parallel(DISPLAY_SURF,question,road_val,numImages,path1,path2):
	print "inside asl parallel of inputbox"
	current_string = []
	display_box(DISPLAY_SURF,0, question + ": " + "".join(current_string))
	i = 1
	j=numImages+1
	k = 0
	imageList = []
	ask = True
	load = True
	while True:
		mouse = pygame.mouse.get_pos()
		if i <= numImages :
			
			str1 =(path1+str(i)+path2,0.1)
			imageList.insert(k,str1)
			i+=1
			k+=1
		elif i==numImages+1 and j==numImages+1:
			k=0
			boltAnim1 = pyganim.PygAnimation(imageList)
			j-=1
			imageList1 = []
		elif i== numImages+1 and j>=1:
			str1 =(path1+str(j)+path2,0.1)
			imageList1.insert(k,str1)
			
			j-=1
			k+=1
		elif i== numImages+1 and j==0:
			if load :
				boltAnim2  = pyganim.PygAnimation(imageList1)
				load = False
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				sys.exit()	
		
		if ask :
			while True:
				event = pygame.event.poll()
				if event.type == pygame.QUIT:
					pygame.quit()
					sys.exit()
				elif event.type == KEYDOWN:
					inkey = event.key
					break
				else:
					if i <= numImages :
						str1 =(path1+str(i)+path2,0.1)
						imageList.insert(k,str1)
						
						i+=1
						k+=1
					elif i==numImages+1 and j==numImages+1:
						k=0
						j-=1
						boltAnim1 = pyganim.PygAnimation(imageList)
						imageList1 = []
					elif i== numImages+1 and j>=1:
						str1 =(path1+str(j)+path2,0.1)
						imageList1.insert(k,str1)
						j-=1
						k+=1
					elif i== numImages+1 and j==0:
						if load :
							boltAnim2  = pyganim.PygAnimation(imageList1)
							load = False

			if inkey == K_BACKSPACE:
				current_string = current_string[0:-1]
			elif inkey == K_RETURN:
				ask = False
			elif inkey == K_MINUS:
				if len(current_string) == 0:
					current_string.append("-")
			elif inkey <= 127:
				current_string.append(chr(inkey))
				
		display_box(DISPLAY_SURF, 0,question + ": " + "".join(current_string))
		if ask:
			print ("")
		elif i+j<=numImages+1:
			return "".join(current_string),boltAnim1,boltAnim2
	
