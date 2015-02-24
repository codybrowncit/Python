from sprite import Sprite
import pygame
import sys
import random
import player



class Fire(Sprite):
    def __init__(self, world, obj):
        self.world = world
        self.gid = obj.gid
        self.x=obj.x
        self.y=obj.y
        tile = world.data.tiles[self.gid]
        Sprite.__init__(self,
                world,
                obj.kind,
                '{} ({},{})'.format(obj.kind, obj.x, obj.y),
                tile.get_width(), tile.get_height(),
                obj.x, obj.y,
                (16.0, 16.0))
        self.addForce('friction', (1.0, 0.0), 'slowdown')
        self.addForce('gravity', (0.0, 1.0), 'constant')
        self.walk=0
        self.left=False
        self.active=False
        self.burnSound=pygame.mixer.Sound('LOZ_Bomb_Blow.wav')
        self.fireSound=pygame.mixer.Sound('LOZ_Candle.wav')
        self.casting=0
   
    def cast(self, x, y):
        self.fireSound.play()
        self.x= x
        self.y= y
        self.active=True
    

        
    def paint(self, surface):
        if self.active:
            left=self.gid+344
            if self.left:
                if self.walk<5:
                    self.paintTile(surface, self.world.data.tiles[left])
                else:
                    self.paintTile(surface, self.world.data.tiles[left+1])
            else:
                if self.walk<5:
                    self.paintTile(surface, self.world.data.tiles[self.gid])
                else:
                    self.paintTile(surface, self.world.data.tiles[self.gid+1])


    def game_logic(self, keys, newkeys):
        if pygame.K_a in keys:
            self.left=True
        elif pygame.K_d in keys:
            self.left=False
        if self.active:
            self.walk+=1
            if self.walk>10:
                self.walk=0
            if self.left:
                oldx=self.x
                self.x-=1
                if ('boundary' in self.world.findCollisions(self) or 'solid' in self.world.findCollisions(self)):
                    self.active=False
                else:
                    self.x=oldx
            else:
                oldx=self.x
                self.x+=1
                if ('boundary' in self.world.findCollisions(self) or 'solid' in self.world.findCollisions(self)):
                    self.active=False
                else:
                    self.x=oldx
            if self.left:
                self.addForce('leftarrow', (-1.5, 0.0), 'onetime')
            else:
                self.addForce('rightarrow',(1.5, 0.0), 'onetime')
            self.move()
        
    def handleCollisionWith(self, name, other):
        # stop when we hit a wall/edge
        if name == 'boundary' or name == 'solid':
            return True

        if other.kind =="player":
          pass
        
        if other.kind == 'coin':
            pass

        if other.kind == 'baddy':
            self.burnSound.play()
            self.active=False
            self.world.removeSprite(other)

        return False



