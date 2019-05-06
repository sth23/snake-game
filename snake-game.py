"""
Final Project: Snake Game
Author: Sean
Credit: Tutorials

Assignment:
Create an old-school snake game
"""

from ggame import App, RectangleAsset, CircleAsset, ImageAsset, Sprite, LineStyle, Color, Frame
import math
import random

class Wall(Sprite):
    # Colors
    black = Color(0,1)
    noline = LineStyle(0,black)
    # Rectangle Assets
    #topwalls = RectangleAsset(self.width, 10, noline, black)
    #sidewalls = RectangleAsset(10, self.height, noline, black)
    
#class Apple(Sprite):
    
class Snake(Sprite):
    # Create asset
    black = Color(0,1)
    noline = LineStyle(0,black)
    rect = RectangleAsset(10, 10, Snake.noline, Snake.black)
    
    def __init__(self, position):
        super().__init__(Snake.rect, position)

class SnakeGame(App):
    
    def __init__(self):
        super().__init__()
        Snake((self.width/2, self.height/2))
        
myapp = SnakeGame()
myapp.run()