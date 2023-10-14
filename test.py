import os
from tkinter import *
from tkinter.filedialog import askopenfilename
configFile = askopenfilename()
clearScreen = 'cls'
os.system(f'installer.bat {configFile}')
