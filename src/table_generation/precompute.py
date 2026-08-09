import itertools
import file_save

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))

import state_index
import cube_moves

table = {}
moves = ["u", "d", "u'", "d'", "u2", "d2", "l2", "r2", "f2", "b2"]
for item in itertools.permutations(range(8), 8):
    table[item] = {}
    for move in moves:
        table[item][move] = cube_moves.move_edge_permutation_UD_slice(item, move)

file_save.save_list_to_txt([table], "edge_perm_move_table.py")