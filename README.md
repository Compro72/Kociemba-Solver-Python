# Kociemba-Solver-Python

This project is a Python implementation of Kociemba's two-phase algorithm for solving the 3x3x3 Rubik's cube solver. It features pruning table generator scripts, an IDA* search algorithm using the pruning table and many utility functions that abstract and turn the cube state.

---

## Demo

![Kociemba Example](main.png)

---

## Features

- **Table Generator:** The `src/table_generation` folder features the table generation scripts for all 6 cube abstractions. Additionally, it also contains scripts to generate combined pruning tables.
- **Solved Tree:** An optimization that is not part of the original algorithm is also featured in this implementation. A tree originating from the solved state is generated so that phase 2 of the IDA* search can exit early.
- **Abstractions:** The file `cube_abstraction.py` holds utility function that abstract the cube (ex: The edge permutation abstraction holds only the positions of the edges).
- **Coordinates:** The file `state_index.py` has functions that convert abstractions into numbers. These are called coordinates in the original two-phase algorithm description.
- **Cubes Moves:** The file `cube_moves.py` contains functions that turn the given cube state. It also includes turning abstractions.
- **Heuristics:** The file `heuristic_eval.py` contains functions that return the heuristic value of the state given. This is used in the IDA* algorithm.
- **Solver:** The file `solver.py` contains main IDA* search algorithm that uses all the above feature to solve the input cube.

---

## Technical Description

[Official Kociemba's Two-Phase Algorithm Description](https://kociemba.org/cube.htm)

---

## Future Improvements

* **:** 

---

## How to Run
1. Clone this repository or download the code.
2. 
