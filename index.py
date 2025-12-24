import pygame
import random
import sys


WIDTH, HEIGHT = 600, 400
BLOCK_SIZE = 20
FPS = 10

WHITE = (255, 255, 255)
GREEN = (0, 200, 0)
RED = (200, 0, 0)
BLACK = (0, 0, 0)



class Snake:
    def __init__(self):
        self.body = [(100,100),(100+BLOCK_SIZE,100)]
        self.direction = (BLOCK_SIZE,0)


    def move(self):
        head_x, head_y = self.body[0]
        dx,dy = self.direction
        self.body.insert(0,(head_x+dx,head_y+dy))
        self.body.pop()

        

    def grow(self):
        pass

    def change_direction(self, new_direction):
        pass

    def draw(self, screen):
        for i in self.body:
            pygame.draw.rect(screen,WHITE,pygame.Rect(i[0],i[1],BLOCK_SIZE,BLOCK_SIZE))



class Food:
    def __init__(self):
       pass

    def random_position(self):
        pass

    def draw(self, screen):
        pass



class Game:
    def __init__(self):
       pygame.init()
       self.screen = pygame.display.set_mode((1280, 720))
       self.running = True
       self.clock = pygame.time.Clock()
       self.snake = Snake()

    def handle_events(self):
       pass

    def check_collision(self):
       pass

    def update(self):
        self.snake.move()

        pygame.display.flip()

    def draw(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen)
        self.snake.move()
        
        
    def run(self):
        while self.running:
           self.clock.tick(FPS)
           self.draw()
           
           self.update()
           

           
        pygame.quit()
        



if __name__ == "__main__":
    game = Game()
    game.run()
