
python cpa700_setup.py build_ext --inplace

python htd188_setup.py build_ext --inplace

python sbmsc_setup.py build_ext --inplace

python a8033_setup.py build_ext --inplace

python a8033ex_setup.py build_ext --inplace

pyinstaller -F  --console --onefile --icon=DDR.ico  cpa700_main.py

pyinstaller -F  --console --onefile --icon=DDR.ico  htd188_main.py

pyinstaller -F  --console --onefile --icon=DDR.ico  sbmsc_main.py

pyinstaller -F  --console --onefile --icon=DDR.ico  a8033_main.py

pyinstaller -F  --console --onefile --icon=DDR.ico  a8033ex_main.py

