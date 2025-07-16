# Introduction to GIS Programming

[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/intro-gispro/HEAD)
[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/intro-gispro/blob/main)
[![Docker Image](https://img.shields.io/badge/docker-giswqs%2Fpygis%3Abook-blue?logo=docker)](https://hub.docker.com/r/giswqs/pygis/tags)
[![Amazon](https://img.shields.io/badge/Buy%20on-Amazon-orange?logo=amazon&logoColor=white)](https://amazon.com/dp/B0FFW34LL3)
[![YouTube](https://img.shields.io/badge/Watch-Video-red?logo=youtube&logoColor=white)](https://www.youtube.com/playlist?list=PLAxJ4-o7ZoPfb18kNe2luWX9xKg1233i9)

## Introduction

Welcome to the official repository for **_Introduction to GIS Programming: A Practical Python Guide to Open Source Geospatial Tools_**. This repository contains all the code examples featured in the book, designed to help you learn and apply Python for geospatial analysis using open-source tools.

## Get the Book

- 🇺🇸 **Full-Color Print Edition (556 pages):** Now available on Amazon ([link](https://amazon.com/dp/B0FFW34LL3))

- 🇺🇸 **English PDF Edition (553 pages):** Available on Leanpub ([link](https://leanpub.com/gispro))

- 🇨🇳 **Chinese PDF Edition (540 pages):** 中文电子版可在 Leanpub 购买 ([link](https://leanpub.com/gispro-zh))

- 🇯🇵 **Japanese PDF Edition (573 pages):** 日本語版が Leanpub で利用可能 ([link](https://leanpub.com/gispro-ja))

- 🇰🇷 **Korean PDF Edition (555 pages):** 한국어판 Leanpub에서 이용 가능 ([link](https://leanpub.com/gispro-ko))

- 🇲🇽 **Spanish PDF Edition (572 pages):** Edición en español disponible en Leanpub ([link](https://leanpub.com/gispro-es))

- 🇫🇷 **French PDF Edition (581 pages):** Édition française disponible sur Leanpub ([link](https://leanpub.com/gispro-fr))

- 🇵🇹 **Portuguese PDF Edition (569 pages):** Edição em português disponível na Leanpub ([link](https://leanpub.com/gispro-pt))

- 🇮🇩 **Indonesian PDF Edition (565 pages):** Edisi bahasa Indonesia tersedia di Leanpub ([link](https://leanpub.com/gispro-id))

- 🇩🇪 **German PDF Edition (582 pages):** Deutschsprachige Edition auf Leanpub verfügbar ([link](https://leanpub.com/gispro-de))

- 🇷🇺 **Russian PDF Edition (599 pages):** Российская версия на Leanpub доступна ([link](https://leanpub.com/gispro-ru))

## Cite the Book

If you use this book in your research or teaching, please consider citing it as follows:

> Wu, Q. (2025). _Introduction to GIS Programming: A Practical Python Guide to Open Source Geospatial Tools_. Independently published. ISBN 979-8286979455. <https://amazon.com/dp/B0FFW34LL3>

![book cover](https://assets.gishub.org/images/gispro-book-cover.png)

## Table of Contents

To download a PDF version of the Table of Contents, please visit <https://gispro.gishub.org/book-toc.pdf>.

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

The code examples are organized into folders, each corresponding to a chapter in the book. The code examples are written in Python and can be run using MyBinder, Google Colab, or Docker. Follow this [video tutorial](https://www.youtube.com/embed/6GwMoV4LOiU) to learn how to run the code examples.

### Using MyBinder

The code examples can be run using MyBinder.

[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/intro-gispro/HEAD)

### Using Google Colab

The code examples can be run using Google Colab.

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/intro-gispro/blob/main)

### Using Docker

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

Dr. Qiusheng Wu is an Associate Professor and the Director of Graduate Studies in the Department of Geography & Sustainability at the University of Tennessee, Knoxville. He also serves as an Amazon Scholar. Dr. Wu's research focuses on geospatial data science and open-source software development, with an emphasis on leveraging big geospatial data and cloud computing to study environmental change, particularly surface water and wetland inundation dynamics. He is the creator of several widely used open-source Python packages, including [geemap](https://geemap.org), [leafmap](https://leafmap.org), [segment-geospatial](https://samgeo.gishub.org), and [geoai](https://opengeoai.org), which support advanced geospatial analysis and interactive visualization. His open-source work is available at the [Open Geospatial Solutions](https://github.com/opengeos) on GitHub.

## Acknowledgments

This book was written using [MyST Markdown](https://mystmd.org) and compiled using [Typst](https://github.com/typst/typst) with the [min-book](https://github.com/mayconfmelo/min-book) template. Credits to developers and maintainers of the Typst and MyST Markdown projects. Special thanks to [@mayconfmelo](https://github.com/mayconfmelo) for the [min-book](https://github.com/mayconfmelo/min-book) template and their help with customizing the template for this book.

## Licensing and Copyright

This book embraces the principles of open science and open education. To support transparency, learning, and reuse, the **code examples** in this book are released under a [Creative Commons Attribution 4.0 International (CC BY 4.0)](https://creativecommons.org/licenses/by/4.0/) license. This means you are free to copy, modify, and distribute the code, even for commercial purposes, as long as appropriate credit is given.

Please attribute code usage by citing the book or linking to the GitHub repository:

> Wu, Q. (2025). _Introduction to GIS Programming: A Practical Python Guide to Open Source Geospatial Tools_. Independently published. ISBN 979-8286979455. <https://amazon.com/dp/B0FFW34LL3>

While the code is freely available, the **text, figures, and images** in this book are **copyrighted** by the author and may not be reproduced, redistributed, or modified without explicit permission. This includes all written content, custom diagrams, and embedded visualizations unless otherwise noted.

If you wish to reuse or adapt any non-code material from the book—for example, for teaching, presentations, or publications—please contact the author to request permission.

This dual licensing approach helps balance open access to learning materials with the protection of original creative work. Thank you for respecting these terms and supporting the open-source geospatial community.
