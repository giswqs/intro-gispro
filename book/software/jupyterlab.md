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
# Working with JupyterLab

## Introduction

## Learning Objectives

## Installing and Setting Up JupyterLab

### Using conda

```bash
conda create -n geo python=3.12
conda activate geo
conda install -c conda-forge jupyterlab leafmap
```

### Using pip

```bash
pip install jupyterlab leafmap
```

### Verifying Your Installation

```bash
jupyter lab --version
```

## Getting Started with JupyterLab

### Launching JupyterLab

```bash
jupyter lab
```

```bash
# Launch on a specific port (useful if the default port is busy)
jupyter lab --port=8889

# Launch without automatically opening browser (useful for remote servers)
jupyter lab --no-browser --port=8888
```

### Understanding the JupyterLab Interface

### Creating Your First Notebook in JupyterLab

## Essential Keyboard Shortcuts

### Understanding Notebook Modes: The Foundation

### The Most Important Shortcuts

### Command Mode Shortcuts (Press `Esc` first)

### Edit Mode Shortcuts (Press `Enter` first)

## Running Code Examples on MyBinder

## Key Takeaways

## Exercises

### Exercise 1: Setting Up Your Geospatial JupyterLab Environment

   ```bash
   conda create -n geolab python=3.12
   conda activate geolab
   ```

   ```bash
   conda install -c conda-forge jupyterlab geopandas matplotlib ipyleaflet
   ```

### Exercise 2: Mastering Keyboard Shortcuts and Efficient Workflow
