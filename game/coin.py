import arcade
from game import constants
from game.player import Player
from game.scene import Scene
from game.sound import Sound
from game.score import Score

class Coin(Score):
    def __init__(self):
        self.coin = None
        self._player_manager = Player()
        self._scene_manager = Scene()
        self._sound_manager = Sound()
        self.coin_hit_list = None
        self._score_manager = Score()

    def set_coin(self, x):
        self.coin = arcade.Sprite(":resources:images/items/coinGold.png", constants.COIN_SCALING)        
        self.coin.center_x = x
        self.coin.center_y = 200

    
            
            
            
            