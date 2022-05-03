class Vector:
    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
    
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
    
    def scaled(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __hash__(self) -> int:
        return hash((self.x, self.y))

def rotated_left(vector):
    return Vector(-vector.y, vector.x)
    
def rotated_right(vector):
    return Vector(vector.y, -vector.x)

def manhattan_distance(v1, v2):
    diff = v2 - v1
    return abs(diff.x) + abs(diff.y)

def copy(vector):
    return Vector(vector.x, vector.y)


m = {Vector(0, 0) : 0, Vector(1, 1,): 2}
print(m[Vector(0, 0)])
    