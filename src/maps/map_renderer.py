# This is used to render the map using Pygame
import pygame
from utils import settings
from utils.spritesheet import SpriteSheet

class MapRenderer:
    def __init__(self, game_map):
        self.game_map = game_map
        self.tile_size = settings.TILE_SIZE
        # Load the tile images from the sprite sheet
        self.sprite_sheet = SpriteSheet(settings.SPRITE_SHEET_PATH)
        
        floor_tiles = self.sprite_sheet.image_at((settings.SPRITE_SHEET_SIZE * 18,
                                                 settings.SPRITE_SHEET_SIZE * 11, 
                                                 settings.SPRITE_SHEET_SIZE,
                                                 settings.SPRITE_SHEET_SIZE))
        
        wall_tiles = self.sprite_sheet.image_at((settings.SPRITE_SHEET_SIZE * 9,  
                                                 settings.SPRITE_SHEET_SIZE * 2,  
                                                 settings.SPRITE_SHEET_SIZE,
                                                 settings.SPRITE_SHEET_SIZE))
        
        self.tiles = {
            "floor": pygame.transform.scale(floor_tiles, (self.tile_size, self.tile_size)),
            "wall": pygame.transform.scale(wall_tiles, (self.tile_size, self.tile_size))
        }
    
    def render(self, screen):
        for y in range(self.game_map.height):
            for x in range(self.game_map.width):
                tile = self.game_map.tiles[y][x]
                image = self.tiles[tile.terrain]
                screen.blit(image, (x * self.tile_size, y * self.tile_size))
                