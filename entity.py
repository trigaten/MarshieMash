import math
import os

import arcade
import random
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
        self.right_texture, self.left_texture = self.load_texture_pair(image)
        self.texture = self.right_texture
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
    def __init__(self, image, scale):
        super().__init__(image, scale)
        if "blue" in image:
            self.player_color = "blue" 
        elif "green" in image:
            self.player_color = "green" 
        else:
            self.player_color = "red"


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


class Enemy(Entity):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.health = 50
        self.should_update_walk = 0

    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip face left or right
        if self.change_x < 0 and self.facing_direction == RIGHT_FACING:
            self.facing_direction = LEFT_FACING
        elif self.change_x > 0 and self.facing_direction == LEFT_FACING:
            self.facing_direction = RIGHT_FACING

        # Idle animation
        if self.change_x == 0:
            self.texture = self.idle_texture_pair[self.facing_direction]
            return

        # Walking animation
        if self.should_update_walk == 3:
            self.cur_texture += 1
            if self.cur_texture > 7:
                self.cur_texture = 0
            self.texture = self.walk_textures[self.cur_texture][self.facing_direction]
            self.should_update_walk = 0
            return

        self.should_update_walk += 1


class BurntOne(Entity):
    def __init__(self, image, scale):
        super().__init__(image, scale)
        self.health = 500
        self.should_update_walk = 0
        self.min_x = 12713.0
        self.min_y = 811.25
        self.max_x = 15265.0

        self.start_pos = (13817.0, 940.0)
        self.x_delta = 3
        self.spawn_wait = 0

    def update(self):
        if random.random() > 0.5:
            self.center_x+=self.x_delta
        else:
            self.center_x-=self.x_delta

            

# class BurntBoi()
    


