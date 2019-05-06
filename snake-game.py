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
    topwalls = RectangleAsset(self.width, 10, noline, black)
    sidewalls = RectangleAsset(10, self.height, noline, black)
    

        

class SnakeGame(app):
    
    def __init__(self):
        super().__init__()