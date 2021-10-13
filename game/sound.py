import arcade

class Sound():
    def __init__(self):
        pass

    def set_sound(self, action):
        if action.lower() == "coin":
            return arcade.load_sound(":resources:sounds/coin1.wav")
        elif action.lower() == "jump":
            return arcade.load_sound(":resources:sounds/jump1.wav")
       

        


