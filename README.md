
# Breakout Game (Turtle Implementation)

A classic Breakout game implementation using Python's Turtle graphics library. Break all the colored bricks with the ball while preventing it from falling below the paddle.

## Features

- Classic Breakout gameplay using Python Turtle
- Colorful brick targets arranged in rows
- Score tracking system
- Lives system (3 attempts)
- Progressive difficulty (ball speeds up as bricks are broken)
- Simple keyboard controls

## Requirements

- Python 3.9+

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Cherund/Breakout-game.git
   cd Breakout-game
   ```

2. No additional dependencies needed (uses built-in Turtle module)

## How to Play

1. Run the game:
   ```bash
   python main.py
   ```

2. Controls:
   - **Left Arrow Key**: Move paddle left
   - **Right Arrow Key**: Move paddle right
   - **Space**: Exit game

3. Game Rules:
   - Bounce the ball with the paddle to break all bricks
   - Each broken brick increases your score (different colors may have different values)
   - The ball speeds up as you break more bricks
   - You have 3 lives to complete the level
   - Game ends when all bricks are broken or you lose all lives


## Code Overview

The game consists of several components:

1. **main.py**: Main game loop and collision detection
2. **paddle.py**: Player-controlled paddle implementation
3. **ball.py**: Ball movement and bouncing physics
4. **targets.py**: Brick targets creation and management
5. **score.py**: Score tracking and lives system

Key mechanics:
- 8 rows of colored bricks (red, orange, green, yellow)
- Ball bounces off walls, paddle, and bricks
- Progressive difficulty as game progresses

## Customization

You can easily modify:
- Game window size in `main.py`
- Brick colors and layout in `main.py` (colors array)
- Game speed by adjusting the ball movement increments
- Number of lives in `score.py`
