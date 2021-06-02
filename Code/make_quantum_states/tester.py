import numpy as np
from hermitianmatrices import rand_hermitian, rand_complex
from utils import extend_diagonal, print_matrix

for i in range(10):
    mat = rand_hermitian(3)
    print(np.linalg.norm(mat))

    mat = rand_complex(3)
    print(np.linalg.norm(mat))
