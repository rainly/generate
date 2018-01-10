<<<<<<< HEAD
python cpa700_setup.py build_ext --inplace

python htd188_setup.py build_ext --inplace
=======
#python cpa700_setup.py build_ext --inplace

#python htd188_setup.py build_ext --inplace
>>>>>>> cc1e53e0eeb357fffb46fdd8aab34b8104c81047

pyinstaller -F cpa700_main.py

pyinstaller -F htd188_main.py