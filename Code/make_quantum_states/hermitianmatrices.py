'''
Density Matrix Generation

March 06:
- random_density_matrix, random_pure_density_matrix, bipartite_state added
- some testing functions
May 04:
- Plans to add better random matrix generation using U+ H U method
May 24:
- New Generators implemented for random unitary operators
'''

import numpy as np
from utils import print_matrix

np.random.seed(2)


def bipartite_state(A, B):
    '''
    Returns full state of two density matrices representing factorized states
    Tensor product implemented using kronecker product of the matrices
    '''
    return np.matrix(np.kron(A, B))


def rand_diag(N):
    '''
    N Dimensional random trace-1 diagonal matrix via the following process:
        - Generate a random row vector
        - Divide by the sum to get trace-1
        - Return diagonal matrix
    '''
    diag_elements = np.random.random(N)
    return np.matrix(np.diag(diag_elements/sum(diag_elements)))


def rand_unitary(N):
    '''
    Random complex unitary matrix via the following process:
        - Generate a random complex matrix
        - Apply QR decomposition to get a unitary Q matrix
        - Return Q
    '''
    reals = np.random.random((N, N))
    imags = np.random.random((N, N)) * 1j

    a = reals + imags
    # Run QR decomposition to get unitary operator
    q, _ = np.linalg.qr(a)
    return np.matrix(q)


def rand_hermitian(N):
    '''
    Random trace-1 hermitian matrix of dimension N
    '''
    U = rand_unitary(N)
    H = rand_diag(N)

    return U * H * U.H


if __name__ == "__main__":
    print_matrix(rand_hermitian(3).H)
