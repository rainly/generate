#python hsgj19_2_setup.py build_ext --inplace
from distutils.core import setup
from Cython.Build import cythonize

setup(ext_modules = cythonize("hsgj19_2.py"))