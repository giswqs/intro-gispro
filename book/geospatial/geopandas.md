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

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/intro-gispro/blob/main/book/geospatial/geopandas.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/intro-gispro/main?urlpath=lab/tree/book/geospatial/geopandas.ipynb)

# Vector Data Analysis with GeoPandas

## Introduction

## Learning Objectives

## Core Concepts

### GeoDataFrame and GeoSeries

### Active Geometry Concept

## Installing GeoPandas

```{code-cell} python
# %pip install geopandas pygis
```

```{code-cell} python
import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
```

## Creating GeoDataFrames

### Creating Points from Coordinate Data

```{code-cell} python
# Creating a GeoDataFrame from coordinate data
data = {
    "City": ["Tokyo", "New York", "London", "Paris"],
    "Latitude": [35.6895, 40.7128, 51.5074, 48.8566],
    "Longitude": [139.6917, -74.0060, -0.1278, 2.3522],
}

# First create a regular pandas DataFrame
df = pd.DataFrame(data)

# Convert to GeoDataFrame by creating Point geometries from coordinates
gdf = gpd.GeoDataFrame(df, geometry=gpd.points_from_xy(df.Longitude, df.Latitude))
gdf
```

## Reading and Writing Geospatial Data

### Understanding Geospatial File Formats

### Reading a GeoJSON File

```{code-cell} python
url = "https://github.com/opengeos/datasets/releases/download/vector/nybb.geojson"
gdf = gpd.read_file(url)
gdf.head()
```

### Writing Geospatial Data

```{code-cell} python
output_file = "nyc_boroughs.geojson"
gdf.to_file(output_file, driver="GeoJSON")
print(f"GeoDataFrame has been written to {output_file}")
```

```{code-cell} python
# Save as Shapefile (traditional GIS format)
output_file = "nyc_boroughs.shp"
gdf.to_file(output_file)

# Save as GeoPackage (modern, single-file format)
output_file = "nyc_boroughs.gpkg"
gdf.to_file(output_file, driver="GPKG")
```

## Projections and Coordinate Reference Systems (CRS)

### Understanding Coordinate Systems

### Checking and Understanding CRS

```{code-cell} python
print(f"Current CRS: {gdf.crs}")
```

### Reprojecting to Different Coordinate Systems

```{code-cell} python
# Reproject to WGS84 (latitude/longitude) for global compatibility
gdf_4326 = gdf.to_crs(epsg=4326)
print(f"Reprojected CRS: {gdf_4326.crs}")
gdf_4326.head()
```

## Spatial Measurements and Analysis

### Preparing Data for Accurate Measurements

```{code-cell} python
gdf = gdf.to_crs("EPSG:2263")

# Set BoroName as index for easier data access
gdf = gdf.set_index("BoroName")
print(f"Now using CRS: {gdf.crs}")
```

### Calculating Areas

```{code-cell} python
# Calculate area in square feet (EPSG:2263 uses US survey feet)
gdf["area_sqft"] = gdf.area

# Convert to square kilometers (1 foot = 0.3048 meters)
gdf["area_km2"] = gdf["area_sqft"] * (0.3048**2) / 1_000_000

# Display results sorted by area
gdf[["area_sqft", "area_km2"]].sort_values("area_km2", ascending=False)
```

### Extracting Geometric Features

```{code-cell} python
# Extract boundary lines from polygons
gdf["boundary"] = gdf.boundary

# Calculate centroids (geometric centers)
gdf["centroid"] = gdf.centroid

# Display the geometric features
gdf[["boundary", "centroid"]].head()
```

### Distance Calculations

```{code-cell} python
# Use Manhattan's centroid as the reference point
manhattan_centroid = gdf.loc["Manhattan", "centroid"]

# Calculate distance from each borough centroid to Manhattan
gdf["distance_to_manhattan"] = gdf["centroid"].distance(manhattan_centroid)

# Convert to kilometers and display results
gdf["distance_to_manhattan_km"] = gdf["distance_to_manhattan"] / 1000

gdf[["distance_to_manhattan_km"]].sort_values("distance_to_manhattan_km")
```

### Statistical Analysis of Spatial Data

```{code-cell} python
# Calculate summary statistics
mean_distance = gdf["distance_to_manhattan_km"].mean()
max_distance = gdf["distance_to_manhattan_km"].max()
total_area = gdf["area_km2"].sum()

print(f"Mean distance to Manhattan: {mean_distance:.2f} km")
print(f"Maximum distance to Manhattan: {max_distance:.2f} km")
print(f"Total NYC area: {total_area:.2f} km²")
```

## Visualizing Geospatial Data

### Setting Up Plotting Environment

```{code-cell} python
import matplotlib.pyplot as plt

# Set high resolution for better quality plots
plt.rcParams["figure.dpi"] = 150
```

### Thematic Mapping

```{code-cell} python
# Create a choropleth map showing borough areas
fig, ax = plt.subplots(figsize=(10, 6))

gdf.plot(
    column="area_km2",
    ax=ax,
    legend=True,
    cmap="YlOrRd",  # Yellow-Orange-Red colormap
    edgecolor="black",
    linewidth=0.5,
)

plt.title("NYC Boroughs by Area (km²)", fontsize=16, fontweight="bold")
plt.axis("off")  # Remove coordinate axes for cleaner appearance
plt.tight_layout()
plt.show()
```

### Multi-Layer Visualization

```{code-cell} python
# Create a comprehensive map with multiple layers
fig, ax = plt.subplots(figsize=(10, 6))

# Plot borough boundaries as base layer
gdf["geometry"].plot(
    ax=ax, color="lightblue", edgecolor="navy", linewidth=1.5, alpha=0.7
)

# Add centroids as point layer
gdf["centroid"].plot(
    ax=ax, color="red", markersize=80, edgecolor="darkred", linewidth=1
)

# Add borough labels
for idx, row in gdf.iterrows():
    # Get centroid coordinates for label placement
    x = row.centroid.x
    y = row.centroid.y
    ax.annotate(
        idx,
        (x, y),
        xytext=(5, 5),
        textcoords="offset points",
        fontsize=10,
        fontweight="bold",
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", alpha=0.8),
    )

plt.title("NYC Borough Boundaries and Centroids", fontsize=16, fontweight="bold")
plt.axis("off")
plt.tight_layout()
plt.show()
```

### Interactive Visualization

```{code-cell} python
# Create an interactive map using Folium integration
m = gdf.explore(
    column="area_km2",
    cmap="YlOrRd",
    tooltip=["area_km2", "distance_to_manhattan_km"],
    popup=True,
    legend=True,
)
m
```

## Advanced Geometric Operations

### Buffer Analysis

```{code-cell} python
# Create 3-kilometer buffer zones around each borough
buffer_distance = 3000  # meters
gdf["buffered"] = gdf.buffer(buffer_distance)

print(f"Created {buffer_distance/1000} km buffer zones around each borough")
```

```{code-cell} python
# Visualize original vs buffered geometries
fig, ax = plt.subplots(figsize=(10, 6))

# Plot buffered areas first (background)
gdf["buffered"].plot(
    ax=ax,
    alpha=0.3,
    color="orange",
    edgecolor="red",
    linewidth=1,
    label="3km Buffer Zone",
)

# Plot original geometries on top
gdf["geometry"].plot(
    ax=ax,
    color="lightblue",
    edgecolor="navy",
    linewidth=1.5,
    label="Original Boundaries",
)

plt.title("NYC Boroughs: Original vs 3km Buffer Zones", fontsize=16, fontweight="bold")
plt.legend(loc="upper right")
plt.axis("off")
plt.tight_layout()
plt.show()
```

### Convex Hull Analysis

```{code-cell} python
# Calculate convex hulls for each borough
gdf["convex_hull"] = gdf.convex_hull

# Compare areas between original shapes and convex hulls
gdf["convex_hull_area"] = gdf["convex_hull"].area / 1_000_000  # Convert to km²
gdf["area_ratio"] = gdf["convex_hull_area"] / gdf["area_km2"]

print("Convex Hull Analysis:")
print(gdf[["area_km2", "convex_hull_area", "area_ratio"]].round(2))
```

```{code-cell} python
# Create comparison visualization
fig, ax = plt.subplots(figsize=(10, 6))

# Plot original geometries
gdf["geometry"].plot(
    ax=ax, color="lightblue", edgecolor="navy", linewidth=2, label="Original Shape"
)

# Plot convex hulls as outlines
gdf["convex_hull"].plot(
    ax=ax,
    facecolor="none",
    edgecolor="red",
    linewidth=2,
    linestyle="--",
    label="Convex Hull",
)

plt.title(
    "NYC Boroughs: Original Shapes vs Convex Hulls", fontsize=16, fontweight="bold"
)
plt.legend(loc="upper right")
plt.axis("off")
plt.tight_layout()
plt.show()
```

## Spatial Relationships and Queries

### Intersection Analysis

```{code-cell} python
# Test which buffered boroughs intersect with Manhattan's original boundary
manhattan_geom = gdf.loc["Manhattan", "geometry"]

gdf["intersects_manhattan"] = gdf["buffered"].intersects(manhattan_geom)
gdf["touches_manhattan"] = gdf["geometry"].touches(manhattan_geom)

# Display results
intersection_results = gdf[["intersects_manhattan", "touches_manhattan"]]
intersection_results
```

### Containment and Spatial Validation

```{code-cell} python
# Verify that centroids fall within their respective borough boundaries
gdf["centroid_within_borough"] = gdf["centroid"].within(gdf["geometry"])

# Check for any anomalies
anomalies = gdf[~gdf["centroid_within_borough"]]
if len(anomalies) > 0:
    print("Warning: Some centroids fall outside their borough boundaries")
    print(anomalies.index.tolist())
else:
    print("✓ All centroids correctly fall within their borough boundaries")
```

## Best Practices and Performance Considerations

### Coordinate System Management

### Memory and Performance

### Data Validation

## Key Takeaways

## Exercises

### Exercise 1: Creating and Manipulating GeoDataFrames with GeoPandas

```{code-cell} python

```

### Exercise 2: Combining NumPy, Pandas, and GeoPandas

```{code-cell} python

```
