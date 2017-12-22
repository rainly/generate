color 0A && echo off


rem protoc程序名
set "PROTOC_EXE=protoc.exe"
rem .proto文件名
set "PROTOCOL_FILE_NAME=protocol.proto"

%PROTOC_EXE% --version

set "WORK_DIR=%cd%"
rem cpp
set "CPP_OUT_PATH=%cd%\cpp"
if not exist %CPP_OUT_PATH% md %CPP_OUT_PATH%
rem cs
set "CS_OUT_PATH=%cd%\cs"
if not exist %CS_OUT_PATH% md %CS_OUT_PATH%
rem java
set "JAVA_OUT_PATH=%cd%\java"
if not exist %JAVA_OUT_PATH% md %JAVA_OUT_PATH%
rem java Nano
set "JAVANANO_OUT_PATH=%cd%\javanano"
if not exist %JAVANANO_OUT_PATH% md %JAVANANO_OUT_PATH%
rem js
set "JS_OUT_PATH=%cd%\js"
if not exist %JS_OUT_PATH% md %JS_OUT_PATH%
rem objc(Objective C)
set "OBJC_OUT_PATH=%cd%\objc"
if not exist %OBJC_OUT_PATH% md %OBJC_OUT_PATH%
rem php
set "PHP_OUT_PATH=%cd%\php"
if not exist %PHP_OUT_PATH% md %PHP_OUT_PATH%
rem python
set "PYTHON_OUT_PATH=%cd%\python"
if not exist %PYTHON_OUT_PATH% md %PYTHON_OUT_PATH%
rem ruby
set "RUBY_OUT_PATH=%cd%\ruby"
if not exist %RUBY_OUT_PATH% md %RUBY_OUT_PATH%

echo.generate cpp
"%WORK_DIR%\%PROTOC_EXE%" --proto_path="%WORK_DIR%" --cpp_out="%CPP_OUT_PATH%" "%WORK_DIR%\%PROTOCOL_FILE_NAME%"
echo.generate cs
"%WORK_DIR%\%PROTOC_EXE%" --proto_path="%WORK_DIR%" --csharp_out="%CS_OUT_PATH%" "%WORK_DIR%\%PROTOCOL_FILE_NAME%"
echo.generate java
"%WORK_DIR%\%PROTOC_EXE%" --proto_path="%WORK_DIR%" --java_out="%JAVA_OUT_PATH%" "%WORK_DIR%\%PROTOCOL_FILE_NAME%"
echo.generate java nano
"%WORK_DIR%\%PROTOC_EXE%" --proto_path="%WORK_DIR%" --javanano_out="%JAVANANO_OUT_PATH%" "%WORK_DIR%\%PROTOCOL_FILE_NAME%"
echo.generate js
"%WORK_DIR%\%PROTOC_EXE%" --proto_path="%WORK_DIR%" --js_out="%JS_OUT_PATH%" "%WORK_DIR%\%PROTOCOL_FILE_NAME%"
echo.generate objective c
"%WORK_DIR%\%PROTOC_EXE%" --proto_path="%WORK_DIR%" --objc_out="%OBJC_OUT_PATH%" "%WORK_DIR%\%PROTOCOL_FILE_NAME%"
echo.generate php
"%WORK_DIR%\%PROTOC_EXE%" --proto_path="%WORK_DIR%" --php_out="%PHP_OUT_PATH%" "%WORK_DIR%\%PROTOCOL_FILE_NAME%"
echo.generate python
"%WORK_DIR%\%PROTOC_EXE%" --proto_path="%WORK_DIR%" --python_out="%PYTHON_OUT_PATH%" "%WORK_DIR%\%PROTOCOL_FILE_NAME%"
echo.generate ruby
"%WORK_DIR%\%PROTOC_EXE%" --proto_path="%WORK_DIR%" --ruby_out="%RUBY_OUT_PATH%" "%WORK_DIR%\%PROTOCOL_FILE_NAME%"
pause