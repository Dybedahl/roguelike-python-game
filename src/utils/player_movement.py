""" 
Defines the PlayerMovement class, which is responsible for handling the player's movement.
Modify the PlayerMovement class to move the player based on the keyboard input.
"""

import pygame

class PlayerMovement:
    def __init__(self, player):
        self.player = player

    def move(self):
        # Get the keyboard input
        keys = pygame.key.get_pressed()
        
        # Move the player based on the keyboard input
        if keys[pygame.K_LEFT]:
            self.player.move(-1, 0)
            # Set the player's direction to left
            self.player.direction = "left"
            self.player.walking = True
        if keys[pygame.K_RIGHT]:
            self.player.move(1, 0)
            # Set the player's direction to right
            self.player.direction = "right"
            self.player.walking = True
        if keys[pygame.K_UP]:
            self.player.move(0, -1)
            # Set the player's direction to up
            self.player.direction = "up"
            self.player.walking = True
        if keys[pygame.K_DOWN]:
            self.player.move(0, 1)
            # Set the player's direction to down
            self.player.direction = "down"
            self.player.walking = True
            
    def attack(self):
        # Attack when the space key is pressed once and play the attack animation
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            # Attack when the space key is pressed and the player is not already attacking
            if not self.player.attacking:
                self.player.attack()
        
    def update(self):
        pass