"""
Test the performance of the best genome produced by evolve-feedforward.py.
"""

from __future__ import print_function
import os
import pickle
from snake_pygame import SnakeUI
from snake_interfaces import ai_interface
import neat
import pygame
import visualize

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

# load the winner
with open('./winner','rb') as f:
    c = pickle.load(f)

print('Loaded genome:')
print(c)

local_dir = os.path.dirname(__file__)
config_path = os.path.join(local_dir, 'config')
config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation,config_path)


node_names = {
        -1: 'is_left_safe', -2: 'is_front_safe', -3: 'is_right_safe', 
        -4: 'food_visible_left', -5: 'food_visible_forward', -6: 'food_visible_right', 
        0: 'move_left', 1: 'move_forward', 2: 'move_right'}


# Load the config file, which is assumed to live in
# the same directory as this script


net = neat.nn.FeedForwardNetwork.create(c, config)
pygame.init()
sim = SnakeUI(10, 10, 20, ai_interface, 20, net)

########################
# Simulate the performance of the loaded network
########################    
sim.game_loop_go_brrrt()


visualize.draw_net(config, c, view=True, node_names=node_names,filename="winner-enabled-pruned.gv", show_disabled=False, prune_unused=True)
print(sim.game.get_fitness())
