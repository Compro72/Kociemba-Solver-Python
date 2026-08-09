def get_edge_permutation_abstraction(state):
    def facelet_sort_order(item):
        order = "UDRLFB"
        return order.index(item)
    
    face_order = "URFDLB"
    colour_order = [state[4], state[13], state[22], state[31], state[40], state[49]]
    
    edge_order = {"UR": 0, "UF": 1, "UL": 2, "UB": 3, "DR": 4, "DF": 5, "DL": 6, "DB": 7, "RF": 8, "LF": 9, "LB": 10, "RB": 11}
    edges = [(5, 10), (7, 19), (3, 37), (1, 46), (32, 16), (28, 25), (30, 43), (34, 52), (12, 23), (41, 21), (39, 50), (14, 48)]

    abstraction = []
    for edge in edges:
        abstraction.append(edge_order["".join(sorted([face_order[colour_order.index(state[edge[0]])], face_order[colour_order.index(state[edge[1]])]], key=facelet_sort_order))])
    
    return tuple(abstraction)


def get_edge_orientation_abstraction(state):
    def facelet_sort_order(item):
        order = "UDFBRL"
        return order.index(item)
    
    face_order = "URFDLB"
    colour_order = [state[4], state[13], state[22], state[31], state[40], state[49]]
    
    #UR, UF, UL, UB, DR, DF, DL, DB, FR, FL, BL, BR
    edges = [(5, 10), (7, 19), (3, 37), (1, 46), (32, 16), (28, 25), (30, 43), (34, 52), (23, 12), (21, 41), (50, 39), (48, 14)]

    abstraction = []
    for edge in edges:
        edge_origin_faces = [face_order[colour_order.index(state[edge[0]])], face_order[colour_order.index(state[edge[1]])]]
        if sorted(edge_origin_faces, key=facelet_sort_order)==edge_origin_faces:
            abstraction.append(0)
        else:
            abstraction.append(1)
    
    return tuple(abstraction)


def get_corner_orientation_abstraction(state):
    face_order = "URFDLB"
    colour_order = [state[4], state[13], state[22], state[31], state[40], state[49]]
    
    #URF, UFL, ULB, UBR, DFR, DLF, DBL, DRB
    corners = [(8, 9, 20), (6, 18, 38), (0, 36, 47), (2, 45, 11), (29, 26, 15), (27, 44, 24), (33, 53, 42), (35, 17, 51)]

    abstraction = []
    for corner in corners:
        corner_origin_faces = [face_order[colour_order.index(state[corner[0]])], face_order[colour_order.index(state[corner[1]])], face_order[colour_order.index(state[corner[2]])]]
        if corner_origin_faces[0]=="U" or corner_origin_faces[0]=="D":
            abstraction.append(0)
        elif corner_origin_faces[1]=="U" or corner_origin_faces[1]=="D":
            abstraction.append(1)
        else:
            abstraction.append(2)
    
    return tuple(abstraction)


def get_corner_permutation_abstraction(state):
    def facelet_sort_order(item):
        order = "UDLRFB"
        return order.index(item)
    face_order = "URFDLB"
    colour_order = [state[4], state[13], state[22], state[31], state[40], state[49]]
    
    #URF, UFL, ULB, UBR, DFR, DLF, DBL, DRB
    corner_order = {"URF": 0, "ULF": 1, "ULB": 2, "URB": 3, "DRF": 4, "DLF": 5, "DLB": 6, "DRB": 7}
    corners = [(8, 9, 20), (6, 18, 38), (0, 36, 47), (2, 45, 11), (29, 26, 15), (27, 44, 24), (33, 53, 42), (35, 17, 51)]

    abstraction = []
    for corner in corners:
        corner_origin_faces = "".join(sorted([face_order[colour_order.index(state[corner[0]])], face_order[colour_order.index(state[corner[1]])], face_order[colour_order.index(state[corner[2]])]], key=facelet_sort_order))
        abstraction.append(corner_order[corner_origin_faces])
    
    return tuple(abstraction)

