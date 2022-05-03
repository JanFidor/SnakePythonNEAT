from numpy import block
import pygame
import constants

from snake_game import SnakeGame
 
class SnakeUI:
    def __init__(self, width, height, block_size, interaction_interface, game_speed, net=None):
        self.interaction_interface = interaction_interface
        self.net = net

        self.block_size = block_size
        self.dis = pygame.display.set_mode((width *  block_size, height * block_size))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("comicsansms", 35)

        self.game = SnakeGame(width, height)
        self.game_speed = game_speed

    def display_title(self):
        pygame.display.set_caption('Snake Game')

    def draw_score(self):
        value = self.font.render("Your Score: " + str(self.game._snake.length - 1), True, constants.yellow)
        self.dis.blit(value, [0, 0])
    
    
    def draw_snake(self, snake_list):
        for pos in snake_list:
            pygame.draw.rect(self.dis, constants.black, 
            [pos.x * self.block_size, (pos.y) * self.block_size, self.block_size, self.block_size])
    
    def game_loop_go_brrrt(self):
        
        while not self.game.finished:
            pygame.display.update()
            stop = True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game.finished = True
                if event.type == pygame.K_SPACE:
                    self.game.move_snake()
                    print(self.game._snake.head().x, self.game._snake.head().y)

            self.interaction_interface(self.game, self.net)

            food_x = self.game._fruit.pos.x * self.block_size
            food_y = self.game._fruit.pos.y * self.block_size

            self.dis.fill(constants.white)
            pygame.draw.rect(self.dis, constants.green, [food_x, food_y, self.block_size, self.block_size])
    
            self.draw_snake(self.game._snake.body)
            self.draw_score()
    
            pygame.display.update()
            self.clock.tick(self.game_speed)

    
        pygame.quit()
