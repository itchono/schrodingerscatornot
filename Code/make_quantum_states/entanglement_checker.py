# based on https://en.wikipedia.org/wiki/Peres%E2%80%93Horodecki_criterion

import numpy as np
import hermitianmatrices
from utils import print_matrix


def partial_transpose(P):
    '''
    partial transposes matrix in place
    '''
    # Partial transpose the array
    for x in range(1, P.shape[0], 2):
        for y in range(1, P.shape[1], 2):
            P[x-1:x+1, y-1:y+1] = P[x-1:x+1, y-1:y+1].T
    return P


def entangled_PPT(P):
    '''
    determines if a state is entangled by the Horodecki criterion

    only works for 2 (x) 2 and 2 (x) 3 cases.
    '''
    Ptb = np.copy(P)

    partial_transpose(Ptb)

    evs = np.linalg.eigvals(Ptb)
    print(evs)


if __name__ == "__main__":
    A = hermitianmatrices.random_pure_density_matrix(2)
    B = hermitianmatrices.random_pure_density_matrix(2)
    P = hermitianmatrices.bipartite_state(A, B)

    print_matrix(P)
    entangled_PPT(P)

    # hmm, this seems wrong..
