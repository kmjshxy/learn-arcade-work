""" Sprite Sample Program """

import arcade

# --- Constants ---
SPRITE_SCALING_BOX = 0.5
SPRITE_SCALING_PLAYER = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

MOVEMENT_SPEED = 5


class MyGame(arcade.Window):
    """ This class represents the main window of the game. """

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprites With Walls Example")

        self.player_list = None
        self.wall_list = None

        self.player_sprite = None

        self.physics_engine = None
        self.score = 0
        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_for_sprites = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)
        self.camera_for_gui = arcade.Camera(SCREEN_WIDTH, SCREEN_HEIGHT)


    def setup(self):
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()

        self.player_sprite = arcade.Sprite("character (1).png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 64
        self.player_list.append(self.player_sprite)

# wall way 1 individual
        wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 300
        wall.center_y = 200
        self.wall_list.append(wall)

        wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
        wall.center_x = 364
        wall.center_y = 200
        self.wall_list.append(wall)
# 2nd way row or collum
        for i in range(10):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = i * 64 + 128
            wall.center_y = 400
            self.wall_list.append(wall)

        for x in range(100, 600, 64):
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = x
            wall.center_y = 600
            self.wall_list.append(wall)
# way 3 lots of not row or collum
        coordinate_list = [[400, 500],
                           [470, 500],
                           [400, 570],
                           [470, 570]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite("boxCrate_double.png", SPRITE_SCALING_BOX)
            wall.center_x = coordinate[0]
            wall.center_y = coordinate[1]
            self.wall_list.append(wall)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)


    def on_update(self, delta_time: float):
        self.physics_engine.update()

        # Scroll the window to the player.
        #
        # If CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        # Anything between 0 and 1 will have the camera move to the location with a smoother
        # pan.
        CAMERA_SPEED = 1
        lower_left_corner = (self.player_sprite.center_x - self.width / 2,
                             self.player_sprite.center_y - self.height / 2)
        self.camera_for_sprites.move_to(lower_left_corner, CAMERA_SPEED)
    def on_draw(self):
        arcade.start_render()
        # Select the scrolled camera for our sprites
        self.camera_for_sprites.use()

        self.wall_list.draw()
        self.player_list.draw()
        # Select the (unscrolled) camera for our GUI

        self.camera_for_gui.use()

        arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 24)
    def on_key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.player_sprite.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0


def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()