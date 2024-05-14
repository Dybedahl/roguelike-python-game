# Map manager class, which is responsible for loading and managing maps.

import pygame
from maps.map import GameMap
from maps.map_renderer import MapRenderer

class MapManager:
    def __init__(self, map_width, map_height):
        self.map_width = map_width
        self.map_height = map_height
        self.game_map = None
        self.map_renderer = None

    def load_map(self):
        self.game_map = GameMap(self.map_width, self.map_height)
        self.game_map.generate_map()
        self.map_renderer = MapRenderer(self.game_map)

    def render_map(self, screen):
        self.map_renderer.render(screen)