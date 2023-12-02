from numba.pycc import CC
from numba import jit, njit
import numpy as np
import math 
cc = CC('calSquareRootAndSquare_AOT')
cc.verbose = True

@cc.export('calSquareRootAndSquare_AOT','f8[:](i4)') ## ('name','float[](int 4 bytes, int 4 bytes)') return float
def calSquareRootAndSquare_AOT(N):
    result = np.zeros(N,dtype=np.float64)
    for i in range(N):
        result[i] = math.sqrt(i)+ math.pow(i,2)
    return result

if __name__ == "__main__":
    cc.compile()
