import arcade
from game import constants

class Camera:
    def __init__(self):
        self.camera_to_player = None
        self.camera_to_gui = None

    def set_camera(self):
        return arcade.Camera(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)