import pygame
from pygame.locals import *
import time
import random

SIZE = 40


class Game:
    def __init__ (self):
        pygame.init()
        pygame.display.set_caption("Jordii's Snake")
        self.screen = pygame.display.set_mode((1000,800))
        self.long = 1
        self.snake = mySnake(self.screen, 1)
        self.snake.draw()
        self.apple = myApple(self.screen)
        self.apple.draw()

    def render_background(self):
        bg = pygame.image.load("bg.jpeg")
        self.screen.blit(bg, (0,0))

    def play(self):
        self.render_background()
        self.snake.walk()
        self.apple.draw()
        self.display_score()

        #collision: apple
        if self.is_collision(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.snake.increase_long()
            self.apple.move()

        #collision: snake
        for i in range(2, self.snake.length):
            if self.is_collision(self.snake.x[0], self.snake.y[0], self.snake.x[i], self.snake.y[i]):
                raise "Collision with yourself!"
        
                #when out of bounds, tp to other side
        if not (0 <= self.snake.x[0] <= 1000 and 0 <= self.snake.y[0] <= 800):
            raise "Collision with boundaries"

    def run(self):
        running = True
        pause = False
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == K_RETURN:
                        pause = False
                    if not pause:
                        if event.key == pygame.K_UP:
                            self.snake.move_up()
                        if event.key == pygame.K_DOWN: 
                            self.snake.move_down()
                        if event.key == pygame.K_LEFT: 
                            self.snake.move_left()
                        if event.key == pygame.K_RIGHT: 
                            self.snake.move_right()
                    
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.display_game_over()
                pause = True
                self.reset()
            
            time.sleep(0.05)
    
    def is_collision(self, x1, y1, x2, y2):
        if x1 >= x2 and x1 < x2 + SIZE:
            if y1 >= y2 and y1 < y2 + SIZE:
                return True 
        return False    

    def display_score(self):
        font = pygame.font.SysFont('arial', 30)
        score = font.render(f"Score: {self.snake.length}", True, (255,255,255))
        self.screen.blit(score, (800,10))
        pygame.display.flip()

    def display_game_over(self):
        self.render_background()
        font = pygame.font.SysFont('arial', 30)
        text1 = font.render(f"Game Over! Your final score is: {self.snake.length}", True, (255,255,255))
        self.screen.blit(text1,(200,300))
        text2 = font.render(f"New game: Press ENTER", True, (255,255,255))
        self.screen.blit(text2,(200,350))
        text3 = font.render(f"Exit game: Press ESCAPE", True, (255,255,255))
        self.screen.blit(text3,(200,400))
        pygame.display.flip()
    
    def reset(self):
        self.snake = mySnake(self.screen,1)
        self.apple = myApple(self.screen)

class mySnake:
    def __init__ (self, dad_screen, length):
        self.dad_screen = dad_screen
        self.length = length
        self.player = pygame.image.load("corpse1.png")
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'right'
    
    def draw(self):
        for i in range(self.length):
            self.dad_screen.blit(self.player, (self.x[i],self.y[i]))
        pygame.display.flip()
    
    def increase_long(self):
        self.length += 1
        self.x.append(-1)
        self.y.append(-1)

    def move_up(self):
        if self.direction != 'down' or self.length == 1: self.direction = 'up'
    def move_down(self):
        if self.direction != 'up' or self.length == 1: self.direction = 'down'
    def move_left(self):
        if self.direction != 'right' or self.length == 1: self.direction = 'left'
    def move_right(self):
        if self.direction != 'left' or self.length == 1: self.direction = 'right'
    
    def walk(self):
        # only the head has the new direction and they pass its command to each other
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

    def move(self):
        self.x = random.randint(1,24)*SIZE
        self.y = random.randint(1,19)*SIZE

if __name__ == '__main__':
    game = Game()
    game.run()

    #disseny serp. que miri sempre en la direccio
    #efectes de sonido