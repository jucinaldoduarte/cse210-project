import arcade
from game import constants

class Sound:
    def __init__(self):
        self.sound = None

    def get_sound(self, action=None):
        if action == "coin":
            sound_source = f"{constants.SOUND_DIR}/money_1.mp3"
        elif action == "jump":
            sound_source = f"{constants.SOUND_DIR}/female_kiai_2.mp3"
        elif action == "gameover":
            sound_source = ":resources:sounds/gameover1.wav"
        else:
            sound_source = ""
        self.sound = arcade.load_sound(sound_source)

        