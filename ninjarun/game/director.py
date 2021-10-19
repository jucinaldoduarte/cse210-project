import os
import arcade
from game import constants
from game.player import Player
from game.score import Score
from game.sound import Sound
from game.map import Map
from game.scene import Scene
from game.camera import Camera
from game.physics_engine import PhysicsEngine
from game.key import Key

class Director(arcade.Window):
    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        # Instances
        self._score_manager = Score()
        self._map_manager = Map()
        self._sound_manager = Sound()
        self._scene_manager = Scene()
        self._camera_manager = Camera()
        self._physics_engine_manager = PhysicsEngine()
        self._key_manager = Key()

        self.points = 0
        
        # Reset
        self._player = None
        self._score_manager.score = 0 
        self._map_manager.map = None
        self._map_manager.end_map = 0        
        self._scene_manager.scene = None        
        self._physics_engine_manager.engine = None        
        self._camera_manager.camera_to_player = None
        self._camera_manager.camera_to_gui = None             

    def setup(self):  
        # Player      
        self._player = Player()

        # Map
        self._map_manager.map = self._map_manager.set_map()        

        # Scene
        self._scene_manager.scene = self._scene_manager.set_scene(self._map_manager.map)

        # Add player to scene
        self._scene_manager.add_player(self._player)

        # Camera to player
        self._camera_manager.camera_to_player = self._camera_manager.set_camera()       

        # Camera to GUI      
        self.camera_to_gui = self._camera_manager.set_camera()

        # Background
        #self._map_manager.set_background()
        self.background = arcade.load_texture(constants.BACKGROUND)

        # Physics Engine
        self._physics_engine_manager.set_engine(self._player, self._scene_manager.scene.get_sprite_list, self._scene_manager.scene)        

    def on_draw(self):
        # Start render       
        arcade.start_render()  

        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                                            self.background)

        # Player camera      
        self._camera_manager.camera_to_player.use() 

        # Draw scene      
        self._scene_manager.scene.draw()

        # GUI camera
        self.camera_to_gui.use()

        # Score
        #arcade.draw_text(self._score_manager.show_score(), 10, 600, arcade.csscolor.BLACK, 22,)
        arcade.draw_text(self._score_manager.show_score(), 10, 600, arcade.csscolor.DARK_SLATE_GREY, 22,)

    def process_keychange(self):
        # UP/DOWN
        
        if self._key_manager.up_pressed and not self._key_manager.down_pressed:
            if self._physics_engine_manager.engine.is_on_ladder():
                self._player.change_y = constants.PLAYER_MOVEMENT_SPEED
            elif (
                self._physics_engine_manager.engine.can_jump(y_distance=10)
                and not self._key_manager.jump_needs_reset
            ):
                self._player.change_y = constants.PLAYER_JUMP_SPEED
                self._key_manager.jump_needs_reset = True
                self._sound_manager.get_sound("jump")                
                arcade.play_sound(self._sound_manager.sound)
        elif self._key_manager.down_pressed and not self._key_manager.up_pressed:
            if self._physics_engine_manager.engine.is_on_ladder():
                self._player.change_y = -constants.PLAYER_MOVEMENT_SPEED

        # UP/DOWN on a ladder and no movement
        if self._physics_engine_manager.engine.is_on_ladder():
            if not self._key_manager.up_pressed and not self._key_manager.down_pressed:
                self._player.change_y = 0
            elif self._key_manager.up_pressed and self._key_manager.down_pressed:
                self._player.change_y = 0

        # LEFT/RIGHT
        if self._key_manager.right_pressed and not self._key_manager.left_pressed:
            self._player.change_x = constants.PLAYER_MOVEMENT_SPEED
        elif self._key_manager.left_pressed and not self._key_manager.right_pressed:
            self._player.change_x = -constants.PLAYER_MOVEMENT_SPEED
        else:
            self._player.change_x = 0

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            self._key_manager.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self._key_manager.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self._key_manager.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self._key_manager.right_pressed = True

        self.process_keychange()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self._key_manager.up_pressed = False
            self._key_manager.jump_needs_reset = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self._key_manager.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self._key_manager.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self._key_manager.right_pressed = False

        self.process_keychange()

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self._physics_engine_manager.engine.update()

        # Update animations
        if self._physics_engine_manager.engine.can_jump():
            self._player.can_jump = False
        else:
            self._player.can_jump = True

        if self._physics_engine_manager.engine.is_on_ladder() and not self._physics_engine_manager.engine.can_jump():
            self._player.is_on_ladder = True
            self.process_keychange()
        else:
            self._player.is_on_ladder = False
            self.process_keychange()

        
        # Update Animations
        self._scene_manager.scene.update_animation(
            #delta_time, [constants.LAYER_NAME_COINS, constants.LAYER_NAME_BACKGROUND, constants.LAYER_NAME_PLAYER]
            delta_time, [constants.LAYER_NAME_COINS, constants.LAYER_NAME_PLAYER]
        )
        

        # Update walls, used with moving platforms
        self._scene_manager.scene.update([constants.LAYER_NAME_MOVING_PLATFORMS])

        # See if the moving wall hit a boundary and needs to reverse direction.
        for wall in self._scene_manager.scene.get_sprite_list(constants.LAYER_NAME_MOVING_PLATFORMS):

            if (
                wall.boundary_right
                and wall.right > wall.boundary_right
                and wall.change_x > 0
            ):
                wall.change_x *= -1
            if (
                wall.boundary_left
                and wall.left < wall.boundary_left
                and wall.change_x < 0
            ):
                wall.change_x *= -1
            if wall.boundary_top and wall.top > wall.boundary_top and wall.change_y > 0:
                wall.change_y *= -1
            if (
                wall.boundary_bottom
                and wall.bottom < wall.boundary_bottom
                and wall.change_y < 0
            ):
                wall.change_y *= -1

        # See if we hit any coins
        coin_hit_list = arcade.check_for_collision_with_list(
            self._player, self._scene_manager.scene.get_sprite_list(constants.LAYER_NAME_COINS)
        )

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:
            self._score_manager.score += 1
            
            # Remove the coin
            coin.remove_from_sprite_lists()
            self._sound_manager.get_sound("coin")
            arcade.play_sound(self._sound_manager.sound)

        # Position the camera
        self._camera_manager.center_camera_to_player(self._player)


