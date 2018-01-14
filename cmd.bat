<<<<<<< HEAD

#python cpa700_setup.py build_ext --inplace
=======
>>>>>>> bdd60dc2ac0d9e6627e4e28be046d0fa809a15bb

python cpa700_setup.py build_ext --inplace

python htd188_setup.py build_ext --inplace




#python sbmsc_setup.py build_ext --inplace


pyinstaller -F  cpa700_main.py

pyinstaller -F  htd188_main.py

pyinstaller -F  sbmsc_main.py