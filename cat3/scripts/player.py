import pygame
from pygame.locals import *

class Player:
    def __init__(self):
        self.player_img = pygame.image.load('player.png').convert()
        self.player_img.set_colorkey((0, 0, 0))
        self.player_rect = pygame.Rect(100, 100, 5, 13)
        self.vertical_momentum = 0

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.player_rect.x += 2
        if keys[K_LEFT]:
            self.player_rect.x -= 2
        if keys[K_UP]:
            if self.on_ground():  # Implement 'on_ground' method to check if player is on the ground
                self.vertical_momentum = -5

    def on_ground(self):
        # Implement this method to check if the player is on the ground
        # You can check if the player's rect is colliding with the ground tiles
        pass

    def update(self, tile_rects):
        # Implement collision detection and vertical movement update here
        pass
