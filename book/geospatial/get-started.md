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
# Introduction to Geospatial Python

## Introduction

## The Geospatial Python Ecosystem

### Foundation Libraries

### Data Structures and Analysis

### Interactive Visualization

### Specialized Analysis

### Application Development

## Understanding Library Relationships

## Setting Up Your Environment

### Option 1: Using uv (Recommended for Beginners)

```bash
# Install uv
# macOS and Linux:
curl -LsSf https://astral.sh/uv/install.sh | sh

# Windows:
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# Create virtual environment
uv venv

# Activate environment
# macOS and Linux:
source .venv/bin/activate

# Windows:
.venv\Scripts\activate

# Install geospatial package (includes most libraries covered in this book)
uv pip install --find-links https://girder.github.io/large_image_wheels gdal pyproj
uv pip install pygis
```

### Option 2: Using pixi (For Complex Dependencies)

```bash
# Install pixi
# macOS and Linux:
curl -fsSL https://pixi.sh/install.sh | bash

# Windows:
iwr -useb https://pixi.sh/install.ps1 | iex

# Initialize project and add dependencies
pixi init
pixi add pygis jupyterlab
pixi run jupyter lab
```

### Option 3: Using conda/mamba (Traditional Approach)

```bash
# Create environment
conda create -n geo python=3.12
conda activate geo

# Install from conda-forge
conda install -c conda-forge mamba
mamba install -c conda-forge pygis
```

## Verification and First Steps

```{code-cell} ipython3
# Test core geospatial libraries
import geopandas as gpd
import rasterio
import xarray as xr
import rioxarray
import leafmap
import pandas as pd
import numpy as np

print("✓ All core libraries imported successfully!")
```

### Create Your First Interactive Map

```{code-cell} ipython3
# Create an interactive map using Leafmap
m = leafmap.Map(center=[40, -100], zoom=4, height="500px")

# Add different basemap options
m.add_basemap("OpenTopoMap")
m.add_basemap("USGS.Imagery")

# Display the map
m
```

## Learning Path and Chapter Overview

### Foundation (Start Here)

### Visualization and Interaction

### Specialized Analysis

### Foundation and Integration

### Application Development

## Key Concepts to Remember

## Getting Help and Resources

## Next Steps

## Exercises
