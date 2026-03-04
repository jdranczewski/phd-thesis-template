"""
Print a sorted list of pdf figure file sizes.
"""

# %%
import os
from glob import glob
# %%
figures = sorted(
    glob("figures/*/*.pdf"),
    key=lambda x: os.path.getsize(x),
    reverse=True
)
if not len(figures):
    figures = sorted(
        glob("../figures/*/*.pdf"),
        key=lambda x: os.path.getsize(x),
        reverse=True
    )
sizes = [os.path.getsize(x) for x in figures]

# %%
for fig, size in zip(figures, sizes):
    print(f"{os.path.basename(fig)}: {size/1024:,.0f} kB")
print("-"*10)
print(f"Total: {sum(sizes)/1024:,.0f} kB")
# %%
