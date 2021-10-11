import arcade
from game import constants

class Ground:
    def __init__(self):
        self.walls = None 
        self.ground = None

    def set_ground(self, x):
        #self.ground = arcade.Sprite(":resources:images/tiles/grassMid.png", constants.TILE_SCALING)
        self.ground = arcade.Sprite(":resources:images/topdown_tanks/tileSand_roadCornerLL.png", constants.TILE_SCALING)        
        self.ground.center_x = x
        self.ground.center_y = 20



    

        
        

