import cube_abstraction
import state_index
import tables

def moves_to_UD_slice(state):
    UD_slice_abstraction = cube_abstraction.get_edge_permutation_abstraction(state)
    index = state_index.get_UD_slice_index(UD_slice_abstraction)
    return tables.UD_slice_table[index]

def moves_to_edge_orientation(state):
    edge_orientation_abstraction = cube_abstraction.get_edge_orientation_abstraction(state)
    index = state_index.get_edge_orientation_index(edge_orientation_abstraction)
    return tables.edge_orientation_table[index]

def moves_to_corner_orientation(state):
    corner_orientation_abstraction = cube_abstraction.get_corner_orientation_abstraction(state)
    index = state_index.get_corner_orientation_index(corner_orientation_abstraction)
    return tables.corner_orientation_table[index]

def moves_to_flip_UD_slice(state):
    UD_slice_abstraction = cube_abstraction.get_edge_permutation_abstraction(state)
    edge_orientation_abstraction = cube_abstraction.get_edge_orientation_abstraction(state)
    index = (495*state_index.get_edge_orientation_index(edge_orientation_abstraction))+state_index.get_UD_slice_index(UD_slice_abstraction)
    return tables.flip_UD_slice_table[index]

def moves_to_corner_permutation(state):
    corner_permutation_abstraction = cube_abstraction.get_corner_permutation_abstraction(state)
    index = state_index.get_corner_permutation_index(corner_permutation_abstraction)
    return tables.corner_permutation_table[index]

def moves_to_edge_permutation_UD_slice(state):
    edge_permutation_UD_slice_abstraction = cube_abstraction.get_edge_permutation_abstraction(state)
    index = state_index.get_edge_permutation_UD_slice_index(edge_permutation_UD_slice_abstraction)
    return tables.edge_permutation_UD_slice_table[index]

def moves_to_edge_permutation_E_slice(state):
    edge_permutation_UD_slice_abstraction = cube_abstraction.get_edge_permutation_abstraction(state)
    index = state_index.get_edge_permutation_E_slice_index(edge_permutation_UD_slice_abstraction)
    return tables.edge_permutation_E_slice_table[index]

def moves_to_corner_edge_permutation_E_slice(state):
    edge_permutation_E_slice_abstraction = cube_abstraction.get_edge_permutation_abstraction(state)
    corner_permutation_abstraction = cube_abstraction.get_corner_permutation_abstraction(state)
    index1 = state_index.get_corner_permutation_index(corner_permutation_abstraction)
    index2 = state_index.get_edge_permutation_E_slice_index(edge_permutation_E_slice_abstraction)
    index = (40320*index2)+index1
    return tables.corner_edge_E_slice_permutation[index]

def moves_to_corner_edge_orientation(state):
    corner_orientation_abstraction = cube_abstraction.get_corner_orientation_abstraction(state)
    edge_orientation_abstraction = cube_abstraction.get_edge_orientation_abstraction(state)
    index1 = state_index.get_corner_orientation_index(corner_orientation_abstraction)
    index2 = state_index.get_edge_orientation_index(edge_orientation_abstraction)
    index = (2187*index2)+index1
    return tables.corner_edge_orientation_table[index]


def heuristic_phase_1(state):
    return max(moves_to_corner_edge_orientation(state), moves_to_UD_slice(state))

def heuristic_phase_2(state):
    return max(moves_to_edge_permutation_UD_slice(state), moves_to_corner_edge_permutation_E_slice(state))


"""
#Other Phase 1 Heuristics:

def heuristic_phase_1(state):
    return max(moves_to_flip_UD_slice(state), moves_to_corner_orientation(state))

def heuristic_phase_1(state):
    return max(moves_to_corner_orientation(state), moves_to_edge_orientation(state), moves_to_corner_orientation(state))


    
#Other Phase 2 Heuristics:

def heuristic_phase_2(state):
    return max(moves_to_corner_permutation(state), moves_to_edge_permutation_UD_slice(state), moves_to_edge_permutation_E_slice(state))

"""