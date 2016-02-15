import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup(name="Pappu Pakia",
	version="1.0",
	description="My implementation of Pappupakia game in Python",
	options={"build_exe": {"include_files": ["data/", "fonts/"]}},
	executables = [Executable("main.py", base=base)])
