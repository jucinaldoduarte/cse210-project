import arcade
from game import constants

class Player:
    def __init__(self):
        self.players = None
        self.player = None

    def set_player(self):
        image_source = constants.PLAYER_IMAGE
        self.player = arcade.Sprite(image_source, constants.CHARACTER_SCALING)     
        self.player.center_x = 64
        self.player.center_y = 40

        
        

