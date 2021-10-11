import arcade
from game import constants

class Scene:
    def __init__(self):
        pass 

    def draw_items(self):
        rectangle = arcade.draw_lrtb_rectangle_filled(0, constants.SCREEN_WIDTH, 200, 0, arcade.csscolor.GREEN)
        return rectangle

         