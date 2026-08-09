from collections import deque
import cube_moves
import time
import heuristic_eval
import random
import tables

def inverse_moves(move_sequence):
    ans = []
    for i in range(len(move_sequence)-1, -1, -1):
        if "'" in move_sequence[i]:
            ans.append(move_sequence[i][0])
        elif "2" in move_sequence[i]:
            ans.append(move_sequence[i])
        else:
            ans.append(move_sequence[i]+"'")
    return ans

def apply_moves(state, move_sequence):
    for move in move_sequence:
        state = cube_moves.apply_move(state, move)
    return state

def letter_colours_to_numbers(state):
    ans = []
    #URFDLB
    colours = state[4]+state[13]+state[22]+state[31]+state[40]+state[49]
    for item in state:
        ans.append(colours.find(item))
    return tuple(ans)

def remove_double_moves(move_sequence):
    if move_sequence==[]:
        return []
    
    new_sequence = []
    for move in move_sequence:
        if new_sequence==[]:
            new_sequence.append(move)
        elif new_sequence[-1]==0:
            new_sequence[-1] = move
        elif new_sequence[-1][0]!=move[0]:
            new_sequence.append(move)
        elif new_sequence[-1][0]==move[0]:
            if "'" in move:
                if "'" in new_sequence[-1]:
                    new_sequence[-1] = move[0] + "2"
                elif "2" in new_sequence[-1]:
                    new_sequence[-1] = move[0]
                else:
                    new_sequence[-1] = 0
            elif "2" in move:
                if "'" in new_sequence[-1]:
                    new_sequence[-1] = move[0]
                elif "2" in new_sequence[-1]:
                    new_sequence[-1] = 0
                else:
                    new_sequence[-1] = move[0] + "'"
            else:
                if "'" in new_sequence[-1]:
                    new_sequence[-1] = 0
                elif "2" in new_sequence[-1]:
                    new_sequence[-1] = move[0] + "'"
                else:
                    new_sequence[-1] = move[0] + "2"
    if new_sequence[-1]==0:
        del new_sequence[-1]

    return new_sequence

def solve_phase_1(start, heuristic_function):
    #IDA*
    def dfs(start, max_depth):
        if heuristic_function(start)==0:
            return [[], start]

        stack = deque([(start, [])])  # (state, move_sequence)
        moves = ["u", "d", "l", "r", "f", "b", "u'", "d'", "l'", "r'", "f'", "b'", "u2", "d2", "l2", "r2", "f2", "b2"]
        lowest = float("inf")

        while stack:
            current_state, move_sequence = stack.pop()
            depth = len(move_sequence)

            for move in moves:
                if move_sequence!=[] and move_sequence[-1][0] in move:
                    continue

                next_state = cube_moves.apply_move(current_state, move)

                admissible_heuristic = heuristic_function(next_state)

                if admissible_heuristic==0:
                    return [move_sequence + [move], next_state]
            
                lowest = min(lowest, depth+admissible_heuristic+1)

                if depth+admissible_heuristic+1<=max_depth:
                    stack.append((next_state, move_sequence + [move]))

        return lowest

    depth = heuristic_function(start)
    while True:
        answer = dfs(start, depth)
        if type(answer)!=list:
            depth = max(depth+1, answer)
        else:
            return answer

def solve_phase_2(start, heuristic_function):
    #IDA*
    def dfs(start, max_depth):
        if heuristic_function(start)==0:
            return [[], start]

        stack = deque([(start, [])])  # (state, move_sequence)
        moves = ["u", "d", "u'", "d'", "u2", "d2", "l2", "r2", "f2", "b2"]
        lowest = float("inf")
        solved = set(tables.solved_tree.keys())

        while stack:
            current_state, move_sequence = stack.pop()
            depth = len(move_sequence)

            
            for move in moves:
                if move_sequence!=[] and move_sequence[-1][0] in move:
                    continue
                next_state = cube_moves.apply_move(current_state, move)
                
                if next_state in solved:
                    return [move_sequence + [move] + inverse_moves(tables.solved_tree[next_state]), apply_moves(next_state, inverse_moves(tables.solved_tree[next_state]))]

                admissible_heuristic = heuristic_function(next_state)
                lowest = min(lowest, depth+admissible_heuristic+1)

                if admissible_heuristic==0:
                    return [move_sequence + [move], next_state]

                if depth+1+admissible_heuristic<=max_depth:
                    stack.append((next_state, move_sequence + [move]))

        return lowest

    depth = max(1, heuristic_function(start))
    while True:
        answer = dfs(start, depth)
        if type(answer)!=list:
            depth = max(depth+1, answer)
        else:
            return answer


def solve_cube(state):
    if type(state)==str:
        state = letter_colours_to_numbers(state)
                
    if state in set(tables.solved_tree.keys()):
        return inverse_moves(tables.solved_tree[state])

    sequence1, current_state = solve_phase_1(state, heuristic_eval.heuristic_phase_1)

    sequence2, current_state = solve_phase_2(current_state, heuristic_eval.heuristic_phase_2)

    return remove_double_moves(remove_double_moves(sequence1) + remove_double_moves(sequence2))