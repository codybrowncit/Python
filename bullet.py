import circle
import game
import pygame
import config
import point
import math

class Bullet(circle.Circle):
    def __init__(self, position, radius, rotation, color):
        circle.Circle.__init__(self, position, radius, rotation, color)
        self.active= False

    def game_logic(self, keys, newkeys):
        if not self.is_active():
            return
        x,y=self.position.pair()
        if x+self.dx > config.SCREEN_X:
            self.set_inactive()
        elif y+self.dy > config.SCREEN_Y:
            self.set_inactive()
        elif x+self.dx < 0:
            self.set_inactive()
        elif y+self.dy < 0:
            self.set_inactive()
        else:
             self.move()

    def fire(self, position, rotation):
        self.position= position
        self.rotation= rotation
        self.set_active()
        self.dx=0
        self.dy=0
        self.accelerate(config.BULLET_SPEED)
        
    def get_rotation(self):
        return self.rotation

    def set_active(self):
        self.active=True
        
