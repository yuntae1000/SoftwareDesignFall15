# -*- coding: utf-8 -*-
"""

"""

class BrickBreakerModel:
    """ Encodes the game state """
    def __init__(self):
        self.bricks = []
        for x in range(30,540,100):
            for y in range(20,120,30):
                brick = Brick((255,0,255),20,80,x,y)
                self.bricks.append(brick)
        self.paddle = Paddle((255,255,255),20,100,200,450)

class Brick:
    """ Encodes the state of a brick in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y

class Paddle:
    """ Encodes the state of the paddle in the game """
    def __init__(self,color,height,width,x,y):
        self.color = color
        self.height = height
        self.width = width
        self.x = x
        self.y = y
            

