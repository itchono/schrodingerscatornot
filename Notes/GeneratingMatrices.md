# Generating Density Matrices
## Papers
* [Generating random density matrices](https://arxiv.org/abs/1010.3570)

## Density Matrices (NxN)
These describe the general state of a `NxN` system. They obey some properties:
* trace = 1; that is, the diagonals add up to 1
* they are [Hermitian](https://en.wikipedia.org/wiki/Hermitian_matrix)


## Generating from State Vector
Given a normalized state vector (c1, c2, c3....., cN) [each c is complex], we can make our density matrix by taking the the product of the vector and its Hermitian conjugate. In such a case, we would have the density matrix of a pure state.

## Generating More Generally?
All I have figured out on this front is that the matrix has to be trace 1 and Hermitian. I'm not sure what the constraints are on the off-diagonal elements, if any.

## Update: Unitary Transformation Matrices
### The Game Plan
* Make a real diagonal matrix whose diagonal elements sum up to 1 (D)
* Generate a random unitary matrix (i.e. Hermitian, orthonormal) (S)
* H = S(dagger)DS
This approach is really nice because unitary matrices take care of almost everything for you!!

### Medium Level Implementation
The above game plan is nice, but let's bring it down into code. 

The basic operation to generate the hermitian matrix is is `M = U * H * U.H`, wherein `U` is a unitary matrix, `H` is a trace-1 diagonal matrix, and `.H` signifies the dagger operator in numpy.

### Generating the diagonal matrix:
* Generate `N` random real numbers from some probability distribution (Gaussian, blah blah etc.) and divide all by their sum.
* For this case, we use `np.random.random()`
* Put these values into a diagonal matrix using `np.diag`, resulting in a trace 1 real diagonal matrix

### Generating the unitary matrix:
* [Credits to this link](https://mathoverflow.net/questions/333187/random-unitary-matrices) for the rough implementation detail.
* Generate two sets `N**2` random numbers from some probability distribution, and multiply the second one by `1j` (imaginary unit)
* Add these together to get a matrix, `A`, which is a complex matrix filled with random values
* Run a QR decomposition, and get the `Q`, matrix, which is now a unitary operator, with orthonormal eigenvectors similar to the results of a Gram-Schmidt orthonormalization process

Finally, we put this all together. This is demonstrated in the `hermitianmatrices.py` source file.