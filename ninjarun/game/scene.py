import arcade
from game import constants
from game.map import Map   

class Scene(Map): 
    """A code for a scene to game
    
    Stereotype:
        Information Holder

    Attributes:
        self (Scene)
        Map        
    """   
    def __init__(self):  
        """The class constructor.
        
        Args:
            self (Scene)
        """              
        self.scene = None        

    def add_player(self, player):
        """Called to add player to sprite list.
        Args: 
           - self (Player)
           - player (Player) 
        Return:
            -      
        """        
        self.scene.add_sprite(constants.LAYER_NAME_PLAYER, player)   

    def set_scene(self, map):  
        """Called to add map to the scene.
        Args: 
           - self (Scene)
           - map (Map) 
        Return:
            - return arcade.Scene     
        """              
        return arcade.Scene.from_tilemap(map)
    
    def add_throw(self, kunai):
        """Called to add throw.
        Args: 
           - self (Scene)
           - kunai (object) 
        Return:
            -      
        """        
        self.scene.add_sprite_list(constants.LAYER_NAME_THROW, kunai)

  