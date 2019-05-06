"""
Final Project: Snake Game
Author: Sean
Credit: Tutorials

Assignment:
Create an old-school snake game
"""

from ggame import App, RectangleAsset, Sprite, LineStyle, Color
import math
import random

class Apple(Sprite):
    # Create asset
    black = Color(0,1)
    noline = LineStyle(0,black)
    rect = RectangleAsset(10, 10, noline, black)
    
    def __init__(self, position):
        super().__init__(Apple.rect, position)

class SnakeTail(Sprite):
    # Create asset
    black = Color(0,1)
    noline = LineStyle(0,black)
    rect = RectangleAsset(10, 10, noline, black)
    
    def __init__(self, position, maxage):
        super().__init__(SnakeTail.rect, position)
        self.age = 0
        self.maxage = maxage
        
    def step(self):
        self.age +=1
        
class Wall(Sprite):
    # Create asset
    black = Color(0,1)
    noline = LineStyle(0,black)
    rect = RectangleAsset(10, 10, noline, black)
    
    def __init__(self, position, asset):
        super().__init__(asset, position)
    
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
        self.length = 1
        
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
        
    def eatApple(self):
        self.length += 1
        self.speed += 0.2
        
    def step(self):
        self.x += self.vx
        self.y += self.vy

class SnakeGame(App):
    def __init__(self):
        super().__init__()
        SnakeHead((self.width/2, self.height/2))
        Apple((random.randint(20,self.width-20), random.randint(20,self.height-20)))
        
        #Create walls
        black = Color(0,1)
        noline = LineStyle(0,black)
        topbottomrect = RectangleAsset(self.width, 10, noline, black)
        siderect = RectangleAsset(10, self.height, noline, black)
        topwall = Wall((0,0), topbottomrect)
        leftwall = Wall((0,0), siderect)
        rightwall = Wall((self.width-10,0), siderect)
        bottomwall = Wall((0,self.height-10),topbottomrect)
        
        self.tailcollision = []
        
    def step(self):
        for head in self.getSpritesbyClass(SnakeHead):
            head.step()
            
            # Eat apple
            if head.collidingWithSprites(Apple):
                head.eatApple()
                self.getSpritesbyClass(Apple)[0].destroy()
                Apple((random.randint(20,self.width-20), random.randint(20,self.height-20)))
                [x.maxage += 10 for x in self.getSpritesbyClass(SnakeTail)]
                
            # Create snake tail with appropriate age
            SnakeTail((head.x, head.y), head.length * 10)
            
            # Check for collisions with tail
            self.tailcollision = head.collidingWithSprites(SnakeTail)
            if self.tailcollision and self.tailcollision[0].age > 20:
                head.destroy()
            
            #Check for collisions with walls
            if head.collidingWithSprites(Wall):
                head.destroy()

        for tail in self.getSpritesbyClass(SnakeTail):
            tail.step()
            if tail.age > tail.maxage:
                tail.destroy()
        
myapp = SnakeGame()
myapp.run()