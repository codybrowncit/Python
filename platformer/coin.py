from sprite import Sprite
import sys

class Coin(Sprite):
    def __init__(self, world, obj):
        if obj.gid is None:
            print >>sys.stderr, 'Coin: must be created from tile object'
            sys.exit(1)
        self.world = world
        self.gid = obj.gid
        tile = world.data.tiles[self.gid]
        self.count=0
        Sprite.__init__(self,
                world,
                obj.kind,
                '{} ({},{})'.format(obj.kind, obj.x, obj.y),
                tile.get_width(), tile.get_height(),
                obj.x, obj.y,
                (0.0, 0.0))

    def paint(self, surface):
        if self.count<5:
            self.paintTile(surface, self.world.data.tiles[self.gid])
        else:
            self.paintTile(surface, self.world.data.tiles[self.gid+2])


    def game_logic(self, keys, newkeys):
        self.count+=1
        if self.count>10:
            self.count=0
