# Generates a procedurally generated map 
import random
import numpy as np

class MapGeneration:
    @staticmethod
    def cellular_automata(width, height, initial_probability=0.45, generations=3):
        """
        Generate a map using cellular automata.
        
        Args:
        width (int): Width of the map.
        height (int): Height of the map.
        initial_probability (float): Initial probability of a cell being a floor tile.
        generations (int): Number of generations to apply cellular automata rules.
        
        Returns:
        list: A 2D list representing the generated map.
        """
        
        # Initialize the map with random tiles
        map_data = [[random.choices(['floor', 'wall'], [initial_probability, 1 - initial_probability])[0] 
                     for _ in range(width)] 
                    for _ in range(height)]
        
        # Apply the cellular automata rules
        for _ in range(generations):
            new_map_data = MapGeneration.apply_rules(map_data, width, height)
            for y in range(height):
                for x in range(width):
                    # Count the number of floor neighbors
                    floor_neighbors = sum(1 for dy in range (-1, 2) for dx in range(-1, 2) 
                                          if 0 <= y + dy < height and 0 <= x + dx < width 
                                          and map_data[y + dy][x + dx] == 'floor')
                    
                    # Apply survival and birth rules
                    if map_data[y][x] == 'floor' and floor_neighbors >= 4:
                        new_map_data[y][x] = 'floor'
                    elif map_data[y][x] == 'wall' and floor_neighbors >= 5:
                        new_map_data[y][x] = 'floor'
                    else:
                        new_map_data[y][x] = 'wall'
            
            # Update the map data
            map_data = new_map_data
            
        return map_data
    
    @staticmethod
    def apply_rules(map_data, width, heigth):
        """
        Apply the cellular automata rules to the map data.
        
        Args:
        map_data (list): A 2D list representing the map.
        width (int): Width of the map.
        height (int): Height of the map.
        
        Returns:
        list: A 2D list representing the updated map data.
        """
        new_map_data = [[tile for tile in row] for row in map_data]
        return new_map_data