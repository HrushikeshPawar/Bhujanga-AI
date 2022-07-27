"""This defines the base Snake Class which all other snakes will inherit from"""
# /bhujanga_ai/snakes/BaseSnake.py


# Import the required modules
from random import randint, sample
from collections import deque


# Import Helper Classes
from helper import Point, Direction, WallCollisionError, BodyCollisionError


# Required Constants
DIRECTIONS = [Direction.UP, Direction.DOWN, Direction.LEFT, Direction.RIGHT]


# The BaseSnake Class
class BaseSnake:
    """The base snake class"""

    def __init__(self, height : int, width : int, random_init : bool = False) -> None:

        # Initialize the snake's environment (board)
        self.board_width = width
        self.board_height = height

        # Initialize the snake's initial position (snake's head)
        # Here we can take two approaches:
        # 1. Random Initialization
        # 2. Fixed Initialization
        self._initialize_snake(random_init)

        # Place the food at random location on the board
        # I first thought of placing the food at random location as well as fixed location on the board
        # But then I decided to just place it randomly
        self._place_food()

        # Initialize the snake's score
        self.score = len(self.body)

    # Initialize the snake (snake's head location)
    def _initialize_snake(self, random_init : bool) -> None:
        """Initialize the snake at random location or fixed location (center of board)"""

        # Initialize the snake's head at random location
        if random_init:
            self.head = Point(randint(0, self.board_width - 1), randint(0, self.board_height - 1))
            self.direction = sample(DIRECTIONS, 1)[0]

            # Here we use `deque` to store the snake's body
            # It has faster appending and popping operations compared to list
            # self.body = deque([self.head])
            # Thoughts: Not storing head in the body
            self.body = deque()

        # Initialize the snake's head at fixed location (center of board moving right)
        else:
            self.head = Point(self.board_width // 2, self.board_height // 2)
            self.direction = Direction.RIGHT
            self.body = deque()

        self.tail = None

    # Place the food at random location on the board
    def _place_food(self) -> None:
        """Place the food at random location on the board"""

        # Place the food at random location
        # But check if the food is on the snake's body
        # If so, then place the food at random location again
        while True:
            self.food = Point(randint(1, self.board_width - 2), randint(1, self.board_height - 2))
            if self.food not in self.body:
                break

    # Move the snake in given direction
    def move(self, direction : Direction) -> None:
        """Move the snake in given direction"""

        # Check if given direction is from Direction class
        if not isinstance(direction, Point):
            raise TypeError("Direction must be from Direction class")
            # pass

        # Check if the given direction is valid
        if direction not in DIRECTIONS:
            raise ValueError("Direction must be one of the following: UP, DOWN, LEFT, RIGHT")
            # pass

        # Check if the given direction is not the opposite of the current direction
        elif direction == -self.direction:
            # raise ValueError("Direction must be different from the opposite of the current direction")
            pass

        else:
            # Update the snake's direction
            self.direction = direction

            # Update the snake's head position
            self.body.appendleft(self.head)
            self.head = self.head + self.direction

            # Check for any collisions (with walls, snake's body or food)
            # Update the snake's body accordingly
            self._check_collisions()

    # Check for any collisions (with walls, snake's body or food)
    def _check_collisions(self) -> None:
        """Check for any collisions (with walls, snake's body or food)"""

        # Check if the snake's head is out of bounds
        if self.head.x < 0 or self.head.x > self.board_width - 1 or self.head.y < 0 or self.head.y > self.board_height - 1:
            # raise ValueError("Snake's head is out of bounds")
            raise WallCollisionError

        # Check if the snake's head is on the food
        if self.head == self.food:
            # Place the food at random location on the board
            self._place_food()
            self.score += 1
        else:
            # Update the snake's body accordingly
            self.body.pop()

        # Check if the snake's head is on the snake's body
        # We check this after updating the snake's body
        # Otherwise it may wrongly detect the snake's head as on the snake's body
        # Specifically the tail point
        if self.head in self.body or self.head == self.tail:
            # raise ValueError("Snake's head is on the snake's body")
            raise BodyCollisionError

    # Printing the Snake Object
    def __str__(self) -> str:
        return f'''Snake(\n\thead\t  = {self.head},\n\tbody\t  = {self.body},\n\tdirection =   {self.direction}\n)'''
