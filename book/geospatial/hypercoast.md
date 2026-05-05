---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.2
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/intro-gispro/blob/main/book/geospatial/hypercoast.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/intro-gispro/main?urlpath=lab/tree/book/geospatial/hypercoast.ipynb)

# Hyperspectral Data Visualization with HyperCoast

## Introduction

## Learning Objectives

## Environment Setup

```{code-cell} ipython3
# %pip install hypercoast pygis
```

```{code-cell} ipython3
import hypercoast
```

```{code-cell} ipython3
hypercoast.nasa_earth_login()
```

## Finding Hyperspectral Data

### Programmatic Search

```{code-cell} ipython3
results, gdf = hypercoast.search_emit(
    bbox=(-83, 25, -81, 28),
    temporal=("2024-04-01", "2024-05-16"),
    count=10,  # use -1 to return all datasets
    return_gdf=True,
)
```

```{code-cell} ipython3
gdf.explore()
```

```{code-cell} ipython3
hypercoast.download_emit(results[:1], out_dir="data")
```

### Interactive Search

```{code-cell} ipython3
m = hypercoast.Map(center=[30.0262, -90.1345], zoom=8)
m.search_emit()
m
```

```{code-cell} ipython3
if hasattr(m, "_NASA_DATA_GDF"):
    display(m._NASA_DATA_GDF.head())
```

```{code-cell} ipython3
hypercoast.download_emit(results[:1], out_dir="data")
```

## Downloading Hyperspectral Data

```{code-cell} ipython3
url = "https://github.com/opengeos/datasets/releases/download/hypercoast/EMIT_L2A_RFL_001_20240404T161230_2409511_009.nc"
filepath = "data/EMIT_L2A_RFL_001_20240404T161230_2409511_009.nc"
hypercoast.download_file(url, filepath, quiet=True)
```

## Reading Hyperspectral Data

```{code-cell} ipython3
dataset = hypercoast.read_emit(filepath)
dataset
```

## Visualizing Hyperspectral Data

```{code-cell} ipython3
m = hypercoast.Map()
m.add_basemap("SATELLITE")
m.add_emit(dataset, wavelengths=[1000, 600, 500], vmin=0, vmax=0.3, layer_name="EMIT")
m.add("spectral")
m
```

## Creating Image Cubes

```{code-cell} ipython3
ds = dataset.sel(longitude=slice(-90.1482, -89.7321), latitude=slice(30.0225, 29.7451))
```

```{code-cell} ipython3
p = hypercoast.image_cube(
    ds,
    variable="reflectance",
    cmap="jet",
    clim=(0, 0.4),
    rgb_wavelengths=[1000, 700, 500],
    rgb_gamma=2,
    title="EMIT Reflectance",
)
p.show()
```

## Interactive Slicing

```{code-cell} ipython3
ds = dataset.sel(longitude=slice(-90.05, -89.99), latitude=slice(30.00, 29.93))
```

```{code-cell} ipython3
p = hypercoast.image_cube(
    ds,
    variable="reflectance",
    cmap="jet",
    clim=(0, 0.5),
    rgb_wavelengths=[1000, 700, 500],
    rgb_gamma=2,
    title="EMIT Reflectance",
    widget="plane",
)
p.add_text("Band slicing", position="upper_right", font_size=14)
p.show()
```

## Interactive Thresholding

```{code-cell} ipython3
p = hypercoast.image_cube(
    ds,
    variable="reflectance",
    cmap="jet",
    clim=(0, 0.5),
    rgb_wavelengths=[1000, 700, 500],
    rgb_gamma=2,
    title="EMIT Reflectance",
    widget="threshold",
)
p.add_text("Thresholding", position="upper_right", font_size=14)
p.show()
```

## Key Takeaways

## Exercises

### Exercise 1: Data Discovery and Acquisition

### Exercise 2: Spectral Profile Analysis

### Exercise 3: Band Combination Exploration

### Exercise 4: Interactive Visualization

### Exercise 5: 3D Cube Analysis
