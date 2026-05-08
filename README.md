# Mancala Game (Python)
This is a command‑line implementation of the classic board game Mancala. The game supports two players, labeled A and B, and follows the traditional rules of sowing stones, capturing, and earning extra turns.

# Features
Fully interactive two‑player Mancala game

Capture rule implemented when landing in an empty pocket on your own side

Extra turn when landing in your own store

Automatic game‑over detection

Winner calculation at the end of the match

Simple text‑based board display

# How the Game Works
The board is represented as a list of 14 pockets:

Pocket 0 is Player A's store

Pockets 1 through 6 are Player A's side

Pocket 7 is Player B's store

Pockets 8 through 13 are Player B's side

Each non‑store pocket starts with 4 stones.

Players take turns choosing a pocket on their side. Stones are distributed counter‑clockwise, skipping the opponent's store. The game ends when one player's side is empty.

At the end, remaining stones are collected into the appropriate store and the player with the most stones wins.

# Controls
When prompted, enter the number of the pocket you want to play:

Player A chooses pockets 1 through 6

Player B chooses pockets 8 through 13

# Running the Game
Make sure you have Python installed.
Run the game with: python3 mancala.py
