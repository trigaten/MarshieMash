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

class MenuView(arcade.View):
    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()

        self.background = arcade.load_texture("assets/big_tree.png", x=800.0, y=800.0, width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        arcade.draw_text("How to have a good hackathon", WIDTH / 2, HEIGHT / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center",
                         font_name=
                             "Comic Sans MS",
                         )
        arcade.draw_text("Step 1: just participate (click)", WIDTH / 2, HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center",
                         font_name= "Comic Sans MS",)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        character_selection_view = CharacterSelection()
        character_selection_view.setup()
        self.window.show_view(character_selection_view)

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
    # character_selection_view.setup()
    window.show_view(menu_view)
    arcade.run()"""


if __name__ == "__main__":
    main()
