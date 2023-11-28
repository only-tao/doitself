# cython: language_level=3

import math
cimport cython

@cython.boundscheck(False)
@cython.wraparound(False)
def calSquareRootAndSquare_CY():
    cdef double result
    cdef int i

    for i in range(1000000):
        result = math.sqrt(i) + math.pow(i, 2)

    return result
