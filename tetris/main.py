import arcade

# Shape of I, O, T, S, Z, J, and L blocks

I = [['..1..',
      '..1..',
      '..1..',
      '..1..',
      '.....'],
     ['.....',
      '1111.',
      '.....',
      '.....', ]]

O = [['.....',
      '.....',
      '.11..',
      '.11..',
      '.....']]

T = [['.....',
      '..1..',
      '.111.',
      '.....',
      '.....'],
     ['.....',
      '..1..',
      '..11.',
      '..1..',
      '.....'],
     ['.....',
      '.....',
      '.111.',
      '..1..',
      '.....'],
     ['.....',
      '..1..',
      '.11..',
      '..1..',
      '.....']]

S = [['.....',
      '.....',
      '..11.',
      '.11..',
      '.....'],
     ['.....',
      '..1..',
      '..11.',
      '...1.',
      '.....']]

Z = [['.....',
      '.....',
      '.11..',
      '..11.',
      '.....'],
     ['.....',
      '..1..',
      '.11..',
      '.1...',
      '.....']]

J = [['.....',
      '.1...',
      '.111.',
      '.....',
      '.....'],
     ['.....',
      '..11.',
      '..1..',
      '..1..',
      '.....'],
     ['.....',
      '.....',
      '.111.',
      '...1.',
      '.....'],
     ['.....',
      '..1..',
      '..1..',
      '.11..',
      '.....']]

L = [['.....',
      '...1.',
      '.111.',
      '.....',
      '.....'],
     ['.....',
      '..1..',
      '..1..',
      '..11.',
      '.....'],
     ['.....',
      '.....',
      '.111.',
      '.1...',
      '.....'],
     ['.....',
      '.11..',
      '..1..',
      '..1..',
      '.....']]

shapes = [I, O, T, S, Z, J, L]

colors = [
    [(255, 0, 255),  # Magenta/Fuchsia
     (255, 0, 0),  # Red
     (0, 255, 0),  # Lime
     (238, 130, 238),  # violet
     (255, 165, 0),  # orange
     (255, 255, 0),  # yellow
     (0, 0, 255)  # blue
     ]]


class TetrisWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(600, 50)  # location of window
        arcade.set_background_color(arcade.color.AMAZON)
        arcade.set_background_color((0, 0, 0))

        self.rectangle_width = 200
        self.rectangle_height = 100
        self.center_x = 100
        self.center_y = 100
        self.rate_x = 200
        self.rate_y = 100

    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(self.center_x, self.center_y, self.rectangle_width, self.rectangle_height,
                                     arcade.color.BLUE)

    def on_update(self, delta_time: float):
        # self.center_x += 100 * delta_time
        # self.center_y += 100 * delta_time
        self.center_x += self.rate_x * delta_time
        self.center_y += self.rate_y * delta_time

        # to make the triangle bounce when it reaches the sides of the window
        if self.center_x + 100 > 720 or self.center_x - 100 < 0:
            self.rate_x *= -1
        if self.center_y + 50 > 985 or self.center_y - 50 < 0:
            self.rate_y *= -1


TetrisWindow(720, 985, 'Tetris')
arcade.run()

#
#     def setup(self):
#         """ Set up the game variables. Call to re-start the game. """
#         # Create your sprites and sprite lists here
#         pass
#
#     def on_draw(self):
#         """
#         Render the screen.
#         """

# This command should happen before we start drawing. It will clear
# the screen to the background color, and erase what we drew last frame.
# self.clear()

# Call draw() on all your sprite lists below

#     def on_update(self, delta_time):
#         """
#         All the logic to move, and the game logic goes here.
#         Normally, you'll call update() on the sprite lists that
#         need it.
#         """
#         pass
#
#     def on_key_press(self, key, key_modifiers):
#         """
#         Called whenever a key on the keyboard is pressed.
#
#         For a full list of keys, see:
#         https://api.arcade.academy/en/latest/arcade.key.html
#         """
#         pass
#
#     def on_key_release(self, key, key_modifiers):
#         """
#         Called whenever the user lets off a previously pressed key.
#         """
#         pass
#
#     def on_mouse_motion(self, x, y, delta_x, delta_y):
#         """
#         Called whenever the mouse moves.
#         """
#         pass
#
#     def on_mouse_press(self, x, y, button, key_modifiers):
#         """
#         Called when the user presses a mouse button.
#         """
#         pass
#
#     def on_mouse_release(self, x, y, button, key_modifiers):
#         """
#         Called when a user releases a mouse button.
#         """
#         pass
#
#
# def main():
#     """ Main function """
#     game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
#     game.setup()
#     arcade.run()
#
#
# if __name__ == "__main__":
#     main()
#
