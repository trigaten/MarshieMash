import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move Sprite with Keyboard Example"

MOVEMENT_SPEED = 5
import os
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)


#character selection
from character_selection import CharacterSelection

WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.5

# class MenuView(arcade.View):
#     def on_show(self):
#         arcade.set_background_color(arcade.color.WHITE)

#     def on_draw(self):
#         self.clear()

#         self.background = arcade.load_texture("assets/start.png")
#         arcade.draw_lrwh_rectangle_textured(0, 0,
#                                             SCREEN_WIDTH, SCREEN_HEIGHT,
#                                             self.background)
#         arcade.draw_text("Marshie's Mission", WIDTH / 2, HEIGHT / 2 + 185,
#                          arcade.color.BLACK, font_size=30, anchor_x="center",
#                          font_name=
#                              "Comic Sans MS",
#                          )
#         arcade.draw_text("Step 1: just participate (click)", WIDTH / 2, HEIGHT / 2 - 75,
#                          arcade.color.GRAY, font_size=20, anchor_x="center",
#                          font_name= "Comic Sans MS",)
#         map = arcade.Sprite("assets/MAP.PNG", 0.4)
#         screen_center_x = self.player_sprite.center_x - (self.camera.viewport_width / 2)
#         screen_center_y = self.player_sprite.center_y - (
#             self.camera.viewport_height / 2
#         )
#         if screen_center_x < 0:
#             screen_center_x = 0
#         if screen_center_y < 0:
#             screen_center_y = 0
#         player_centered = screen_center_x, screen_center_y

#         map.center_x = screen_center_x
#         map.center_y = screen_center_y

#         # print('map x,y: ' + str(map.center_x) + ', ' + str(map.center_y))
#         map.alpha = 0
#         self.scene.add_sprite('Map', map)
        
#     def on_mouse_press(self, _x, _y, _button, _modifiers):
#         character_selection_view = CharacterSelection()
#         character_selection_view.setup()
#         self.window.show_view(character_selection_view)

class MenuView(arcade.View):
    def __init__(self):
        super().__init__()

        # Our Scene Object
        self.scene = None

        # Separate variable that holds the player sprite
        self.blue = None
        self.red = None
        self.green = None
        self.char_list = None
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
        # map_name = ":resources:tiled_maps/map.json"
        # layer_options = {
        #     "Platforms": {
        #         "use_spatial_hash": True,
        #     },
        # }
        # Set up the Game Camera
        self.camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # self.background = arcade.load_texture("big_tree.png")
        self.background = arcade.load_texture("assets/start.png")

        # Set up the GUI Camera

        self.gui_camera = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)

        # Keep track of the score

        self.score = 0

        # Read in the tiled map
        # self.tile_map = arcade.load_tilemap(map_name, TILE_SCALING, layer_options)

        # Initialize Scene with our TileMap, this will automatically add all layers
        # from the map as SpriteLists in the scene in the proper order.
        # self.scene = arcade.Scene.from_tilemap(self.tile_map)

                # Set the background color
        # if self.tile_map.background_color:
            # arcade.set_background_color(self.tile_map.background_color)

        # # Initialize Scene
        self.scene = arcade.Scene()

        # Set up the player, specifically placing it at these coordinates.
        # self.player_sprite = arcade.Sprite(image_source, 0.02)

        map = arcade.Sprite('assets/MAP.PNG', 0.22)

        # self.char_list.append(map)
        # self.char_list.append(self.red)
        # self.char_list.append(self.green)

        map.center_x = 400
        map.center_y = 315
        

        self.scene.add_sprite("Map", map)
        # self.scene.add_sprite("Red", self.red)

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
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        arcade.draw_text("Marshie's Adventure..... Awaits", WIDTH / 2, HEIGHT / 2 + 180,
                    arcade.color.BLACK, font_size=30, anchor_x="center",
                    font_name=
                        "Comic Sans MS",
                    )

        arcade.draw_text("Click to begin!", WIDTH / 2, HEIGHT / 2 - 75,
                        arcade.color.BLACK, font_size=20, anchor_x="center",
                        font_name= "Comic Sans MS",)
        self.scene.draw()

        # Activate the GUI camera before drawing GUI elements

        self.gui_camera.use()



        # Draw our score on the screen, scrolling it with the viewport

        score_text = f"Score: {self.score}"

        # arcade.draw_text(

        #     score_text,

        #     10,

        #     10,

        #     arcade.csscolor.WHITE,

        #     18,

        # )
        ####TEXT DRAWER HEREEE
        # text_drawer(self, "Click your character", 400, 400)


    def on_mouse_press(self, x, y, button, key_modifiers):
            characterselection = CharacterSelection()
            characterselection.setup()
            self.window.show_view(characterselection)

def main():

    window = arcade.Window(WIDTH, HEIGHT, "Different Views Example")
    window.total_score = 0# menu_view = MenuView()
    character_selection_view = CharacterSelection()
    character_selection_view.setup()
    # window.show_view(menu_view)
    window.show_view(character_selection_view)
    arcade.run()
    """    window = arcade.Window(WIDTH, HEIGHT, "Different Views Example")
    window.total_score = 0
    menu_view = MenuView()
    # character_selection_view = CharacterSelection()
    menu_view.setup()
    window.show_view(menu_view)
    arcade.run()"""
    # window.show_view(character_selection_view)
    arcade.run()


if __name__ == "__main__":
    main()
