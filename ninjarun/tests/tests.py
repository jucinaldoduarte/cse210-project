import pytest
import arcade
from game import constants
from game.camera import Camera
from game.player import Player
from game.map import Map
from game.physics_engine import PhysicsEngine
from game.scene import Scene

def test_set_camera():
    camera = Camera()
    assert camera.set_camera() == arcade.Camera(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

def test_center_camera_to_player():
    camera = Camera()
    player = Player()
    screen_center_x = player.center_x - (camera.camera_to_player.viewport_width / 2)
    screen_center_y = player.center_y - (camera.camera_to_player.viewport_height / 2)
    camera.center_camera_to_player(player)
    assert screen_center_x == 0
    assert screen_center_y == 0

def set_map_test():
    map = Map()
    my_map = map.set_map()
    assert my_map == arcade.load_tilemap(map.name, constants.TILE_SCALING, map.layer_options)

def set_engine_test():
    player = Player()
    engine = PhysicsEngine()
    this_scene = Scene()
    engine.set_engine(player, this_scene.scene.get_sprite_list, this_scene.scene )
    assert engine == arcade.PhysicsEnginePlatformer(
            player,
            [
                this_scene.scene.get_sprite_list(constants.LAYER_NAME_PLATFORMS),
                this_scene.scene.get_sprite_list(constants.LAYER_NAME_MOVING_PLATFORMS),
            ],
            gravity_constant=constants.GRAVITY,
            ladders=this_scene.scene.get_sprite_list(constants.LAYER_NAME_LADDERS),
        )

def load_image(self, action):
        for i in range(10):
            texture = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\run__00{i}.png")
            if action == "walk":
                self.walk_textures.append(texture)









