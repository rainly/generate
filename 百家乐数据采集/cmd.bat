
python sbmsc_setup.py build_ext --inplace

pyinstaller -F  --console --onefile --icon=DDR.ico  sbmsc_main.py


