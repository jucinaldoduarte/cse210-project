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
        
        # Keys
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.jump_needs_reset = False     
        
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

        # Add foreground to scene
            # self._scene_manager.scene.add_sprite_list_before("Player", constants.LAYER_NAME_FOREGROUND)
        self._scene_manager.scene.add_sprite_list(constants.LAYER_NAME_FOREGROUND)
        
        # Camera to player
        self._camera_manager.camera_to_player = self._camera_manager.set_camera()       

        # Camera to GUI      
        self.camera_to_gui = self._camera_manager.set_camera()

        # Background
        self._map_manager.set_background()

        # Physics Engine
        self._physics_engine_manager.set_engine(self._player, self._scene_manager.scene.get_sprite_list, self._scene_manager.scene)        

    def on_draw(self):
        # Start render       
        arcade.start_render()  

        # Player camera      
        self._camera_manager.camera_to_player.use() 

        # Draw scene      
        self._scene_manager.scene.draw()

        # GUI camera
        self.camera_to_gui.use()

        # Score
        arcade.draw_text(self._score_manager.show_score(), 10, 600, arcade.csscolor.WHITE, 22,)

    def process_keychange(self):
        # UP/DOWN
        if self.up_pressed and not self.down_pressed:
            if self._physics_engine_manager.engine.is_on_ladder():
                self._player.change_y = constants.PLAYER_MOVEMENT_SPEED
            elif (
                self._physics_engine_manager.engine.can_jump(y_distance=10)
                and not self.jump_needs_reset
            ):
                self._player.change_y = constants.PLAYER_JUMP_SPEED
                self.jump_needs_reset = True
                self._sound_manager.get_sound("jump")
                arcade.play_sound(self._sound_manager.sound)
        elif self.down_pressed and not self.up_pressed:
            if self._physics_engine_manager.engine.is_on_ladder():
                self._player.change_y = -constants.PLAYER_MOVEMENT_SPEED

        # UP/DOWN on a ladder and no movement
        if self._physics_engine_manager.engine.is_on_ladder():
            if not self.up_pressed and not self.down_pressed:
                self._player.change_y = 0
            elif self.up_pressed and self.down_pressed:
                self._player.change_y = 0

        # LEFT/RIGHT
        if self.right_pressed and not self.left_pressed:
            self._player.change_x = constants.PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self._player.change_x = -constants.PLAYER_MOVEMENT_SPEED
        else:
            self._player.change_x = 0

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W or key == arcade.key.SPACE:
            self.up_pressed = True
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = True
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = True
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = True

        self.process_keychange()

    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self.up_pressed = False
            self.jump_needs_reset = False
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.down_pressed = False
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.left_pressed = False
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.right_pressed = False

        self.process_keychange()       

    def center_camera_to_player(self):
        screen_center_x = self._player.center_x - (self._camera_manager.camera_to_player.viewport_width / 2)
        screen_center_y = self._player.center_y - (
            self._camera_manager.camera_to_player.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self._camera_manager.camera_to_player.move_to(player_centered, 0.2)

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
            delta_time, [constants.LAYER_NAME_COINS, constants.LAYER_NAME_BACKGROUND, constants.LAYER_NAME_PLAYER]
        )

        # Update walls, used with moving platforms
        self._scene_manager.scene.update([constants.LAYER_NAME_MOVING_PLATFORMS])

        self._scene_manager.scene.update([constants.LAYER_NAME_KUNAI])

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

        kunai_hit_list = arcade.check_for_collision_with_list(
            self._player, self._scene_manager.scene.get_sprite_list(constants.LAYER_NAME_KUNAI) 
        )

        # Loop through each coin we hit (if any) and remove it
        for coin in coin_hit_list:

            # Figure out how many points this coin is worth
            if "Points" not in coin.properties:
                print("Warning, collected a coin without a Points property.")
            else:
                points = int(coin.properties["Points"])
                self._score_manager.score += points

            # Remove the coin
            coin.remove_from_sprite_lists()
            self._sound_manager.get_sound("coin")
            arcade.play_sound(self._sound_manager.sound)

        for kunai in kunai_hit_list:
            #self.background = constants.BACKGROUND_GAME_OVER
            self._sound_manager.get_sound("gameover")
            arcade.play_sound(self._sound_manager.sound)
            if self._score_manager.score > 1:
                self._score_manager.score -= 1

        # Did the player fall off of the map?
        if self._player.center_y < -100:
            self._player.center_x = constants.PLAYER_START_X
            self._player.center_y = constants.PLAYER_START_Y

            self._sound_manager.get_sound("gameover")

        # If the player touches something they shouldn't
        """
        if arcade.check_for_collision_with_list(
            self._player, self._scene_manager.scene.get_sprite_list(constants.LAYER_NAME_DONT_TOUCH)
        ):
            self._player.change_x = 0
            self._player.change_y = 0
            self._player.center_x = constants.PLAYER_START_X
            self._player.center_y = constants.PLAYER_START_Y

            self._sound_manager.get_sound("gameover")

        # Check if user got to the end of the level
        if self._player.center_x >= self._map_manager.end_map:
            # Advance to the next level
            pass
            # Load the next level
        """
        # Position the camera
        self.center_camera_to_player()


