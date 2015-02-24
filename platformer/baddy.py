from sprite import Sprite
import pygame
import sys
import random
import player
import fire

class Baddy(Sprite):
    def __init__(self, world, obj):
        if obj.gid is None:
            print >>sys.stderr, 'Baddy: must be created from tile object'
            sys.exit(1)
        self.world = world
        self.gid = obj.gid
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
        self.left=True


        
        
    def paint(self, surface):
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
        self.walk+=1
        if self.walk>10:
            self.walk=0
        oldx=self.x
        oldy=self.y
        if self.left:
            self.x-=1
            if ('boundary' in self.world.findCollisions(self) or 'solid' in self.world.findCollisions(self)):
                self.left=False
            self.x=oldx
            self.y+=1
            self.x-=1
            if ('solid' in self.world.findCollisions(self)):
                self.y=oldy
                self.x=oldx
            else:
                self.left=False
                self.x=oldx
                self.y=oldy          
        else:
            self.x+=1
            if ('boundary' in self.world.findCollisions(self) or 'solid' in self.world.findCollisions(self)):
                self.left=True
            self.x=oldx
            self.y+=1
            self.x+=1
            if ('solid' in self.world.findCollisions(self)):
                self.y=oldy
                self.x=oldx
            else:
                self.left=True
                self.x=oldx
                self.y=oldy
        if self.left:
            self.addForce('leftarrow', (-1.0, 0.0), 'onetime')
        else:
            self.addForce('rightarrow',(1.0, 0.0), 'onetime')
        self.move()
        
    def handleCollisionWith(self, name, other):
        # stop when we hit a wall/edge
        if name == 'boundary' or name == 'solid':
          return True
        if other.kind == 'coin':
            pass
        if other.kind== 'fire':
            pass



        return False


