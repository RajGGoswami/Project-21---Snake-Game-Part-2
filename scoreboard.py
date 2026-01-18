from turtle import Turtle

# Font configuration constants for score display
FONT_TUP = ("Arial", 14, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    """
    The Scoreboard class manages:
    - Current score
    - High score persistence using a file
    - Displaying scores on screen
    """

    def __init__(self):
        super().__init__()

        # Current game score
        self.score = 0

        # Load high score from file for persistence between sessions
        with open("data.txt") as data:
            self.high_score = int(data.read())

        self.ht()
        self.penup()
        self.goto(0, 270)
        self.color("white")

        # Display the initial score
        self.update_score()

    def update_score(self):
        """Clears and redraws the score display."""
        self.clear()
        self.write(
            f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT,
            font=FONT_TUP
        )

    def reset_score(self):
        """
        Resets the score after a collision.
        Updates the high score if the current score is greater.
        """
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))

        self.score = 0
        self.update_score()
