import arcade
arcade.open_window(5, 5, "sound")
laser_sound = arcade.load_sound("resource:sounds/fall2.wav")

arcade.play_sound(laser_sound)
arcade.run()
