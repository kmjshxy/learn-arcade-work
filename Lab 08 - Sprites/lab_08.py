""" Sprite Sample Program """

import random
import arcade

# --- Constants ---
SPRITE_SCALING_PLAYER = 0.3

SPRITE_SCALING_FIRE = 0.1
FIRE_COUNT = 20

SPRITE_SCALING_JAR = 0.01
JAR_COUNT = 20

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600


class Fire(arcade.Sprite):
    def update(self):
        self.center_y -= 3

        if self.top < 0:
            self.bottom = (SCREEN_HEIGHT + random.randrange(0, 200))
            self.center_x = random.randrange(SCREEN_WIDTH)


class Jar(arcade.Sprite):
    def update(self):
        self.center_x -= 3

        if self.left < 0:
            self.right = (SCREEN_WIDTH + random.randrange(20, 200))
            self.center_y = random.randrange(0, SCREEN_HEIGHT)


class MyGame(arcade.Window):
    """ Our custom Window Class"""

    def __init__(self):
        """ Initializer """
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        self.player_list = None
        self.fire_list = None
        self.jar_list = None

        self.player_sprite = None

        self.score = 0

        self.good_noise = arcade.load_sound(":resources:sounds/coin3.wav")
        self.bad_noise = arcade.load_sound(":resources:sounds/hurt5.wav")

        self.set_mouse_visible(False)

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.fire_list = arcade.SpriteList()
        self.jar_list = arcade.SpriteList()

        self.score = 0

        self.player_sprite = arcade.Sprite("ghost.png", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_y = 50
        self.player_sprite.center_x = 50
        self.player_list.append(self.player_sprite)

        for i in range (FIRE_COUNT):
            fire = Fire("unnamed.png", SPRITE_SCALING_FIRE)

            fire.center_y = random.randrange(SCREEN_HEIGHT)
            fire.center_x = random.randrange(SCREEN_WIDTH)
            self.fire_list.append(fire)

        for i in range (JAR_COUNT):
            jar = Jar("27-271949_potion-bottle-icon-png-clip-art-free-boo (1).png", SPRITE_SCALING_JAR)

            jar.center_x = random.randrange(SCREEN_WIDTH)
            jar.center_y = random.randrange(SCREEN_HEIGHT)
            self.jar_list.append(jar)

        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        arcade.start_render()
        self.player_list.draw()
        self.fire_list.draw()
        self.jar_list.draw()
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

        if len(self.jar_list) == 0:
            arcade.draw_text("GAME OVER", 50, 50, arcade.color.WHITE, 80)

    def on_mouse_motion(self, x: float, y: float, dx: float, dy: float):
        if len(self.jar_list) > 0:
            self.player_sprite.center_x = x
            self.player_sprite.center_y = y

    def update(self, delta_time: float):

        if len(self.jar_list) > 0:
            self.fire_list.update()
            self.jar_list.update()

        fire_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.fire_list)

        jar_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.jar_list)

        for fire in fire_hit_list:
            self.score -= 1
            arcade.play_sound(self.bad_noise)
            fire.center_y = random.randrange(SCREEN_HEIGHT + 20, SCREEN_HEIGHT + 50)
            fire.center_x = random.randrange(SCREEN_WIDTH)
        for jar in jar_hit_list:
            self.score += 1
            arcade.play_sound(self.good_noise)
            jar.remove_from_sprite_lists()


def main():
    """ Main method """
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()
