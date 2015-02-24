from sprite import Sprite
import pygame
import sys
import mapfile

class Player(Sprite):
    def __init__(self, world, obj):
        pygame.mixer.init(44100, -16, 2, 2048)
        if obj.gid is None:
            print >>sys.stderr, 'Player: must be created from tile object'
            sys.exit(1)
        self.left=False
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
        self.count=0
        self.coins=0
        pygame.font.init()
        self.hurtSound=pygame.mixer.Sound('OOT_AdultLink_Hurt1.wav')
        self.jumpSound=pygame.mixer.Sound('OOT_AdultLink_Jump1.wav')
        self.jewelSound=pygame.mixer.Sound('LOZ_Get_Rupee.wav')
        self.dieSound=pygame.mixer.Sound('LA_Link_Dying.wav')
        self.font = pygame.font.SysFont("Times New Roman",36)
        self.font2 = pygame.font.SysFont("Courier New",20)
        self.text_color = (255,225,225)
        self.score_color = (255, 0, 0)
        self.score_x = 10
        self.score_y = 30
        self.game_x = 230
        self.game_y = 240
        self.coins=0
        self.lives=3
        self.newlife=0
        self.hurt=False
        self.active=True




            
    def drawTextLeft(self, surface, text, color, x, y,font):
        textobj = font.render(text, False, color)
        textrect = textobj.get_rect()
        textrect.bottomleft = (x, y)
        surface.blit(textobj, textrect)
        return       
        
    def paint(self, surface):
        if self.active:
            left=self.gid+344
            if pygame.K_d in self.keys:
                self.left=False
                if self.hurt:
                    if self.count<5:
                        self.paintTile(surface, self.world.data.tiles[self.gid])
                    else:
                       self.paintTile(surface, self.world.data.tiles[self.gid+3])                   
                else:
                    if self.count<5:
                        self.paintTile(surface, self.world.data.tiles[self.gid])
                    else:
                        self.paintTile(surface, self.world.data.tiles[self.gid+1])
            elif pygame.K_a in self.keys:
                self.left=True
                if self.hurt:
                    if self.count<5:
                        self.paintTile(surface, self.world.data.tiles[left])
                    else:
                        self.paintTile(surface, self.world.data.tiles[left+3])
                else:
                    if self.count<5:
                        self.paintTile(surface, self.world.data.tiles[left])
                    else:
                        self.paintTile(surface, self.world.data.tiles[left+1])
            else:
                if self.left:
                    if self.hurt:
                        if self.count>5:
                            self.paintTile(surface, self.world.data.tiles[left])
                        else:
                            self.paintTile(surface, self.world.data.tiles[left+2])
                    else:
                        self.paintTile(surface, self.world.data.tiles[left])
                else:
                    if self.hurt:
                        if self.count>5:
                            self.paintTile(surface, self.world.data.tiles[self.gid])
                        else:
                            self.paintTile(surface, self.world.data.tiles[self.gid+2])
                    else:
                        self.paintTile(surface, self.world.data.tiles[self.gid])
        else:
            self.gameover= "GAME OVER"
            self.drawTextLeft(surface, self.gameover, self.score_color, self.game_x, self.game_y, self.font2)


        self.coinstr="Jewels: " + str(self.coins)+" Lives: " + str(self.lives)
        self.drawTextLeft(surface, self.coinstr, self.score_color, self.score_x, self.score_y, self.font2)

    def set_active(self):
        self.fire=True
        
    def game_logic(self, keys, newkeys):
        if self.active:
            if self.lives<0:
                self.lives=0
            self.newlife+=1
            if self.newlife>150:
                self.newlife=0
                self.hurt=False
            self.count+=1
            if self.count>10:
                self.count=0
            self.keys=keys
            self.newkeys=newkeys
            if pygame.K_w in newkeys:
                oldy=self.y
                self.y+=1
                if ('solid' in self.world.findCollisions(self)):
                    self.jumpSound.play()
                    self.addForce('uparrow', (0.0, -20.0), 'onetime')
            if pygame.K_RETURN in keys:
                if pygame.K_s in keys:
                    self.addForce('downarrow', (0.0, 6.0), 'onetime')
                if pygame.K_a in keys:
                    self.addForce('leftarrow', (-6.0, 0.0), 'onetime')
                if pygame.K_d in keys:
                    self.addForce('rightarrow', (6.0, 0.0), 'onetime')
            else:
                if pygame.K_s in keys:
                    self.addForce('downarrow', (0.0, 3.0), 'onetime')
                if pygame.K_a in keys:
                    self.addForce('leftarrow', (-1.0, 0.0), 'onetime')
                if pygame.K_d in keys:
                    self.addForce('rightarrow', (1.0, 0.0), 'onetime')


                    
            (x, y) = (self.x, self.y)
          
            self.move()
            # move the world to match our motion
            (dx, dy) = (self.x - x, self.y - y)
            self.world.x += dx
            self.world.y += dy


        
    def handleCollisionWith(self, name, other):
        # stop when we hit a wall/edge
        if name == 'boundary' or name == 'solid':
            return True

        if other.kind == 'coin':
            self.jewelSound.play()
            self.coins+=1
            self.world.removeSprite(other)
            
        if other.kind == 'baddy':
            if self.hurt:
                return 
            else:
                self.lives-=1
                self.hurt=True
                self.newlife=1
                self.hurtSound.play()
            if self.lives==0:
                print self.lives
                self.dieSound.play()
                self.active=False
        return False
    
