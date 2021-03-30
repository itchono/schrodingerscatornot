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
