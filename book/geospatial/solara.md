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
# Building Interactive Dashboards with Voilà and Solara

## Introduction

## Learning Objectives

## Installing Voilà and Solara

```{code-cell} ipython3
# %pip install voila solara pygis
```

```{code-cell} ipython3
import voila
import solara
```

## Introduction to Hugging Face Spaces

### Installing the Hugging Face CLI

```{code-cell} ipython3
# %pip install -U "huggingface_hub[cli]"
```

### Logging in to Hugging Face

```bash
huggingface-cli login
```

## Creating a Basic Voilà Application

### Creating a new Hugging Face Space

### Embedding the Hugging Face Space in Your Website

### Running the Voilà Application

```{code-cell} ipython3
import leafmap.maplibregl as leafmap

m = leafmap.Map(
    style="liberty", projection="globe", sidebar_visible=True, height="750px"
)
m.add_basemap("USGS.Imagery")
cities = (
    "https://github.com/opengeos/datasets/releases/download/world/world_cities.geojson"
)
m.add_geojson(cities, name="Cities")
m
```

### Exploring the File Structure of the Space

### Updating the Hugging Face Space

#### Updating the Space from the Hugging Face Website

#### Updating the Space from the Command Line

```bash
git clone https://huggingface.co/spaces/YOUR-USERNAME/leafmap-voila
cd leafmap-voila
```

```bash
voila notebooks/
```

```bash
voila notebooks/ --strip_sources=False
```

## Creating an Advanced Web Application with Solara

### Understanding Solara

### Using a Leafmap Template for Solara

### Exploring the File Structure of the Solara Web App

### Introduction to Solara Components

```{code-cell} ipython3
import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="liberty",
        projection="globe",
        height="750px",
        zoom=2.5,
        sidebar_visible=True,
    )
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()


Page()
```

### Creating a New Page

```{code-cell} ipython3
import solara
import leafmap.maplibregl as leafmap


def create_map():

    m = leafmap.Map(
        style="positron",
        projection="globe",
        height="750px",
        zoom=2.5,
        sidebar_visible=True,
    )
    geojson = "https://github.com/opengeos/datasets/releases/download/world/mgrs_grid_zone.geojson"
    m.add_geojson(geojson)
    m.add_labels(geojson, "GZD", text_color="white", min_zoom=2, max_zoom=10)
    return m


@solara.component
def Page():
    m = create_map()
    return m.to_solara()
```

### Running the Solara Web App Locally

```bash
cd solara-maplibre
solara run pages/
```

### Pushing Changes to the Hugging Face Space

```bash
git add .
git commit -m "Update the web app"
git push
```

## Key Takeaways

## Exercises

### Exercise 1: Create a Simple Voilà Dashboard

### Exercise 2: Build a Multi-Page Solara Application
