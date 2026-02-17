# PoC Window Application

## Description

This project is a simple Proof of Concept (PoC) Windows application built with Python using `tkinter`.

The script creates a small graphical window that displays the text:

PoC

The application can be converted into a standalone `.exe` file using PyInstaller.

---

## Requirements

-- Python 3.x
-- PyInstaller

Install PyInstaller:
```python
pip install pyinstaller
```

## Build the Executable

To create the .exe file, run:
```python
python -m PyInstaller --onefile --noconsole poc.py
```

After the build completes, the executable will be located in:
```python
dist/poc.exe
```
