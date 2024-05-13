"""
The player entity.
"""

# Import the necessary modules
from pygame import image, sprite
import pygame
from utils import settings

class Player(sprite.Sprite):
    """ The player entity.

    Args:
        sprite (Sprite): The base class for all the game objects.
        
    Attributes:
        images_walking (list): The list of images for the player's walking animation.
        images_attacking (list): The list of images for the player's attacking animation.
        image_index (int): The index of the current image in the animation.
        image (Surface): The current image of the player.
        rect (Rect): The rectangle that represents the player's position and size.
        screen_rect (Rect): The rectangle that represents the screen's position and size.
        speed (int): The speed at which the player moves.
        animation_delay (int): The delay between each animation frame.
        last_update (int): The time of the last update.
        attacking (bool): The flag that indicates if the player is attacking.
        defending (bool): The flag that indicates if the player is defending.
        walking (bool): The flag that indicates if the player is walking.
        
    Methods:
        move: Move the player based on the given x and y coordinates.
        attack: Attack with the player.
        update: Update the player's image based on the current animation.
    """    
    def __init__(self):
        super().__init__()
        # Load the player images as a list
        self.images_walking = [image.load(settings.PLAYER_IMAGE_WALK_PATH + "0.png"),
                               image.load(settings.PLAYER_IMAGE_WALK_PATH + "1.png"),
                               image.load(settings.PLAYER_IMAGE_WALK_PATH + "2.png"),
                               image.load(settings.PLAYER_IMAGE_WALK_PATH + "3.png")]
        self.images_attacking = [image.load(settings.PLAYER_IMAGE_ATTACK_PATH + "0.png"),
                                 image.load(settings.PLAYER_IMAGE_ATTACK_PATH + "1.png"),
                                 image.load(settings.PLAYER_IMAGE_ATTACK_PATH + "2.png"),
                                 image.load(settings.PLAYER_IMAGE_ATTACK_PATH + "3.png")]

        self.image_index = 0
        self.image = self.images_walking[self.image_index]
        self.rect = self.image.get_rect()
        self.screen_rect = self.rect

        self.rect.x = settings.PLAYER_WIDTH
        self.rect.y = settings.PLAYER_HEIGHT
        self.speed = settings.PLAYER_SPEED
        self.animation_delay = settings.ANIMATION_DELAY

        self.last_update = pygame.time.get_ticks()
        # Set the player's attacking state
        self.attacking = False
        # Set the player's defense state
        self.defending = False
        # Set the player's walking state
        self.walking = False

    """ Move the player based on the given x and y coordinates.
    
    Args:
        dx (int): The x coordinate.
        dy (int): The y coordinate.
        
    Returns:
        None
    """
    def move(self, dx, dy):
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed

        # Update the player's image index to animate movement
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_delay:
            self.image_index = (self.image_index + 1) % len(self.images_walking)
            self.image = self.images_walking[self.image_index]
            self.last_update = now

        # Prevent the player from going out of the screen
        self.rect.x = max(0, min(self.rect.x, settings.SCREEN_WIDTH - settings.PLAYER_WIDTH))
        self.rect.y = max(0, min(self.rect.y, settings.SCREEN_HEIGHT - settings.PLAYER_HEIGHT))

    """ Attack with the player.
    
    Args:
        None
        
    Returns:
        None
    """
    def attack(self):
        # Reset image index to start attack animation from the beginning
        self.image_index = 0

        # Make the player box bigger to simulate an attack
        self.rect.width = settings.PLAYER_WIDTH + 10

        # Set attacking flag to True
        self.attacking = True

    """ Update the player's image based on the current animation.
    
    Args:
        None
        
    Returns:
        None
    """
    def update(self):
        # Update player's image based on current animation
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_delay:
            self.image_index = (self.image_index + 1) % len(self.images_attacking)
            self.image = self.images_attacking[self.image_index]
            self.last_update = now

            # If the attack animation has finished, switch back to walking images
            if self.attacking and self.image_index == len(self.images_attacking) - 1:
                self.images = self.images_walking
                self.attacking = False
