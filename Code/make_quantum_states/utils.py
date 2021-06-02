import numpy as np
import pandas as pd


def print_matrix(P):
    '''
    Just pretty prints matrices so that I can call it in one line
    '''
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        print(pd.DataFrame(P))


def extend_diagonal(matrix: np.matrix, n: int):
    '''
    Makes the matrix n dimensions bigger with new elements filled with zeroes
    '''
    new_dim = matrix.shape[0] + n
    new_mat = np.zeros((new_dim, new_dim)).astype(complex)
    new_mat[:matrix.shape[0], :matrix.shape[1]] = matrix
    return np.matrix(new_mat)
