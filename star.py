import circle
import game
import pygame
import config
import point
import math
import random

class Star(circle.Circle):
    def __init__(self, position, radius, rotation, color):
        circle.Circle.__init__(self, position, radius, rotation, color)
        self.x,self.y,self.z=color
        #print self.x

        

    def game_logic(self, keys, newkeys):
        plusormin= random.randint(-1,1)
        self.brightness= random.randrange(0, config.STAR_TWINKLE_SPEED)*plusormin
        self.x+=self.brightness
        self.y+=self.brightness
        self.z+=self.brightness
        if self.x>255:
            self.x=255
        if self.y>255:
            self.y=255
        if self.z>255:
            self.z=255
        if self.x<0:
            self.x=0
        if self.y<0:
            self.y=0
        if self.z<0:
            self.z=0    
        self.color=(self.x,self.y,self.z)

       
        
        
