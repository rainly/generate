
python cpa700_setup.py build_ext --inplace

python htd188_setup.py build_ext --inplace

python sbmsc_setup.py build_ext --inplace

python a8033_setup.py build_ext --inplace

pyinstaller -F  cpa700_main.py

pyinstaller -F  htd188_main.py

pyinstaller -F  sbmsc_main.py

pyinstaller -F  a8033_main.py

