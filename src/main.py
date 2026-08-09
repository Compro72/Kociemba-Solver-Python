# Umar Ahmed
# 2025
# This python project implements the Kociemba search algorithm for solving a 3x3 Rubik's cube

import solver
import cube_moves
import random
import time

scramble = input("Enter Cube Code: ")

if scramble=="R" or scramble=="r":
    scramble = "RRRRRRRRRBBBBBBBBBYYYYYYYYYOOOOOOOOOGGGGGGGGGWWWWWWWWW"
    moves = ["u", "d", "l", "r", "f", "b", "u'", "d'", "l'", "r'", "f'", "b'", "u2", "d2", "l2", "r2", "f2", "b2"]

    for i in range(1000):
        scramble = cube_moves.apply_move(scramble, moves[random.randrange(0, 18)])

    print("".join(scramble))

solution = solver.solve_cube(scramble)

print("FINAL SOLUTION:", end=" ")
for move in solution:
    print(move, end=" ")

input("\nPress Enter to exit...")