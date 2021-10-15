import arcade
import random
from game import constants
from game.score import Score

class Coin(Score):
    def __init__(self):
        self.coin = None
        self.coin_hit_list = None
        self._coin_count = 50

    """
    def set_coin(self):
        for i in range(self._coin_count):
            self.coin = arcade.Sprite(":resources:images/items/coinGold.png", constants.COIN_SCALING)        
            self.coin.center_x = random.randrange(constants.SCREEN_WIDTH)
            self.coin.center_y = 200
    """

    def set_coin(self, x):
        self.coin = arcade.Sprite(":resources:images/items/coinGold.png", constants.COIN_SCALING)        
        self.coin.center_x = x
        self.coin.center_y = 200
    

    
            
            
            
            