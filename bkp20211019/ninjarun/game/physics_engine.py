from game import constants
import arcade

class PhysicsEngine:
    def __init__(self):
        self.engine = None

    def set_engine(self, player, sprite_list, scene):
        self.engine = arcade.PhysicsEnginePlatformer(
            player,
            [
                sprite_list(constants.LAYER_NAME_PLATFORMS),
                scene.get_sprite_list(constants.LAYER_NAME_MOVING_PLATFORMS),
            ],
            gravity_constant=constants.GRAVITY,
            ladders=scene.get_sprite_list(constants.LAYER_NAME_LADDERS),
        )
      
