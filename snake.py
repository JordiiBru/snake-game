import pygame
from pygame.locals import *
import time

SIZE = 50

class Game:
    def __init__ (self):
        pygame.init()
        self.screen = pygame.display.set_mode((1000,800))
        self.screen.fill((110,110,5))
        self.snake = mySnake(self.screen,6)
        self.snake.draw()
        self.apple = myApple(self.screen)
        self.apple.draw()

    def play(self):
        self.snake.walk()
        self.apple.draw()

    def run(self):
        self.crashed = False
        while not self.crashed:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: self.crashed = True
                elif event.type == pygame.KEYDOWN:
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

            self.play()
            time.sleep(0.2)

class mySnake:
    def __init__ (self, dad_screen, length):
        self.dad_screen = dad_screen
        self.length = length
        self.player = pygame.image.load("corpse1.png")
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'right'
    
    def draw(self):
        self.dad_screen.fill((171, 94, 7))
        for i in range(self.length):
            self.dad_screen.blit(self.player, (self.x[i],self.y[i]))
        pygame.display.flip()
    
    def move_up(self):
        self.direction = 'up'
    def move_down(self):
        self.direction = 'down'
    def move_left(self):
        self.direction = 'left'
    def move_right(self):
        self.direction = 'right'
    
    def walk(self):
        "only the head has the new direction and they pass its command to each other"
        for i in range(self.length-1,0,-1):
            self.x[i] = self.x[i-1]
            self.y[i] = self.y[i-1]
        
        if self.direction == 'up': self.y[0] -= SIZE
        if self.direction == 'down': self.y[0] += SIZE
        if self.direction == 'left': self.x[0] -= SIZE
        if self.direction == 'right': self.x[0] += SIZE
        self.draw()

class myApple:
    def __init__ (self, dad_screen):
        self.dad_screen = dad_screen
        self.fruit = pygame.image.load("apple.png")
        self.x = SIZE*3
        self.y = SIZE*3

    def draw(self):
        self.dad_screen.blit(self.fruit, ((self.x,self.y)))
        pygame.display.flip()

if __name__ == '__main__':
    game = Game()
    game.run()
