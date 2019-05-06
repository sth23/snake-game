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

class SnakeTail(Sprite):
    # Create asset
    black = Color(0,1)
    noline = LineStyle(0,black)
    rect = RectangleAsset(10, 10, noline, black)
    
    def __init__(self,position):
        super().__init__(SnakeTail.rect, position)
        self.age = 0
        
    def step(self):
        self.age +=1
    
class SnakeHead(Sprite):
    # Create asset
    black = Color(0,1)
    noline = LineStyle(0,black)
    rect = RectangleAsset(10, 10, noline, black)
    
    def __init__(self, position):
        super().__init__(SnakeHead.rect, position)
        self.speed = 1
        self.vy = -self.speed
        self.vx = 0
        
        SnakeGame.listenKeyEvent("keydown", "up arrow", self.moveUp)
        SnakeGame.listenKeyEvent("keydown", "down arrow", self.moveDown)
        SnakeGame.listenKeyEvent("keydown", "right arrow", self.moveRight)
        SnakeGame.listenKeyEvent("keydown", "left arrow", self.moveLeft)
        
    def moveUp(self, event):
        self.vy = -self.speed
        self.vx = 0
        
    def moveRight(self, event):
        self.vx = self.speed
        self.vy = 0
        
    def moveDown(self, event):
        self.vy = self.speed
        self.vx = 0
    
    def moveLeft(self, event):
        self.vx = -self.speed
        self.vy = 0
        
    def step(self):
        self.x += self.vx
        self.y += self.vy

class SnakeGame(App):
    
    def __init__(self):
        super().__init__()
        SnakeHead((self.width/2, self.height/2))
        
    def step(self):
        for head in self.getSpritesbyClass(SnakeHead):
            head.step()
            
        for tail in self.getSpritesbyClass(SnakeTail):
            tail.step()
            if tail.age > 20:
                tail.destroy()
        
myapp = SnakeGame()
myapp.run()