import arcade
from game import constants

class Ground:
    def __init__(self):        
        self.wall = None

    def set_ground(self, x):
        self.wall = arcade.Sprite(":resources:images/topdown_tanks/tileSand_roadCornerLL.png", constants.TILE_SCALING)        
        self.wall.center_x = x
        self.wall.center_y = 20



    

        
        

