import arcade


WIDTH = 60
HEIGHT = 60
MARGIN = 5
COLLUM_COUNT = 10
ROW_COUNT = 10

SCREEN_WIDTH = (WIDTH + MARGIN) * COLLUM_COUNT + MARGIN
SCREEN_HEIGHT = (HEIGHT + MARGIN) * ROW_COUNT + MARGIN



class MyGame(arcade.Window):
    """
    Main application class.
    """

    def __init__(self, width, height):
        super().__init__(width, height)

        arcade.set_background_color(arcade.color.DARK_PASTEL_PURPLE)
        self.grid = []
        for row in range(ROW_COUNT):
            self.grid[row].append(0)
    def on_draw(self):
        """
        Render the screen.
        """

        arcade.start_render()
        for row in range(ROW_COUNT):
            for collum in range (COLLUM_COUNT):
                    x = WIDTH / 2 + collum * ( WIDTH + MARGIN) + MARGIN
                    y = HEIGHT / 2 + row * (HEIGHT + MARGIN) + MARGIN
                    arcade.draw_rectangle_filled(x, y, WIDTH, HEIGHT, arcade.color.WHITE)

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass


def main():

    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()


if __name__ == "__main__":
    main()