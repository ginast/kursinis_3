import pygame
from scripts.enemy import Enemy

class Map:
    def __init__(self):
        self.tile_size = 16 

     
    def load_map(self, path):
        f = open(path + '.txt', 'r')
        data = f.read()
        f.close()
        data = data.split('\n')
        self.game_map = []
        for row in data:
            self.game_map.append(list(row))
    
    

    # def create_enemies(self):
    #     enemies = pygame.sprite.Group()  # Create a new group for enemies
    #     for y, row in enumerate(self.game_map):
    #         for x, tile_type in enumerate(row):
    #             if tile_type == 'E':
    #                 # # Adjust the position based on the tile size
    #                 # x_pixel = x * self.tile_size
    #                 # y_pixel = y * self.tile_size
    #                 # blob = Enemy(x_pixel, y_pixel, self.tile_size)  # Pass the tile_size as an argument
    #                 # enemies.add(blob)  # Add the enemy to the group
    #     return enemies

