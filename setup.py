from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\Ja\AppData\Local\Programs\Python\Python35-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Ja\AppData\Local\Programs\Python\Python35-32\tcl\tk8.6'

setup(name='distme',
      version='0,1',
      description='stuff',
      executables = [Executable('distme.pyw')])
