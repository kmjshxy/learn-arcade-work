""" Lab 7 - User Control """

import arcade

# --- Constants ---
SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
MOVEMENT_SPEED = 5

def window(x,y):
    arcade.draw_circle_filled(x, y , 19, arcade.color.DARK_SLATE_GRAY)
    arcade.draw_circle_filled(x, y, 15, arcade.color.BLUE)
    arcade.draw_circle_filled(x, y, 12, arcade.color.YELLOW)


def submarine(x,y):
    arcade.draw_rectangle_filled(320 + x - 350, 230 + y - 200, 15, 50, arcade.color.ARSENIC)
    arcade.draw_rectangle_filled(327 + x - 350, 230 + y - 200, 40, 20, arcade.color.ARSENIC)
    arcade.draw_arc_filled(312 + x - 350, 255 + y - 200, 30, 30, arcade.color.ARSENIC, 0, 90)
    arcade.draw_rectangle_filled(310 + x - 350, 262 + y - 200, 10, 15, arcade.color.ARSENIC)
    arcade.draw_ellipse_filled(350 + x - 350, 200 + y - 200, 200, 50, arcade.color.CHARCOAL)
    window( x-10, y)
    window(x+ 30, y)


def fish(x,y,s,color):
    arcade.draw_ellipse_filled(x, y, s * 2.5 , s, color)
    arcade.draw_arc_filled(x-s-(s/6), y, s / 2, s / 4, arcade.color.OXFORD_BLUE, 180,360)
    arcade.draw_circle_filled(x-s + (s / 4), y + (s / 5), s / 10, arcade.color.BLACK)
    arcade.draw_arc_filled(x + (s / 5), y + (s / 3), s, s, color, 80, 180)
    arcade.draw_triangle_filled(x + s + (s / 2), y + (s / 2), x + s + (s / 2), y - (s / 2), x + (s / 3), y, color)


class Submarine:

    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y

    def draw(self):
        submarine(self.position_x, self.position_y)

class Fish:
    def __init__(self, position_x, position_y):
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = 0
        self.change_y = 0
        self.fish_noise = arcade.load_sound(":resources:sounds/jump1.wav")
    def draw(self):
        fish(self.position_x, self.position_y, 25, arcade.color.YELLOW_ORANGE)

    def update(self):
        self.position_y += self.change_y
        self.position_x += self.change_x

        if self.position_x < 25:
            self.position_x = 25
        if self.position_x > SCREEN_WIDTH - 25:
            self.position_x = SCREEN_WIDTH - 25

        if self.position_y < 14:
            self.position_y = 14
        if self.position_y > SCREEN_HEIGHT - 14:
            self.position_y = SCREEN_HEIGHT - 14

        if self.position_x < 28:
            arcade.play_sound(self.fish_noise)
        if self.position_x > SCREEN_WIDTH - 28:
            arcade.play_sound(self.fish_noise)
        if self.position_y < 15:
            arcade.play_sound(self.fish_noise)
        if self.position_y > SCREEN_HEIGHT - 15:
            arcade.play_sound(self.fish_noise)



class MyGame(arcade.Window):
    """ Our Custom Window Class"""

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Lab 7 - User Control")
        self.submarine = Submarine(130, 80)

        self.set_mouse_visible(False)
        self.sub_sound = arcade.load_sound(":resources:sounds/explosion2.wav")
        self.fish = Fish(400, 450)

    def on_draw(self):
        arcade.start_render()
        arcade.set_background_color(arcade.color.OXFORD_BLUE)
        self.fish.draw()
        self.submarine.draw()

        fish(90, 420, 65, arcade.color.TWILIGHT_LAVENDER)
        fish(40, 250, 30, arcade.color.MEDIUM_JUNGLE_GREEN)
        fish(500, 280, 63, arcade.color.TURKISH_ROSE)
        submarine(400, 200)

        submarine(130, 80)

        submarine(250, 400)

        fish(200, 25, 80, arcade.color.MEDIUM_JUNGLE_GREEN)
        fish(200, 300, 50, arcade.color.BLUE_SAPPHIRE)

        fish(300, 170, 30, arcade.color.TURKISH_ROSE)


        arcade.finish_render()

    def update(self, delta_time):
        self.fish.update()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.fish.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.fish.change_x = MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.fish.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.fish.change_y = -MOVEMENT_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.fish.change_x = 0
        elif key == arcade.key.UP or key == arcade.key.DOWN:
            self.fish.change_y = 0

    def on_mouse_motion(self, x, y, dx, dy):
        self.submarine.position_x = x
        self.submarine.position_y = y
    def on_mouse_press(self, x: float, y: float, button: int, modifiers: int):
        if button == arcade.MOUSE_BUTTON_LEFT:
            arcade.play_sound(self.sub_sound)

def main():
    window = MyGame()
    arcade.run()


main()