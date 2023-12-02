# cython: language_level=3

import math
cimport cython
import numpy as np
import array

@cython.boundscheck(False) 
@cython.wraparound(False)
def calSquareRootAndSquare_CY(N,result):
    #cdef double[:] result = array.array('d', [0.0] * N)
    cdef int i

    for i in range(N):
        result[i] = math.sqrt(i) + math.pow(i, 2)

    return
