# Day 21 – Snake Game (Part 2)
# This version builds on Part 1 by introducing:
# - Food spawning and consumption
# - Snake growth
# - Wall collision detection
# - Tail collision detection
# - Score tracking with persistent high score

from snake import Snake
from turtle import Screen
from food import Food
import time
from scoreboard import Scoreboard

# Screen setup for the game window
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("Raj's Snake game")

# Disable automatic redraws for smoother animation control
screen.tracer(0)

# Core game objects
# Each object has a single responsibility:
# - Snake handles movement and body logic
# - Food handles spawning and repositioning
# - Scoreboard handles score display and persistence
snake = Snake()
food = Food()
score_board = Scoreboard()

# Keyboard bindings connect player input to snake movement
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

# Main game loop
# Runs continuously until manually exited
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    # If the snake's head is close enough to the food,
    # the snake grows, score increases, and food respawns
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score_board.score += 1
        score_board.update_score()

    # Detect collision with wall
    # If the snake crosses the screen boundary,
    # the game resets instead of ending
    if (
        snake.head.xcor() > 280
        or snake.head.xcor() < -280
        or snake.head.ycor() > 280
        or snake.head.ycor() < -280
    ):
        score_board.reset_score()
        snake.reset_snake()

    # Detect collision with tail
    # The head should not collide with any body segment
    # Excluding the head itself prevents false positives
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset_score()
            snake.reset_snake()

# Keep the window open until user clicks
screen.exitonclick()
