import os

# PATH                      
ABSOLUTE_PATH = os.path.abspath(__file__)
THIS_DIRECTORY = os.path.dirname(ABSOLUTE_PATH)
IMAGE_DIR = os.path.join(THIS_DIRECTORY, 'images') 
SOUND_DIR = os.path.join(THIS_DIRECTORY, 'sounds') 
MAP_DIR = os.path.join(THIS_DIRECTORY, 'tilemaps')

# Constants
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Platformer"

# Constants used to scale our sprites from their original size
TILE_SCALING = 1.5 # 0.5 for resource map

#CHARACTER_SCALING = TILE_SCALING * 2
SCALE = 0.2
COIN_SCALING = TILE_SCALING
SHURIKEN_SCALING = 0.2
SHURIKEN_SPEED = 5
SPRITE_PIXEL_SIZE = 32
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 7
GRAVITY = 1.5
PLAYER_JUMP_SPEED = 30

PLAYER_START_X = SPRITE_PIXEL_SIZE * TILE_SCALING * 2
PLAYER_START_Y = SPRITE_PIXEL_SIZE * TILE_SCALING * 2

# Constants used to track if the player is facing left or right
RIGHT = 0
LEFT_FACING = 1

LAYER_NAME_GROUND = "Ground"
LAYER_NAME_MOVING_PLATFORMS = "Moving Platforms"
LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_COINS = "Coins"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_LADDERS = "Ladders"
LAYER_NAME_PLAYER = "Player"
LAYER_NAME_FOREGROUND = "Foreground"
LAYER_NAME_DONT_TOUCH = "Don't Touch"
LAYER_NAME_KUNAI = "Kunais"