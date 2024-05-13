"""
This is the main file for the game. It will be responsible for initializing the game and running the game loop.
"""
# Import the necessary modules
import pygame
import utils.settings as settings
from pygame import display, event, QUIT
from entities.player import Player
from utils.player_movement import PlayerMovement

def main():
    # Initialize the game
    init()
    screen = display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
    display.set_caption("Rougelike Game")
    
    # Set the game tick
    clock = pygame.time.Clock()
    
    # Draw the background for the game
    screen.fill((255, 0, 0))
    
    # Draw the player from the player entity
    player = Player()
    screen.blit(player.image, player.rect)
    
    # Initialize the player movement
    player_movement = PlayerMovement(player)

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
        screen.blit(player.image, player.rect)
        
        
        display.flip()

    quit()
    
def init():
    print("Initializing the game")
    
if __name__ == "__main__":
    main()