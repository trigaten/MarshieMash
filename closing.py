import arcade
from arcade import TextureAtlas
SPRITE_SCALING = 0.5
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move Sprite with Keyboard Example"

MOVEMENT_SPEED = 5
import os
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

from game import GameView

#character selection
from character_selection import CharacterSelection

WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.5


class MenuView(arcade.View):

    def __init__(self):
        super().__init__()
        self.counter = 1

        self.viewBackground = False
        self.background2 = arcade.Sprite("assets/standing_marshies.png", scale = 0.37, image_x= 0, image_y=150,
                             image_width=2160, image_height=1728)
        self.background2.set_position(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

        self.background1 = arcade.Sprite("assets/jumping_marshies.png", scale = 0.37, image_x= 0, image_y=150,
                                     image_width=2160, image_height=1728)
        self.background1.set_position(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)


    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()

                # Draw the Sprite to the screen.
        self.background2.draw()
        self.background1.draw()
        time.sleep(0.02)

        """arcade.draw_lrwh_rectangle_textured(0, 0,
                                                    SCREEN_WIDTH, SCREEN_HEIGHT,
                                                    self.background2)
        arcade.draw_text("Game Complete", WIDTH / 2, HEIGHT / 2-100,
                         arcade.color.BLACK, font_size=30, anchor_x="center",
                         font_name=
                             "Comic Sans MS",
                         )"""


    def on_update(self, delta_time):

        self.counter = self.counter + 1
        if self.counter %10 == 0:
            if (self.viewBackground):
                self.background2.visible = True
                self.background1.visible = False

            else:
                self.background1.visible = True

                self.background2.visible = False
            self.viewBackground = not self.viewBackground




def main():
    window = arcade.Window(WIDTH, HEIGHT, "Different Views Example")
    window.total_score = 0
    menu_view = MenuView()
    # character_selection_view = CharacterSelection()
    # character_selection_view.setup()
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
