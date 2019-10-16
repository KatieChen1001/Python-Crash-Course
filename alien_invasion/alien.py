import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
	
	def __init__(self, ai_settings, screen, ship): 
		super(Alien, self).__init__()
		
		self.screen = screen
		self.ai_settings = ai_settings
		
		#Load the ship image and get its rect
		self.image = pygame.image.load('images/alien.bmp')
		self.rect = self.image.get_rect()
		self.screen_rect = screen.get_rect()
		
		# Start the first alien at the top left corner
		self.x = self.rect.width
		self.y = self.rect.height
		
		# Store a decimal value for the ship's center 
		self.x = float(self.rect.x)
		
	def blitme(self):
		""" Draw alien at its current location """
		self.screen.blit(self.image, self.rect)
		
	def update(self):
		""" Update the alien's position based on the movement flag"""

			
