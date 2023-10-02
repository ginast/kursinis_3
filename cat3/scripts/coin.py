import pygame
import random

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('coin.png')
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.start_x = self.rect.x
        self.move_direction = random.choice([-1, 1])  # Randomly select -1 or 1 as the initial direction
        self.move_counter = 0
        self.change_direction_interval = random.randint(50, 150)  # Random interval for changing direction
        
    def check_collision(self, player_rect):
        if self.rect.colliderect(player_rect):
            # Handle collision with the player (e.g., increment player score)
            return True
        return False

    def update(self):
        self.rect.y += self.move_direction
        self.move_counter += 1
        
        if self.move_counter >= self.change_direction_interval:
            self.move_direction *= -1  # Change direction
            self.move_counter = 0
            self.change_direction_interval = random.randint(50, 150)  # Randomize the interval again
