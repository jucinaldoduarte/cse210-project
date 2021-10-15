import arcade
from game.director import Director

def main():
    """Main function"""
    director = Director()
    director.setup()
    arcade.run()

if __name__ == "__main__":
    main()