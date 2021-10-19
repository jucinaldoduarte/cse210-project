from game import constants
from pathlib import Path
import arcade
import os

class Map:
    def __init__(self):
        self.root = Path(__file__).parent        
        #self.name = f":resources:tiled_maps/map_with_ladders.json"
        self.name = self.root / "map" / "map_with_ladders.json"
      
        self.layer_options = {
            constants.LAYER_NAME_PLATFORMS: {
                "use_spatial_hash": True,
            },
            constants.LAYER_NAME_MOVING_PLATFORMS: {
                "use_spatial_hash": True,
            },
            constants.LAYER_NAME_LADDERS: {
                "use_spatial_hash": True,
            },
            constants.LAYER_NAME_COINS: {
                "use_spatial_hash": True,
            },
        }
        
        self.map = arcade.load_tilemap(self.name, constants.TILE_SCALING, self.layer_options)

        self.end_map = self.map.tiled_map.map_size.width * constants.GRID_PIXEL_SIZE

    #def set_background(self):
        #if self.map.tiled_map.background_color:
        # arcade.set_background_color(self.map.tiled_map.background_color)

    def set_map(self):
        return arcade.load_tilemap(self.name, constants.TILE_SCALING, self.layer_options)

