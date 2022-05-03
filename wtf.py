import pygame

from snake_game import SnakeGame
print("a")

pygame.init()
print("b")

 
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
 
dis_width = 400
dis_height = 400
 
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game by Edureka')
 
clock = pygame.time.Clock()
 
snake_block = 20
snake_speed = 10
 
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)
 
 
def draw_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])
 
 
def draw_snake(snake_block, snake_list):
    for pos in snake_list:
        pygame.draw.rect(dis, black, [pos.x * snake_block, pos.y * snake_block, snake_block, snake_block])
 
def gameLoop():
    print("c")
    game = SnakeGame(20, 20)
    print("d")

    while not game.finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.finished = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    game._snake.turn_right()
                elif event.key == pygame.K_e:
                    game._snake.turn_left()
 
        game.move_snake()
        foodx, foody = game._fruit.pos.x * snake_block, game._fruit.pos.y * snake_block
        dis.fill(blue)
        pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
 
        draw_snake(snake_block, game._snake.body)
        draw_score(game._snake.length - 1)
 
        pygame.display.update()
 
        clock.tick(snake_speed)
    
    print("You Lost! Press C-Play Again or Q-Quit")

    while game.game_close:
            dis.fill(blue)
            draw_score(game._snake.length - 1)
            pygame.display.update()
 
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game.finished = True
                        game.game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
 
    pygame.quit()
    quit()
 
 
gameLoop()