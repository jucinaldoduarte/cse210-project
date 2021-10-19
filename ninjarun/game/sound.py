import arcade
from pathlib import Path
from game import constants



class Sound:
    def __init__(self):
        self.sound = None

        self.root = Path(__file__).parent

    def get_sound(self, action=None):
        if action == "coin":
            sound_source = ":resources:sounds/coin1.wav"
        elif action == "jump":
            sound_source = f"{self.root}/sounds/female_kiai_2.mp3"
            #sound_source = ":resources:sounds/jump1.wav"
        elif action == "gameover":
            sound_source = ":resources:sounds/gameover1.wav"
        else:
            sound_source = ""
        self.sound = arcade.load_sound(sound_source)


         

        