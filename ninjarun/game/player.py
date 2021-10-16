import arcade
from game import constants


class Player(arcade.Sprite):
    """Player Sprite"""

    def __init__(self):
        
        super().__init__()

        self.gender = "girl"
        self.weapon = None        
        self.scale = constants.SCALE
        self.direction = constants.RIGHT  
        self.present_texture = 0 

        self.center_x = constants.PLAYER_START_X
        self.center_y = constants.PLAYER_START_Y

        # State
        self.attack = False
        self.climb = False
        self.dead = False
        self.glide = False
        self.idle = False
        self.jump = False
        self.jump_attack = False
        self.jump_throw = False
        self.slide = False

        # Default images
        self.image_attack = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\attack__000.png")
        self.image_climb = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\climb__000.png")
        self.image_dead = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\dead__000.png")
        self.image_glide = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\glide__000.png")        
        self.image_idle = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\idle__000.png")
        self.image_jump = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\jump__000.png")
        self.image_jump_attack = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\jump_attack__000.png")
        self.image_jump_throw = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\jump_throw__000.png")
        self.image_jump_slide = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\slide__000.png")

        # Textures lists
        self.attack_textures = []
        self.climb_textures = []
        self.dead_textures = []
        self.glide_textures = []
        self.idle_textures = []
        self.jump_textures = []
        self.jump_attack_textures = []
        self.jump_throw_textures = []
        self.slide_textures = []
        self.walk_textures = []
        self.walk_textures = []
        
        # Load textures - WE NEED TO CHANGE TO ONE FUNCTION
        for i in range(10):
            texture = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\attack__00{i}.png")
            self.attack_textures.append(texture)

        for i in range(10):
            texture = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\climb__00{i}.png")
            self.climb_textures.append(texture)

        for i in range(10):
            texture = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\dead__00{i}.png")
            self.dead_textures.append(texture)

        for i in range(10):
            texture = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\glide__00{i}.png")
            self.glide_textures.append(texture)

        for i in range(10):
            texture = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\idle__00{i}.png")
            self.idle_textures.append(texture)

        for i in range(10):
            texture = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\jump__00{i}.png")
            self.jump_textures.append(texture)

        for i in range(10):
            texture = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\jump_attack__00{i}.png")
            self.jump_attack_textures.append(texture)

        for i in range(10):
            texture = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\jump_throw__00{i}.png")
            self.jump_throw_textures.append(texture)

        for i in range(10):
            texture = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\slide__00{i}.png")
            self.slide_textures.append(texture)        
        
        for i in range(10):
            texture = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\run__00{i}.png")
            self.walk_textures.append(texture)
       
        # Initial image
        self.texture = self.image_idle[0]

        # Hit box
        self.hit_box = self.texture.hit_box_points

    def get_image(self, filename):
        return [
        arcade.load_texture(filename),
        arcade.load_texture(filename, flipped_horizontally=True),
        ]

    def load_image(self, action):       
        for i in range(10):
            texture = self.get_image(f"{constants.IMAGE_DIR }\\{self.gender}\\run__00{i}.png")
            if action == "walk":
                self.walk_textures.append(texture)        

    def update_animation(self, delta_time: float = 1 / 60):
        # Left or right
        if self.change_x < 0 and self.direction == constants.RIGHT:
            self.direction = constants.LEFT_FACING
        elif self.change_x > 0 and self.direction == constants.LEFT_FACING:
            self.direction = constants.RIGHT   

        # Attack        

        # Climb
        if self.is_on_ladder:
            self.climb = True
        if not self.is_on_ladder and self.climb:
            self.climb = False
        if self.climb and abs(self.change_y) > 1:
            self.present_texture += 1
            if self.present_texture > 9:
                self.present_texture = 0
        if self.climb:
            self.texture = self.climb_textures[self.present_texture // 4]
            return

        # Dead
        # ADD CODE HERE

        # Glide
        # ADD CODE HERE

        # Idle 
        if self.change_x == 0:
            self.texture = self.image_idle[self.direction]
            return
        
        # Jump
        if self.change_y > 0 and not self.is_on_ladder:
            self.texture = self.image_jump[self.direction]
            return
        elif self.change_y < 0 and not self.is_on_ladder:
            self.texture = self.image_dead[self.direction]
            return

        # Jump attack
        # ADD CODE HERE

        # Jump throw
        # ADD CODE HERE

        # Slide 
        # # ADD CODE HERE       

        # Walk
        self.present_texture += 1
        if self.present_texture > 9:
            self.present_texture = 0
        self.texture = self.attack_textures[self.present_texture][
            self.direction
        ]


    

        
