# YT - is an open-source, permissively-licensed Python library for analyzing and visualizing volumetric data.

# https://github.com/yt-project/yt
# https://yt-project.org/data/
# https://github.com/yt-project/yt/tree/main/doc/source/quickstart

"""
Using the Automatic Downloader
To use the load_sample command to utilize the pooch auto-downloader.
ds = yt.load_sample("IsolatedGalaxy")
"""


# Simple Visualizations of Data
import yt

ds = yt.load_sample("enzo_tiny_cosmology")
print("Redshift =", ds.current_redshift)

p = yt.ProjectionPlot(ds, "y", ("gas", "density"))
p.show()


p.zoom(2.0)

p.pan_rel((0.1, 0.0))

p.zoom(10.0)

p.pan_rel((-0.25, -0.5))

p.zoom(0.1)

p = yt.ProjectionPlot(
    ds,
    "z",
    [("gas", "density"), ("gas", "temperature")],
    weight_field=("gas", "density"),
)
p.show()
