import arcade
from game.scene import Scene
from game.player import Player

class UserControl:
    def __init__(self):
        self.physics_engine = None
        self._scene_manager = Scene()
        self._player_manager = Player()

    def get_physics_engine(self):
        self.physics_engine = arcade.PhysicsEngineSimple(
            self._player_manager.player, self._scene_manager.scene.get_sprite_list("Player")
        )


