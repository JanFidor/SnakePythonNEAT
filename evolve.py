import os
import pickle
from snake_game import SnakeGame
import neat
from snake_interfaces import ai_interface
from snake_pygame import SnakeUI
from vector import manhattan_distance
import visualize

os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'

generations = 15

# Use the NN network phenotype and the discrete actuator force function.
def eval_genome(genome, config):
    # IMPORTANT
    runs_per_net = 3
    board_width = 10
    board_height = 10
    moves_limit = 1000


    net = neat.nn.FeedForwardNetwork.create(genome, config)
    fitnesses = []
    
    for _ in range(runs_per_net):
        sim = SnakeGame(board_width, board_height)              # create new snake game instance
        moves_made = 0                              
        
        # Run the given simulation for up to num_steps time steps.
        while not sim.finished and moves_made <= moves_limit:
            input = sim.are_moves_safe_bfs() + sim.new_food_distances()

            action = net.activate(input)
            
            sim.actuator(action)
            sim.move_snake()
            moves_made += 1
            
        # Evaluate genome fitness
        fitness = sim.get_fitness()
        fitnesses.append(fitness)
    # The genome's fitness is its worst performance across all runs (if multiple runs) or simply its single-run performance (if only 1 run)
    return min(fitnesses)


def main():
    # Load the config file, which is assumed to live in the same directory as this script.
    local_dir = os.path.dirname(__file__)
    config_path = os.path.join(local_dir, 'config')
    config = neat.Config(neat.DefaultGenome, neat.DefaultReproduction,neat.DefaultSpeciesSet, neat.DefaultStagnation,config_path)

    pop = neat.Population(config)
    stats = neat.StatisticsReporter()
    pop.add_reporter(stats)
    pop.add_reporter(neat.StdOutReporter(True))

    pe = neat.ParallelEvaluator(6, eval_genome)
    winner = pop.run(pe.evaluate,generations)

    # Save the winner.
    with open('winner', 'wb') as f:
        pickle.dump(winner, f)

    # Show winning neural network
    print(winner)

    node_names = {
        -1: 'collision_distance_left', -2: 'collision_distance_forward', -3: 'collision_distance_right', 
        -4: 'food_distance_left', -5: 'food_distance_forward', -6: 'food_distance_right', 
        0: 'move_left', 1: 'move_forward', 2: 'move_right'}
    visualize.draw_net(config, winner, view=True, node_names=node_names,filename="winner-enabled-pruned.gv", show_disabled=False, prune_unused=True)


    winning_net = neat.nn.FeedForwardNetwork.create(winner, config)
    
    # pygame.init()
    # sim = SnakeUI(15, 15, 20, ai_interface, 30, winning_net)

    # ########################
    # # Simulate the performance of the loaded network
    # ########################    
    # sim.gameLoop()

    # print(sim.game._snake.length)
    


if __name__ == '__main__':
    main()

