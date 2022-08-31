import pygame
from pygame.locals import *


class Game:
    def __init__ (self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,750))
        self.screen.fill((110,110,5))
        self.snake = Snake(self.screen)
        self.snake.draw()

    def run(self):
        self.crashed = False
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: crashed = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.snake.move_up()
                    if event.key == pygame.K_DOWN: 
                        self.snake.move_down()
                    if event.key == pygame.K_LEFT: 
                        self.snake.move_left()
                    if event.key == pygame.K_RIGHT: 
                        self.snake.move_right()
                    if event.key == pygame.K_ESCAPE:
                        self.crashed = True

class Snake:
    def __init__ (self, dad_screen):
        self.dad_screen = dad_screen
        self.ball = pygame.image.load("poke.png")
        self.x = 475
        self.y = 350
    
    def draw(self):
        self.dad_screen.fill((110,110,5))
        self.dad_screen.blit(self.ball, (self.x,self.y))
        pygame.display.flip()
    
    def move_up(self):
        self.y -= 25
        self.draw()
    def move_down(self):
        self.y += 25
        self.draw()
    def move_left(self):
        self.x -= 25
        self.draw()
    def move_right(self):
        self.x += 25
        self.draw()


if __name__ == '__main__':
    game = Game()
    game.run()
