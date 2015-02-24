import pygame.draw
from point import Point
import config
import shaped
import math

class Circle(shaped.Shape):
    def __init__(self, position, radius, rotation, color):
        self.position = position
        self.rotation = rotation
        self.radius= radius
        self.color = color
        self.active = True
        self.cache_points = (None, None, None)
        self.dx = 0
        self.dy = 0
        shaped.Shape.__init__(self, position, rotation, color)
        
    def paint(self, surface):
        if self.active== False:
            return
        rect= pygame.draw.circle(surface, self.color, self.position.pair(), self.radius)

    
    def rotate(self, degrees):
        degree=self.rotation+degrees
        if degree>360.00:
            degree-=360
        if degree<0.00:
            degree+=360
        self.rotation=degree

        
    def is_active(self):
        return self.active

    def set_inactive(self):
        self.active = False

    def getPoints(self):
        points=[]
        for i in range(0, 360, 360/config.BULLET_POINT_COUNT):
            radian=math.radians(i)
            x=math.cos(radian)*self.radius
            y=math.sin(radian)*self.radius
            points.append(Point(x,y))
        return points

    def contains(self, point):
        dist_x = self.position.x - point.x
        dist_y = self.position.y - point.y
        return dist_x*dist_x + dist_y*dist_y <= self.radius*self.radius
            
        
        
        
