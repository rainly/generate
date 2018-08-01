#python aaw222_setup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("aaw222.py"))