import arcade
from game import constants
from game.player import Player

class Camera:
    def __init__(self):
        self.camera = arcade.Camera(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self.gui_camera = None
        self._player_manager = Player()

    

