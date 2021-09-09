import arcade

arcade.open_window(200, 1000, "Drawing")

arcade.set_background_color((50, 50, 50))

arcade.start_render()
# Light
arcade.draw_rectangle_filled(100, 800, 25, 800, arcade.color.GREEN)
arcade.draw_rectangle_filled(100, 800, 20, 800, arcade.color.WHITE)


# Black after the copper.
arcade.draw_ellipse_filled(100, 395, 70, 10, arcade.color.BLACK)
arcade.draw_rectangle_filled(100, 444, 50, 20, arcade.color.BLACK)
arcade.draw_rectangle_filled(100, 360, 40, 150, arcade.color.BLACK)
arcade.draw_ellipse_filled(100, 295, 70, 20, arcade.color.BLACK)
arcade.draw_rectangle_filled(100, 320, 50, 15, arcade.color.BLACK)

# Copper.
arcade.draw_ellipse_filled(100, 444, 70, 10, arcade.color.ALLOY_ORANGE)
arcade.draw_rectangle_filled(100, 452, 70, 20, arcade.color.ALLOY_ORANGE)
arcade.draw_ellipse_filled(100, 460, 70, 10, arcade.color.CHINESE_RED)
arcade.draw_rectangle_filled(100, 466, 30, 30, arcade.color.ALLOY_ORANGE)
arcade.draw_rectangle_filled(100, 458, 30, 4, arcade.color.CHINESE_RED)

# Top.
arcade.draw_ellipse_filled(100, 484, 70, 10, arcade.csscolor.DARK_GRAY)
arcade.draw_rectangle_filled(100, 492, 70, 20, arcade.csscolor.DARK_GRAY)
arcade.draw_ellipse_filled(100, 500, 70, 10, arcade.csscolor.GRAY)

arcade.draw_ellipse_filled(100, 494, 80, 5, arcade.csscolor.DARK_GRAY)
arcade.draw_rectangle_filled(100, 502, 80, 10, arcade.csscolor.DARK_GRAY)
arcade.draw_ellipse_filled(100, 510, 80, 5, arcade.csscolor.GRAY)

# Rings.
arcade.draw_line(65, 390, 135, 390, arcade.color.SILVER, 5)
arcade.draw_line(65, 380, 135, 380, arcade.color.SILVER, 5)
arcade.draw_line(65, 370, 135, 370, arcade.color.SILVER, 5)
arcade.draw_line(65, 360, 135, 360, arcade.color.SILVER, 5)
arcade.draw_line(65, 350, 135, 350, arcade.color.SILVER, 5)
arcade.draw_line(65, 340, 135, 340, arcade.color.SILVER, 5)
arcade.draw_line(65, 330, 135, 330, arcade.color.SILVER, 5)
arcade.draw_line(65, 320, 135, 320, arcade.color.SILVER, 5)
arcade.draw_line(65, 310, 135, 310, arcade.color.SILVER, 5)

# Box.
arcade.draw_rectangle_filled(54, 240, 20, 90, arcade.color.ALLOY_ORANGE)
arcade.draw_rectangle_filled(60, 240, 20, 90, arcade.color.CINEREOUS)
arcade.draw_rectangle_filled(58, 215, 10, 35, arcade.color.BLACK)
arcade.draw_triangle_filled(54, 250, 59, 245, 64, 250, arcade.color.RED)
arcade.draw_triangle_filled(54, 260, 59, 265, 64, 260, arcade.color.GREEN)

# Base.
arcade.draw_rectangle_filled(100, 130, 60, 60, arcade.color.CINEREOUS)
arcade.draw_rectangle_filled(100, 130, 70, 30, arcade.color.SILVER)
arcade.draw_rectangle_filled(100, 225, 70, 140, arcade.color.SILVER)






arcade.finish_render()

arcade.run()