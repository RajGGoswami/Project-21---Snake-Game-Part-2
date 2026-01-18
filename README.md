# Project-21---Snake-Game-Part-2

Snake Game – Part 2 (Food, Collisions & Scoreboard)

This project is part of my 100 Days of Code (Python) journey and builds directly on Snake Game – Part 1.

Part 2 introduces gameplay mechanics that turn the project into a complete, replayable game.

**Project Overview**

This version of the Snake game includes:

Food spawning and consumption

Snake growth on eating food

Wall collision detection

Tail collision detection

Score tracking

Persistent high score storage using a file

**Why this project exists**

This project was built to practice:

Multi-class game architecture

Collision detection logic

File handling for persistent data

Game state resets instead of hard endings

Coordinating multiple interactive objects

**What I learned**

How independent classes communicate through a game loop

Why separating responsibilities simplifies game logic

How to store and retrieve persistent data

How to reset game state cleanly

How to scale a project incrementally without refactoring early

**How the game works (high level)**

The screen initializes and disables auto-refresh.

Snake, Food, and Scoreboard objects are created.

The game loop:

Updates the screen

Moves the snake

Detects food collisions

Detects wall collisions

Detects tail collisions

On collision:

Score resets

Snake resets

High score persists

**Project File Structure**

├── main.py          # Game loop and collision handling

├── snake.py         # Snake movement, growth, and reset logic

├── food.py          # Food spawning and repositioning

├── scoreboard.py   # Score display and high score persistence

├── data.txt        # Stores the high score


**Design Notes**

The game resets instead of ending to encourage replayability

Logic is intentionally simple and readable

No premature optimizations or refactors

Each class has a single, clear responsibility
