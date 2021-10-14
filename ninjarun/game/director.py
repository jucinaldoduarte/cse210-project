import arcade
from game import constants
from game.camera import Camera
from game.coin import Coin
from game.ground import Ground
from game.player import Player
from game.scene import Scene
from game.score import Score
from game.sound import Sound
from game.user_control import UserControl

class Director(arcade.Window): 

    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        # Instances
        self._camera_manager = Camera()
        self._coin_manager = Coin()     
        self._ground_manager = Ground()
        self._player_manager = Player()
        self._scene_manager = Scene()
        self._score_manager = Score()
     
        self._sound_manager = Sound()
        self._user_control_manager = UserControl()

        # Reset
        self._camera_manager.camera = None
        self._camera_manager.gui_camera = None
        self._player_manager.player = None  
        self._scene_manager.scene = None
        self._score_manager.points = 0 
        self._user_control_manager.physics_engine = None        
                
        # Background color
        arcade.set_background_color(arcade.csscolor.PURPLE)
        # arcade.set_background_color(arcade.csscolor.WHITE)

        # Image as background
        self.background = arcade.load_texture(constants.BACKGROUND_SOURCE)
        
    def setup(self):
        # Cameras
        self._camera_manager.camera = arcade.Camera(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        self._camera_manager.gui_camera = arcade.Camera(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

        # Initial score
        self._score_manager.points = 0

        # Sprite Lists to the scene
        self._scene_manager.scene = arcade.Scene()
        self._scene_manager.scene.add_sprite_list("Player")
        self._scene_manager.scene.add_sprite_list("Walls", use_spatial_hash=True)       

        # Player       
        self._player_manager.set_player() 
        self._scene_manager.scene.add_sprite("Player", self._player_manager.player)

        # Ground
        for x in range(0, 12500, 64):
            self._ground_manager.set_ground(x)            
            self._scene_manager.scene.add_sprite("Walls", self._ground_manager.wall) 
        
        self._user_control_manager.physics_engine = arcade.PhysicsEnginePlatformer(
            self._player_manager.player, self._scene_manager.scene.get_sprite_list("Walls"), constants.GRAVITY
        )

        # Coins
        for x in range(128, 12500, 256):
            self._coin_manager.set_coin(x)
            self._scene_manager.scene.add_sprite("Coins", self._coin_manager.coin)        
       

    def on_draw(self):
        """Render the screen."""
        arcade.start_render()   

        # Draw the background
        # arcade.draw_lrwh_rectangle_textured(0, 0, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, self.background)

        self._camera_manager.camera.use()
        self._scene_manager.scene.draw()
        self._camera_manager.gui_camera.use()
        self._score_manager.count_points()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            if self._user_control_manager.physics_engine.can_jump():
                self._player_manager.player.change_y = constants.PLAYER_JUMP_SPEED
                sound = self._sound_manager.set_sound("jump")
                arcade.play_sound(sound)
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self._player_manager.player.change_y = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self._player_manager.player.change_x = -constants.PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self._player_manager.player.change_x = constants.PLAYER_MOVEMENT_SPEED
            


    def on_key_release(self, key, modifiers):
        """Called when the user releases a key."""

        if key == arcade.key.UP or key == arcade.key.W:
            self._player_manager.player.change_y = 0
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self._player_manager.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self._player_manager.player.change_x = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self._player_manager.player.change_x = 0
    
    def center_camera_to_player(self):
        screen_center_x = self._player_manager.player.center_x - (self._camera_manager.camera.viewport_width / 2)
        screen_center_y = self._player_manager.player.center_y - (
            self._camera_manager.camera.viewport_height / 2
        ) 
   
        # Don't let camera travel past 0
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y

        self._camera_manager.camera.move_to(player_centered)   

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self._user_control_manager.physics_engine.update()
        
        hits = arcade.check_for_collision_with_list(
            self._player_manager.player, self._scene_manager.scene.get_sprite_list("Coins")
        )        

        self._score_manager.hits(hits) 

        # Position the camera
        self.center_camera_to_player()
        