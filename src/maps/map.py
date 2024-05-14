# This file contains the GameMap class, which is used to represent the game map.

from .tile import Tile
from .map_generator import MapGeneration

class GameMap:
    """
    This class represents the game map. It contains the width and height of the map, as well as the tiles that make up the map.
    
    Attributes:
    width (int): The width of the map.
    height (int): The height of the map.
    tiles (list): A 2D list of Tile objects that make up the map.
    
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.tiles = [[Tile('floor') for _ in range(width)] for _ in range(height)]
        
    def generate_map(self):
        """
        Generate the map using cellular automata.
        """
        map_data = MapGeneration.cellular_automata(self.width, self.height)
        
        # Update tiles based on map data
        for y in range(self.height):
            for x in range(self.width):
                terrain = map_data[y][x]
                self.tiles[y][x] = Tile(terrain)