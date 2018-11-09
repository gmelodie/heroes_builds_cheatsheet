from cx_Freeze import setup, Executable
from multiprocessing import Queue

# Run file with 'build' command to generate exe in corresponding folder
#
# Has to be built with Python 3.6 or earlier because of bug with cx_Freeze

base = "Win32GUI"

executables = [Executable("hbc.py", base=base)]

packages = ["idna", "sys", "mainWindow", "multiprocessing"]
includes = ["PyQt5", "heroes_build_scrapper"]
options = {
    'build_exe': {
        'packages':packages,
        'includes':includes
    },
}

setup(
    name = "hbc",
    options = options,
    version = "1.1",
    description = 'In-game cheatsheet for hero builds in Heroes of the Storm',
    executables = executables
)
