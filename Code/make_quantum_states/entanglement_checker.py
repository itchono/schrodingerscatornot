# based on https://en.wikipedia.org/wiki/Peres%E2%80%93Horodecki_criterion

import numpy as np
import hermitianmatrices
from utils import print_matrix
from scipy.linalg import svdvals

TOLERANCE = 1e-12


def partial_transpose(P: np.array) -> np.array:
    '''
    partial transposes matrix in place
    '''
    # Partial transpose the array
    for x in range(1, P.shape[0], 2):
        for y in range(1, P.shape[1], 2):
            P[x-1:x+1, y-1:y+1] = P[x-1:x+1, y-1:y+1].T
    return P


def PPT_criterion(P: np.array) -> bool:
    '''
    Runs PPT criterion to check if eigenvalues
    of partial transpose are all positive

    True -> Factorizable for 2 (x) 2 and 2 (x) 3 cases.
    A False returned by this test means
    ENTANGLED for any dimensionality. (I think**)
    '''
    Ptb = np.copy(P)
    partial_transpose(Ptb)

    evs = np.linalg.eigvals(Ptb)  # Solve for evs

    # Check if any evs are negative, within a tolerance
    return (evs[evs < -TOLERANCE]).size == 0
    # Return true if no eigenvalues are negative


def schmidt_test(P: np.array) -> bool:
    '''
    Runs singular value decomposition on density matrix from
    pure state to determine if it is factorizable or not.

    Incompatible for mixed states.

    True -> Factorizable
    False -> Entangled
    '''
    svals = svdvals(P)

    # Check if any svals are negative, within a tolerance
    return (svals[svals < -TOLERANCE]).size == 0
    # Return true if no singular values are negative


if __name__ == "__main__":
    print("Factorizable matrix test")
    A = hermitianmatrices.random_pure_density_matrix(2)
    B = hermitianmatrices.random_pure_density_matrix(2)
    P = hermitianmatrices.bipartite_state(A, B)

    print_matrix(P)
    print(PPT_criterion(P))

    print("Random matrix test")
    P2 = hermitianmatrices.random_density_matrix(4)
    print_matrix(P2)
    print(PPT_criterion(P2))

    D = hermitianmatrices.random_pure_density_matrix(4)
    print(schmidt_test(D))
