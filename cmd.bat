python cpa700_setup.py build_ext --inplace

python htd188_setup.py build_ext --inplace

pyinstaller -F cpa700_main.py

pyinstaller -F htd188_main.py