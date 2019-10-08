"""
Process

1. create canvas w. pygame 
2. class Settings
3. create class "ship"
	- pass in the screen size into class "ship"
4. Refactoring: 
	- create game_function module
	- move check events into game_function module
5. Let user move ship (in game_functions)
6. let user move ship continueously

"""

import sys
import pygame 
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
	#Initialize game and create a screen object 
	pygame.init()
	ai_settings = Settings()
	screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
	pygame.display.set_caption("Alien Invasion")
	
	# Make a ship
	ship = Ship(ai_settings, screen)
	
	#Start the main loop for the game 
	while True:
		gf.check_events(ship)
		ship.update()
		gf.update_screen(ai_settings, screen, ship)
		
run_game()
