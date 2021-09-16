import arcade

arcade.open_window(500, 500, "functions drawing")


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

def main():
    arcade.set_background_color(arcade.color.OXFORD_BLUE)

    arcade.start_render()

    fish(90, 420, 65, arcade.color.TWILIGHT_LAVENDER)
    fish(40, 250, 30, arcade.color.MEDIUM_JUNGLE_GREEN)
    fish(500, 280, 63, arcade.color.TURKISH_ROSE)
    submarine(400, 200)

    submarine(130, 80)

    submarine(250, 400)

    fish(200, 25, 80, arcade.color.MEDIUM_JUNGLE_GREEN)
    fish(200, 300, 50, arcade.color.BLUE_SAPPHIRE)

    fish(300, 170, 30, arcade.color.TURKISH_ROSE)

    fish(400, 450, 25, arcade.color.YELLOW_ORANGE)

    arcade.finish_render()
    arcade.run()


main()