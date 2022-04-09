import math
import os

import arcade

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
TILE_SCALING = 0.5
CHARACTER_SCALING = TILE_SCALING * 2
COIN_SCALING = TILE_SCALING
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# Shooting Constants
SPRITE_SCALING_LASER = 0.8
SHOOT_SPEED = 15
BULLET_SPEED = 12
BULLET_DAMAGE = 25

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 7
GRAVITY = 1.5
PLAYER_JUMP_SPEED = 30

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
LEFT_VIEWPORT_MARGIN = 200
RIGHT_VIEWPORT_MARGIN = 200
BOTTOM_VIEWPORT_MARGIN = 150
TOP_VIEWPORT_MARGIN = 100

PLAYER_START_X = 2
PLAYER_START_Y = 1

# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1

LAYER_NAME_MOVING_PLATFORMS = "Moving Platforms"
LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_COINS = "Coins"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_LADDERS = "Ladders"
LAYER_NAME_PLAYER = "Player"
LAYER_NAME_ENEMIES = "Enemies"
LAYER_NAME_BULLETS = "Bullets"

class Entity(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__()
        self.texture = self.load_texture_pair(image)[0]
        # Default to facing right
        self.facing_direction = RIGHT_FACING

        self.scale = scale
        self.set_hit_box(self.texture.hit_box_points)

    def load_texture_pair(self, filename):
        """
        Load a texture pair, with the second being a mirror image.
        """
        return [
            arcade.load_texture(filename),
            arcade.load_texture(filename, flipped_horizontally=True),
        ]

class Player(Entity):
    def __init__(self, color, scale):
        super().__init__("marshie_blue.png", scale)


    def update(self):

        """ Move the player """

        # Move player.

        # Remove these lines if physics engine is moving player.

        self.center_x += self.change_x

        self.center_y += self.change_y


        # Check for out-of-bounds

        if self.left < 0:

            self.left = 0

        elif self.right > SCREEN_WIDTH - 1:

            self.right = SCREEN_WIDTH - 1

        if self.bottom < 0:

            self.bottom = 0

        elif self.top > SCREEN_HEIGHT - 1:

            self.top = SCREEN_HEIGHT - 1