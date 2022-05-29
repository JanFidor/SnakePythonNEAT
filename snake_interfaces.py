import pygame
from vector import rotated_left, rotated_right

def ai_interface(sim, net):
    input = sim.are_moves_valid() + sim.new_food_distances()
    # print(sim.new_coll_distances(), sim.extra_coll_distances())
    action = net.activate(input)
    sim.actuator(action)
    sim.move_snake()
    

def human_interface(sim, net=None):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sim.finished = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                sim._snake.turn_right()
            elif event.key == pygame.K_e:
                sim._snake.turn_left()