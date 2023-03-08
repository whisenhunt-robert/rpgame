# This imports the arcade feature.
import arcade

# This creates the game screen's width.
SCREEN_WIDTH = 600
# This creates the game screen's height.
SCREEN_HEIGHT = 600
# This gives the game screen a title.
SCREEN_TITLE = "Welcome to my RPG Stimulator."
RADIUS = 150

# This class creates the game screen itself.
class Screen(arcade.Window):
    # This function creates the game screen.
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        # This gives the game screen a background color. In this case, white.
        arcade.set_background_color(arcade.color.WHITE)
    
    # This function renders the game screen.
    def on_draw(self):
        arcade.start_render()

# This class is for the player, and gives the player a name and age.
class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# This creates the player and gives it the name "Robert" with the age of 36.
p1 = Player("Robert", 36)

# This finializes the code and makes it run.
if __name__ == "__main__":
    app = Screen()
    arcade.run()