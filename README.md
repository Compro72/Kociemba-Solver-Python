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

The core parts of this project implement the two-phase algorithm that is described in detail in the link above. The 3x3x3 Rubik's cube can be represented by a string of 54 character (6 faces * 9 facelets/face = 54 facelets). Each facelet is represented by a character from ["R", "B", "Y", "O", "G", "W"] representing the facelet's colour. The order of faces is URFDLB.

```
             +---+---+---+
             | 53| 52| 51|
             +---+---+---+
             | 50| 49| 48|
             +---+---+---+
             | 47| 46| 45|
 +---+---+---+---+---+---+---+---+---+---+---+---+                  +---+
 | 33| 30| 27| 0 | 1 | 2 | 11| 14| 17| 44| 43| 42|                  | B |
 +---+---+---+---+---+---+---+---+---+---+---+---+              +---+---+---+---+
 | 34| 31| 28| 3 | 4 | 5 | 10| 13| 16| 41| 40| 39|              | L | U | R | D |
 +---+---+---+---+---+---+---+---+---+---+---+---+              +---+---+---+---+
 | 35| 32| 29| 6 | 7 | 8 | 9 | 12| 15| 38| 37| 36|                  | F |
 +---+---+---+---+---+---+---+---+---+---+---+---+                  +---+
             | 18| 19| 20|
             |---+---+---|
             | 21| 22| 23|
             |---+---+---|
             | 24| 25| 26|
             +---+---+---+
```

---

## Future Improvements

* **:** 

---

## How to Run
1. Clone this repository or download the code.
2. 
