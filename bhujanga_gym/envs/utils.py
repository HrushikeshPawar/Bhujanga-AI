# bhujanga_gym/envs/utils.py

# Error Classes
# Wall Collision Error
class WallCollisionError(Exception):
    """Raised when the snake collides with the wall"""
    pass


# Collision with body Error
class BodyCollisionError(Exception):
    """Raised when the snake collides with its body"""
    pass


# Truncation Error
class TruncationError(Exception):
    """Raised when the snake travles more than the board size"""
    pass


# Point Class
class Point:
    """Class to help in defining the location of Snake's head and body and also the food"""

    # Changing it from namedtuple to normal class
    def __init__(self, x, y, parent=None, name=None):
        self.x = x
        self.y = y
        self.parent = parent
        self.name = name

    # Adding and Subtracting Points
    # Used in changing the direction of the snake
    def __add__(self, other: 'Point') -> 'Point':
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other: 'Point') -> 'Point':
        return Point(self.x - other.x, self.y - other.y)

    # Negating the point coordinates
    def __neg__(self) -> 'Point':
        return Point(-self.x, -self.y)

    # Multiplying the Point by a scalar(int) from both the sides (left and right multiplication)
    def __mul__(self, other: int) -> 'Point':
        return Point(self.x * other, self.y * other)

    def __rmul__(self, other: int) -> 'Point':
        return Point(self.x * other, self.y * other)

    # The way point object is printed on screen
    def __str__(self) -> str:
        if self.name:
            return str(self.name)
        return f"Point({self.x}, {self.y})"

    __repr__ = __str__

    # Checking if the point is equal to another point
    def __eq__(self, other: 'Point') -> bool:
        return isinstance(other, Point) and self.x == other.x and self.y == other.y

    # Checking if the point is not equal to another point
    def __ne__(self, other: 'Point') -> bool:
        return not isinstance(other, Point) or self.x != other.x or self.y != other.y

    # Creats the hash of the point object
    # Don't know why I added this
    # If I don't find any use then I will remove it
    # TODO: Find out how this can be used
    def __hash__(self) -> int:
        return hash((self.x, self.y))

    # Copying the point object
    def copy(self) -> 'Point':
        return Point(self.x, self.y)

    # Distance function
    def distance(self, other: 'Point') -> int:
        return abs(self.x - other.x) + abs(self.y - other.y)

    # Move in give direction
    def move(self, direction: 'Direction') -> 'Point':
        return self + direction


# Direction Class
class Direction:
    """Class to help in defining the direction of Snake"""

    # Four Major Directions
    UP    = Point(0, -1, name='UP')
    DOWN  = Point(0, 1, name='DOWN')
    LEFT  = Point(-1, 0, name='LEFT')
    RIGHT = Point(1, 0, name='RIGHT')

    # Four Diagonal Directions
    UP_LEFT    = Point(-1, -1)
    UP_RIGHT   = Point(1, -1)
    DOWN_LEFT  = Point(-1, 1)
    DOWN_RIGHT = Point(1, 1)

    # Eight Sub Diagonal Directions
    UP_UP_LEFT       = Point(-1, -2)
    UP_UP_RIGHT      = Point(1, -2)
    UP_LEFT_LEFT     = Point(-2, -1)
    UP_RIGHT_RIGHT   = Point(2, -1)
    DOWN_DOWN_LEFT   = Point(-1, 2)
    DOWN_DOWN_RIGHT  = Point(1, 2)
    DOWN_LEFT_LEFT   = Point(-2, 1)
    DOWN_RIGHT_RIGHT = Point(2, 1)

    # Multiplication of a point object by a scalar
    def __mul__(self, other: int) -> Point:
        return Point(self.value.x * other, self.value.y * other)

    # Multiplication of a scalar by a point object
    def __rmul__(self, other: int) -> Point:
        return Point(self.value.x * other, self.value.y * other)
