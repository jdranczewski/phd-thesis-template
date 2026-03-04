# phd-thesis-template
Complete and well-designed LaTeX template for PhD theses, for Imperial College London and beyond.

The heart of this template is `thesis_style.sty`, which imports relevant packages and adjusts the style of the document.
Then, `main.tex` uses that style and contains scaffolding for laying out your thesis, with each chapter being a `.tex` file in `sections`.
Note that SyncTeX, references, and the bibliography will all track across the multiple files!
Just use `main.tex` as your document root, and LaTeX should figure it out.

You can use this repository as a GitHub repository template (green button in the top right corner), or just download it as a zip file.

## Working with LaTeX
My editor of choice is TeXstudio, with the MikTeX LaTeX distribution on Windows.
I prefer working locally, because I can keep all the figures in the same folder, and sync it all to GitHub.
That said, this should all work with Overleaf too!
You can just upload this folder to it, or sync a repository from GitHub.

If your compilation times are too long, you may want to use the `\includeonly` statement at the top of `main.tex`, and look at whether your document is being compiled multiple times.
Also, check your figure file sizes with `figures/figure_sizes.py`!

## Plotting and Python
This template includes my preferred way to deal with figures, but of course you don't have to follow it.
In case you do, here are some notes on that.

I use Python and matplotlib to make my figures.
It's important to make sure the styling of your figures is consistent, and matplotlib provides a nice mechanism for that -- `.mplstyle` files.
You can have a look at `figures/report.mplstyle` for the settings I changed from the matplotlib defaults.
Loading that file before making all of your figures ensures that they will have consistent line widths, colours, and font sizes. You should try to make the matplotlib figures the same size in inches as they will be in the document, this way the size of the font specified in matplotlib will be the same as seen in the document, and there will be no scaling issues between the figures.
**For this template, the figure width should be 6.29921 inches.**

You can easily set these defaults in your code by importing `figures/report_plot.py`!
Make sure Python can find the file by adding `figures` to your PYTHONPATH, and call `import report_plot as rp` -- see `figures/z_example_a_name/example.py` for an example.

I prefer to have a separate folder for each figure.
These are named following an alphabetical convention to ensure good sorting: `[chapter letter]_[chapter short name]_[figure letter]_[figure short name]`. For example, `a_introduction_b_machine_learning`.
You can use `figures/make_folder.py` to make these folders for you.
They will be populated with a Python file template (`figures/template.py`) and an Inkscape svg template (`figures/template.svg`).
The final figure PDF is named the same as the folder, to distinguish it from helper files, and make including it in the TeX document easier (`a_introduction_b_machine_learning/a_introduction_b_machine_learning` is easy to copy-paste in, however clumsy it looks).

The workflow I used is to open the Python file in Visual Studio Code with the Jupyter and Python extensions installed, and you can then run sections of the file in an interactive IPython session.
Easier to inspect the files than a full Jupyter Notebook, but you get the benefits of quick iteration in an interactive environment.
See `figures/z_example_a_name/example.py` for more details.

Also `figures/z_example_a_name/example.py` for my preferred way to assemble figures from functions that plot single Axes, and `figures/snippets.py` for useful matplotlib snippets for more advanced layouts.

I recommend reading through https://matplotlib.org/stable/users/explain/quick_start.html (even if you think you know matplotlib. Also, use the object-oriented interface rather than the pyplot-style one in my opinion!) and https://matplotlib.org/cheatsheets/ -- both are great resources.

## Inkscape for plotting
I used Inkscape to lay out my final figures, and you can find a useful template in `figures/template.svg`, including arrows, shapes, and text sizes.
It's also the right width to be included without scaling, as with Python figures.
I would make the figure, then select all the visible parts, and export it to pdf while marking "export only selection".

You can use `figures/snippets.py` to generate an Inkscape palette with the selected matplotlib colours, see https://inkscape-manuals.readthedocs.io/en/latest/palette.html on how to add it.
