import sys
from cx_Freeze import setup,Executable
import os

#下载cx_Freeze 库打包成exe，
#安装命令 pip install cx_Freeze-5.0.2-cp27-cp27m-win32.whl
#打包命令 Python setup.py  bdist_msi

os.environ['TCL_LIBRARY'] = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python36\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Administrator\AppData\Local\Programs\Python\Python36\tcl\tk8.6'

include_files={
    r'C:\Users\Administrator\AppData\Local\Programs\Python\Python36\DLLs\tcl86t.dll',
    r'C:\Users\Administrator\AppData\Local\Programs\Python\Python36\DLLs\tk86t.dll',
}

build_exe_options = {
    "packages": ['os','tkinter'],
    "include_files": include_files,#包含用到的包

}

base = None
# 判断Windows系统
if sys.platform == 'win32':
    base = 'Win32GUI'


setup(
          # 产品名称
           name='xl_dict',
            # 版本号
            version='0.1',
            # 产品说明
            description='XLDICT_0.1 ',
            options={'build_exe':build_exe_options},
            executables={Executable('xldict.py',base=base)}

      )


