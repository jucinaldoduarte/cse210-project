import arcade
from game import constants
from game.player import Player
from game.ground import Ground
from game.scene import Scene
from game.user_control import UserControl

class Director(arcade.Window):    

    def __init__(self):
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)

        self._player_manager = Player()
        self._ground_manager = Ground()
        self._scene_manager = Scene()
        self._user_control_manager = UserControl()

        
        #self._player_manager.players = None
        #self._ground_manager.walls = None 

        self._scene_manager.scene = None 
        self._player_manager.player = None
        self._user_control_manager.physics_engine = None

        arcade.set_background_color(arcade.csscolor.PURPLE)     
        
    def setup(self):
        self._scene_manager.scene = arcade.Scene()
        self._scene_manager.scene.add_sprite_list("Player")
        self._scene_manager.scene.add_sprite_list("Walls", use_spatial_hash=True)

        # Set the player
        #self._player_manager.players = arcade.SpriteList()
        self._player_manager.set_player()       
        #self._player_manager.players.append(self._player_manager.player)
        self._scene_manager.scene.add_sprite("Player", self._player_manager.player)

        # Set the ground
        # self._ground_manager.walls = arcade.SpriteList(use_spatial_hash=True)

        for x in range(0, 1250, 64):
            self._ground_manager.set_ground(x)
            #self._ground_manager.walls.append(self._ground_manager.ground) 
            self._scene_manager.scene.add_sprite("Walls", self._ground_manager.wall) 

        #self._user_control_manager.physics_engine = self._user_control_manager.get_physics_engine() 
        self._user_control_manager.physics_engine = arcade.PhysicsEnginePlatformer(
            self._player_manager.player, self._scene_manager.scene.get_sprite_list("Walls"), constants.GRAVITY
        )      

    def on_draw(self):
        """Render the screen."""
        arcade.start_render()           
        
        # Draw the player
        # self._player_manager.players.draw()

        # Draw the ground
        # self._ground_manager.walls.draw()

        self._scene_manager.scene.draw()

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed."""

        if key == arcade.key.UP or key == arcade.key.W:
            if self._user_control_manager.physics_engine.can_jump():
                self._player_manager.player.change_y = constants.PLAYER_JUMP_SPEED
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

    def on_update(self, delta_time):
        """Movement and game logic"""

        # Move the player with the physics engine
        self._user_control_manager.physics_engine.update()
