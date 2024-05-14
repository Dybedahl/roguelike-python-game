"""
This is the main file for the game. It will be responsible for initializing the game and running the game loop.
"""
# Import the necessary modules
import pygame
from utils import settings
from pygame import display, event, QUIT
from entities.player import Player
from utils.player_movement import PlayerMovement
from maps.map import GameMap
from maps.map_renderer import MapRenderer


def main():
    # Initialize the game
    init()
    screen = display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    display.set_caption("Roguelike Game by Dybedahl")
    
    # Set the game tick
    clock = pygame.time.Clock()
    
    # Draw the background for the game
    screen.fill((255, 0, 0))
    
    # Draw the player from the player entity
    player = Player()
    screen.blit(player.image, player.rect)
    
    # Initialize the player movement
    player_movement = PlayerMovement(player)
    
    # Initialize the map generation
    game_map = GameMap(settings.MAP_WIDTH, settings.MAP_HEIGHT)
    game_map.generate_map()
    
    # Initialize the map renderer
    map_renderer = MapRenderer(game_map)
    
    
    # Load the game
    running = True
    while running:
        for e in event.get():
            if e.type == QUIT:
                running = False
        # Set the game tick
        clock.tick(60)
        
        # Move the player based on the keyboard input
        player_movement.move()
        # Attack when the space key is pressed
        player_movement.attack()
        
        # Check if the player is attacking
        if player.attacking:
            # Update the player's attack animation
            player.update()
        
        # Draw the player on the screen
        screen.fill((255, 255, 255))  # Clear the screen
        map_renderer.render(screen)
        screen.blit(player.image, player.rect)
        
        
        display.flip()

    quit()
    
def init():
    print("Initializing the game")
    
if __name__ == "__main__":
    main()