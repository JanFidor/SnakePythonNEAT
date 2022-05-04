import math
from snake_model import Snake
from snake_fruit import Fruit
import itertools as iter
from vector import Vector, manhattan_distance, rotated_left, rotated_right, copy

class SnakeGame:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height

        self.finished = False

        # order important, fruit won't start inside snake
        self._snake = Snake(self.width // 2, self.height // 2)
        self._fruit = Fruit(self.get_empty_positions())
    
    def get_empty_positions(self):
        all_squares = tuple(iter.product(range(self.width), range(self.height)))
        all_vectors = map(lambda x: Vector(x[0], x[1]), all_squares)
        empty_vectors = filter(lambda x: x not in self._snake.body, all_vectors)
        return tuple(empty_vectors)

    def replace_food(self):
        self._fruit = Fruit(self.get_empty_positions())

    def move_snake(self):
        self._snake.move()
        if self._snake.head() == self._fruit.pos:
            self._snake.elongate()
            self.replace_food()
        self.check_game_finished()
        
    def check_game_finished(self):
        if self.is_colliding(self._snake.head()):
            self.finished = True
    
    def is_colliding(self, vector):
        return any((
            vector in self._snake.body[1:],
            not 0 <= vector.x < self.width,
            not 0 <= vector.y < self.height
            ))

    def straight_line_to_food(self, direction):
        new_pos = copy(self._snake.head())
        while not self.is_colliding(new_pos):
            new_pos += direction
            if new_pos == self._fruit.pos:
                return 1
        return 0
    
    def new_coll_distances(self):
        return (
            1 - self.is_colliding(self._snake.head() + rotated_left(self._snake.direction)),
            1 - self.is_colliding(self._snake.head() + self._snake.direction),
            1 - self.is_colliding(self._snake.head() + rotated_right(self._snake.direction))
        )

    def extra_coll_distances(self):
        return (
                self.is_safe(rotated_left(self._snake.direction)),
                self.is_safe(self._snake.direction) ,
                self.is_safe(rotated_right(self._snake.direction))
            )
    
    

    def is_safe(sim, direction):
        start = sim._snake.head() + direction
        queue = [(start, direction)]
        visited = set()


        while queue:
            pos, dir = queue.pop(0)
            visited.add(pos)
            possible_moves = (rotated_left(dir), dir, rotated_right(dir))
            
            if sim.is_colliding(pos): continue
            
            for move in (possible_moves):
                new_pos = pos + move
                if new_pos == sim._fruit.pos:
                    return 1
                if len(visited) > sim.width * sim.height // 4:
                    return 1
                if not sim.is_colliding(new_pos) and new_pos not in visited:
                    queue.append((new_pos, move))
        return 0

    def new_food_distances(self):
        return (
            self.straight_line_to_food(rotated_left(self._snake.direction)),
            self.straight_line_to_food(self._snake.direction),
            self.straight_line_to_food(rotated_right(self._snake.direction))
        )

    def get_angle_to_food(self):
        fruit_pos = self._fruit.pos
        head = self._snake.head()
        return math.atan2(-fruit_pos.y + head.y, -fruit_pos.x + head.x)

    def get_distance_to_food(self):
        fruit_pos = self._fruit.pos
        head = self._snake.head()
        return manhattan_distance(fruit_pos, head)

    def actuator(self, weights):
        best_action_index = max(enumerate(weights), key=lambda x: x[1])[0]

        if best_action_index == 0:
            self._snake.turn_left()
        if best_action_index == 2:
            self._snake.turn_right()
    
    def get_fitness(self):
        negative_points =  0 if (self.finished and self._snake.length != self.width * self.height) else 0
        return self._snake.length + negative_points - 1



# game = SnakeGame(10, 10)

# game._snake.body.append(Vector(7, 7))
# print(game._snake.head().x, game._snake.head().y)
# print(game.get_angle_to_food())
# print(game.get_collision_distances())
