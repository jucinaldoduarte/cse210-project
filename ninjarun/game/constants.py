from pathlib import Path

ROOT = Path(__file__).parent

# Constants
L1 = "Platforms"
L2 = "Coins"
L3 = "platforms"
L4 = "background-1"

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Ninja Run"

# Constants used to scale our sprites from their original size
TILE_SCALING = 0.5

#CHARACTER_SCALING = TILE_SCALING * 2
SCALE = 0.2
COIN_SCALING = TILE_SCALING
SPRITE_PIXEL_SIZE = 128
GRID_PIXEL_SIZE = SPRITE_PIXEL_SIZE * TILE_SCALING

# Movement speed of player, in pixels per frame
PLAYER_MOVEMENT_SPEED = 7
GRAVITY = 1.5
PLAYER_JUMP_SPEED = 30

PLAYER_START_X = SPRITE_PIXEL_SIZE * TILE_SCALING * 2
PLAYER_START_Y = SPRITE_PIXEL_SIZE * TILE_SCALING * 1

# Constants used to track if the player is facing left or right
RIGHT = 0
LEFT_FACING = 1

LAYER_NAME_MOVING_PLATFORMS = "Moving Platforms"
LAYER_NAME_PLATFORMS = "Platforms"
LAYER_NAME_COINS = "Coins"
LAYER_NAME_BACKGROUND = "Background"
LAYER_NAME_LADDERS = "Ladders"
LAYER_NAME_PLAYER = "Player"

BACKGROUND = f"{ROOT}/images/background.png"

