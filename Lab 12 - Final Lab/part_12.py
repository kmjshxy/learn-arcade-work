
"""
Artwork from https://kenney.nl
"""

import datetime
import random
import arcade


SPRITE_SCALING = 2.5
CHARACTER_SCALING = 2.5
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
RIGHT_FACING = 0
LEFT_FACING = 1



def load_texture_pair(filename):
    """
    Load a texture pair, with the second being a mirror image.
    """
    return [
        arcade.load_texture(filename),
        arcade.load_texture("plat1fl.png", flipped_horizontally=True)]


class PlayerCharacter(arcade.Sprite):
    """Player Sprite"""

    def __init__(self):

        # Set up parent class
        super().__init__()

        # Default to face-right
        self.character_face_direction = LEFT_FACING

        # Used for flipping between image sequences
        self.cur_texture = 0
        self.scale = CHARACTER_SCALING

        # Track our state

        # --- Load Textures ---

        # Images from Kenney.nl's Asset Pack 3

        self.main_path = ("plat1fl.png")

        """ I drew the character texture"""
        self.idle_texture_pair = load_texture_pair(self.main_path)



        # Load textures for walking
        self.walk_textures = []
        texture = load_texture_pair("plat2.png")
        self.walk_textures.append(texture)
        texture = load_texture_pair("plat3.png")
        self.walk_textures.append(texture)

        # Load textures for climbing

        # Set the initial texture
        self.texture = self.idle_texture_pair[0]

        # Hit box will be set based on the first image used. If you want to specify
        # a different hit box, you can do it like the code below.
        # set_hit_box = [[-22, -64], [22, -64], [22, 28], [-22, 28]]
        self.hit_box = self.texture.hit_box_points

    def update_animation(self, delta_time: float = 1 / 60):

        # Figure out if we need to flip face left or right
        if self.change_x > 0 and self.character_face_direction == RIGHT_FACING:
            self.character_face_direction = LEFT_FACING
        elif self.change_x > 0 and self.character_face_direction == LEFT_FACING:
            self.character_face_direction = RIGHT_FACING

        # Walking animation

            self.cur_texture += 1
            if self.cur_texture > 7:
                self.cur_texture = 0
            self.texture = self.walk_textures[self.cur_texture][
                self.character_face_direction
            ]


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
        self.rock_list = arcade.SpriteList()
        self.holding_rn = 0
        self.in_the_basket = 0
        self.END = False

        self.rock_sound = arcade.load_sound(":resources:sounds/rockHit2.wav")
        self.jump = arcade.load_sound(":resources:sounds/jump4.wav")

        self.total_time = 0.0
        self.output = "00:00:00"

        # Set up the player
        self.player_sprite = None
        # Physics engine so we don't run into walls.
        self.physics_engine = None
        arcade.load_tilemap("level1.json")
        # Create the cameras. One for the GUI, one for the sprites.
        # We scroll the 'sprite world' but not the GUI.
        self.camera_sprites = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)
        self.camera_gui = arcade.Camera(DEFAULT_SCREEN_WIDTH, DEFAULT_SCREEN_HEIGHT)

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList()
        self.basket_list = arcade.SpriteList()

        # Set up the player
        self.player_sprite = PlayerCharacter()
        self.player_sprite.center_x = 1000
        self.player_sprite.center_y = 1200
        self.player_list.append(self.player_sprite)
        """ pixel art gallery
        basket 2
        creator id: 6c4751
        http://pixelartmaker.com/art/8eb55a4e52f96b7"""
        self.basket = arcade.Sprite("basket.png", .3)
        self.basket.center_x = 956
        self.basket.center_y = 1295
        self.basket_list.append(self.basket)

        self.total_time = 55





        map_name = "level1.json"
        self.tile_map = arcade.load_tilemap(map_name, scaling=.3, )
        self.wall_list = self.tile_map.sprite_lists["walls"]

        self.scene = arcade.Scene.from_tilemap(self.tile_map)

        rock_count = [[830,1245],
                      [1560,1055],
                      [1700, 360],
                      [3000,515],
                      [3100, 1360],
                      [2510, 1400],
                      [3750, 745],
                      [3600, 1400],
                      [3500, 975],
                      [410, 400]]
        for coordinate in rock_count:
            """ pixel art gallery
            rock 
            creator id:9664c4"""
            # http://pixelartmaker.com/art/384d668556ef0fc
            rock = arcade.Sprite("rock.png", .1)

            rock.center_x = coordinate[0]
            rock.center_y = coordinate[1]

            self.rock_list.append(rock)

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite, self.wall_list,
                                                             gravity_constant=0.35)

        if self.tile_map.background_color:
            arcade.set_background_color(self.tile_map.background_color)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Select the camera we'll use to draw all our sprites
        self.camera_sprites.use()

        # Draw all the sprites.
        self.basket_list.draw()
        self.wall_list.draw()
        self.scene.draw()
        self.rock_list.draw()
        self.player_list.draw()

        arcade.draw_text("collect all the rocks before the time runs out!", 700, 1500, arcade.color.BLACK_BEAN,
                         15, font_name='segoe print')
        arcade.draw_text("you can only hold 4 rocks at a time tho...", 900, 1450, arcade.color.BLACK_BEAN,
                         15, font_name= 'segoe print')
        arcade.draw_text("use the arrow keys on your keyboard to move", 700, 1400, arcade.color.BLACK_BEAN,
                         15, font_name='segoe print')


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

        arcade.draw_text(f"holding: {self.holding_rn}", 10, 10, arcade.color.BLACK_BEAN, 20)
        arcade.draw_text(f"in the basket: {self.in_the_basket}", 170, 10, arcade.color.BLACK_BEAN, 20)
        arcade.draw_text(f"seconds left:{self.total_time}", 580, 10, arcade.color.BLACK_BEAN, 20)
        if self.in_the_basket == 10:
            self.END = True
            arcade.draw_rectangle_filled(self.width // 2, 20, self.width, 8000, arcade.color.LIGHT_GREEN)
            arcade.draw_text("CONGRATS YOU WON!!", 100, 300, arcade.color.BLACK_BEAN, 40)
            arcade.draw_text(f"you collected all the rocks with {self.total_time // 1} seconds to spare", 150, 250,
                             arcade.color.BLACK_BEAN, 15)
        if self.total_time <= 0:
            arcade.draw_rectangle_filled(self.width // 2, 20, self.width, 8000, arcade.color.PINK)
            arcade.draw_text("GAME OVER!", 250, 300, arcade.color.BLACK_BEAN, 40)
            arcade.draw_text(f"you collected {self.in_the_basket} rocks. "
                             f"only {10 - self.in_the_basket} rocks away!", 200, 250,
                             arcade.color.BLACK_BEAN, 20)




    def prossess_keychange(self):
        # Process left/right
        if self.right_pressed and not self.left_pressed:
            self.player_sprite.change_x = PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self.player_sprite.change_x = -PLAYER_MOVEMENT_SPEED
        else:
            self.player_sprite.change_x = 0

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed. """

        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = 9
                arcade.play_sound(self.jump)
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

        self.rock_list.update()

        rock_pick_up_list = arcade.check_for_collision_with_list(self.player_sprite, self.rock_list)
        for rock in rock_pick_up_list:
            if self.holding_rn <= 3:
                rock.remove_from_sprite_lists()
                self.holding_rn += 1
                arcade.play_sound(self.rock_sound)
        placed_in_the_basket = arcade.check_for_collision_with_list(self.player_sprite, self.basket_list)
        if placed_in_the_basket:
            self.in_the_basket += self.holding_rn
            self.holding_rn = 0


        if self.END == False:
            self.total_time -= delta_time

            # Calculate minutes
            minutes = int(self.total_time) // 60

            # Calculate seconds by using a modulus (remainder)
            seconds = int(self.total_time) % 60

            # Calculate 100s of a second
            seconds_100s = int((self.total_time - seconds) * 100)

            # Figure out our output
            self.output = f"{minutes:02d}:{seconds:02d}"








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