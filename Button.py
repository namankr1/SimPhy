import pygame

class Button:
	def __init__(self, text):
		self.text = text
		self.is_hover = False
		self.default_color = (100,100,100)
		self.hover_color = (255,255,255)
		self.font_color = (0,0,0)
		self.obj = None
		
	def setColor(self, button_color):
		self.default_color = button_color
		
	def setHoverColor(self,hover_color):
		self.hover_color = hover_color
		
	def setFontColor(self,font_color):
		self.font_color = font_color
		
	def label(self,font_size):
		'''button label font'''
		font = pygame.font.Font(None, font_size)
		return font.render(self.text, 1, self.font_color)
	def color(self):
		'''change color when hovering'''
		if self.is_hover:
			return self.hover_color
		else:
			return self.default_color
	def draw(self, screen, mouse, rectcoord, labelcoord,font_size=20):
		'''create rect obj, draw, and change color based on input'''
		self.obj  = pygame.draw.rect(screen, self.color(), rectcoord)
		screen.blit(self.label(font_size), labelcoord)
		self.check_hover(mouse)
	
	def check_hover(self, mouse):
		'''adjust is_hover value based on mouse over button - to change hover color'''
		if self.obj.collidepoint(mouse):
			self.is_hover = True
		else:
			self.is_hover = False
