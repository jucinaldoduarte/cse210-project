import arcade
from math import atan
import time
from game import constants
from game.player import Player
from game.score import Score
from game.sound import Sound
from game.map import Map
from game.scene import Scene
from game.camera import Camera
from game.mouse import Mouse
from game.physics_engine import PhysicsEngine

class Director(arcade.Window):
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller
    Attributes:
        self._score_manager
        self._map_manager
        self._sound_manager
        self._scene_manager
        self._camera_manager
        self._physics_engine_manager
        self.left_pressed
        self.right_pressed
        self.up_pressed
        self.down_pressed
        self.jump_needs_reset
        self._player        
        self._enemy
        self._map_manager.map
        self._map_manager.end_map 
        self._score_manager.score
        self._scene_manager.scene       
        self._physics_engine_manager.engine        
        self._camera_manager.camera_to_player
        self._camera_manager.camera_to_gui
        self._ammo_list
        self._red_background
        self._life
        self._track_life
        self._level
    """
    def __init__(self):
        """The super class constructor.
        
        Args:
            constants.SCREEN_WIDTH: The screen width as an integer
            constants.SCREEN_HEIGHT: The screen height as an integer
            constants.SCREEN_TITLE: The screen title as a string
        """
        super().__init__(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
        self._score_manager = Score()
        self._map_manager = Map()
        self._sound_manager = Sound()
        self._scene_manager = Scene()
        self._camera_manager = Camera()
        self._mouse_manager = Mouse()    
        self._physics_engine_manager = PhysicsEngine()
        self.left_pressed = False
        self.right_pressed = False
        self.up_pressed = False
        self.down_pressed = False
        self.jump_needs_reset = False
        self._player = None        
        self._enemy = None
        self._map_manager.map = None
        self._map_manager.end_map = 0 
        self._score_manager.score = 0
        self._scene_manager.scene = None        
        self._physics_engine_manager.engine = None        
        self._camera_manager.camera_to_player = None
        self._camera_manager.camera_to_gui = None 
        self._ammo_list = []
        self._red_background = False
        self._life = 0
        self._track_life = 0 
        self._level = 2 
        self._start_background = None                

    def setup(self):  
        """Starts the game loop to control the sequence of play.
        Args: self (Director)
        """         
        self._player = Player()
        self._life = 6 
        self._life_bar = 940
        self._track_life = 0
        self._score_manager.score = 0
        self._map_manager.level = self._level
        self._map_manager.map = self._map_manager.set_map()
        self._scene_manager.scene = self._scene_manager.set_scene(self._map_manager.map)        
        self._scene_manager.add_player(self._player)
        self._scene_manager.scene.add_sprite_list(constants.LAYER_NAME_FOREGROUND)
        self._camera_manager.camera_to_player = self._camera_manager.set_camera()
        self.camera_to_gui = self._camera_manager.set_camera()
        self._map_manager.set_background()
        self._physics_engine_manager.set_engine(self._player, self._scene_manager.scene.get_sprite_list, self._scene_manager.scene) 
        arcade.set_background_color(arcade.color.BLACK)
        self._start_background = arcade.load_texture(constants.START_BACKGROUND) 
        self._end_background = arcade.load_texture(constants.END_BACKGROUND) 
      
    def on_draw(self):
        """Render the screen.
         Args: self (Director)
        """        
        arcade.start_render()
        """Start"""
        if self._player.center_x < 327.0:
            arcade.draw_lrwh_rectangle_textured(0, 0,
                                            constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                                            self._start_background) 
        """End Game"""
        if self._player.center_x > constants.YOU_WIN:            
            arcade.draw_lrwh_rectangle_textured(0, 55,
                                            constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT,
                                            self._end_background)       

        """Cameras and Scene"""
        self._camera_manager.camera_to_player.use() 
        self._scene_manager.scene.draw()
        self.camera_to_gui.use()        

        """Score"""
        arcade.draw_text(self._score_manager.show_score(), 10, 610, arcade.csscolor.WHITE, 16,)

        """Life Bar"""
        arcade.draw_lrtb_rectangle_filled(self._life_bar, 1120, 640, 630, arcade.csscolor.WHITE)        

    def process_keychange(self):
        """Called whenever a key is pressed.
         Args: self (Director)       
        """        
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

        if self._physics_engine_manager.engine.is_on_ladder():
            if not self.up_pressed and not self.down_pressed:
                self._player.change_y = 0
            elif self.up_pressed and self.down_pressed:
                self._player.change_y = 0

        if self.right_pressed and not self.left_pressed:
            self._player.change_x = constants.PLAYER_MOVEMENT_SPEED
        elif self.left_pressed and not self.right_pressed:
            self._player.change_x = -constants.PLAYER_MOVEMENT_SPEED
        else:
            self._player.change_x = 0

    def on_key_press(self, key, modifiers):
        """Called whenever a key is pressed.
         Args: 
          - self (Director)
          - key
          - modifiers
        """
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
        """Called when the user releases a key.
        Args: 
          - self (Director)
          - key
          - modifiers
        """
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
        """Called to center camera to player.
        Args: 
          - self (Director)          
        """
        screen_center_x = self._player.center_x - (self._camera_manager.camera_to_player.viewport_width / 2)
        screen_center_y = self._player.center_y - (
            self._camera_manager.camera_to_player.viewport_height / 2
        )
        if screen_center_x < 0:
            screen_center_x = 0
        if screen_center_y < 0:
            screen_center_y = 0
        player_centered = screen_center_x, screen_center_y    
        self._camera_manager.camera_to_player.move_to(player_centered, 0.02) #0.2    

    def on_update(self, delta_time):
        """Movement and game logic
        Args: 
          - self (Director)
          - delta
          - delta_time          
        """    

        """Physics Engine"""   
        self._physics_engine_manager.engine.update()
        
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
       
        self._scene_manager.scene.update_animation(
            delta_time, [constants.LAYER_NAME_COINS, constants.LAYER_NAME_BACKGROUND, constants.LAYER_NAME_PLAYER])
  
        self._scene_manager.scene.update([constants.LAYER_NAME_MOVING_PLATFORMS])
        self._scene_manager.scene.update([constants.LAYER_NAME_KUNAI])
        self._scene_manager.scene.update([constants.LAYER_NAME_ENEMIES])

        """Walls"""
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

        coin_hit_list = arcade.check_for_collision_with_list(
            self._player, self._scene_manager.scene.get_sprite_list(constants.LAYER_NAME_COINS))
      
        kunai_hit_list = arcade.check_for_collision_with_list(
            self._player, self._scene_manager.scene.get_sprite_list(constants.LAYER_NAME_KUNAI)
            ) 
     
        if len(kunai_hit_list) > 0:
            if len(kunai_hit_list) > self._track_life:
                if self._life > 0:
                    if self._life_bar >= 760:
                        self._life_bar = self._life_bar + 30
                        self._life = self._life - 1
                elif self._life <= 0:  
                    self._sound_manager.get_sound("gameover")
                    self.setup() 
        self._track_life = len(kunai_hit_list)  
        

        for coin in coin_hit_list:
            if "Points" not in coin.properties:
                print("Warning, collected a coin without a Points property.")
            else:
                points = int(coin.properties["Points"])
                self._score_manager.score += points
                if self._life < 6:
                    self._life_bar = self._life_bar - 30
                    self._life = self._life + 1
            
            coin.remove_from_sprite_lists()
            self._sound_manager.get_sound("coin")
            arcade.play_sound(self._sound_manager.sound)
            arcade.set_background_color(arcade.color.BLACK)            

        for kunai in kunai_hit_list:  
            kunai.remove_from_sprite_lists()          
            self._sound_manager.get_sound("kunai")
            arcade.set_background_color(arcade.color.RED_DEVIL)

        """ Fall """
        if self._player.center_y < -100:
            self._sound_manager.get_sound("gameover")
            self.setup()

        """Surprise, you dead"""        
        if arcade.check_for_collision_with_list(
            self._player, self._scene_manager.scene.get_sprite_list(constants.LAYER_NAME_DONT_TOUCH)):
            self._sound_manager.get_sound("gameover")
            self.setup()

        """ End game sound"""
        if self._player.center_x > constants.YOU_WIN and self._player.center_x < constants.YOU_WIN + 10:
            self._sound_manager.get_sound("win")        
            
        """ End of level"""        
        if self._player.center_x <= self._map_manager.end_map:
            self._level += 1
            self.setup()
            
        """ Camera""" 
        self.center_camera_to_player()
