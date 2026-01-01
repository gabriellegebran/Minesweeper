# Minesweeper
A fully functional Minesweeper game implemented in Python, playable in the terminal/console. This project includes board generation, mine placement, flagging, revealing cells, difficulty levels, and an automatic solver.

## Features
- Custom board size (rows & columns)
- Difficulty levels:
  - EASY (10% mines)
  - MEDIUM (30% mines)
  - HARD (50% mines)
- Random mine placement
- Flag / unflag cells
- Automatic neighbor mine counting
- Lose instantly when revealing a mine
- Win when all non-mine cells are revealed
- Built-in logical solver (no guessing)

## Technologies Used
- Pyhton 3
- Standard library only (random)

## How the Game Works
The game uses two boards:
- Helper Board (int values):
  - mine : -1
  - number of adjacent mines: 0-8
- Game Board (str values):
  - unrevealed: ?
  - flagged: ⚑
  - revealed numbers: 0-8
The helper board is hidden from the player and used for logic.

## Learning Objectives
- 2D list manipulation
- Game logic design
- Input validation
- Randomization
- Recursion-free logical solving
- Clean functional decomposition
- Algorithmic thinking

## Possible Improvements
- Add a graphical interface
- Add input validation
- Save/load games

## License 
This project is intended for educational purposes and is free to use, modify, and learn from.
