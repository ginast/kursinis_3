import pygame
import sys
import math
from pygame.locals import *
from scripts.tilemap import Map 
from scripts.enemy import Enemy 
from scripts.coin import Coin
from scripts.player import Player
from scripts.button import Button

BLACK = (0, 0, 0)

# 
# font_score = pygame.font.SysFont('Bauhaus 93', 30)
game_over = 0

screen_width = 640
screen_height = 480



class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption('Pygame Platformer')

        self.tile_rect = []

        

        self.WINDOW_SIZE = (1280, 960)
        self.screen = pygame.display.set_mode(self.WINDOW_SIZE, 0, 32)
        self.display = pygame.Surface((640, 480)) #turi buti sumazintas
        self.clock = pygame.time.Clock()
        self.background_img = pygame.image.load('background.png')

        self.grass_img = pygame.image.load('grass.png')
        self.dirt_img = pygame.image.load('dirt.png')
        self.restart_img = pygame.image.load('restart_btn.png')
        self.start_img = pygame.image.load('start_btn.png')
        self.exit_img = pygame.image.load('exit_btn.png')

        # #create buttons
       
      
        self.restart_button = Button(screen_width // 2 - 50, screen_height // 2 + 100, self.restart_img)
        self.start_button = Button(screen_width // 2 - 350, screen_height // 2, self.start_img)
        self.exit_button = Button(screen_width // 2 + 150, screen_height // 2, self.exit_img)

        
        
        
        self.main_menu = True

        self.moving_right = False
        self.moving_left = False
        self.vertical_momentum = 0
        self.air_timer = 0

        

        self.map = Map()
        self.map.load_map('map')
        self.enemy_tile = '3'
        self.coin_tile = '4'

       
        
        self.player = Player()  # Initialize the player object
        self.player_score = 0
        self.player_lives = 10
        self.player_img = pygame.image.load('player.png').convert()
        self.player_img.set_colorkey((0, 0, 0))

        self.player_rect = pygame.Rect(100, 400, 5, 13)

        self.coin_group = pygame.sprite.Group()
        for y, row in enumerate(self.map.game_map):
            for x, tile in enumerate(row):
                if tile == '4':
                    coin = Coin(x * 16, y * 16)
                    self.coin_group.add(coin)

        self.enemies = pygame.sprite.Group()
        for y, row in enumerate(self.map.game_map):
            for x, tile in enumerate(row):
                if tile == '3':
                    enemy = Enemy(x * 16, y * 16 - 2)
                    self.enemies.add(enemy)

        


    def collision_test(self, rect, tiles, ignore_tiles=None):
        if ignore_tiles is None:
            ignore_tiles = []
        
        

        hit_list = []
        for tile in tiles:
            if rect.colliderect(tile) and tile not in ignore_tiles:
                hit_list.append(tile)

        return hit_list
    
    


    


    def move(self, rect, movement, tiles):
        collision_types = {'top': False, 'bottom': False, 'right': False, 'left': False}
        rect.x += movement[0]
        hit_list = self.collision_test(rect, tiles)
        for tile in hit_list:
            if movement[0] > 0:
                rect.right = tile.left
                collision_types['right'] = True
            elif movement[0] < 0:
                rect.left = tile.right
                collision_types['left'] = True
        rect.y += movement[1]
        hit_list = self.collision_test(rect, tiles)
        for tile in hit_list:
            if movement[1] > 0:
                rect.bottom = tile.top
                collision_types['bottom'] = True
            elif movement[1] < 0:
                rect.top = tile.bottom
                collision_types['top'] = True
        return rect, collision_types
    




    def run(self):
        
        tile_rects = []
        

        

        while True:  # game loop
            
            # self.game_started = False  # Initialize the game state
            self.display.fill((146, 244, 255))  # clear screen by filling it with blue
            self.display.blit(self.background_img, (0, 0)) 
            
        

            self.enemies.draw(self.display)  # Draw the enemies on the display surface

            # self.coin_group.update(self.player_rect)  # Update enemy behavior
            self.coin_group.draw(self.display)  # Draw the enemies on the display surface
            
            
            # Check collisions while ignoring enemy and coin tiles
            




            for enemy in self.enemies:
                enemy.update()
                if self.player_rect.colliderect(enemy.rect):
                    # Handle collision with enemy (e.g., player loses a life, game over, etc.)
                    self.player_lives -= 1  # Decrease player's lives by one
                    if self.player_lives <= 0:
                        # Game over logic (e.g., display game over screen, reset the level, etc.)
                        print("Game Over")
                        pygame.quit()
                        sys.exit()
            
            
            for coin in self.coin_group:
                coin.update()
                if self.player_rect.colliderect(coin.rect):
                    self.player_score += 1  # Increment the player's score
                    self.coin_group.remove(coin)  # Remove the coin from the group
                # Handle collision with enemy (e.g., player loses a life, game over, etc.)
                    print(self.coin_group)
            
            

            if self.player_score >= 5:
                # Implement win condition (e.g., display a win screen, end the game, etc.)
                print("You win!")
                    


            
            
            
            y = 0
            for layer in self.map.game_map:
                x = 0
                for tile in layer:
                    if tile == '1':
                        self.display.blit(self.dirt_img, (x * 16 , y * 16 ))
                    elif tile == '2':
                        self.display.blit(self.grass_img, (x * 16 , y * 16 ))
                    if tile != '0':
                        tile_rects.append(pygame.Rect(x * 16, y * 16, 16, 16))
                    x += 1
                y += 1
            
            self.colliding_tiles = self.collision_test(self.player_rect, tile_rects, ignore_tiles=[self.enemy_tile, self.coin_tile])
            


            # if self.main_menu:
            #     self.start_button.draw(self.display)  # Update the button state
            #     self.exit_button.draw(self.display)   # Update the button state
               
            #     if self.start_button.clicked:
            #         self.main_menu = False
            #     elif self.exit_button.clicked:
            #         pygame.quit()
            #         sys.exit()
            # if self.start_button.clicked:
            #                 self.main_menu = False




            player_movement = [0, 0]
            if self.moving_right:
                player_movement[0] += 2
            if self.moving_left:
                player_movement[0] -= 2
            player_movement[1] += self.vertical_momentum
            self.vertical_momentum += 0.2
            if self.vertical_momentum > 3:
                self.vertical_momentum = 3

            self.player_rect, collisions = self.move(self.player_rect, player_movement, tile_rects)

            if collisions['bottom']:
                self.air_timer = 0
                self.vertical_momentum = 0
            else:
                self.air_timer += 1

            self.display.blit(self.player_img, (self.player_rect.x , self.player_rect.y ))
   
  

            for event in pygame.event.get():  # event loop
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_RIGHT:
                        self.moving_right = True
                    if event.key == K_LEFT:
                        self.moving_left = True
                    if event.key == K_UP:
                        if self.air_timer < 6:
                            self.vertical_momentum = -5
                if event.type == KEYUP:
                    if event.key == K_RIGHT:
                        self.moving_right = False
                    if event.key == K_LEFT:
                        self.moving_left = False


        
        




            self.screen.blit(pygame.transform.scale(self.display, self.WINDOW_SIZE), (0, 0))
            pygame.display.update()
            self.clock.tick(60)

            

if __name__ == "__main__":
    game = Game()
    game.run()
