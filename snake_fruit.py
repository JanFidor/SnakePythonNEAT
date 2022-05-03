from random import choice


class Fruit:
    def __init__(self, possible_positions):
        self.pos = choice(possible_positions)