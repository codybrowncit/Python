import game
import config
import pygame
import polygon
import point
import random
import math

class Rock(polygon.Polygon):
    def __init__(self, position, rotation, color, rotation_speed, forward_speed):
        self.rotationspeed=rotation_speed
        self.forwardspeed=forward_speed
        self.points=[]
        for i in range(0,360, 360/config.ROCK_POLYGON_SIZE):
            radius= random.uniform(config.ROCK_MIN_RADIUS, config.ROCK_MAX_RADIUS)
            radian=math.radians(i)
            x=math.cos(radian)* radius
            y=math.sin(radian)* radius
            self.points.append(point.Point(x,y))
        #self.points= [point.Point(20,20),point.Point(10,10),point.Point(30,10)]
        polygon.Polygon.__init__(self, self.points, position, rotation, color)
        self.accelerate(self.forwardspeed)
        
    def game_logic(self, keys, newkeys):
        if self.active== False:
            return
        self.move()
        self.rotate(self.rotationspeed)



