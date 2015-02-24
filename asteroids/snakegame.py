import game
import snake
import pygame

class SnakeGame(game.Game):
    def __init__(self, h, w):
        game.Game.__init__(self, "A fabulous snake game", h, w)
        self.snake = snake.Snake(10, (127,127,250), h, w, 20)

    def paint(self, surface):
        surface.fill((0,0,0))
        self.snake.paint(surface)

    def game_logic(self, keys, newkeys):
        if pygame.K_UP in newkeys:
            self.snake.up()
        elif pygame.K_DOWN in newkeys:
            self.snake.down()
        elif pygame.K_LEFT in newkeys:
            self.snake.left()
        elif pygame.K_RIGHT in newkeys:
            self.snake.right()
            
        self.snake.move()

def main():
    g = SnakeGame(640, 480)
    g.main_loop()

main()
