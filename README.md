##Clobber Game AI
#What's Clobber?

Clobber is a strategy board game for two players, similar to checkers . 
Played on a grid (like a checkerboard), the objective is to be the last player able to make a move. 
Players capture adjacent opponent pieces by moving one of their own pieces onto them. 
The game ends when a player has no legal moves remaining, resulting in a win for their opponent.

#Tech Stack

This project is built with Python, with the addition of the Pygame library for its graphical user interface and game loop management.
I'm also using standard Python libraries like copy for board state duplication (essential for AI search algorithms) and random for basic AI behaviors are also utilized.

#Algorithms

The AI players in this implementation rely on classic game theory search algorithms: Minimax and its optimized variant, Alpha-Beta Pruning. 
These algorithms explore possible future game states to determine the optimal move for the AI. 
Different AI "personalities" are achieved through various heuristics (aggressive, defensive, positional, and random) 
that evaluate the quality of a given board state, guiding the search process and defining the AI's strategic approach.
