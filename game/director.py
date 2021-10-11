import arcade
from game import constants
from game.player import Player
from game.ground import Ground

class Director(arcade.Window):    

    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        self._player_manager = Player()
        self._ground_manager = Ground()

        self._player_manager.player = None
        self._player_manager.players = None
        self._ground_manager.walls = None   

        arcade.set_background_color(arcade.csscolor.PURPLE)     
        
    def setup(self):
        # Set the player
        self._player_manager.players = arcade.SpriteList()
        self._player_manager.set_player()       
        self._player_manager.players.append(self._player_manager.player)

        # Set the ground
        self._ground_manager.walls = arcade.SpriteList(use_spatial_hash=True)

        for x in range(0, 1250, 64):
            self._ground_manager.set_ground(x)
            self._ground_manager.walls.append(self._ground_manager.ground)                

    def on_draw(self):
        """Render the screen."""
        arcade.start_render()           
        
        # Draw the player
        self._player_manager.players.draw()

        # Draw the ground
        self._ground_manager.walls.draw()
