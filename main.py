import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Welcome to my RPG Stimulator."
RADIUS = 150

class Screen(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE)
    
    def on_draw(self):
        arcade.start_render()

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Player("Robert", 36)

if __name__ == "__main__":
    app = Screen()
    arcade.run()