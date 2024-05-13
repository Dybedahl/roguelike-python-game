"""
The player entity.
"""

# Import the necessary modules
from pygame import image, sprite
import pygame
import utils.settings as settings

class Player(sprite.Sprite):
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
        # Set the player's health
        self.health = 100
        # Set the player's damage
        self.damage = 10
        # Set the player's score
        self.score = 0
        # Set the player's level
        self.level = 1
        # Set the player's experience
        self.experience = 0
        # Set the player's experience needed to level up based on the level
        self.experience_needed = 100 * self.level
        # Set the player's defense
        self.defense = 5
        # Set the player's gold
        self.gold = 0
        # Set the player's inventory
        self.inventory = []
        # Set the player's equipped items
        self.equipped_items = {"weapon": None, "armor": None, "shield": None}
        # Set the player's status effects
        self.status_effects = []
        # Set the player's position
        self.position = (0, 0)
        # Set the player's direction
        self.direction = "right"
        
    def move(self, dx, dy):
        self.images = self.images_walking
        self.rect.x += dx * self.speed
        self.rect.y += dy * self.speed
        
        # Update the player's image index to animate movement
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_delay:
            self.image_index = (self.image_index + 1) % len(self.images)
            self.image = self.images[self.image_index]
            self.last_update = now
        
        # Prevent the player from going out of the screen
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > settings.SCREEN_WIDTH - self.rect.width:
            self.rect.x = settings.SCREEN_WIDTH - self.rect.width
        if self.rect.y < 0:
            self.rect.y = 0
        if self.rect.y > settings.SCREEN_HEIGHT - self.rect.height:
            self.rect.y = settings.SCREEN_HEIGHT - self.rect.height
            
    def attack(self):
        # Switch to attack images
        self.images = self.images_attacking
        
        # Reset image index to start attack animation from the beginning
        self.image_index = 0

        # Make the player box bigger to simulate an attack
        self.rect.width = settings.PLAYER_WIDTH + 10

        # Set attacking flag to True
        self.attacking = True
        
    def update(self):
        # Update player's image based on current animation
        now = pygame.time.get_ticks()
        if now - self.last_update > self.animation_delay:
            self.image_index = (self.image_index + 1) % len(self.images_attacking)
            self.image = self.images_attacking[self.image_index]
            self.last_update = now

            # If the attack animation has finished, switch back to walking images
            if self.attacking and self.image_index == len(self.images) - 1:
                self.images = self.images_walking
                self.attacking = False
    