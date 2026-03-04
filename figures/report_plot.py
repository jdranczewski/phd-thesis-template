"""
A set of tools and matplotlib defaults to make plotting figures for your
thesis easier. Have a look at the comments below, explaining what each
section does.

We assume you would run `import report_plot as rp` at the top of your
plotting file.

See the `z_example_a_name` folder for example usage, and `README.md` in
the main repository (https://github.com/jdranczewski/phd-thesis-template)
for more notes.
"""

import os
from functools import wraps

import numpy as np
import matplotlib # This lets you do rp.matplotlib if needed in your files
import matplotlib.pyplot as plt
from matplotlib.axes import Axes # Useful for type hinting
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.gridspec import GridSpec

# Use a consistent matplotlib style file
plt.style.use(os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'report.mplstyle'
))
# See here for things that you can customise by editing the
# `report.mplstyle` file:
# https://matplotlib.org/stable/users/explain/customizing.html

# Default values
width = 6.29921
height = 2.756
figsize = (width, height)

letters = 'abcdefghijklmnopqrstuvwxyz'

# Data folders
# You can use these to reference files from OneDrive with Python's f-strings:
# f"{rp.onedrive}/folder/file.extension"
box = "C:/Users/<username>/Box"
onedrive = "C:/Users/<username>/OneDrive - Imperial College London"

# Colour cycle
# This is slightly updated from matplotlib's default tab cycle, with
# slightly more muted, pleasant colours, but keeping the good readability.
# See https://jrnold.github.io/ggthemes/reference/tableau_color_pal.html
# and also https://github.com/matplotlib/matplotlib/issues/21840 for discussion
# on why these are not the current matplotlib default.
tab10x = {
    'tabx:blue': "#4e79a7",
    'tabx:orange': "#f28e2b",
    'tabx:red': "#e15759",
    'tabx:cyan': "#76b7b2",
    'tabx:green': "#59a14f",
    'tabx:yellow': "#edc948",
    'tabx:purple': "#b07aa1",
    'tabx:pink': "#ff9da7",
    'tabx:brown': "#9c755f",
    'tabx:grey': "#bab0ac",
}
tab10x_cycle = [tab10x[key] for key in tab10x]


####################
# Helper functions #
####################

# Plotting

def axes_plotter(function):
    """
    Enables a function to plot on an Axes, and if None are given,
    creates a placeholder one.

    See `z_example_a_name/example.py` for example usage.
    """
    @wraps(function)
    def make_or_pass_ax(ax: None | Axes = None, **kwargs):
        if ax is None:
            fig, ax = plt.subplots(figsize=(width/2, height))
        value = function(ax, **kwargs)
        return value
    return make_or_pass_ax

def axes_plotter_3d(function):
    """
    Enables a function to plot on a 3D Axes, and if None are given,
    creates a placeholder one.
    """
    @wraps(function)
    def make_or_pass_ax(ax: None | Axes = None, **kwargs):
        if ax is None:
            fig = plt.figure(figsize=(width/2, height))
            ax = fig.add_subplot(1, 1, 1, projection="3d")
        value = function(ax, **kwargs)
        return value
    return make_or_pass_ax

# Colour management

def hex2rgb(hex: str):
    hex = hex.lstrip("#")
    return np.array(tuple((int(hex[i:i+2], 16) for i in (0, 2, 4))))

@axes_plotter
def plot_colours(ax: Axes):
    """
    Preview the current colour cycle.
    """
    ax.scatter(
        np.arange(10)%5, np.arange(10)//5,
        c=[f"C{i}" for i in range(10)], s=500
    )
    for i in range(10):
        ax.text(
            i%5, i//5, i, ha="center", va="center"
        )
    ax.set_ylim(2, -1)

# Qt GUI
# These functions should work both in IPython and when running files directly.

_qapp = None
def enable_gui():
    # Save a reference to the QApplication so it doesn't get garbage collected
    global _qapp
    # Check if we're in IPython
    import IPython
    ipython = IPython.get_ipython()
    if ipython:
        # This is equivalent to the "%gui qt" magic
        ipython.enable_gui("qt")
    else:
        # Create a QApplication ourselves
        from qtpy import QtWidgets
        _qapp = QtWidgets.QApplication([])

def show_widget(widget):
    # Always show the widget
    # (note that if a QApplication doesn't exist, Widget creation
    # would have failed, so we can just assume it exists.)
    widget.show()
    # Check if we're in IPython
    import IPython
    ipython = IPython.get_ipython()
    if not ipython:
        # If we're _not_ in IPython, we have to execute
        # the QApp ourselves.
        from qtpy import QtCore
        QtCore.QCoreApplication.instance().exec()
        # This will return once the Widget is closed