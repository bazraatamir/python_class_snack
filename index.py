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
        pass

    def move(self):
        pass

    def grow(self):
        pass

    def change_direction(self, new_direction):
        pass

    def draw(self, screen):
        pass



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

    def handle_events(self):
       pass

    def check_collision(self):
       pass

    def update(self):
        pass

    def draw(self):
            pass

    def run(self):
        while self.running:
           pass

        pygame.quit()
        



if __name__ == "__main__":
    game = Game()
    game.run()
