import pygame
import random

class Snake:
    def __init__(self, length, color, pixel_width,pixel_height, pixels_per_cell):
        self.width = pixel_width/pixels_per_cell
        self.height = pixel_height/pixels_per_cell
        self.pixels_per_cell = pixels_per_cell
        self.color = color
    # color
    # shape & size
        self.body = []
        x = self.width/2
        y = self.height/2
        for segment in range(length):
            self.body.append( (x,y) )
            y+=1

        self.rate_x = 0
        self.rate_y = -1

    def move(self):
        (x,y) = self.body[0]

        x += self.rate_x
        y += self.rate_y
        if x < 0:
            x = self.width - 1
        if y < 0:
            y = self.height - 1
        if x > self.width - 1:
            x = 0
        if y > self.height - 1:
            y = 0


        collision = False
        for (bx, by) in self.body:
            if bx == x and by == y:
                collision = True

        if collision:
            r = random.randrange(0,255)
            g = random.randrange(0,255)
            b = random.randrange(0,255)
            self.color = (r,g,b)
        self.body.pop()
        self.body.insert(0, (x, y))
        

    def up(self):
        self.rate_x = 0
        self.rate_y = -1

    def down(self):
        self.rate_x = 0
        self.rate_y = 1

    def left(self):
        self.rate_x = -1
        self.rate_y = 0

    def right(self):
        self.rate_x = 1
        self.rate_y = 0

    # render (draw)
    def paint(self, surface):
        for (x,y) in self.body:
            xpixel = x * self.pixels_per_cell + self.pixels_per_cell/2
            ypixel = y * self.pixels_per_cell + self.pixels_per_cell/2
            rpixel = self.pixels_per_cell/2
            pygame.draw.circle(surface, self.color, (xpixel, ypixel), rpixel)


        
