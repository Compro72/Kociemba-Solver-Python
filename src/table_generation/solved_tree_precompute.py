from collections import deque
import file_save

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import cube_moves


def generate_solve_tree(max_depth):
    table = {}
    moves = ["u", "d", "u'", "d'", "u2", "d2", "l2", "r2", "f2", "b2"]
    queue = deque()

    start = (0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5)
    initial_state = (start, 0, [])
    queue.append(initial_state)
    visited = set()
    visited.add(start)
    table[start] = []

    while queue:
        state, depth, move_sequence = queue.popleft()

        for move in moves:
            if not move_sequence==[] and move_sequence[-1][0] in move:
                continue

            new_state = cube_moves.apply_move(state, move)

            if new_state not in visited:
                table[new_state] = move_sequence + [move]
                visited.add(new_state)
                if not depth+1==max_depth:
                    queue.append((new_state, depth+1, move_sequence + [move]))

    file_save.save_list_to_txt([table])

    return table

generate_solve_tree(6)