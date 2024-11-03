#
def get_p_distance(s1, s2):
    """Calculate the p-distance between two DNA strings."""
    difference = sum (1 for a, b in zip(s1, s2) if a != b)
    return difference / len(s1)

def get_p_distance_matrix(dna_list):
    """Calculate the p-distance matrix for a list of DNA strings"""
    matrix = []
    for s1 in dna_list:
        row = []
        for s2 in dna_list:
            row.append(get_p_distance(s1, s2))
        matrix.append(row)
    return matrix