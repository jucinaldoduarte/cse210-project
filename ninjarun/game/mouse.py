import arcade
from game import constants
from pathlib import Path

class Mouse(arcade.Sprite):
    """Class to manage mouse input
    
    Stereotype:
        Information Holder
        Coordinator

    Attributes:
        self (Sprite)        
    """
    def __init__(self):
        """ The class constructor

        Attributes:
            self.ammo_count - for throwable "ammo"
            self.ammo_count - a list for ammo sprites
            self.center_x - starting point for thrown object
            self.center_y - starting point for thrown object        
        """
        super().__init__()
        self._ammo_count = 0
        self._ammo_list = []
        self.center_x = 0
        self.center_y = 0

   