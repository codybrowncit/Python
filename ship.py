import polygon
import game
import pygame
import config
import point
import math

class Ship(polygon.Polygon):
    def __init__(self, position, rotation, color):
##        self.points= [point.Point(60,30), point.Point(40,40), point.Point(30,50),point.Point(20,40),
##                      point.Point(10,40), point.Point(20,30), point.Point(10,20),
##                      point.Point(20,20), point.Point(30,10), point.Point(40,20)]
        self.points= [point.Point(30,20), point.Point(0,10), point.Point(0,30)]
        polygon.Polygon.__init__(self, self.points, position, rotation, color) 
        
    def game_logic(self, keys, newkeys):
        if self.active== False:
            return
        self.move()
        if pygame.K_LEFT in keys:
            self.rotation -= config.SHIP_ROTATION_RATE
        elif pygame.K_RIGHT in keys:
            self.rotation += config.SHIP_ROTATION_RATE
        elif pygame.K_UP in keys:
            self.accelerate(config.SHIP_ACCELERATION_RATE)
        elif pygame.K_DOWN in keys:
            self.accelerate(-config.SHIP_ACCELERATION_RATE)
            
    
