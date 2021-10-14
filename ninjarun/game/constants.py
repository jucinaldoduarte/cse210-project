import os

# PATH                      
absolute_path = os.path.abspath(__file__)
this_directory = os.path.dirname(absolute_path)
image_directory = os.path.join(this_directory, 'images')   

# SCREEN
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Final Project"

# SCALE FROM THEIR ORIGINAL SIZE
CHARACTER_SCALING = 0.5
TILE_SCALING = 0.5
COIN_SCALING = 0.5
SHURIKEN_SCALING = 0.05

# PLAYER
# PLAYER_IMAGE = ":resources:images/animated_characters/robot/robot_fall.png"
PLAYER_IMAGE = f"{image_directory}\\boy\\attack__001.png" #for animations - Does it cycle through numbered files of certain type for action?
 # like - provide path to image folder then loop through all images with a _idle tag?
PLAYER_MOVEMENT_SPEED = 5
GRAVITY = 1
PLAYER_JUMP_SPEED = 20
PLAYER_MOVEMENT_SPEED = 5

# BACKGROUND
BACKGROUND_SOURCE = f"{image_directory}\\background.png"

# CRATES
CRATES = ":resources:images/tiles/boxCrate_double.png"

# COORDINATES TO CRATES
CRATES_COORDINATE_LIST = [[512, 96], [256, 96], [768, 96]]

# SHURIKENS
SHURIKEN_IMAGE = f"{image_directory}\\shuriken.png"

# MAP
MAP_PATH = ":resources:tiled_maps/map.json"





