import arcade
from game import constants
from game.player import Player
from game.scene import Scene

class Director(arcade.Window):    

    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        self._player_manager = Player()

        self._player_manager.player = None
        self._player_manager.players = None

        self._scene_manager = Scene()

        arcade.set_background_color(arcade.csscolor.PURPLE)     
        
    def setup(self):
        self._player_manager.players = arcade.SpriteList()
        self._player_manager.set_player()       
        self._player_manager.players.append(self._player_manager.player)
                

    def on_draw(self):
        """Render the screen."""
        arcade.start_render()
           
        
        self._scene_manager.draw_items()
        self._player_manager.players.draw()
