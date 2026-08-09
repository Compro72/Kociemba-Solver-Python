import bz2
import os
import pickle

data_file = os.path.join(os.path.dirname(__file__), "tables.dat.bz2")

with bz2.BZ2File(data_file, "rb") as f:
    _data = pickle.load(f)

UD_slice_table = _data["UD_slice_table"]
edge_orientation_table = _data["edge_orientation_table"]
corner_orientation_table = _data["corner_orientation_table"]
flip_UD_slice_table = _data["flip_UD_slice_table"]
corner_edge_orientation_table = _data["corner_edge_orientation_table"]
corner_permutation_table = _data["corner_permutation_table"]
edge_permutation_UD_slice_table = _data["edge_permutation_UD_slice_table"]
edge_permutation_E_slice_table = _data["edge_permutation_E_slice_table"]
corner_edge_E_slice_permutation = _data["corner_edge_E_slice_permutation"]
solved_tree = _data["solved_tree"]