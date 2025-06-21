# Introduction to GIS Programming

[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/intro-gispro/HEAD)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/intro-gispro/blob/main)

## Introduction

This repository contains the code examples for the book - **Introduction to GIS Programming: A Practical Python Guide to Open Source Geospatial Tools**

Stay tuned for more information about the book and its release date.

![book cover](https://assets.gishub.org/images/gispro-book-cover.png)

## Table of Contents

- **Preface**
- **Software Setup**
  - Overview of Software Tools
  - Introduction to Python Package Management
  - Setting Up Visual Studio Code
  - Version Control with Git
  - Using Google Colab
  - Working with JupyterLab
  - Using Docker
- **Python Programming Fundamentals**
  - Variables and Data Types
  - Python Data Structures
  - String Operations
  - Loops and Conditional Statements
  - Functions and Classes
  - Working with Files
  - Data Analysis with NumPy and Pandas
- **Geospatial Programming with Python**
  - Introduction to Geospatial Python
  - Vector Data Analysis with GeoPandas
  - Working with Raster Data using Rasterio
  - Multi-dimensional Data Analysis with Xarray
  - Raster Analysis with Rioxarray
  - Interactive Visualization with Leafmap
  - Geoprocessing with WhiteboxTools
  - 3D Mapping with MapLibre
  - Cloud Computing with Earth Engine and Geemap
  - Hyperspectral Data Visualization with HyperCoast
  - High-Performance Geospatial Analytics with DuckDB
  - Geospatial Data Processing with GDAL and OGR
  - Building Interactive Dashboards with Voila and Solara
  - Distributed Computing with Apache Sedona

## How to Run Code Examples

The code examples can be run using Docker. There are two Docker [images](https://hub.docker.com/r/giswqs/pygis/tags) available:

A lightweight docker image without Apache Sedona:

```bash
docker pull giswqs/pygis:book
docker run -it -p 8888:8888 -v $(pwd):/app/workspace giswqs/pygis:book
```

A docker image with Apache Sedona:

```bash
docker pull giswqs/pygis:sedona
docker run -it -p 8888:8888 -p 4040:4040 -p 8080:8080 -p 8081:8081 -p 7077:7077 -p 8085:8085 -v $(pwd):/app/workspace giswqs/pygis:sedona
```

## Acknowledgments

This book was written using [MyST Markdown](https://mystmd.org) and compiled using [Typst](https://github.com/typst/typst) with the[ min-book](https://github.com/mayconfmelo/min-book) template. Credits to developers and maintainers of the Typst and MyST Markdown projects. Special thanks to [@mayconfmelo](https://github.com/mayconfmelo) for the [min-book](https://github.com/mayconfmelo/min-book) template and their help with customizing the template for this book.
