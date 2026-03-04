"""
A bunch of useful templates, mostly for doing different things in matplotlib.

This is a Python file, but you can open it in Visual Studio Code to get
the ability to run it cell by cell in an interactive environment - either
by pressing shift+enter, or "Run cell" above the sections marked with "#%%".
"""

#%%
import numpy as np
import matplotlib.pyplot as plt
import report_plot as rp

#%%
# Basic plot wiht some rows and columns
fig, axes = plt.subplots(
    nrows=1, ncols=1,
    figsize=rp.figsize,
)

for i in range(10):
    axes.plot(np.random.random(10))

#%%
# Adding axes manually, which lets you specify axis dimensions,
# labels, titles, etc.
fig = plt.figure(
    figsize=rp.figsize,
)
ax = fig.add_subplot(
    1, 2, 1, # number of rows, number of columns, index of this Axes
    title="",
    xlabel="",
    ylabel=""
)
ax = fig.add_subplot(
    1, 2, 2,
    title="",
    xlabel="",
    ylabel=""
)

# %%
# Gridspec plots let you have a lot of freedom on how the Axes
# should be laid out.
fig = plt.figure(
    figsize=rp.figsize
)
spec = rp.GridSpec(
    ncols=2, nrows=2,
    figure=fig,
)
ax1 = fig.add_subplot(
    spec[:, 0],
    title="Bar chart",
    xlabel="np.arange(10)",
    ylabel="np.random.random(10)+1"
)
ax2 = fig.add_subplot(
    spec[0, 1],
    title="Many lines",
    ylabel="np.random"
)
ax3 = fig.add_subplot(
    spec[1, 1],
    sharex=ax2,
    xlabel="np.arange(20)"
)
ax2.tick_params(labelbottom=False)

ax1.bar(np.arange(10), np.random.random(10)+1, color=rp.tab10x_cycle)
for i in range(5):
    ax2.plot(np.random.random(20), label=f"Label {i}" if i<3 else None)
for i in range(10):
    ax3.plot(np.random.random(20))
ax2.legend()

# %%
# Convert cycle to GIMP palette for use in Inkscape
# Follow https://inkscape-manuals.readthedocs.io/en/latest/palette.html and
# paste the output into a .gpl file.
for c, key in zip(rp.tab10x_cycle, rp.tab10x):
    print("{:3d} {:3d} {:3d}  {}".format(*(int(c[1+i:i+3], 16) for i in (0, 2, 4)), key))

# %%
