# Schrodinger's Cat or Not?
### Mingde Yin & Amar Vutha
### March 2021-

A classifier for determining whether a bipartite system is in an entangled state or not.

# Background
Consider a case where where have an `N` and `M` level system sitting next to each other in a box. Together, these form a bipartite `NM` level system.

Given a general density matrix of the NM level system, **can we determine if this is an entangled quantum state?**

## Entanglement
First, let us define two exclusive definitions, `entangled` and `factorizable`.

For a `NM` level system, if the density matrix can be written as the tensor product of a `NxN` and `MxM` system, then the bipartite system is said to be `factorizable`. In such a case, this is equivalent to saying that the two systems are operating independently from each other, and this is pretty boring.

If this is NOT possible, then we say that the state is `entangled`.

This problem falls into the category of NP Hard. I don't really understand the formal definition of a NP Hard problem, but my understanding is that it means it's very hard to "check the answer".

## Neural Networks
We've often heard of neural networks as being very powerful for classifying images, particularly convolutional networks. One of the best things they can do is answering a simple yes or no question about an image (is this a cat, a dog, an apple?).

Hence the question at hand, can we design and train a network to classify these `NMxNM` matrices as being entangled or not?

# Directory Structure
`Notes` - A place for links, concepts, and a logbook of work

`Code` - Main body of code

README last updated: March 6, 2021



