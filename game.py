"""
This program shows how to:
  * Have one or more instruction screens
  * Show a 'Game over' text and halt the game
  * Allow the user to restart the game

Make a separate class for each view (screen) in your game.
The class will inherit from arcade.View. The structure will
look like an arcade.Window as each view will need to have its own draw,
update and window event methods. To switch a view, simply create a view
with `view = MyView()` and then use the view.show() method.

This example shows how you can set data from one View on another View to pass data
around (see: time_taken), or you can store data on the Window object to share data between
all Views (see: total_score).

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.view_instructions_and_game_over.py
"""
from re import L
import arcade
from entity import Player

from level2 import GameView1
import time
# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"
TILE_SPRITE_SCALING = 0.5

LAYER_NAME_MOVING_PLATFORMS = "Moving Platforms"
LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_COINS = "Coins"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_LADDERS = "Ladders"
LAYER_NAME_PLAYER = "Player"
LAYER_NAME_ENEMIES = "Enemies"
LAYER_NAME_BULLETS = "Bullets"
PLAYER_SCALING = 0.6
BULLET_SPEED = 12
BULLET_DAMAGE = 25
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
LAYER_NAME_BULLETS = "Bullets"

SCREEN_TITLE = "Sprite Tiled Map with Levels Example"
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SPRITE_SCALING
# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SPRITE_SCALING_LASER = 0.8
SHOOT_SPEED = 15


# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20
# Constants used to track if the player is facing left or right
RIGHT_FACING = 0
LEFT_FACING = 1
import arcade
import random
import os
import random
import math
import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move Sprite with Keyboard Example"

MOVEMENT_SPEED = 5

file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.5

SCREEN_WIDTH = 1024.0
SCREEN_HEIGHT = 600.0

TOTALDISTANCE =  2600

def text_drawer(self, text, x_coord, y_coord, font_size = 30, font_name = "Comic Sans MS",
                color = arcade.color.WHITE):
    self.text_sprite = arcade.create_text_sprite(text, x_coord, y_coord,
    color, font_size = font_size, font_name = font_name)
    return self.scene.add_sprite("message", self.text_sprite)




class GameView(arcade.View):
    def __init__(self, playerType):
        super().__init__()

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None
        
        self.player_type = playerType
        print('in init, playerType: ' + str(self.player_type))
        # Our physics engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None


        # A Camera that can be used to draw GUI elements

        self.gui_camera = None



        # Keep track of the score

        self.score = 0

        self.campfireTracker = 0
        self.firstTimeVisiting = [True] * 7
        self.inGameCoords = []
        self.mapCoords = []
        # arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        map_name = ":resources:tiled_maps/map.json"
        #"/Users/sander/map.tmx"
        layer_options = {
            "Platforms": {
                "use_spatial_hash": True,
            },
        }
        # Set up the Game Camera
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.background = arcade.load_texture("assets/big_tree.png")

        # Set up the GUI Camera

        self.gui_camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Keep track of the score

        self.score = 0

        # Read in the tiled map
        self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        # Initialize Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

                # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        # # Initialize Scene
        # self.scene = arcade.Scene()

        # Set up the player, specifically placing it at these coordinates.
        player_types = {'Blue': 'assets/marshie_blue.png', 'Red': 'assets/marshie_red.png', 'Green': 'assets/marshie_green.png'}
        self.player_sprite = Player(player_types[self.player_type], 0.02)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 96
        self.scene.add_sprite("Player", self.player_sprite)



        # Use a loop to place some coins for our character to pick up
        for x in range(128, 1250, 256):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", COIN_SCALING)
            coin.center_x = x
            coin.center_y = 96
            self.scene.add_sprite("Coins", coin)

        inGameCoords = []

        for i in range(200, TOTALDISTANCE-200, (TOTALDISTANCE-200) // 7):
            fire = arcade.Sprite('assets/bitcamplogo_nolit.png', 0.15)
            fire.center_x = i
            fire.center_y = 100
            inGameCoords.append((i, 100))
            self.scene.add_sprite('Fire', fire)
        # inGameCoords.reverse()
        self.inGameCoords = inGameCoords

        map = arcade.Sprite("assets/MAP.PNG", 0.4)
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        map.center_x = screen_center_x
        map.center_y = screen_center_y

        # print('map x,y: ' + str(map.center_x) + ', ' + str(map.center_y))
        map.alpha = 0
        self.scene.add_sprite('Map', map)
        

        mapCoords = [(130, 280), (205, 175), (350, 440),
                            (410, 250), (615, 350), (590, 430),
                            (530, 230)]
        self.mapCoords = mapCoords
        for i in range(7):
            fire = arcade.Sprite('assets/bitcamplogo_nolit.png', 0.08)
            fire.center_x = mapCoords[i][0]
            fire.center_y = mapCoords[i][1]
            fire.alpha = 255     
            fire.visible = False
            self.scene.add_sprite('MapFire', fire) 



        # fire = arcade.Sprite('assets/bitcamplogo_nolit.png', 0.15)
        # fire.center_x = 1800
        # fire.center_y = 100


        # print('HERE')


        # Create the 'physics engine'
        # self.physics_engine = arcade.PhysicsEnginePlatformer(
        #     self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["Walls"]
        # )

                # Name of map file to load

        # Layer specific options are defined based on Layer names in a dictionary
        # Doing this will make the SpriteList for the platforms layer
        # use spatial hashing for detection.




        # Create the 'physics engine'
        self.physics_engine = arcade.PhysicsEnginePlatformer(
            self.player_sprite, gravity_constant=GRAVITY, walls=self.scene["Platforms"]
        )

        # BULLET
        self.scene.add_sprite_list(LAYER_NAME_BULLETS)
        # Shooting mechanics
        self.can_shoot = True
        self.shoot_timer = 0
        self.shoot_pressed = False



    def on_draw(self):
        """Render the screen."""

        # Clear the screen to the background color
        self.clear()

        # Activate the game camera
        self.camera.use()
        # arcade.draw_lrwh_rectangle_textured(0, 0,
        #                                     SCREEN_WIDTH, SCREEN_HEIGHT,
        #                                     self.background)
        # Draw our Scene
        self.scene.draw()


        # Activate the GUI camera before drawing GUI elements

        self.gui_camera.use()



        # Draw our score on the screen, scrolling it with the viewport

        score_text = f"Score: {self.score}"

        arcade.draw_text(

            score_text,

            10,

            10,

            arcade.csscolor.WHITE,

            18,

        )
        
        # text_drawer(self, "The journeys of 1000 hackathons begins with 7 steps", 400, 400)


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
            self.player_sprite.facing_direction = LEFT_FACING
            self.player_sprite.texture = self.player_sprite.left_texture
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
            self.player_sprite.facing_direction = RIGHT_FACING
            self.player_sprite.texture = self.player_sprite.right_texture


        if key == arcade.key.Q:
            self.shoot_pressed = True
        
        if key == arcade.key.M:
            self.scene.get_sprite_list('Map')[0].alpha = 215
            for i in range(len(self.scene.get_sprite_list('MapFire'))):
                self.scene.get_sprite_list('MapFire')[i].visible = True




    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

        if key == arcade.key.Q:
            self.shoot_pressed = False

        if key == arcade.key.M:
            self.scene.get_sprite_list('Map')[0].alpha = 0
            for i in range(len(self.scene.get_sprite_list('MapFire'))):
                self.scene.get_sprite_list('MapFire')[i].visible =False


    def center_camera_to_player(self):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y
        # print('(' + str(screen_center_x) + ', ' + str(screen_center_y) + ')')
        self.camera.move_to(player_centered)
        self.scene.get_sprite_list('Map')[0].center_x = screen_center_x + 400
        self.scene.get_sprite_list('Map')[0].center_y = screen_center_y + 300


        coords = [(130, 280), (205, 175), (350, 440),
                                    (410, 250),  (590, 430),(615, 350),
                                    (530, 230)]
        for i in range(7):
            self.scene.get_sprite_list('MapFire')[i].center_x = screen_center_x + coords[i][0]
            self.scene.get_sprite_list('MapFire')[i].center_y = screen_center_y + coords[i][1]


    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["Coins"]
        )
        
        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            # Remove the coin
            coin.remove_from_sprite_lists()
            # Play a sound
            # Add one to the score

            self.score += 1



        fireHit = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["Fire"]
        )

        if len(fireHit) > 0:
            # print('LEVEL END')
            fire = arcade.Sprite("assets/bitcamplogo_lit.png", 0.15)
            fire.center_x = fireHit[0].center_x
            fire.center_y = fireHit[0].center_y

            fire.remove_from_sprite_lists()
            self.scene.add_sprite('Fire', fire)
            fireHit.pop()
            idx = self.inGameCoords.index((fire.center_x, fire.center_y))
            if (self.firstTimeVisiting[idx] == True):
                fire = arcade.Sprite("assets/bitcamplogo_lit.png", 0.08)
                fire.center_x = self.scene['MapFire'][idx].center_x
                fire.center_y = self.scene['MapFire'][idx].center_y
                fire.visible = self.scene['MapFire'][idx].visible
                self.scene['MapFire'][idx] = fire
                # fire.remove_from_sprite_lists()
                # self.scene.add_sprite('MapFire', fire)
                self.firstTimeVisiting[idx] = False
                # self.campfireTracker += 1

            # fireHit.pop()

            # self.scene["Fire"][0]
            
            # time.sleep(1)
            # gameview = GameView1(self.player_type)
            # gameview.setup()
            # self.window.show_view(gameview)
            # print('here')
        # Position the camera
        self.center_camera_to_player()



        # reset on fall off map
        if self.player_sprite.center_y < -100:
            self.player_sprite.center_x = 64
            self.player_sprite.center_y = 96

        ### BULLET STUFF
        if self.can_shoot:
            if self.shoot_pressed:
                # SANDER BULLET CODE
                bullet_image = None
               
                if self.player_sprite.player_color == "blue":
                    bullet_scaling = SPRITE_SCALING_LASER/10
                    bullet_image = "assets/owl.png"
                elif self.player_sprite.player_color == "green":
                    bullet_scaling = SPRITE_SCALING_LASER/11
                    bullet_image = "assets/banjo.png"
                else:
                    bullet_scaling = SPRITE_SCALING_LASER/3
                    bullet_image = "assets/sword.png"

                bullet = arcade.Sprite(
                    bullet_image,
                    bullet_scaling,
                )

                if self.player_sprite.facing_direction == RIGHT_FACING:
                    bullet.change_x = BULLET_SPEED
                else:
                    bullet.change_x = -BULLET_SPEED

                bullet.center_x = self.player_sprite.center_x
                bullet.center_y = self.player_sprite.center_y

                self.scene.add_sprite(LAYER_NAME_BULLETS, bullet)

                self.can_shoot = False
        else:
            self.shoot_timer += 1
            if self.shoot_timer == SHOOT_SPEED:
                self.can_shoot = True
                self.shoot_timer = 0

        # Update moving platforms, enemies, and bullets
        self.scene.update(
            [LAYER_NAME_BULLETS]
        )
        for bullet in self.scene[LAYER_NAME_BULLETS]:
            hit_list = arcade.check_for_collision_with_lists(
                bullet,
                [
                    # self.scene[LAYER_NAME_MOVING_PLATFORMS],
                ],
            )

            if hit_list:
                bullet.remove_from_sprite_lists()

                # for collision in hit_list:
                #     if (
                #         self.scene[LAYER_NAME_ENEMIES]
                #         in collision.sprite_lists
                #     ):
                #         # The collision was with an enemy
                #         collision.health -= BULLET_DAMAGE

                #         if collision.health <= 0:
                #             collision.remove_from_sprite_lists()
                #             self.score += 100

                #         # Hit sound
                #         arcade.play_sound(self.hit_sound)

                return

            if (bullet.right < 0) or (
                bullet.left
                > (self.tile_map.width * self.tile_map.tile_width) * TILE_SCALING
            ):
                bullet.remove_from_sprite_lists()
    # def on_mouse_press(self, _x, _y, _button, _modifiers):
    #         gameview = GameView1(self.player_type)
    #         gameview.setup()
    #         self.window.show_view(gameview)
    #         print('here')


class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.time_taken = 0

    def on_show(self):
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        self.clear()
        """
        Draw "Game over" across the screen.
        """
        arcade.draw_text("Game Over", 240, 400, arcade.color.WHITE, 54)
        arcade.draw_text("Click to restart", 310, 300, arcade.color.WHITE, 24)

        time_taken_formatted = f"{round(self.time_taken, 2)} seconds"
        arcade.draw_text(f"Time taken: {time_taken_formatted}",
                         WIDTH / 2,
                         200,
                         arcade.color.GRAY,
                         font_size=15,
                         anchor_x="center")

        output_total = f"Total Score: {self.window.total_score}"
        arcade.draw_text(output_total, 10, 10, arcade.color.WHITE, 14)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = GameView()
        self.window.show_view(game_view)
