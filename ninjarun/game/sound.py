import arcade
from pathlib import Path
from game import constants



class Sound:
    def __init__(self):
        self.sound = None

        self.root = Path(__file__).parent

    def get_sound(self, action=None):
        if action == "coin":
            sound_source = f"{constants.SOUND_DIR}/money_1.mp3"
        elif action == "jump":
            sound_source = f"{self.root}/sounds/female_kiai_2.mp3"
            #sound_source = ":resources:sounds/jump1.wav"
        elif action == "gameover":
            sound_source = f"{self.root}/sounds/hard_hit_2.mp3"
        elif action == "throw":
            sound_source = f"{self.root}/sounds/shuriken_throw_1.mp3"
        elif action == "stick":
            sound_source = f"{self.root}/sounds/shuriken_stick.mp3"
        else:
            sound_source = ""
        self.sound = arcade.load_sound(sound_source)


         

        