
python aaw222_setup.py build_ext --inplace

pyinstaller -F  --console --onefile --icon=DDR.ico  aaw222_main.py


