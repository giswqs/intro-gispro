---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.16.4
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---
# Working with Raster Data Using Rasterio

## Introduction

### What is Raster Data?

### Why Use Rasterio?

## Learning Objectives

## Installing Rasterio

```{code-cell} ipython3
# %pip install rasterio pygis
```

```{code-cell} ipython3
import rasterio
import rasterio.plot
import geopandas as gpd
import numpy as np
import matplotlib.pyplot as plt
```

## Reading Raster Data

### Opening Raster Files

```{code-cell} ipython3
raster_path = (
    "https://github.com/opengeos/datasets/releases/download/raster/dem_90m.tif"
)
src = rasterio.open(raster_path)
print(src)
```

### Understanding Raster Metadata

#### Basic File Information

```{code-cell} ipython3
print(f"File name: {src.name}")
print(f"File mode: {src.mode}")
```

```{code-cell} ipython3
print("Raster metadata:")
for key, value in src.meta.items():
    print(f"{key}: {value}")
```

#### Spatial Properties

```{code-cell} ipython3
print(f"Coordinate Reference System: {src.crs}")
```

```{code-cell} ipython3
print(f"Pixel size (x, y): {src.res}")
```

```{code-cell} ipython3
print(f"Raster dimensions: {src.width} x {src.height} pixels")
```

```{code-cell} ipython3
print(f"Geographic bounds: {src.bounds}")
```

#### Data Properties

```{code-cell} ipython3
print(f"Data types: {src.dtypes}")
```

```{code-cell} ipython3
print(f"Number of bands: {src.count}")
```

### The Affine Transform

```{code-cell} ipython3
print("Affine transform:")
print(src.transform)
```

## Visualizing Raster Data

### Basic Raster Visualization

```{code-cell} ipython3
rasterio.plot.show(src)
```

### Understanding Color Maps

```{code-cell} ipython3
fig, ax = plt.subplots(figsize=(8, 8))
rasterio.plot.show(src, cmap="terrain", ax=ax, title="Digital Elevation Model (DEM)")
plt.show()
```

### Adding Colorbars

```{code-cell} ipython3
elev_band = src.read(1)
plt.figure(figsize=(8, 8))
plt.imshow(elev_band, cmap="terrain")
plt.colorbar(label="Elevation (meters)", shrink=0.5)
plt.title("DEM with Terrain Colormap")
plt.show()
```

### Visualizing Multiple Bands

```{code-cell} ipython3
raster_path = "https://github.com/opengeos/datasets/releases/download/raster/LC09_039035_20240708_90m.tif"
src = rasterio.open(raster_path)
```

#### Single Band Visualization

```{code-cell} ipython3
rasterio.plot.show((src, 1), cmap="gray", title="Band 1")
```

#### RGB Composite

```{code-cell} ipython3
nir_band = src.read(5)
red_band = src.read(4)
green_band = src.read(3)

# Stack the bands into a single array
rgb = np.dstack((nir_band, red_band, green_band)).clip(0, 1)

# Plot the stacked array
plt.figure(figsize=(8, 8))
plt.imshow(rgb)
plt.title("Bands NIR, Red, and Green combined")
plt.show()
```

#### Creating a Multi-Panel Plot

```{code-cell} ipython3
band_names = ["Coastal Aerosol", "Blue", "Green", "Red", "NIR", "SWIR1", "SWIR2"]

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(8, 10))
axes = axes.flatten()  # Flatten the 2D array of axes to 1D for easy iteration

for band in range(1, src.count):
    data = src.read(band)
    ax = axes[band - 1]
    im = ax.imshow(data, cmap="gray", vmin=0, vmax=0.5)
    ax.set_title(f"Band {band_names[band - 1]}")
    fig.colorbar(im, ax=ax, label="Reflectance", shrink=0.5)

plt.tight_layout()
plt.show()
```

### Overlaying Vector Data

```{code-cell} ipython3
# Load raster data
raster_path = (
    "https://github.com/opengeos/datasets/releases/download/raster/dem_90m.tif"
)
src = rasterio.open(raster_path)

# Load vector data
vector_path = (
    "https://github.com/opengeos/datasets/releases/download/places/dem_bounds.geojson"
)
gdf = gpd.read_file(vector_path)
gdf = gdf.to_crs(src.crs)  # Ensure same CRS as raster

# Create the plot
fig, ax = plt.subplots(figsize=(8, 8))
rasterio.plot.show(src, cmap="terrain", ax=ax, title="DEM with Vector Overlay")
gdf.plot(ax=ax, edgecolor="red", facecolor="none", linewidth=2)
plt.show()
```

## Accessing and Manipulating Raster Bands

### Stacking Multiple Bands

```{code-cell} ipython3
raster_path = "https://github.com/opengeos/datasets/releases/download/raster/LC09_039035_20240708_90m.tif"
src = rasterio.open(raster_path)
```

```{code-cell} ipython3
nir_band = src.read(5)
red_band = src.read(4)
green_band = src.read(3)

# Stack the bands into a single array
rgb = np.dstack((nir_band, red_band, green_band)).clip(0, 1)

print(rgb.shape)
```

### Basic Band Math (NDVI Calculation)

```{code-cell} ipython3
# NDVI Calculation: NDVI = (NIR - Red) / (NIR + Red)
ndvi = (nir_band - red_band) / (nir_band + red_band)
ndvi = ndvi.clip(-1, 1)

plt.figure(figsize=(8, 8))
plt.imshow(ndvi, cmap="RdYlGn", vmin=-1, vmax=1)
plt.colorbar(label="NDVI", shrink=0.75)
plt.title("NDVI")
plt.xlabel("Column #")
plt.ylabel("Row #")
plt.show()
```

## Writing Raster Data

```{code-cell} ipython3
with rasterio.open(raster_path) as src:
    profile = src.profile
print(profile)
```

```{code-cell} ipython3
profile.update(dtype=rasterio.float32, count=1, compress="lzw")
print(profile)
```

```{code-cell} ipython3
output_raster_path = "ndvi.tif"

with rasterio.open(output_raster_path, "w", **profile) as dst:
    dst.write(ndvi, 1)
print(f"Raster data has been written to {output_raster_path}")
```

## Clipping Raster Data

### Clipping with a Bounding Box

```{code-cell} ipython3
raster_path = "https://github.com/opengeos/datasets/releases/download/raster/LC09_039035_20240708_90m.tif"
src = rasterio.open(raster_path)
data = src.read()
```

```{code-cell} ipython3
data.shape
```

```{code-cell} ipython3
subset = data[:, 900:1400, 700:1200].clip(0, 1)
rgb_subset = np.dstack((subset[4], subset[3], subset[2]))
rgb_subset.shape
```

```{code-cell} ipython3
# Plot the stacked array
plt.figure(figsize=(8, 8))
plt.imshow(rgb_subset)
plt.title("Las Vegas, NV")
plt.show()
```

```{code-cell} ipython3
from rasterio.windows import Window
from rasterio.transform import from_bounds

# Assuming subset and src are already defined
# Define the window of the subset (replace with actual window coordinates)
window = Window(col_off=700, row_off=900, width=500, height=500)

# Calculate the bounds of the window
window_bounds = rasterio.windows.bounds(window, src.transform)

# Calculate the new transform based on the window bounds
new_transform = from_bounds(*window_bounds, window.width, window.height)
```

```{code-cell} ipython3
with rasterio.open(
    "las_vegas.tif",
    "w",
    driver="GTiff",
    height=subset.shape[1],
    width=subset.shape[2],
    count=subset.shape[0],
    dtype=subset.dtype,
    crs=src.crs,
    transform=new_transform,
    compress="lzw",
) as dst:
    dst.write(subset)
```

### Clipping with a Vector Dataset

```{code-cell} ipython3
import fiona
import rasterio.mask
```

```{code-cell} ipython3
geojson_path = "https://github.com/opengeos/datasets/releases/download/places/las_vegas_bounds_utm.geojson"
bounds = gpd.read_file(geojson_path)
```

```{code-cell} ipython3
fig, ax = plt.subplots()
rasterio.plot.show(src, ax=ax)
bounds.plot(ax=ax, edgecolor="red", facecolor="none")
```

```{code-cell} ipython3
with fiona.open(geojson_path, "r") as f:
    shapes = [feature["geometry"] for feature in f]
out_image, out_transform = rasterio.mask.mask(src, shapes, crop=True)
```

```{code-cell} ipython3
out_meta = src.meta
out_meta.update(
    {
        "driver": "GTiff",
        "height": out_image.shape[1],
        "width": out_image.shape[2],
        "transform": out_transform,
    }
)

with rasterio.open("las_vegas_clip.tif", "w", **out_meta) as dst:
    dst.write(out_image)
```

## Key Takeaways

## Exercises

### Sample Datasets

### Exercise 1: Reading and Exploring Raster Data

```{code-cell} ipython3

```

### Exercise 2: Working with Raster Bands

```{code-cell} ipython3

```

### Exercise 3: Basic Raster Operations

```{code-cell} ipython3

```

### Exercise 4: Writing and Saving Raster Data

```{code-cell} ipython3

```

### Exercise 5: Clipping and Subsetting

```{code-cell} ipython3

```
