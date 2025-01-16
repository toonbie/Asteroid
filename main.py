import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
def main(): 
	pygame.init()
	clock = pygame.time.Clock()
	dt = 0
	print("Starting asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	updatable = pygame.sprite.Group()
	drawable = pygame.sprite.Group()
	asteroids = pygame.sprite.Group()
	Player.containers = (updatable,drawable)
	Asteroid.containers =(asteroids,updatable,drawable)
	AsteroidField.containers=(updatable)
	player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	asteroidfield = AsteroidField()
	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				return
		for updates in updatable:
			updates.update(dt)

		screen.fill((0,0,0))

		for draw in drawable:
			draw.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60)/1000

if __name__ == "__main__":
	main()
