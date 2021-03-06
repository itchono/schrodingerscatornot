'''
Density Matrix Generation

March 06:
- random_density_matrix, random_pure_density_matrix, bipartite_state added
- some testing functions

'''

import numpy as np
import pandas as pd

np.random.seed(2)


def random_density_matrix(N):
    '''
    Makes a random density matrix for an N level system.
    Broken right now.

    Obeys:
    - Hermiticity
    - Tr = 1
    '''
    # Off-diagonal elements
    reals = np.random.random((N, N))
    imgs = np.random.random((N, N)) * 1j

    # Make the upper trianglular portion of the matrix
    U = np.triu(reals + imgs, 1)

    # Diagonal elements
    weights = np.random.random(N)
    weights = weights / sum(weights)  # normalize trace
    diagonal = np.diag(weights)

    # Mirror elements over
    return np.matrix(diagonal + (U.conj().T + U))


def random_pure_density_matrix(N):
    '''
    Makes a random pure density matrix for an N level system.
    This is done by taking the state vectors for a pure state.

    Obeys:
    - Hermiticity
    - Tr = 1
    - P^2 = P
    '''
    # state vector
    reals = np.random.random(N)
    imgs = np.random.random(N) * 1j
    state = np.matrix((reals+imgs).reshape((N, 1)))

    # normalize
    state = state / np.linalg.norm(state)

    # make density matrix
    return np.matmul(state, state.H)


def bipartite_state(A, B):
    '''
    Returns full state of two density matrices representing factorized states
    Tensor product implemented using kronecker product of the matrices
    '''
    return np.matrix(np.kron(A, B))


if __name__ == "__main__":
    P1 = random_density_matrix(2)

    print("Mixed Density Matrix")
    print(pd.DataFrame(P1))
    print(pd.DataFrame(P1**2))
    # Is there anything special we need for the general density matrix?
    # Do I need to control anything on the off-diagonals?

    P2 = random_pure_density_matrix(2)
    print("\nPure Density Matrix")
    print(pd.DataFrame(P2))
    print(pd.DataFrame(P2**2))

    print("\nBig System")
    P3 = bipartite_state(
                random_pure_density_matrix(2),
                random_pure_density_matrix(2))
    print(pd.DataFrame(P3))
