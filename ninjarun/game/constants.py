import os
import sys

#Path to image directory                        
absolute_path = os.path.abspath(__file__)
this_directory = os.path.dirname(absolute_path)
image_directory = os.path.join(this_directory, 'images')   

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Final Project"

# Constants used to scale our sprites from their original size
CHARACTER_SCALING = 1
TILE_SCALING = 0.5
COIN_SCALING = 0.5

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20

# The player
#IMAGE_SOURCE = ":resources:images/animated_characters/robot/robot_fall.png"
IMAGE_SOURCE = f"{image_directory}\\player\\ninja.png"
BACKGROUND_SOURCE = f"{image_directory}\\background.png"

# The crates
CRATES = ":resources:images/tiles/boxCrate_double.png"

# Coordinates to crates
CRATES_COORDINATE_LIST = [[512, 96], [256, 96], [768, 96]]

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 5

# MAP
MAP_PATH = ":resources:tiled_maps/map.json"





