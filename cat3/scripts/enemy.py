import pygame

class Enemy(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.image.load('enemy.png')
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		self.move_direction = 1
		self.move_counter = 0
		

	def update(self):
		self.rect.x += self.move_direction
		self.move_counter += 1
		self.collided = True 
		if abs(self.move_counter) > 10:
			self.move_direction *= -1
			self.move_counter *= -1
