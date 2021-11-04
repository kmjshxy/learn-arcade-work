import random
import arcade

SPRITE_SCALING = 0.5
FLOWER_SCALING = 0.1
JAR_SCALING = 0.02

DEFAULT_SCREEN_WIDTH = 800
DEFAULT_SCREEN_HEIGHT = 600
SCREEN_TITLE = "Sprite Move with Scrolling Screen Example"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 220

# How fast the camera pans to the player. 1.0 is instant.
CAMERA_SPEED = 0.1

# How fast the character moves
PLAYER_MOVEMENT_SPEED = 7





class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title, resizable=True)

        # Sprite lists
        self.player_list = None
        self.wall_list = None
        self.jar_list = None
        self.score = 0

        # Set up the player
        self.player_sprite = None

        # Physics engine so we don't run into walls.
        self.physics_engine = None

        self.jar_noise = arcade.load_sound(":resources:sounds/secret4.wav")

        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.jar_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = arcade.Sprite("ghost.png",
                                           scale=0.2)
        self.player_sprite.center_x = 20
        self.player_sprite.center_y = 20
        self.player_list.append(self.player_sprite)

# outside walls
        for x in range(81):
                # if random.randrange(5) > 0:
                    wall = arcade.Sprite("wall.png", SPRITE_SCALING)
                    wall.center_x = x * 20
                    wall.center_y = 0
                    self.wall_list.append(wall)
        for x in range(81):
                # if random.randrange(5) > 0:
                    wall = arcade.Sprite("wall.png", SPRITE_SCALING)
                    wall.center_x = x * 20
                    wall.center_y = 900
                    self.wall_list.append(wall)
        for y in range(44):
                # if random.randrange(5) > 0:
                    wall = arcade.Sprite("wall.png", SPRITE_SCALING)
                    wall.center_x = 0
                    wall.center_y = y * 20
                    self.wall_list.append(wall)
        for y in range(44):
                # if random.randrange(5) > 0:
                    wall = arcade.Sprite("wall.png", SPRITE_SCALING)
                    wall.center_x = 1600
                    wall.center_y = y * 20
                    self.wall_list.append(wall)
# inside walls
        for collum in range(8):
            if collum % 2:
                for first_row in range (20):
                    if first_row % 4:
                        wall = arcade.Sprite("wall.png", SPRITE_SCALING)
                        wall.center_x = first_row * 64 + 150
                        wall.center_y = 118 * collum
                        self.wall_list.append(wall)

        coordinate_list = [[400, 502],
                           [459, 620],
                           [900, 502],
                           [959, 620],
                           [1018, 502],
                           [1500, 502],
                           [200, 384],
                           [450, 384],
                           [1000, 384],
                           [870, 384],
                           [550, 266],
                           [997, 266],
                           [1400, 266]]
        for coordinate in coordinate_list:
            wall = arcade.Sprite("flower.png", FLOWER_SCALING)
            wall.center_x = coordinate[0]
            wall.bottom = coordinate[1]
            self.wall_list.append(wall)

        for collum in range(6):
            if collum % 2:
                for second_row in range (23):
                    if second_row % 7:
                        wall = arcade.Sprite("wall.png", SPRITE_SCALING)
                        wall.center_x = second_row * 64 + 59
                        wall.center_y = 118 * collum + 118
                        self.wall_list.append(wall)
        jar1 = arcade.Sprite("27-271949_potion-bottle-icon-png-clip-art-free-boo (1).png", JAR_SCALING)
        jar1.center_y = 100
        jar1.center_x = 100
        self.jar_list.append(jar1)

        for row in range(4):
            jar1 = arcade.Sprite("27-271949_potion-bottle-icon-png-clip-art-free-boo (1).png", JAR_SCALING)
            jar1.bottom = 27
            jar1.center_x = 400 * row + 250
            self.jar_list.append(jar1)
        for row in range(3):
                jar2 = arcade.Sprite("27-271949_potion-bottle-icon-png-clip-art-free-boo (1).png", JAR_SCALING)
                jar2.center_y = 173
                jar2.center_x = 600 * row + 60
                self.jar_list.append(jar2)
        for row in range(2):
                jar3 = arcade.Sprite("27-271949_potion-bottle-icon-png-clip-art-free-boo (1).png", JAR_SCALING)
                jar3.center_y = 290
                jar3.center_x = 900 * row + 400
                self.jar_list.append(jar3)
        for row in range(2):
            jar4 = arcade.Sprite("27-271949_potion-bottle-icon-png-clip-art-free-boo (1).png", JAR_SCALING)
            jar4.center_y = 410
            jar4.center_x = 620 * row + 710
            self.jar_list.append(jar4)
        for row in range(4):
            jar2 = arcade.Sprite("27-271949_potion-bottle-icon-png-clip-art-free-boo (1).png", JAR_SCALING)
            jar2.center_y = 527
            jar2.center_x = 900 * row + 200
            self.jar_list.append(jar2)
        for row in range(4):
            jar1 = arcade.Sprite("27-271949_potion-bottle-icon-png-clip-art-free-boo (1).png", JAR_SCALING)
            jar1.bottom = 737
            jar1.center_x = 400 * row + 250
            self.jar_list.append(jar1)

        self.physics_engine = arcade.PhysicsEngineSimple(self.player_sprite, self.wall_list)
        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.wall_list.draw()
        self.player_list.draw()
        self.jar_list.draw()

        # Select the (unscrolled) camera for our GUI
        self.camera_gui.use()



        # Draw the GUI
        arcade.draw_rectangle_filled(self.width // 2,
                                     20,
                                     self.width,
                                     40,
                                     arcade.color.ALMOND)
        text = f"Scroll value: ({self.camera_sprites.position[0]:5.1f}, " \
               f"{self.camera_sprites.position[1]:5.1f})"
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 10, arcade.color.BLACK_BEAN, 20)


    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            self.player_sprite.change_y = PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player_sprite.change_y = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key. """

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player_sprite.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def on_update(self, delta_time):
        """ Movement and game logic """

        # Call update on all sprites (The sprites don't do much in this
        # example though.)
        self.physics_engine.update()

        # Scroll the screen to the player
        self.scroll_to_player()

        self.jar_list.update()

        jar_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.jar_list)
        for jar in jar_hit_list:
            arcade.play_sound(self.jar_noise)
            jar.remove_from_sprite_lists()
            self.score += 1

    def scroll_to_player(self):
        """
        Scroll the window to the player.

        if CAMERA_SPEED is 1, the camera will immediately move to the desired position.
        Anything between 0 and 1 will have the camera move to the location with a smoother
        pan.
        """

        position = self.player_sprite.center_x - self.width / 2, \
            self.player_sprite.center_y - self.height / 2
        self.camera_sprites.move_to(position, CAMERA_SPEED)

    def on_resize(self, width, height):
        """
        Resize window
        Handle the user grabbing the edge and resizing the window.
        """
        self.camera_sprites.resize(int(width), int(height))
        self.camera_gui.resize(int(width), int(height))


def main():
    """ Main function """
    window = MyGame(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()