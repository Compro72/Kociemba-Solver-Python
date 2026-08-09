# Saving from algorithm to raw py file

def save_list_to_txt(data_list, filename="output.txt"):
    with open(filename, 'w') as file:
        for item in data_list:
            file.write(str(item) + "\n")

def load_list_from_txt(filename="output.txt"):
    loaded = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            loaded.append(line)



# Saving from raw py file to binary file
import bz2
import pickle

import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
import tables

data_to_save = {
    "UD_slice_table": tables.UD_slice_table,
    "edge_orientation_table": tables.edge_orientation_table,
    "corner_orientation_table": tables.corner_orientation_table,
    "flip_UD_slice_table": tables.flip_UD_slice_table,
    "corner_edge_orientation_table": tables.corner_edge_orientation_table,
    "corner_permutation_table": tables.corner_permutation_table,
    "edge_permutation_UD_slice_table": tables.edge_permutation_UD_slice_table,
    "edge_permutation_E_slice_table": tables.edge_permutation_E_slice_table,
    "corner_edge_E_slice_permutation": tables.corner_edge_E_slice_permutation,
    "solved_tree": tables.solved_tree,
}

with bz2.BZ2File("tables.dat.bz2", "wb") as f:
    pickle.dump(data_to_save, f, protocol=pickle.HIGHEST_PROTOCOL)

input("done...")