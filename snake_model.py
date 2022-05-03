from vector import Vector, rotated_left, rotated_right


class Snake:
    def __init__(self, head_x, head_y) -> None:
        self.direction = Vector(1, 0)
        self.body = [Vector(head_x, head_y)]
        self.length = 1
    
    def head(self):
        return self.body[0]

    def turn_left(self):
        self.direction = rotated_left(self.direction)
    
    def turn_right(self):
        self.direction = rotated_right(self.direction)
    
    def move(self):
        self.body.insert(0, self.head() + self.direction)
        self.body = self.body[:self.length]

    def elongate(self):
        self.length += 1
