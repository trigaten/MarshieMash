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
import arcade
# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"
TILE_SPRITE_SCALING = 0.5
PLAYER_SCALING = 0.6

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Tiled Map with Levels Example"
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SPRITE_SCALING
# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20
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

def text_drawer(self, text, x_coord, y_coord, font_size = 30, font_name = "Comic Sans MS",
                color = arcade.color.WHITE):
    self.text_sprite = arcade.create_text_sprite(text, x_coord, y_coord,
    color, font_size = font_size, font_name = font_name)
    return self.scene.add_sprite("message", self.text_sprite)


class Player(arcade.Sprite):

    """ Player Class """

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


class GameView(arcade.View):
    def __init__(self):
        super().__init__()

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.player_sprite = None

        # Our physics engine
        self.physics_engine = None

        # A Camera that can be used for scrolling the screen
        self.camera = None


        # A Camera that can be used to draw GUI elements

        self.gui_camera = None



        # Keep track of the score

        self.score = 0


        # arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        map_name = "/Users/sander/map.tmx"
        layer_options = {
            "Platforms": {
                "use_spatial_hash": True,
            },
        }
        # Set up the Game Camera
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        self.background = arcade.load_texture("big_tree.png")

        # Set up the GUI Camera

        self.gui_camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Keep track of the score

        self.score = 0

        # Read in the tiled map
        self.tile_map = arcade.load_tilemap("/Users/sander/map.tmx", TILE_SCALING, layer_options)

        # Initialize Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.
        self.scene = arcade.Scene.from_tilemap(self.tile_map)

                # Set the background color
        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

        # # Initialize Scene
        # self.scene = arcade.Scene()

        # Set up the player, specifically placing it at these coordinates.
        image_source = "marshie_blue.png"
        self.player_sprite = arcade.Sprite(image_source, 0.02)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 96
        self.scene.add_sprite("Player", self.player_sprite)




        # Use a loop to place some coins for our character to pick up
        for x in range(128, 1250, 256):
            coin = arcade.Sprite(":resources:images/items/coinGold.png", COIN_SCALING)
            coin.center_x = x
            coin.center_y = 96
            self.scene.add_sprite("Coins", coin)

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
        text_drawer(self, "Bob", 400, 400)


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = PLAYER_JUMP_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.LEFT or key == arcade.key.A:
            self.player_sprite.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.player_sprite.change_x = 0

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

        self.camera.move_to(player_centered)

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


        # Position the camera
        self.center_camera_to_player()

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
