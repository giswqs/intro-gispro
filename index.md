# Introduction to GIS Programming

[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/intro-gispro/HEAD)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/intro-gispro/blob/main)

## Introduction

This repository contains the code examples for the book - **Introduction to GIS Programming: A Practical Python Guide to Open Source Geospatial Tools**

To purchase a PDF version of the book, please visit <https://leanpub.com/gispro>.

The color print version of the book will soon be available on Amazon. Stay tuned!

![book cover](https://assets.gishub.org/images/gispro-book-cover.png)

## Table of Contents

- **Preface**

  - Introduction
  - Who This Book Is For
  - What This Book Covers
  - Getting the Most Out of This Book
  - Conventions Used in This Book
  - Downloading the Code Examples
  - Video Tutorials
  - Get in Touch
  - Acknowledgments
  - About the Author
  - Licensing and Copyright

- **Software Setup**
  - Overview of Software Tools
  - Introduction to Python Package Management
  - Setting Up Visual Studio Code
  - Version Control with Git
  - Using Google Colab
  - Working with JupyterLab
  - Using Docker
-
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

## Video Tutorials

Complementing the written content, this book is supported by a comprehensive series of video tutorials that walk through key concepts and provide additional examples:

**https://tinyurl.com/intro-gispro-videos**

The videos are designed to complement, not replace, the written material. They're particularly helpful for:

- Visual learners who benefit from seeing code being written and executed
- Understanding complex concepts through multiple explanations
- Learning about the development workflow and best practices
- Seeing how to approach problems and debug issues

The playlist is organized to follow the book's structure. You can watch them in order as you progress through the book, or jump to specific topics as needed.

The videos were created in Fall 2024 when I was teaching the [**Introduction to GIS Programming**](https://geog-312.gishub.org) course at the University of Tennessee. Although the course has concluded, the videos remain relevant and can be used as a reference for the book. Additional videos will be added in the future.

## Enroll for Certification

Please note that you can access the [course materials](https://geog-312.gishub.org) and [lecture videos](https://tinyurl.com/intro-gispro-videos) on the course website without enrolling in the course. However, if you're interested in submitting lab assignments, receiving grades, and earning a certificate of completion, you can enroll in the course at any time by clicking the link below. There is no deadline for enrollment, and you can complete the course at your own pace.

[Enroll Now](https://tiny.utk.edu/intro-gis-programming)

## About the Author

Dr. Qiusheng Wu is an Associate Professor and the Director of Graduate Studies in the Department of Geography & Sustainability at the University of Tennessee, Knoxville. He also serves as an Amazon Scholar. Dr. Wu's research focuses on geospatial data science and open-source software development, with an emphasis on leveraging big geospatial data and cloud computing to study environmental change, particularly surface water and wetland inundation dynamics. He is the creator of several widely used open-source Python packages, including [geemap](https://geemap.org) [^geemap], [leafmap](https://leafmap.org) [^leafmap], [segment-geospatial](https://samgeo.gishub.org) [^samgeo], and [geoai](https://opengeoai.org) [^geoai], which support advanced geospatial analysis and interactive visualization. His open-source work is available at the [Open Geospatial Solutions](https://github.com/opengeos) [^opengeos] on GitHub.

## Acknowledgments

This book was written using [MyST Markdown](https://mystmd.org) and compiled using [Typst](https://github.com/typst/typst) with the[min-book](https://github.com/mayconfmelo/min-book) template. Credits to developers and maintainers of the Typst and MyST Markdown projects. Special thanks to [@mayconfmelo](https://github.com/mayconfmelo) for the [min-book](https://github.com/mayconfmelo/min-book) template and their help with customizing the template for this book.

## Licensing and Copyright

This book embraces the principles of open science and open education. To support transparency, learning, and reuse, the **code examples** in this book are released under a [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license. This means you are free to copy, modify, and distribute the code, even for commercial purposes, as long as appropriate credit is given.

Please attribute code usage by citing the book or linking to the GitHub repository:

> Wu, Q. (2025). _Introduction to GIS Programming: A Practical Python Guide to Open Source Geospatial Tools_. [https://gispro.gishub.org](https://gispro.gishub.org)

While the code is freely available, the **text, figures, and images** in this book are **copyrighted** by the author and may not be reproduced, redistributed, or modified without explicit permission. This includes all written content, custom diagrams, and embedded visualizations unless otherwise noted.

If you wish to reuse or adapt any non-code material from the book—for example, for teaching, presentations, or publications—please contact the author to request permission.

This dual licensing approach helps balance open access to learning materials with the protection of original creative work. Thank you for respecting these terms and supporting the open-source geospatial community.
