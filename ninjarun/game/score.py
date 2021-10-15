import arcade
from game.sound import Sound

class Score:
    def __init__(self):
        self.points = 0
        self._sound_manager = Sound()

    def count_points(self):        
        score_text = f"Score: {self.points}"
        arcade.draw_text(
            score_text,
            10,
            600,
            arcade.csscolor.WHITE,
            18,
        )
    
    def hits(self, hits):
        # Loop through each coin we hit (if any) and remove it
        for coin in hits:
            # Remove the coin
            coin.remove_from_sprite_lists()
            # Play a sound
            sound = self._sound_manager.set_sound("coin")
            arcade.play_sound(sound)
            # Increment score
            self.points += 1

    def hits_shuriken(self, hits):
        # Loop through each coin we hit (if any) and remove it
        for shuriken in hits:
            # Remove the coin
            shuriken.remove_from_sprite_lists()
            # Play a sound
            sound = self._sound_manager.set_sound("shuriken")
            arcade.play_sound(sound)
            # Decrement score
            self.points -= 1
        

