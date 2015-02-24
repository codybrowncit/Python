import math

import pygame.draw

from point import Point
import config

class Shape:
    def __init__(self, position, rotation, color):
        self.position = position
        self.rotation = rotation
        self.color = color
        self.active = True
        self.cache_points = (None, None, None)
        self.dx = 0
        self.dy = 0

    def paint(self, surface):
        raise NotImplementedError()

    def game_logic(self, keys, newkeys):
        raise NotImplementedError()

    def move(self):
        x,y= self.position.pair()
        x+= self.dx
        y+= self.dy
        if x > config.SCREEN_X:
            x = 0.0
        if y > config.SCREEN_Y:
             y = 0.0
        if y < 0:
            y = float(config.SCREEN_Y)
        if x < 0:
            x = float(config.SCREEN_X)
        self.position=Point(x,y)

    def accelerate(self, acceleration):
        angleinradians = math.radians(self.rotation)
        self.dx = self.dx + acceleration * math.cos(angleinradians)
        self.dy = self.dy + acceleration * math.sin(angleinradians)

    def intersect(self, other_polygon):
        for p in self.getPoints():
            if other_polygon.contains(p):
                return True
        for p in other_polygon.getPoints():
            if self.contains(p):
                return True
        return False

    def contains(self, point):
        NotImplementedError()

    def getPoints(self):
        NotImplementedError()

    
