import math

def get_UD_slice_index(UD_slice_abstraction):
    def binomial_coefficient(n, k):
        if k < 0 or k > n:
            return 0
        if k == 0 or k == n:
            return 1

        return math.factorial(n)//(math.factorial(k)*math.factorial(n-k))
    count = -1
    index = 0
    for i in range(len(UD_slice_abstraction)):
        if UD_slice_abstraction[i]>=8:
            count += 1
        elif count>=0:
            index += binomial_coefficient(i, count)
    return index

def get_corner_orientation_index(corner_orientation_abstraction):
    index = 0
    for i in range(len(corner_orientation_abstraction)-2, -1, -1):
        index += corner_orientation_abstraction[i]*(3**(6-i))
    return index

def get_edge_orientation_index(edge_orientation_abstraction):
    index = 0
    for i in range(len(edge_orientation_abstraction)-2, -1, -1):
        index += edge_orientation_abstraction[i]*(2**(10-i))
    return index

def get_corner_permutation_index(corner_permutation_abstraction):
    index = 0
    for i in range(1, len(corner_permutation_abstraction)):
        count = 0
        for j in range(i-1, -1, -1):
            if corner_permutation_abstraction[j]>corner_permutation_abstraction[i]:
                count += 1
        index += count*math.factorial(i)
    return index

def get_edge_permutation_UD_slice_index(edge_permutation_abstraction):
    edge_permutation_abstraction = list(edge_permutation_abstraction)[:8]
    index = 0
    for i in range(1, len(edge_permutation_abstraction)):
        count = 0
        for j in range(i-1, -1, -1):
            if edge_permutation_abstraction[j]>edge_permutation_abstraction[i]:
                count += 1
        index += count*math.factorial(i)
    return index

def get_edge_permutation_E_slice_index(edge_permutation_abstraction):
    edge_permutation_abstraction = list(edge_permutation_abstraction)
    edge_permutation_abstraction = edge_permutation_abstraction[8:12]
    index = 0
    for i in range(1, len(edge_permutation_abstraction)):
        count = 0
        for j in range(i-1, -1, -1):
            if edge_permutation_abstraction[j]>edge_permutation_abstraction[i]:
                count += 1
        index += count*math.factorial(i)
    return index