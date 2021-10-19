import arcade
from game import constants
from game.map import Map   

class Scene(Map):    
    def __init__(self):        
        self.scene = None        

    def add_player(self, player):
        self.scene.add_sprite(constants.LAYER_NAME_PLAYER, player)

    def set_scene(self, map):        
        return arcade.Scene.from_tilemap(map)
    