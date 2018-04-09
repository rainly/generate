

python a8033_setup.py build_ext --inplace

python a8033ex_setup.py build_ext --inplace

python d3s4_setup.py build_ext --inplace

python s3d4_setup.py build_ext --inplace

pyinstaller -F  --console --onefile --icon=DDR.ico  a8033_main.py

pyinstaller -F  --console --onefile --icon=DDR.ico  a8033ex_main.py

pyinstaller -F  --console --onefile --icon=DDR.ico  d3s4_main.py

pyinstaller -F  --console --onefile --icon=DDR.ico  s3d4_main.py

