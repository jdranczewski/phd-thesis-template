"""
Create folder for a figure, containing an SVG template for Inkscape and
a Python template for plotting.

Either run the file with a figure name as the argument::

    python make_folder.py z_example_a_name

Or run the script without arguments and provide the name when prompted.

The folder name will be copied to your clipboard.
"""

import sys, os
import shutil
import pyperclip

if __name__ == "__main__":
    try:
        folder_name = sys.argv[1]
    except IndexError:
        folder_name = input("folder name: ")

    print(f"Making folder: '{folder_name}'")
    os.mkdir(folder_name)
    shutil.copy2("template.svg", f"{folder_name}/{folder_name}.svg")
    shutil.copy2("template.py", folder_name)
    pyperclip.copy(folder_name)
