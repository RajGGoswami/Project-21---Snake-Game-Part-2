from turtle import Turtle
import random


class Food(Turtle):
    """
    The Food class represents the consumable object for the snake.
    It inherits from Turtle so it can be positioned and styled easily.
    """

    def __init__(self):
        """Initializes the food with a shape, color, and random position."""
        super().__init__()
        self.shape("turtle")
        self.penup()

        # Make the food smaller than a normal turtle
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)

        self.color("blue")
        self.speed("fastest")

        # Place the food at a random location on creation
        self.refresh()

    def refresh(self):
        """
        Moves the food to a new random location within the screen bounds.
        Called when the snake eats the food.
        """
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
