import arcade

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 500
BACKGROUND_COLOR = arcade.color.ANTIQUE_WHITE
GAME_TITLE = "Ada or Potato?"

TIMER_MAXIMUM = 6

IMAGE_ADA = arcade.load_texture("images/ada.png")
IMAGE_POTATO = arcade.load_texture("images/potato.png", scale=.21)


class Ada(arcade.Sprite):
    timer: int

    def __init__(self):
        super().__init__()
        self.timer = 0
        self.center_x = WINDOW_WIDTH/2
        self.center_y = WINDOW_HEIGHT/2
        self.texture = IMAGE_ADA

    def update_timer(self):
        if self.timer < TIMER_MAXIMUM:
            self.timer += 1
        else:
            self.timer = 0
            self.switch_image()

    def update(self):
        self.update_timer()

    def switch_image(self):
        if self.texture == IMAGE_ADA:
            self.texture = IMAGE_POTATO
        else:
            self.texture = IMAGE_ADA


class AdaGame(arcade.Window):

    def __init__(self):
        super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, GAME_TITLE)
        self.points = 0
        self.status = Ada()

    def setup(self):
        arcade.set_background_color(BACKGROUND_COLOR)

    def on_draw(self):
        """ Called when it is time to draw the world """
        arcade.start_render()
        self.status.draw()
        output = f"Score: {self.points}"
        arcade.draw_rectangle_outline(35, 55, 60.0, 45.0, arcade.color.BLACK)
        arcade.draw_text(output, 10, 50, arcade.color.BLACK, 13)

    def on_update(self, delta_time):
        self.status.update()

    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if self.status.texture == IMAGE_ADA:
            self.points += 1
        else:
            self.points -= 1

def main():
    window = AdaGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()