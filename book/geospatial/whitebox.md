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
# Geoprocessing with WhiteboxTools

## Introduction

## Learning Objectives

## Why Whitebox?

### What is Whitebox?

### What can Whitebox do?

### How is Whitebox different?

## Useful Resources for Whitebox

## Installing Whitebox

```{code-cell} ipython3
# %pip install whitebox "pygis[lidar]"
```

```{code-cell} ipython3
import os
import leafmap
import numpy as np
```

```{code-cell} ipython3
os.environ["NODATA"] = "-32768"
```

## Watershed Analysis

### Create Interactive Maps

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("OpenTopoMap")
m.add_basemap("USGS 3DEP Elevation")
m.add_basemap("USGS Hydrography")
m
```

### Download Watershed Data

```{code-cell} ipython3
lat = 44.361169
lon = -122.821802

m = leafmap.Map(center=[lat, lon], zoom=10)
m.add_marker([lat, lon])
m
```

```{code-cell} ipython3
geometry = {"x": lon, "y": lat}
gdf = leafmap.get_wbd(geometry, digit=10, return_geometry=True)
gdf.explore()
```

```{code-cell} ipython3
gdf.to_file("basin.geojson")
```

### Download and Display DEM

```{code-cell} ipython3
array = leafmap.get_3dep_dem(
    gdf,
    resolution=30,
    output="dem.tif",
    dst_crs="EPSG:3857",
    to_cog=True,
    overwrite=True,
)
array
```

```{code-cell} ipython3
m.add_raster("dem.tif", palette="terrain", nodata=np.nan, layer_name="DEM")
m
```

### Get DEM metadata

```{code-cell} ipython3
metadata = leafmap.image_metadata("dem.tif")
metadata
```

### Add colorbar

```{code-cell} ipython3
leafmap.image_min_max("dem.tif")
```

```{code-cell} ipython3
m.add_colormap(cmap="terrain", vmin="60", vmax=1500, label="Elevation (m)")
m
```

### Initialize WhiteboxTools

```{code-cell} ipython3
wbt = leafmap.WhiteboxTools()
```

```{code-cell} ipython3
wbt.version()
```

```{code-cell} ipython3
leafmap.whiteboxgui()
```

### Initialize WhiteboxTools

### Set working directory

```{code-cell} ipython3
wbt.set_working_dir(os.getcwd())
wbt.verbose = False
```

### Smooth DEM

```{code-cell} ipython3
wbt.feature_preserving_smoothing("dem.tif", "smoothed.tif", filter=9)
```

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("Satellite")
m.add_raster("smoothed.tif", colormap="terrain", layer_name="Smoothed DEM")
m.add_geojson("basin.geojson", layer_name="Watershed", info_mode=None)
m.add_basemap("USGS Hydrography", show=False)
m
```

### Create hillshade

```{code-cell} ipython3
wbt.hillshade("smoothed.tif", "hillshade.tif", azimuth=315, altitude=35)
```

```{code-cell} ipython3
m.add_raster("hillshade.tif", layer_name="Hillshade")
m.layers[-1].opacity = 0.6
```

### Find no-flow cells

```{code-cell} ipython3
wbt.find_no_flow_cells("smoothed.tif", "noflow.tif")
```

```{code-cell} ipython3
m.add_raster("noflow.tif", layer_name="No Flow Cells")
```

### Fill depressions

```{code-cell} ipython3
wbt.fill_depressions("smoothed.tif", "filled.tif")
```

```{code-cell} ipython3
wbt.breach_depressions("smoothed.tif", "breached.tif")
```

```{code-cell} ipython3
wbt.find_no_flow_cells("breached.tif", "noflow2.tif")
```

```{code-cell} ipython3
m.layers[-1].visible = False
m.add_raster("noflow2.tif", layer_name="No Flow Cells after Breaching")
m
```

### Delineate flow direction

```{code-cell} ipython3
wbt.d8_pointer("breached.tif", "flow_direction.tif")
```

### Calculate flow accumulation

```{code-cell} ipython3
wbt.d8_flow_accumulation("breached.tif", "flow_accum.tif")
```

```{code-cell} ipython3
m.add_raster("flow_accum.tif", layer_name="Flow Accumulation")
```

### Extract streams

```{code-cell} ipython3
wbt.extract_streams("flow_accum.tif", "streams.tif", threshold=5000)
```

```{code-cell} ipython3
m.layers[-1].visible = False
m.add_raster("streams.tif", layer_name="Streams")
m
```

### Calculate distance to outlet

```{code-cell} ipython3
wbt.distance_to_outlet(
    "flow_direction.tif", streams="streams.tif", output="distance_to_outlet.tif"
)
```

```{code-cell} ipython3
m.add_raster("distance_to_outlet.tif", layer_name="Distance to Outlet")
```

### Vectorize streams

```{code-cell} ipython3
wbt.raster_streams_to_vector(
    "streams.tif", d8_pntr="flow_direction.tif", output="streams.shp"
)
```

```{code-cell} ipython3
leafmap.vector_set_crs(source="streams.shp", output="streams.shp", crs="EPSG:3857")
```

```{code-cell} ipython3
m.add_shp(
    "streams.shp",
    layer_name="Streams Vector",
    style={"color": "#ff0000", "weight": 3},
    info_mode=None,
)
m
```

### Delineate the longest flow path

```{code-cell} ipython3
wbt.basins("flow_direction.tif", "basins.tif")
```

```{code-cell} ipython3
wbt.longest_flowpath(
    dem="breached.tif", basins="basins.tif", output="longest_flowpath.shp"
)
```

```{code-cell} ipython3
leafmap.select_largest(
    "longest_flowpath.shp", column="LENGTH", output="longest_flowpath.shp"
)
```

```{code-cell} ipython3
m.add_shp(
    "longest_flowpath.shp",
    layer_name="Longest Flowpath",
    style={"color": "#ff0000", "weight": 3},
)
m
```

### Generate a pour point

```{code-cell} ipython3
if m.user_roi is not None:
    m.save_draw_features("pour_point.shp", crs="EPSG:3857")
else:
    lat = 44.284642
    lon = -122.611217
    leafmap.coords_to_vector([lon, lat], output="pour_point.shp", crs="EPSG:3857")
    m.add_marker([lat, lon])
```

### Snap pour point to stream

```{code-cell} ipython3
wbt.snap_pour_points(
    "pour_point.shp", "flow_accum.tif", "pour_point_snapped.shp", snap_dist=300
)
```

```{code-cell} ipython3
m.add_shp("pour_point_snapped.shp", layer_name="Pour Point", info_mode=False)
```

### Delineate watershed

```{code-cell} ipython3
wbt.watershed("flow_direction.tif", "pour_point_snapped.shp", "watershed.tif")
```

```{code-cell} ipython3
m.add_raster("watershed.tif", layer_name="Watershed")
m
```

### Convert watershed raster to vector

```{code-cell} ipython3
wbt.raster_to_vector_polygons("watershed.tif", "watershed.shp")
```

```{code-cell} ipython3
m.layers[-1].visible = False
m.add_shp(
    "watershed.shp",
    layer_name="Watershed Vector",
    style={"color": "#ffff00", "weight": 3},
    info_mode=False,
)
```

## LiDAR Data Analysis

### Set up whitebox

```{code-cell} ipython3
wbt = leafmap.WhiteboxTools()
wbt.set_working_dir(os.getcwd())
wbt.verbose = False
```

### Download a sample dataset

```{code-cell} ipython3
url = "https://github.com/opengeos/datasets/releases/download/lidar/madison.zip"
filename = "madison.las"
leafmap.download_file(url, "madison.zip", quiet=True)
```

### Read LAS/LAZ data

```{code-cell} ipython3
laz = leafmap.read_lidar(filename)
laz
```

```{code-cell} ipython3
str(laz.header.version)
```

### Upgrade file version

```{code-cell} ipython3
las = leafmap.convert_lidar(laz, file_version="1.4")
str(las.header.version)
```

### Write LAS data

```{code-cell} ipython3
leafmap.write_lidar(las, "madison.las")
```

### Histogram analysis

```{code-cell} ipython3
wbt.lidar_histogram("madison.las", "histogram.html")
```

### Visualize LiDAR data

```{code-cell} ipython3
leafmap.view_lidar("madison.las")
```

### Remove outliers

```{code-cell} ipython3
wbt.lidar_elevation_slice("madison.las", "madison_rm.las", minz=0, maxz=450)
```

### Visualize LiDAR data after removing outliers

```{code-cell} ipython3
leafmap.view_lidar("madison_rm.las", cmap="terrain")
```

### Create DSM

```{code-cell} ipython3
wbt.lidar_digital_surface_model(
    "madison_rm.las", "dsm.tif", resolution=1.0, minz=0, maxz=450
)
```

```{code-cell} ipython3
leafmap.add_crs("dsm.tif", epsg=2255)
```

### Visualize DSM

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("Satellite")
m.add_raster("dsm.tif", colormap="terrain", layer_name="DSM")
m
```

### Create DEM

```{code-cell} ipython3
wbt.remove_off_terrain_objects("dsm.tif", "dem.tif", filter=25, slope=15.0)
```

### Visualize DEM

```{code-cell} ipython3
m.add_raster("dem.tif", palette="terrain", layer_name="DEM")
m
```

### Create CHM

```{code-cell} ipython3
chm = wbt.subtract("dsm.tif", "dem.tif", "chm.tif")
```

```{code-cell} ipython3
m.add_raster("chm.tif", palette="gist_earth", layer_name="CHM")
m.add_layer_manager()
m
```

## Key Takeaways

## Exercises

### Exercise 1: Watershed Analysis for a Different Location

### Exercise 2: LiDAR Analysis for Forest Structure Assessment
