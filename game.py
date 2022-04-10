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
from entity import Enemy, BurntOne
from entity import Player
import math
import random
from main import MenuView

# Constants
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Marshie's Marshiful Adventure"
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
import random
import os
import random
import math

import character_selection

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

        self.showPause = False
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
        map_name = "map/map.tmx"

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
        sign1 = arcade.Sprite('assets/sign.png',0.25)
        sign1.center_x = 120
        sign1.center_y = 308
        self.scene.add_sprite("Signs", sign1)

        sign2 = arcade.Sprite('assets/sign1.png',0.25)
        sign2.center_x = 669
        sign2.center_y = 402
        self.scene.add_sprite("Signs", sign2)

        # Set up the player, specifically placing it at these coordinates.
        player_types = {'Blue': 'assets/marshie_blue.png', 'Red': 'assets/marshie_red.png', 'Green': 'assets/marshie_green.png'}
        self.player_sprite = Player(player_types[self.player_type], 0.02)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 200
        self.scene.add_sprite("Player", self.player_sprite)


        coinCoords = [
                (364, 260),
                (393.0, 735.75),
                (1252.0, 858.75),
                (3062.0, 849.75),
                (4883.0, 1080.5),
                (5589.0, 1090.75),
                (6291.0, 1057.75),
                (7926.0, 2014.75),
                (10326.0, 1681.0)]
        cool_sponsor_logos = [
        "assets/sponsors/1517.png",
        "assets/sponsors/Appian.png",
        "assets/sponsors/Bloomberg.png",
        "assets/sponsors/BlueHalo.png",
        "assets/sponsors/CockroachLabs.png",
        "assets/sponsors/ionq.png",
        "assets/sponsors/IBMQuant.png",
        "assets/sponsors/M&T.png",
        "assets/sponsors/SoKat.png",
        "assets/sponsors/TwoSix.png",
        "assets/sponsors/Visionist.png",
        "assets/sponsors/Costar.png",
        "assets/sponsors/LTS.png",
        ]
        sponsors = random.choices(cool_sponsor_logos,k=len(coinCoords))
        # Use a loop to place some coins for our character to pick up
        for x in range(len(coinCoords)):
            coin = arcade.Sprite(sponsors[x], COIN_SCALING/5)
            coin.center_x = coinCoords[x][0]
            coin.center_y = coinCoords[x][1]
            self.scene.add_sprite("Coins", coin)

<<<<<<< HEAD
        inGameCoords = [
         (224, 226),
         (1860, 218),
         (3531, 427.25),
         (5112, 806),
         (6890, 486),
         (9133, 1551),
         (11533, 808)]
=======
        # inGameCoords = [(224, 226), (1860, 218), (3531, 427.25), (5112, 806), (6890, 486), (9133, 1551), (11533, 808)]
        inGameCoords = [(799, 212), (1860, 218), (3531, 427.25), (5112, 806), (6890, 486), (9133, 1551), (11533, 808)]
>>>>>>> origin/main

        for i in range(7):
            fire = arcade.Sprite('assets/bitcamplogo_nolit.png', 0.15)
            fire.center_x = inGameCoords[i][0]
            fire.center_y = inGameCoords[i][1]
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

        enemy_locs = [(384.0, 258.0)]
        # enemies to add
        for loc in enemy_locs:
            enemy = Enemy("assets/enemy.png", 0.2)
            x1, y1 = loc
            enemy.center_x = x1
            enemy.center_y = y1

            enemy.boundary_left = x1-200
            enemy.boundary_right = x1+200
            enemy.change_x = 4

            self.scene.add_sprite(LAYER_NAME_ENEMIES, enemy)


        self.burnny = BurntOne("assets/big_boi.png", 0.5)
        self.burnny.center_x, self.burnny.center_y = self.burnny.start_pos
        self.scene.add_sprite("BURNTONE", self.burnny)

        try:
                    # -- Enemies
            enemies_layer = self.tile_map.object_lists[LAYER_NAME_ENEMIES]

            for my_object in enemies_layer:
                x1, y1 = my_object.shape[0]
                cartesian = self.tile_map.get_cartesian(
                    x1, y1
                )

                enemy = Enemy("assets/enemy.png", 0.2)
                enemy.center_x = math.floor(
                    x1/2#cartesian[0] #* TILE_SCALING * self.tile_map.tile_width * 0.5
                )
                enemy.center_y = math.floor(
                    y1/(-11)
                    # abs((cartesian[1] + 1) * (self.tile_map.tile_height * TILE_SCALING)) * 0.5
                )
                if "boundary_left" in my_object.properties:
                    enemy.boundary_left = my_object.properties["boundary_left"]
                if "boundary_right" in my_object.properties:
                    enemy.boundary_right = my_object.properties["boundary_right"]
                if "change_x" in my_object.properties:
                    enemy.change_x = my_object.properties["change_x"]

                self.scene.add_sprite(LAYER_NAME_ENEMIES, enemy)
        except Exception as e:
            raise e


        pause_background = arcade.Sprite("assets/scroll.png", scale = 1, image_x= 0, image_y=0,
        image_width=860, image_height=673)

        continue_button = arcade.Sprite("assets/ContinueButton.png", scale = 0.5, image_x= 0, image_y=2,
                image_width=250, image_height=90)
        reset_button = arcade.Sprite("assets/ResetButton.png", scale = 0.5, image_x= 0, image_y=2,
                                image_width=188, image_height=90)
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (
            self.camera.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y
        pause_background.center_x = screen_center_x
        pause_background.center_y = screen_center_y
        continue_button.center_x = screen_center_x + 100
        reset_button.center_x = screen_center_x - 100
        continue_button.center_y = screen_center_y - 200
        reset_button.center_y = screen_center_y - 200

        # print('map x,y: ' + str(map.center_x) + ', ' + str(map.center_y))
        pause_background.alpha = 0
        continue_button.alpha = 0
        reset_button.alpha = 0

        self.scene.add_sprite('Pause', pause_background)
        self.scene.add_sprite('Pause', continue_button)
        self.scene.add_sprite('Pause', reset_button)


        self.coffeeAlertSprite =  arcade.Sprite("assets/CoffeeBreak.png", scale = 0.4, image_x= 0, image_y=0,
                                        image_width=520, image_height=123)
        self.background_music = arcade.load_sound("assets/sounds/campfire.mp3")
        self.positivesound = arcade.load_sound("assets/sounds/positivesound.mp3")
        self.coffeeAlertSprite.center_x = screen_center_x
        self.coffeeAlertSprite.center_y = screen_center_y
        self.scene.add_sprite("coffeeAlert", self.coffeeAlertSprite)
        self.coffeeCounter = 0
        self.scene.get_sprite_list('coffeeAlert')[0].alpha = 0

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




        if key == arcade.key.P and not self.showPause:
            self.scene.get_sprite_list('Pause')[0].alpha = 235
            self.scene.get_sprite_list('Pause')[1].alpha = 235
            self.scene.get_sprite_list('Pause')[2].alpha = 235
            self.showPause = True
        elif key == arcade.key.P:
            self.scene.get_sprite_list('Pause')[0].alpha = 0
            self.scene.get_sprite_list('Pause')[1].alpha = 0
            self.scene.get_sprite_list('Pause')[2].alpha = 0
            self.showPause = False

    def on_mouse_press(self, x, y, button, key_modifiers):
        screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
        screen_center_y = self.player_sprite.center_y - (self.camera.viewport_height / 2)


        # print('mousepress (' + str(x) + ', ' + str(y) + ')')
        # print('sprite0 loc (' + str(self.scene.get_sprite_list('Pause')[1].center_x) + ', ' + str(self.scene.get_sprite_list('Pause')[1].center_y) + ')')
        # print('screen_center (' + str(screen_center_x) + ', ' + str(screen_center_y))
        characters = []
        if screen_center_y > 0:
            characters = arcade.get_sprites_at_point((x+screen_center_x,y+screen_center_y), self.scene.get_sprite_list('Pause'))
        elif screen_center_x > 0:
            characters = arcade.get_sprites_at_point((x+screen_center_x,y), self.scene.get_sprite_list('Pause'))
        else:
            characters = arcade.get_sprites_at_point((x,y), self.scene.get_sprite_list('Pause'))

        if len(characters) > 0:
            if self.scene.get_sprite_list('Pause')[2] in characters:
                # print("RESET")
                self.showPause  =  False
                self.scene.get_sprite_list('Pause')[0].alpha = 0
                self.scene.get_sprite_list('Pause')[1].alpha = 0
                self.scene.get_sprite_list('Pause')[2].alpha = 0
                # character_selection_view = character_selection.CharacterSelection()
                # character_selection_view.setup()
                # window.show_view(menu_view)
                self.clear()

                # self.window.show_view(character_selection_view)
                # arcade.run()

                # window = arcade.Window(WIDTH, HEIGHT, "Different Views Example")
                # window.total_score = 0
                menu_view = MenuView()
                # character_selection_view = CharacterSelection()
                menu_view.setup()
                self.window.show_view(menu_view)

            if self.scene.get_sprite_list('Pause')[1] in characters:
                print("Continue")
                self.scene.get_sprite_list('Pause')[0].alpha = 0
                self.scene.get_sprite_list('Pause')[1].alpha = 0
                self.scene.get_sprite_list('Pause')[2].alpha = 0
                self.showPause  =  False





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

    # def on_mouse_press(self, x, y, button, key_modifiers):
    #     characters = arcade.get_sprites_at_point((x,y), self.scene.get_sprite_list('Pause'))
    #     print(self.scene.sprite_lists)
    #     if len(characters) > 0:
    #         if self.scene.get_sprite_list('Pause')[2] in characters:
    #             print("RESET")
    #             self.showPause  =  False
    #             self.scene.get_sprite_list('Pause')[0].alpha = 0
    #             self.scene.get_sprite_list('Pause')[1].alpha = 0
    #             self.scene.get_sprite_list('Pause')[2].alpha = 0
    #             character_selection_view = character_selection.CharacterSelection()
    #             character_selection_view.setup()
    #             # window.show_view(menu_view)
    #             self.clear()

    #             self.window.show_view(character_selection_view)
    #             arcade.run()
    #         if self.scene.get_sprite_list('Pause')[1] in characters:
    #             print("Continue")
    #             self.scene.get_sprite_list('Pause')[0].alpha = 0
    #             self.scene.get_sprite_list('Pause')[1].alpha = 0
    #             self.scene.get_sprite_list('Pause')[2].alpha = 0
    #             self.showPause  =  False

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
        self.scene.get_sprite_list('Pause')[0].center_x = screen_center_x + 400
        self.scene.get_sprite_list('Pause')[0].center_y = screen_center_y + 300
        self.coffeeAlertSprite.center_x  = screen_center_x + 400
        self.coffeeAlertSprite.center_y  = screen_center_y + 300

        self.scene.get_sprite_list('Pause')[1].center_x = screen_center_x + 500
        self.scene.get_sprite_list('Pause')[2].center_x = screen_center_x + 300
        self.scene.get_sprite_list('Pause')[1].center_y = screen_center_y + 150
        self.scene.get_sprite_list('Pause')[2].center_y = screen_center_y + 150
        self.scene.get_sprite_list('Map')[0].center_x = screen_center_x + 400
        self.scene.get_sprite_list('Map')[0].center_y = screen_center_y + 300


        coords = [(130, 280), (205, 175), (350, 440),
                                    (410, 250),  (590, 430),(615, 350),
                                    (530, 230)]
        for i in range(7):
            self.scene.get_sprite_list('MapFire')[i].center_x = screen_center_x + coords[i][0]
            self.scene.get_sprite_list('MapFire')[i].center_y = screen_center_y + coords[i][1]


    def on_update(self, delta_time):
        # print(self.player_sprite.center_x, self.player_sprite.center_y)
        """Movement and game logic"""

        # Move the player with the physics engine
        self.physics_engine.update()

        # add checkpoint guard
        if self.burnny.spawn_wait >= 100 and self.firstTimeVisiting[len(self.firstTimeVisiting)-1] == False:
            self.burnny.spawn_wait = 0
            enemy = Enemy("assets/enemy.png", 0.3)
            enemy.center_x = self.burnny.center_x + (0.5 - random.random()) * 400
            enemy.center_y = max(self.burnny.center_y + (0.5 - random.random()) * 400, self.burnny.min_y+10)
            enemy.boundary_left = self.burnny.center_x-100
            enemy.boundary_right = self.burnny.center_x+100
            enemy.change_x = 5
            #     if "boundary_right" in my_object.properties:
            #         enemy.boundary_right = my_object.properties["boundary_right"]
            #     if "change_x" in my_object.properties:
            #         enemy.change_x = my_object.properties["change_x"]
            # enemy.center_x
            self.scene.add_sprite(LAYER_NAME_ENEMIES, enemy)
        else:
            self.burnny.spawn_wait += 1
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

            self.score += 10

        ENEMYHIT = arcade.check_for_collision_with_lists(
            self.player_sprite, [
                self.scene[LAYER_NAME_ENEMIES],
                self.scene["BURNTONE"],
            ]
        )

        if len(ENEMYHIT) > 0:
            for i in range(len(self.firstTimeVisiting)):
                if self.firstTimeVisiting[i] == True:
                    if i > 0:
                        self.player_sprite.center_x = self.inGameCoords[i-1][0]
                        self.player_sprite.center_y = self.inGameCoords[i-1][1]
                        # print(self.player_sprite.center_x)
                        # print(self.player_sprite.center_y)
                        break
                    else:
                        self.player_sprite.center_x = 64
                        self.player_sprite.center_y = 200
                        break

        fireHit = arcade.check_for_collision_with_list(
            self.player_sprite, self.scene["Fire"]
        )


        if len(fireHit) > 0:
            # print('LEVEL END')
            fire = arcade.Sprite("assets/bitcamplogo_lit.png", 0.15)
            fire.center_x = fireHit[0].center_x
            fire.center_y = fireHit[0].center_y
            fireHit.pop()
            idx = self.inGameCoords.index((fire.center_x, fire.center_y))
            if (self.firstTimeVisiting[idx] == True):
                fire.remove_from_sprite_lists()
                self.scene.add_sprite('Fire', fire)
                fire = arcade.Sprite("assets/bitcamplogo_lit.png", 0.08)
                fire.center_x = self.scene['MapFire'][idx].center_x
                fire.center_y = self.scene['MapFire'][idx].center_y
                fire.visible = self.scene['MapFire'][idx].visible
                self.scene['MapFire'][idx] = fire
                # fire.remove_from_sprite_lists()
                # self.scene.add_sprite('MapFire', fire)
                self.firstTimeVisiting[idx] = False
                # self.campfireTracker = idx

                self.coffeeCounter = self.coffeeCounter + 1
                self.scene.get_sprite_list('coffeeAlert')[0].alpha = 255
                arcade.play_sound(self.positivesound, looping= False)


<<<<<<< HEAD
=======
                if (self.coffeeCounter > 0):
                    self.coffeeCounter = self.coffeeCounter + 1
                if (self.coffeeCounter > 20):
                    self.coffeeCounter = 0
                if (self.coffeeCounter == 0):
                    self.scene.get_sprite_list('coffeeAlert')[0].alpha = 0

>>>>>>> origin/main


            # fireHit.pop()

            # self.scene["Fire"][0]

            # time.sleep(1)
            # gameview = GameView1(self.player_type)
            # gameview.setup()
            # self.window.show_view(gameview)
            # print('here')
        # Position the camera
<<<<<<< HEAD
        if (self.scene.get_sprite_list('coffeeAlert')[0].alpha != 0):
            self.coffeeCounter = self.coffeeCounter + 1
        if (self.coffeeCounter > 20):
            self.coffeeCounter = 0
            self.scene.get_sprite_list('coffeeAlert')[0].alpha = 0
=======
        self.center_camera_to_player()
        # print('(' +  str(self.player_sprite.center_x) + ', ' + str(self.player_sprite.center_y) + ')')
>>>>>>> origin/main

        print(self.scene.get_sprite_list('coffeeAlert')[0].alpha)
        self.center_camera_to_player()

        # reset on fall off map
        if self.player_sprite.center_y < -100:
            #GERSON
            # print(self.firstTimeVisiting)
            for i in range(len(self.firstTimeVisiting)):
                if self.firstTimeVisiting[i] == True:
                    if i > 0:
                        self.player_sprite.center_x = self.inGameCoords[i-1][0]
                        self.player_sprite.center_y = self.inGameCoords[i-1][1]
                        # print(self.player_sprite.center_x)
                        # print(self.player_sprite.center_y)
                        break
                    else:
                        self.player_sprite.center_x = 64
                        self.player_sprite.center_y = 200
                        break

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


                if self.player_sprite.facing_direction == RIGHT_FACING:
                    bullet = arcade.Sprite(
                                        bullet_image,
                                        bullet_scaling,
                    )

                    bullet.change_x = BULLET_SPEED
                else:

                    bullet = arcade.Sprite(
                        bullet_image,
                        bullet_scaling,
                        flipped_horizontally=True
                    )
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
            [LAYER_NAME_BULLETS, LAYER_NAME_ENEMIES, "BURNTONE"]
        )

        # See if the enemy hit a boundary and needs to reverse direction.
        for enemy in self.scene[LAYER_NAME_ENEMIES]:
            if (
                enemy.boundary_right
                and enemy.right > enemy.boundary_right
                and enemy.change_x > 0
            ):
                enemy.change_x *= -1

            if (
                enemy.boundary_left
                and enemy.left < enemy.boundary_left
                and enemy.change_x < 0
            ):
                enemy.change_x *= -1

        player_collision_list = arcade.check_for_collision_with_lists(
            self.player_sprite,
            [
                self.scene[LAYER_NAME_COINS],
                self.scene[LAYER_NAME_ENEMIES],
                self.scene["BURNTONE"]
            ],
        )

        for bullet in self.scene[LAYER_NAME_BULLETS]:
            hit_list = arcade.check_for_collision_with_lists(
                bullet,
                [
                    self.scene[LAYER_NAME_ENEMIES],
                    self.scene[LAYER_NAME_PLATFORMS],
                    self.scene["BURNTONE"]
                ],
            )
# (1810.0, 214.75)/
            if hit_list:
                bullet.remove_from_sprite_lists()

                for collision in hit_list:
                    if (
                        self.scene[LAYER_NAME_ENEMIES]
                        in collision.sprite_lists
                    ) or self.scene["BURNTONE"] in collision.sprite_lists:
                        # The collision was with an enemy
                        collision.health -= BULLET_DAMAGE

                        if collision.health <= 0:
                            collision.remove_from_sprite_lists()
                            self.score += 100

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

                # Loop through each coin we hit (if any) and remove it
        for collision in player_collision_list:

            if self.scene[LAYER_NAME_ENEMIES] in collision.sprite_lists or self.scene["BURNTONE"] in collision.sprite_lists:
                self.setup()
                return
            else:
                # Figure out how many points this coin is worth
                if "Points" not in collision.properties:
                    print("Warning, collected a coin without a Points property.")
                else:
                    # points = int(collision.properties["Points"])
                    self.score += 1

                # Remove the coin
                collision.remove_from_sprite_lists()

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
