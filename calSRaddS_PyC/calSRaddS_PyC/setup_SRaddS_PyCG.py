#!/usr/bin/env python3

from distutils.core import setup, Extension
import numpy
calSquareRootAndSquare_PyC_module = Extension(
    'calSquareRootAndSquare_PyCG',
    sources=['dllmain.cpp'],
    language='c',
    include_dirs=[numpy.get_include()],
    library_dirs=['D:\Anaconda3'],
    libraries=[],
    # extra_compile_args=['-O3','-DNDEBUG','-v'],
    extra_compile_args=['-DNDEBUG'],

    # extra_link_args=['-m64']
    extra_link_args=['/machine:x64']

)

setup(name='calSquareRootAndSquare_PyCG',
      ext_modules=[calSquareRootAndSquare_PyC_module])
# It 's work !!!!! 
