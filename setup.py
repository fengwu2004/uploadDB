from cx_Freeze import setup, Executable
import sys

build_exe_options = {"packages": ['appdirs', 'packaging', 'openpyxl', 'pymongo'], 'path':sys.path + [sys.path[0] + '/data', sys.path[0] + '/stockmgr']}

print(build_exe_options['path'])

setup(
    name = 'guifoo',
    version = '0.1',
    options = {'build_exe': build_exe_options},
    executables = [Executable('main.py', base = 'Console')]
)