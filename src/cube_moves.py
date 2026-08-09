def move_edge_permutation(state, move):
    #UR, UF, UL, UB, DR, DF, DL, DB, FR, FL, BL, BR
    #0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11
    
    new_state = list(state)
    move = move.lower()

    if move == "u":
        new_state[0] = state[3] 
        new_state[1] = state[0]
        new_state[2] = state[1]
        new_state[3] = state[2]
    elif move == "d":
        new_state[4] = state[5]
        new_state[5] = state[6]
        new_state[6] = state[7]
        new_state[7] = state[4]
    elif move == "r":
        new_state[0] = state[8]
        new_state[4] = state[11]
        new_state[8] = state[4]
        new_state[11] = state[0]
    elif move == "l":
        new_state[2] = state[10]
        new_state[6] = state[9]
        new_state[9] = state[2]
        new_state[10] = state[6]
    elif move == "f":
        new_state[1] = state[9]
        new_state[5] = state[8]
        new_state[8] = state[1]
        new_state[9] = state[5]
    elif move == "b":
        new_state[3] = state[11]
        new_state[7] = state[10]
        new_state[10] = state[3]
        new_state[11] = state[7]
    elif "'" in move:
        new_state = move_edge_permutation(move_edge_permutation(move_edge_permutation(state, move[0]), move[0]), move[0])
    elif "2" in move:
        new_state = move_edge_permutation(move_edge_permutation(state, move[0]), move[0])

    return tuple(new_state)



def move_corner_orientation(state, move):
    #URF, ULF, ULB, URB, DRF, DLF, DLB, DRB
    #0,   1,   2,   3,   4,   5,   6,   7
    
    new_state = list(state)
    move = move.lower()

    if move == "u":
        new_state[0] = state[3] 
        new_state[1] = state[0]
        new_state[2] = state[1]
        new_state[3] = state[2]
    elif move == "d":
        new_state[4] = state[5]
        new_state[5] = state[6]
        new_state[6] = state[7]
        new_state[7] = state[4]
    elif move == "r":
        new_state[0] = (state[4]+2)%3
        new_state[3] = (state[0]+1)%3
        new_state[4] = (state[7]+1)%3
        new_state[7] = (state[3]+2)%3
    elif move == "l":
        new_state[1] = (state[2]+1)%3
        new_state[2] = (state[6]+2)%3
        new_state[5] = (state[1]+2)%3
        new_state[6] = (state[5]+1)%3
    elif move == "f":
        new_state[0] = (state[1]+1)%3
        new_state[1] = (state[5]+2)%3
        new_state[4] = (state[0]+2)%3
        new_state[5] = (state[4]+1)%3
    elif move == "b":
        new_state[2] = (state[3]+1)%3
        new_state[3] = (state[7]+2)%3
        new_state[6] = (state[2]+2)%3
        new_state[7] = (state[6]+1)%3
    elif "'" in move:
        new_state = move_corner_orientation(move_corner_orientation(move_corner_orientation(state, move[0]), move[0]), move[0])
    elif "2" in move:
        new_state = move_corner_orientation(move_corner_orientation(state, move[0]), move[0])

    return tuple(new_state)



def move_edge_orientation(state, move):
    #UR, UF, UL, UB, DR, DF, DL, DB, FR, FL, BL, BR
    #0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10, 11
    
    new_state = list(state)
    move = move.lower()

    if move == "u":
        new_state[0] = state[3] 
        new_state[1] = state[0]
        new_state[2] = state[1]
        new_state[3] = state[2]
    elif move == "d":
        new_state[4] = state[5]
        new_state[5] = state[6]
        new_state[6] = state[7]
        new_state[7] = state[4]
    elif move == "r":
        new_state[0] = state[8]
        new_state[4] = state[11]
        new_state[8] = state[4]
        new_state[11] = state[0]
    elif move == "l":
        new_state[2] = state[10]
        new_state[6] = state[9]
        new_state[9] = state[2]
        new_state[10] = state[6]
    elif move == "f":
        new_state[1] = (state[9]+1)%2
        new_state[5] = (state[8]+1)%2
        new_state[8] = (state[1]+1)%2
        new_state[9] = (state[5]+1)%2
    elif move == "b":
        new_state[3] = (state[11]+1)%2
        new_state[7] = (state[10]+1)%2
        new_state[10] = (state[3]+1)%2
        new_state[11] = (state[7]+1)%2
    elif "'" in move:
        new_state = move_edge_orientation(move_edge_orientation(move_edge_orientation(state, move[0]), move[0]), move[0])
    elif "2" in move:
        new_state = move_edge_orientation(move_edge_orientation(state, move[0]), move[0])

    return tuple(new_state)



def move_corner_permutation(state, move):
    #URF, ULF, ULB, URB, DRF, DLF, DLB, DRB
    #0,   1,   2,   3,   4,   5,   6,   7
    
    new_state = list(state)
    move = move.lower()

    if move == "u":
        new_state[0] = state[3] 
        new_state[1] = state[0]
        new_state[2] = state[1]
        new_state[3] = state[2]
    elif move == "d":
        new_state[4] = state[5]
        new_state[5] = state[6]
        new_state[6] = state[7]
        new_state[7] = state[4]
    elif move == "r":
        new_state[0] = state[4]
        new_state[3] = state[0]
        new_state[4] = state[7]
        new_state[7] = state[3]
    elif move == "l":
        new_state[1] = state[2]
        new_state[2] = state[6]
        new_state[5] = state[1]
        new_state[6] = state[5]
    elif move == "f":
        new_state[0] = state[1]
        new_state[1] = state[5]
        new_state[4] = state[0]
        new_state[5] = state[4]
    elif move == "b":
        new_state[2] = state[3]
        new_state[3] = state[7]
        new_state[6] = state[2]
        new_state[7] = state[6]
    elif "'" in move:
        new_state = move_corner_permutation(move_corner_permutation(move_corner_permutation(state, move[0]), move[0]), move[0])
    elif "2" in move:
        new_state = move_corner_permutation(move_corner_permutation(state, move[0]), move[0])

    return tuple(new_state)



def apply_move(state, move):
    # U1, U2, U3, U4, U5, U6, U7, U8, U9
    # 0,  1,  2,  3,  4,  5,  6,  7,  8

    # R1, R2, R3, R4, R5, R6, R7, R8, R9
    # 9,  10, 11, 12, 13, 14, 15, 16, 17

    # F1, F2, F3, F4, F5, F6, F7, F8, F9
    # 18, 19, 20, 21, 22, 23, 24, 25, 26

    # D1, D2, D3, D4, D5, D6, D7, D8, D9
    # 27, 28, 29, 30, 31, 32, 33, 34, 35

    # L1, L2, L3, L4, L5, L6, L7, L8, L9
    # 36, 37, 38, 39, 40, 41, 42, 43, 44

    # B1, B2, B3, B4, B5, B6, B7, B8, B9
    # 45, 46, 47, 48, 49, 50, 51, 52, 53
    

    new_state = list(state)
    move = move.lower()

    if move == "u":
        new_state[0] = state[6]
        new_state[1] = state[3]
        new_state[2] = state[0]
        new_state[3] = state[7]
        #new_state[4] = state[4]
        new_state[5] = state[1]
        new_state[6] = state[8]
        new_state[7] = state[5]
        new_state[8] = state[2]
        new_state[9] = state[45]
        new_state[10] = state[46]
        new_state[11] = state[47]
        new_state[18] = state[9]
        new_state[19] = state[10]
        new_state[20] = state[11]
        new_state[36] = state[18]
        new_state[37] = state[19]
        new_state[38] = state[20]
        new_state[45] = state[36]
        new_state[46] = state[37]
        new_state[47] = state[38]
    elif move == "d":
        new_state[15] = state[24]
        new_state[16] = state[25]
        new_state[17] = state[26]
        new_state[24] = state[42]
        new_state[25] = state[43]
        new_state[26] = state[44]
        new_state[27] = state[33]
        new_state[28] = state[30]
        new_state[29] = state[27]
        new_state[30] = state[34]
        #new_state[31] = state[31]
        new_state[32] = state[28]
        new_state[33] = state[35]
        new_state[34] = state[32]
        new_state[35] = state[29]
        new_state[42] = state[51]
        new_state[43] = state[52]
        new_state[44] = state[53]
        new_state[51] = state[15]
        new_state[52] = state[16]
        new_state[53] = state[17]
    elif move == "r":
        new_state[2] = state[20]
        new_state[5] = state[23]
        new_state[8] = state[26]
        new_state[9] = state[15]
        new_state[10] = state[12]
        new_state[11] = state[9]
        new_state[12] = state[16]
        #new_state[13] = state[13]
        new_state[14] = state[10]
        new_state[15] = state[17]
        new_state[16] = state[14]
        new_state[17] = state[11]
        new_state[20] = state[29]
        new_state[23] = state[32]
        new_state[26] = state[35]
        new_state[29] = state[51]
        new_state[32] = state[48]
        new_state[35] = state[45]
        new_state[45] = state[8]
        new_state[48] = state[5]
        new_state[51] = state[2]
    elif move == "l":
        new_state[0] = state[53]
        new_state[3] = state[50]
        new_state[6] = state[47]
        new_state[18] = state[0]
        new_state[21] = state[3]
        new_state[24] = state[6]
        new_state[27] = state[18]
        new_state[30] = state[21]
        new_state[33] = state[24]
        new_state[36] = state[42]
        new_state[37] = state[39]
        new_state[38] = state[36]
        new_state[39] = state[43]
        #new_state[40] = state[40]
        new_state[41] = state[37]
        new_state[42] = state[44]
        new_state[43] = state[41]
        new_state[44] = state[38]
        new_state[47] = state[33]
        new_state[50] = state[30]
        new_state[53] = state[27]
    elif move == "f":
        new_state[6] = state[44]
        new_state[7] = state[41]
        new_state[8] = state[38]
        new_state[9] = state[6]
        new_state[12] = state[7]
        new_state[15] = state[8]
        new_state[18] = state[24]
        new_state[19] = state[21]
        new_state[20] = state[18]
        new_state[21] = state[25]
        #new_state[22] = state[22]
        new_state[23] = state[19]
        new_state[24] = state[26]
        new_state[25] = state[23]
        new_state[26] = state[20]
        new_state[27] = state[15]
        new_state[28] = state[12]
        new_state[29] = state[9]
        new_state[38] = state[27]
        new_state[41] = state[28]
        new_state[44] = state[29]
    elif move == "b":
        new_state[0] = state[11]
        new_state[1] = state[14]
        new_state[2] = state[17]
        new_state[11] = state[35]
        new_state[14] = state[34]
        new_state[17] = state[33]
        new_state[33] = state[36]
        new_state[34] = state[39]
        new_state[35] = state[42]
        new_state[36] = state[2]
        new_state[39] = state[1]
        new_state[42] = state[0]
        new_state[45] = state[51]
        new_state[46] = state[48]
        new_state[47] = state[45]
        new_state[48] = state[52]
        #new_state[49] = state[49]
        new_state[50] = state[46]
        new_state[51] = state[53]
        new_state[52] = state[50]
        new_state[53] = state[47]
    elif "'" in move:
        new_state = apply_move(apply_move(apply_move(state, move[0]), move[0]), move[0])
    elif "2" in move:
        new_state = apply_move(apply_move(state, move[0]), move[0])
    
    return tuple(new_state)

def move_parity(parity, move):
    if "2" in move:
        return parity
    else:
        return (parity+1)%2
    

def move_edge_permutation_UD_slice(state, move):
    #UR, UF, UL, UB, DR, DF, DL, DB
    #0,  1,  2,  3,  4,  5,  6,  7,
    
    new_state = list(state)
    move = move.lower()

    if move == "u":
        new_state[0] = state[3]
        new_state[1] = state[0]
        new_state[2] = state[1]
        new_state[3] = state[2]
    elif move == "d":
        new_state[4] = state[5]
        new_state[5] = state[6]
        new_state[6] = state[7]
        new_state[7] = state[4]
    elif move == "u'":
        new_state[0] = state[1]
        new_state[1] = state[2]
        new_state[2] = state[3]
        new_state[3] = state[0]
    elif move == "d'":
        new_state[4] = state[7]
        new_state[5] = state[4]
        new_state[6] = state[5]
        new_state[7] = state[6]
    elif move == "r2":
        new_state[0] = state[4]
        new_state[4] = state[0]
    elif move == "l2":
        new_state[2] = state[6]
        new_state[6] = state[2]
    elif move == "f2":
        new_state[1] = state[5]
        new_state[5] = state[1]
    elif move == "b2":
        new_state[3] = state[7]
        new_state[7] = state[3]
    elif "2" in move:
        new_state = move_edge_permutation(move_edge_permutation(state, move[0]), move[0])

    return tuple(new_state)