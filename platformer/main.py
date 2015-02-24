import game
import coin
import player
import mapfile
import world
import pygame
import baddy
import fire

class Platformer(game.Game):
    def __init__(self, name, map_filename, width, height, frames_per_second):
        game.Game.__init__(self, name, width, height, frames_per_second)
        self.map=map_filename
        # parse the map data
        data = mapfile.MapFile(map_filename)

        # create the world
        self.world = world.World(data)

        # create the sprites
        for elt in data.objects:
            # is this the player?
            if elt.kind == 'player':
                self.p = player.Player(self.world, elt)
                self.world.addSprite(self.p)

                # the world revolves around the player
                self.world.x = self.p.x + self.p.width / 2 - width / 2
                self.world.y = self.p.y + self.p.height / 2 - height / 2

            # is this a coin?
            elif elt.kind == 'coin':
                c = coin.Coin(self.world, elt)
                self.world.addSprite(c)
                
            # is this a baddy?
            elif elt.kind == 'baddy':
                b= baddy.Baddy(self.world, elt)
                self.world.addSprite(b)

                # is this a fireball?
            elif elt.kind == 'fire':
                self.f= fire.Fire(self.world, elt)
                self.world.addSprite(self.f)
      

            else:
                print 'Sprite of unknown type {} found'.format(elt.kind)
        
        pygame.mixer.init(44100, -16, 2, 2048)
        self.bkMusic=pygame.mixer.Sound('POL-mecha-world-short.wav')
        self.bkMusic.play(999999)
                        
    def game_logic(self, keys, newkeys):
        self.world.game_logic(keys, newkeys)
        if pygame.K_SPACE in newkeys:
            self.f.cast(self.p.x, self.p.y)
        

    def paint(self, surface):
        self.world.paint(surface)

def main():
    p = Platformer('Jewel Wizard!', 'simplemap.tmx', 480, 480, 30)
    p.main_loop()

main()
#!/usr/bin/python

