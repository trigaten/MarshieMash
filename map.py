import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move Sprite with Keyboard Example"

MOVEMENT_SPEED = 5
import os
file_path = os.path.dirname(os.path.abspath(__file__))
os.chdir(file_path)

from game import GameView



WIDTH = 800
HEIGHT = 600
SPRITE_SCALING = 0.5

SCREEN_WIDTH = 1024.0
SCREEN_HEIGHT = 600.0
class MenuView(arcade.View):

    def set_level(self, level = 0):
        self.level = level

    def on_show(self):
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        self.clear()

        self.background = arcade.load_texture("assets/map.PNG", x=25, y=0, width=2500, height=1264)
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        arcade.draw_text("", WIDTH / 2, HEIGHT / 2,
                         arcade.color.BLACK, font_size=30, anchor_x="center",
                         font_name=
                             "Comic Sans MS",
                         )
        spot_coordinates = [(90, 280), (205, 135), (325, 440),
                            (410, 220), (590, 450), (615, 350),
                            (530, 200)]
        self.dead_fire  = arcade.load_texture("assets/bitcamp_unlit.png", x=0, y=0, width=476, height=475)
        self.icon = arcade.load_texture("assets/bitcampfire.gif", x=0, y=0, width=300, height=300)
        self.fire = arcade.load_animated_gif("assets/bitcampfire.gif")

        for x in range(len(spot_coordinates)):

            if x > self.level:
                arcade.draw_lrwh_rectangle_textured(spot_coordinates[x][0]-25,
                                            spot_coordinates[x][1]-25,
                                            50, 50,
                                            self.dead_fire)
            else:
                arcade.draw_lrwh_rectangle_textured(spot_coordinates[x][0]-30,
                                                    spot_coordinates[x][1]-30,
                                                    60, 60,
                                                    self.icon)


        """arcade.draw_circle_outline(205, 135, 10, arcade.color.WHITE, 9,-1)
        arcade.draw_circle_outline(325, 440, 10, arcade.color.WHITE, 9,-1)
        arcade.draw_circle_outline(410, 220, 10, arcade.color.WHITE, 9,-1)
        arcade.draw_circle_outline(590, 450, 10, arcade.color.WHITE, 9,-1)
        arcade.draw_circle_outline(615, 350, 10, arcade.color.WHITE, 9,-1)
        arcade.draw_circle_outline(530, 200, 10, arcade.color.WHITE, 9,-1)"""

        #self.icon = arcade.load_texture("assets/bitcampfire.gif", x=0, y=0, width=300, height=300)



        arcade.draw_text("", WIDTH / 2, HEIGHT / 2 - 75,
                         arcade.color.GRAY, font_size=20, anchor_x="center",
                         font_name= "Comic Sans MS",)


def main():
    window = arcade.Window(WIDTH, HEIGHT, "Different Views Example")
    window.total_score = 0
    menu_view = MenuView()
    menu_view.set_level(4)
    window.show_view(menu_view)
    arcade.run()


if __name__ == "__main__":
    main()
