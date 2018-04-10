#python a8033_setup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("Betting3.py"))