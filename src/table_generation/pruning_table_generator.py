from collections import deque
import time
import file_save

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import cube_moves
import state_index


def generate_UD_slice_table():
    #UR, UF, UL, UB, DR, DF, DL, DB, FR, FL, BL, BR
    #0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11
    table = [None]*495
    
    moves = ["u", "d", "l", "r", "f", "b", "u'", "d'", "l'", "r'", "f'", "b'", "u2", "d2", "l2", "r2", "f2", "b2"]
    #moves = ["u", "d", "l", "r", "f", "b", "u'", "d'", "l'", "r'", "f'", "b'"]
    queue = deque()
    visited = set()
    queue.append((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11))
    layer = []
    depth = 0

    while True:
        if None not in table:
            break

        current = queue.popleft()
        visited.add(current)

        index = state_index.get_UD_slice_index(current)
        if table[index]==None:
            table[index] = depth

        for move in moves:
            state = cube_moves.move_edge_permutation(current, move)
            if state not in visited:
                layer.append(state)

        if len(queue)==0:
            depth += 1
            for item in layer:
                queue.append(item)
            layer = []

    return table


def generate_corner_orientation_table():
    table = [None]*2187

    moves = ["u", "d", "l", "r", "f", "b", "u'", "d'", "l'", "r'", "f'", "b'", "u2", "d2", "l2", "r2", "f2", "b2"]
    #moves = ["u", "d", "l", "r", "f", "b", "u'", "d'", "l'", "r'", "f'", "b'"]
    queue = deque()
    visited = set()
    queue.append((0, 0, 0, 0, 0, 0, 0, 0))
    layer = []
    depth = 0

    while True:
        if None not in table:
            break

        current = queue.popleft()
        visited.add(current)

        index = state_index.get_corner_orientation_index(current)
        if table[index]==None:
            table[index] = depth

        for move in moves:
            state = cube_moves.move_corner_orientation(current, move)
            if state not in visited:
                layer.append(state)

        if len(queue)==0:
            depth += 1
            for item in layer:
                queue.append(item)
            layer = []

    return table


def generate_edge_orientation_table():
    table = [None]*2048

    moves = ["u", "d", "l", "r", "f", "b", "u'", "d'", "l'", "r'", "f'", "b'", "u2", "d2", "l2", "r2", "f2", "b2"]
    #moves = ["u", "d", "l", "r", "f", "b", "u'", "d'", "l'", "r'", "f'", "b'"]
    queue = deque()
    visited = set()
    queue.append((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0))
    layer = []
    depth = 0

    while True:
        if None not in table:
            break

        current = queue.popleft()
        visited.add(current)

        index = state_index.get_edge_orientation_index(current)
        if table[index]==None:
            table[index] = depth

        for move in moves:
            state = cube_moves.move_edge_orientation(current, move)
            if state not in visited:
                layer.append(state)

        if len(queue)==0:
            depth += 1
            for item in layer:
                queue.append(item)
            layer = []

    return table


def generate_flip_UD_slice_table():
    table = [None] * 1013760
    moves = ["u", "d", "l", "r", "f", "b", "u'", "d'", "l'", "r'", "f'", "b'", "u2", "d2", "l2", "r2", "f2", "b2"]
    queue = deque()

    # [Edge Orientation, UD_slice, depth, move]
    initial_state = ((0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), 0, "0")
    queue.append(initial_state)
    table[0] = 0

    depth = 0
    unsolved_count = len(table)  # Track unsolved entries
    start_time = time.time()

    while queue:
        if time.time() - start_time > 1:
            print(f"Queue Length: {len(queue)}")
            print(f"Number Solved: {len(table) - unsolved_count}")
            print(f"Depth: {depth}")
            print(f"Unsolved Count: {unsolved_count}")
            print("_____________________________________")
            start_time = time.time()

        if unsolved_count == 0:
            break

        current_edge_orientation, current_UD_slice, depth, prev_move = queue.popleft()

        for move in moves:
            if prev_move[0] in move:  # Skip redundant moves
                continue

            state_edge_orientation = cube_moves.move_edge_orientation(current_edge_orientation, move)
            state_UD_slice = cube_moves.move_edge_permutation(current_UD_slice, move)

            index1 = state_index.get_UD_slice_index(state_UD_slice)
            index2 = state_index.get_edge_orientation_index(state_edge_orientation)
            index = (495 * index2) + index1

            if table[index]==None:
                table[index] = depth+1
                unsolved_count-=1
                queue.append((state_edge_orientation, state_UD_slice, depth+1, move))

    file_save.save_list_to_txt(table)

    return table


def generate_edge_permutation_UD_slice_table():
    table = [None] * 40320
    moves = ["u", "d", "u'", "d'", "u2", "d2", "l2", "r2", "f2", "b2"]
    queue = deque()

    initial_state = ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), 0, "0")
    queue.append(initial_state)
    table[0] = 0

    depth = 0
    unsolved_count = len(table)  # Track unsolved entries
    start_time = time.time()

    while queue:
        if time.time() - start_time > 1:
            print(f"Queue Length: {len(queue)}")
            print(f"Number Solved: {len(table) - unsolved_count}")
            print(f"Depth: {depth}")
            print(f"Unsolved Count: {unsolved_count}")
            print("_____________________________________")
            start_time = time.time()

        if unsolved_count == 0:
            break

        current_edge_permutation, depth, prev_move = queue.popleft()

        for move in moves:
            if prev_move[0] in move:  # Skip redundant moves
                continue

            state_edge_permutation = cube_moves.move_edge_permutation(current_edge_permutation, move)

            index = state_index.get_edge_permutation_UD_slice_index(state_edge_permutation)

            if table[index]==None:
                table[index] = depth+1
                unsolved_count -= 1
                queue.append((state_edge_permutation, depth+1, move))

    file_save.save_list_to_txt(table)

    return table

def generate_corner_permutation_table():
    table = [None] * 40320
    moves = ["u", "d", "u'", "d'", "u2", "d2", "l2", "r2", "f2", "b2"]
    #moves = ["u", "d", "l", "r", "f", "b", "u'", "d'", "l'", "r'", "f'", "b'", "u2", "d2", "l2", "r2", "f2", "b2"]
    queue = deque()

    initial_state = ((0, 1, 2, 3, 4, 5, 6, 7, 8), 0, "0")
    queue.append(initial_state)
    table[0] = 0

    depth = 0
    unsolved_count = len(table)  # Track unsolved entries
    start_time = time.time()

    while queue:
        if time.time() - start_time > 1:
            print(f"Queue Length: {len(queue)}")
            print(f"Number Solved: {len(table) - unsolved_count}")
            print(f"Depth: {depth}")
            print(f"Unsolved Count: {unsolved_count}")
            print("_____________________________________")
            start_time = time.time()

        if unsolved_count == 0:
            break

        current_corner_permutation, depth, prev_move = queue.popleft()

        for move in moves:
            if prev_move[0] in move:  # Skip redundant moves
                continue

            state_corner_permutation = cube_moves.move_corner_permutation(current_corner_permutation, move)

            index = state_index.get_corner_permutation_index(state_corner_permutation)

            if table[index] is None:
                table[index] = depth+1
                unsolved_count-=1
                queue.append((state_corner_permutation, depth+1, move))

    file_save.save_list_to_txt(table)

    return table


def generate_edge_permutation_E_slice_table():
    table = [None] * 24
    moves = ["u", "d", "u'", "d'", "u2", "d2", "l2", "r2", "f2", "b2"]
    queue = deque()

    initial_state = ((0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), 0, "0")
    queue.append(initial_state)
    table[0] = 0

    depth = 0
    unsolved_count = len(table)  # Track unsolved entries
    start_time = time.time()

    while queue:
        if time.time() - start_time > 1:
            print(f"Queue Length: {len(queue)}")
            print(f"Number Solved: {len(table) - unsolved_count}")
            print(f"Depth: {depth}")
            print(f"Unsolved Count: {unsolved_count}")
            print("_____________________________________")
            start_time = time.time()

        if unsolved_count == 0:
            break

        current_edge_permutation, depth, prev_move = queue.popleft()

        for move in moves:
            if prev_move[0] in move:  # Skip redundant moves
                continue

            state_edge_permutation = cube_moves.move_edge_permutation(current_edge_permutation, move)

            index = state_index.get_edge_permutation_E_slice_index(state_edge_permutation)

            if table[index]==None:
                table[index] = depth+1
                unsolved_count -= 1
                queue.append((state_edge_permutation, depth+1, move))

    file_save.save_list_to_txt(table)

    return table
"""
def generate_corner_edge_E_slice_permutation_table():
    table = [None] * 967680
    moves = ["u", "d", "u'", "d'", "u2", "d2", "l2", "r2", "f2", "b2"]
    #moves = ["u", "d", "l", "r", "f", "b", "u'", "d'", "l'", "r'", "f'", "b'", "u2", "d2", "l2", "r2", "f2", "b2"]
    queue = deque()

    initial_state = ((0, 1, 2, 3, 4, 5, 6, 7, 8), (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11), 0, "0")
    queue.append(initial_state)
    table[0] = 0

    depth = 0
    unsolved_count = len(table)  # Track unsolved entries
    start_time = time.time()

    while queue:
        if time.time() - start_time > 10:
            print(f"Queue Length: {len(queue)}")
            print(f"Number Solved: {len(table) - unsolved_count}")
            print(f"Depth: {depth}")
            print(f"Unsolved Count: {unsolved_count}")
            print("_____________________________________")
            start_time = time.time()

        if unsolved_count == 0:
            break

        current_corner_permutation, current_edge_permutation, depth, prev_move = queue.popleft()

        for move in moves:
            if prev_move[0] in move:  # Skip redundant moves
                continue

            state_corner_permutation = cube_moves.move_corner_permutation(current_corner_permutation, move)
            state_edge_permutation = cube_moves.move_edge_permutation(current_edge_permutation, move)

            index1 = state_index.get_corner_permutation_index(state_corner_permutation)
            index2 = state_index.get_edge_permutation_E_slice_index(state_edge_permutation)
            index = (40320*index2)+index1

            if table[index] is None:
                table[index] = depth+1
                unsolved_count-=1
                queue.append((state_corner_permutation, state_edge_permutation, depth+1, move))

    file_save.save_list_to_txt(table)

    return table
"""
"""
def generate_corner_edge_UD_slice_permutation_table():
    table = {}
    moves = ["u", "d", "u'", "d'", "u2", "d2", "l2", "r2", "f2", "b2"]
    queue = deque()

    initial_state = ((0, 1, 2, 3, 4, 5, 6, 7), (0, 1, 2, 3, 4, 5, 6, 7), 0, "0")
    queue.append(initial_state)
    table[0] = 0
    visited = set()
    visited.add(0)

    unsolved_count = 812851200
    depth = 0
    start_time = time.time()

    while queue:
        if time.time() - start_time > 1:
            print(f"Queue Length: {len(queue)}")
            print(f"Number Solved: {812851200 - unsolved_count}")
            print(f"Depth: {depth}")
            print(f"Unsolved Count: {unsolved_count}")
            print("_____________________________________")
            start_time = time.time()

        if unsolved_count <= 0:
            break

        current_corner_permutation, current_edge_permutation, depth, prev_move = queue.popleft()

        for move in moves:
            if prev_move[0] in move:
                continue

            state_corner_permutation = corner_perm_move_table.table[current_corner_permutation][move]
            state_edge_permutation = edge_perm_move_table.table[current_edge_permutation][move]

            index1 = state_index_precompute.index_table[state_corner_permutation]
            index2 = state_index_precompute.index_table[state_edge_permutation]
            index = (40320*index2)+index1

            if index not in visited:
                table[index] = depth+1
                unsolved_count-=1
                visited.add(index)
                queue.append((state_corner_permutation, state_edge_permutation, depth+1, move))

    file_save.save_list_to_txt([table])

    return table
"""

def generate_corner_edge_orientation_table():
    table = [None]*4478976
    moves = ["u", "d", "l", "r", "f", "b", "u'", "d'", "l'", "r'", "f'", "b'", "u2", "d2", "l2", "r2", "f2", "b2"]
    queue = deque()

    initial_state = ((0, 0, 0, 0, 0, 0, 0, 0), (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0), 0, "0")
    queue.append(initial_state)
    table[0] = 0

    unsolved_count = 4478976
    depth = 0
    start_time = time.time()

    while queue:
        if time.time() - start_time > 1:
            print(f"Queue Length: {len(queue)}")
            print(f"Number Solved: {4478976 - unsolved_count}")
            print(f"Depth: {depth}")
            print(f"Unsolved Count: {unsolved_count}")
            print("_____________________________________")
            start_time = time.time()

        if unsolved_count <= 0:
            break

        current_corner_orientation, current_edge_orientation, depth, prev_move = queue.popleft()

        for move in moves:
            if prev_move[0] in move:
                continue

            state_corner_orientation = cube_moves.move_corner_orientation(current_corner_orientation, move)
            state_edge_orientation = cube_moves.move_edge_orientation(current_edge_orientation, move)

            index1 = state_index.get_corner_orientation_index(state_corner_orientation)
            index2 = state_index.get_edge_orientation_index(state_edge_orientation)
            index = (2187*index2)+index1

            if table[index]==None:
                table[index] = depth+1
                unsolved_count-=1
                queue.append((state_corner_orientation, state_edge_orientation, depth+1, move))

    file_save.save_list_to_txt([table])

    return table

print(generate_corner_edge_orientation_table())