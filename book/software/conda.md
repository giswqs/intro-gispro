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

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/intro-gispro/blob/main/book/software/conda.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/intro-gispro/main?urlpath=lab/tree/book/software/conda.ipynb)

# Introduction to Python Package Management

## Introduction

## Learning Objectives

## Installing Conda (Miniconda)

### Why Miniconda?

### Installation

#### Windows

```bash
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe -o .\miniconda.exe
start /wait "" .\miniconda.exe /S
del .\miniconda.exe
```

#### macOS

```bash
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-arm64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

```bash
mkdir -p ~/miniconda3
curl https://repo.anaconda.com/miniconda/Miniconda3-latest-MacOSX-x86_64.sh -o ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

```bash
source ~/miniconda3/bin/activate
conda init --all
```

#### Linux

```bash
mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh
```

```bash
source ~/miniconda3/bin/activate
conda init --all
```

### Verifying Installation

```bash
conda --version
conda info
```

```bash
conda config --set auto_activate_base false
```

## Understanding Conda Concepts

### Environments

### Channels

## Creating Your First Geospatial Environment

```bash
# Create a new environment named 'geo' with Python 3.12
conda create -n geo python=3.12

# Activate the environment
conda activate geo

# Install mamba for faster package management
conda install -n base mamba -c conda-forge

# Install essential packages for geospatial programming
mamba install -c conda-forge pygis
```

## Troubleshooting Conda

```bash
conda init cmd.exe
```

## Essential Conda Commands

### Creating and Managing Environments

```bash
# Basic environment with specific Python version
conda create -n myenv python=3.12

# Environment with multiple packages from the start
conda create -n geoenv python=3.12 numpy pandas matplotlib

# Create environment with packages from specific channels
conda create -n geoenv2 python=3.12 -c conda-forge geopandas
```

```bash
conda activate myenv
```

```bash
conda deactivate
```

```bash
conda env list
# or
conda info --envs
```

```bash
# Remove entire environment and all its packages
conda remove -n myenv --all

# Alternative method using env remove
conda env remove -n myenv
```

```bash
# Create a copy of an existing environment
conda create -n newenv --clone oldenv
```

### Installing and Managing Packages

```bash
# Install a package from the main channel
conda install numpy

# Install multiple packages from the main channel
conda install scipy matplotlib seaborn

# Install specific versions
conda install numpy=1.24.0 pandas>=1.5.0
```

```bash
# Install without activating the environment
conda install -n myenv pandas

# Useful for setting up environments remotely
conda install -n geoenv -c conda-forge geopandas rasterio
```

```bash
# Install from conda-forge (recommended for geospatial packages)
conda install -c conda-forge geopandas
```

```bash
# Update all packages in current environment
conda update --all

# Update specific packages
conda update numpy pandas

# Update conda itself
conda update conda
```

```bash
# Search for packages
conda search scikit-learn
conda search "*gdal*"  # wildcard search

# Get package information
conda search -c conda-forge geopandas --info

# List all installed packages
conda list

# List packages matching a pattern
conda list "*geo*"
```

```bash
# Remove a single package
conda remove numpy

# Remove multiple packages
conda remove scipy matplotlib

# Remove packages and their dependencies (if not needed by others)
conda remove numpy --all
```

### Using Mamba (Faster Package Management)

```bash
# Install mamba in the base environment (do this once)
conda install -n base mamba -c conda-forge
```

```bash
# These commands are much faster with mamba
mamba create -n geofast python=3.12
mamba activate geofast
mamba install -c conda-forge geopandas rasterio geemap leafmap

# All conda commands work with mamba
mamba list
mamba update --all
mamba remove geopandas
```

### Environment Files for Reproducibility

```bash
# Export all packages and versions
conda env export > environment.yml

# Export with specific name
conda env export -n myenv > myenv.yml
```

```bash
# Create environment from exported file
conda env create -f environment.yml

# Create with different name
conda env create -f environment.yml -n newname
```

## Introducing uv: The Fast Alternative

### Installing uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

```bash
pip install uv
```

### Basic uv Usage

```bash
# Navigate to your project directory
cd /path/to/your/project

# Create a virtual environment
uv venv

# Create with specific Python version
uv venv --python 3.12

# Activate the environment (varies by OS)
# On macOS/Linux:
source .venv/bin/activate
# On Windows:
.venv\Scripts\activate
```

```bash
# Install packages
uv pip install jupyterlab leafmap

# Install from requirements file
uv pip install -r requirements.txt

# Run Python directly in the environment
uv run python script.py

# Run Jupyter directly
uv run jupyter lab
```

### uv vs pip Performance

## Best Practices for Package Management

### Environment Management

### Package Installation

### Collaboration and Reproducibility

### Troubleshooting Tips

## Key Takeaways

## Exercises

### Exercise 1: Setting Up Your First Geospatial Environment

### Exercise 2: Environment Management and Reproducibility

### Exercise 3: Exploring uv for Fast Development
