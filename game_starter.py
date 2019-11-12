import arcade


# Define constants
WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.BLUE
GAME_TITLE = "Hot Air Adventure"
GAME_SPEED = 1/60


class YourGameClassRenameThis(arcade.Window):
    def __init__(self, width, height, title):
        """ Initialize variables """
        w
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        arcade.set_background_color(arcade.color.AIR_FORCE_BLUE)

    def setup(self):
        """ Setup the game (or reset the game) """
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()

    def on_update(self, delta_time):
        """ Called every frame of the game (1/GAME_SPEED times per second)"""


def main():
    window = YourGameClassRenameThis()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
