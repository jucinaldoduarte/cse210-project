import arcade
from game import constants

class Camera:
    def __init__(self):
        self.camera_to_player = None
        self.camera_to_gui = None

    def set_camera(self):
        return arcade.Camera(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

    def center_camera_to_player(self, player):
        screen_center_x = player.center_x - (self.camera_to_player.viewport_width / 2)
        screen_center_y = player.center_y - (self.camera_to_player.viewport_height / 2)
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self.camera_to_player.move_to(player_centered, 0.2)