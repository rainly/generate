
python alipay_setup.py build_ext --inplace

pyinstaller -F  --console --onefile --icon=DDR.ico  alipay_main.py


