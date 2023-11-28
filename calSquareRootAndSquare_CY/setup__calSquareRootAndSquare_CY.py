from distutils.core import setup,Extension
from Cython.Build import cythonize
# import numpy
setup(
    ext_modules=cythonize(Extension(
    'calSquareRootAndSquare_CY_O2',
    sources=['calSquareRootAndSquare_CY.pyx'],
    extra_compile_args=['-O2','-DNDEBUG'],
)))
# setup(
#     ext_modules=cythonize("calSquareRootAndSquare_CY.pyx"),
# )
