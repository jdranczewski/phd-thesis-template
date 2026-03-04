"""
This is a Python file, but you can open it in Visual Studio Code to get
the ability to run it cell by cell in an interactive environment - either
by pressing shift+enter, or "Run cell" above the sections marked with "#%%".
"""

# %%
import sys
sys.path.append("..")
import report_plot as rp

import numpy as np
import matplotlib.pyplot as plt

# %%
# Make a function for plotting a single Axes in your plot.
# Here we decorate it with rp.axes_plotter, which means that if
# it's called without an argument, it will create a placeholder
# plot for you!
# Note also the type hint for the `ax`` argument (`ax: rp.Axes`).
# This tells your code editor that ax will be a matplotlib Axes,
# which gives you autocomplete and documentation for the matplotlib
# functions!
@rp.axes_plotter
def plot_random(ax: rp.Axes):
    ax.plot(np.random.random(100))

# Calling plot_random without an argument creates an example plot,
# just to see how this Axes will work.
plot_random()

# %%
# Let's create another Axes plotter. This one takes an optional
# keyword argument.
@rp.axes_plotter
def plot_ordered(ax: rp.Axes, mult=1):
    ax.plot(np.arange(100)*mult)

# You don't have to supply the keyword argument when calling this method
plot_ordered()

# %%
# Finally, let's assemble the two plotters into the final figure!
fig = plt.figure(
    figsize=rp.figsize,
)

ax1 = fig.add_subplot(
    1, 2, 1,  # number of rows, number of columns, index of this Axes
    title="Random",
    xlabel="Index",
    ylabel="Value"
)
# Call the plotter defined above, passing an Axes this time -
# it will plot into the provided Axes.
plot_random(ax1)

ax2 = fig.add_subplot(
    1, 2, 2,
    title="Ordered",
    xlabel="Index",
)
# We can provide a keyword argument to the plotter
plot_ordered(ax2, mult=.5)
# %%
fig.savefig("z_example_a_name.pdf")
# %%
# You can also save as an SVG to edit in Inkscape, add additional labesl etc
fig.savefig("plot.svg")