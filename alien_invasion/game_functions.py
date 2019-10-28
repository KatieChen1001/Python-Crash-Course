import sys 
import pygame
from bullet import Bullet
from alien import Alien

def check_keydown_event(event, ai_settings, screen, ship, bullets):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = True
	elif event.key == pygame.K_LEFT:
		ship.moving_left = True
	elif event.key == pygame.K_SPACE: 
		fire_bullet(ai_settings, screen, ship, bullets)
	elif event.key == pygame.K_q:
		sys.exit()

def fire_bullet(ai_settings, screen, ship, bullets):
	# create a new bullet and add it to the bullets group
	if len(bullets) < ai_settings.bullets_allowed:
		new_bullet = Bullet(ai_settings, screen, ship)
		bullets.add(new_bullet)

def check_keyup_event(event, ship):
	if event.key == pygame.K_RIGHT:
		ship.moving_right = False
	elif event.key == pygame.K_LEFT: 
		ship.moving_left = False	

def check_events(ai_settings, screen, ship, bullets):
	#Watch for keyboard and mouse events
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		
		elif event.type == pygame.KEYDOWN:
			check_keydown_event(event,ai_settings, screen, ship, bullets)
		
		elif event.type == pygame.KEYUP:
			check_keyup_event(event,ship)

def update_bullets(bullets):
	bullets.update()
	
	for bullet in bullets.copy(): # Do not remove items froma  list within a for loop, create a copy instead
		if bullet.rect.bottom <= 0: 
			bullets.remove(bullet)
			

def update_screen(ai_settings, screen, ship, bullets, aliens):
	#Redraw the screen during each pass through the loop
	screen.fill(ai_settings.bg_color)
	
	for bullet in bullets.sprites():
		bullet.draw_bullet()
	
	ship.blitme()
	aliens.draw(screen)
	

	#Make the most recently drawn screen visible
	pygame.display.flip()
	

