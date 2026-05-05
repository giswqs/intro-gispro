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

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/intro-gispro/blob/main/book/software/docker.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/intro-gispro/main?urlpath=lab/tree/book/software/docker.ipynb)

# Using Docker

## Introduction

### Why Use Docker for Geospatial Programming?

## Learning Objectives

## Installing Docker Desktop

### Windows and macOS

### Linux

### Verifying Installation

```bash
docker --version
```

## Basic Concepts

### Images vs. Containers

### Key Docker Terms

## Running Code Examples in Docker

```bash
docker pull giswqs/pygis:book
```

```bash
docker run -it -p 8888:8888 -v $(pwd):/app/workspace giswqs/pygis:book
```

### Working with Files

### Stopping a Container

### Listing Running Containers

```bash
docker ps
```

## Common Docker Commands

### Basic Operations

```bash
# Pull an image from Docker Hub
docker pull giswqs/pygis:book

# List downloaded images
docker images

# List running containers
docker ps

# List all containers (including stopped ones)
docker ps -a

# Stop a container
docker stop container_name

# Remove a container
docker rm container_name

# Remove an image
docker rmi image_name
```

### Getting Help

```bash
# Get help for any Docker command
docker help
docker run --help
```

### Choosing Port Numbers

```bash
# Use port 8889 instead
docker run -it -p 8889:8888 -v $(pwd):/app/workspace giswqs/pygis:book
```

### Saving Your Work

## Key Takeaways

## Exercises

### Exercise 1: First Docker Run

```bash
docker run -it -p 8888:8888 -v $(pwd):/home/jovyan/work ghcr.io/opengeos/leafmap:latest
```

### Exercise 2: Exploring the Environment

```{code-cell} python
import geopandas as gpd
import rasterio
import leafmap
print("All libraries imported successfully!")
```

```{code-cell} python
import leafmap.maplibregl as leafmap
m = leafmap.Map(projection="globe")
m
```

### Exercise 3: Working with Different Ports

### Exercise 4: Docker Commands Practice
