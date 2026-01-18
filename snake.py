from turtle import Turtle

# Starting body positions for the snake
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]

# Movement and direction constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake(Turtle):
    """
    The Snake class controls:
    - Body creation
    - Movement logic
    - Growth
    - Reset behavior after collisions
    """

    def __init__(self):
        super().__init__()

        # Stores all body segments as Turtle objects
        self.segments = []

        # Create the initial snake body
        self.create_snake()

        # The head is always the first segment
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the snake using predefined starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a new body segment at the given position."""
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset_snake(self):
        """
        Resets the snake after a collision.
        Existing segments are moved off-screen and recreated.
        """
        for seg in self.segments:
            seg.goto(1000, 1000)

        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Adds a new segment to the end of the snake."""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """
        Moves the snake by shifting each segment forward
        and moving the head in the current direction.
        """
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Turns the snake upward unless moving down."""
        if self.head.heading() != DOWN:
            self.head.seth(UP)

    def down(self):
        """Turns the snake downward unless moving up."""
        if self.head.heading() != UP:
            self.head.seth(DOWN)

    def left(self):
        """Turns the snake left unless moving right."""
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)

    def right(self):
        """Turns the snake right unless moving left."""
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)
