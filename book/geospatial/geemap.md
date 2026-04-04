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
# Cloud Computing with Earth Engine and Geemap

## Introduction

## Learning Objectives

## Introduction to Google Earth Engine

### Google Earth Engine Overview

### Account Registration

### Installing Geemap

```{code-cell} ipython3
# %pip install -U geemap pygis
```

### Import Libraries

```{code-cell} ipython3
import ee
import geemap
```

### Authenticate and Initialize Earth Engine

```{code-cell} ipython3
ee.Authenticate()
```

```{code-cell} ipython3
ee.Initialize(project="your-ee-project")
```

### Creating Interactive Maps

```{code-cell} ipython3
m = geemap.Map()
```

```{code-cell} ipython3
m
```

```{code-cell} ipython3
m = geemap.Map(center=[40, -100], zoom=4, height="600px")
m
```

```{code-cell} ipython3
m = geemap.Map(data_ctrl=False, toolbar_ctrl=False, draw_ctrl=False)
m
```

### Adding Basemaps

```{code-cell} ipython3
m = geemap.Map(basemap="Esri.WorldImagery")
m
```

#### Adding Multiple Basemaps

```{code-cell} ipython3
m.add_basemap("Esri.WorldTopoMap")
```

```{code-cell} ipython3
m.add_basemap("OpenTopoMap")
```

### Google Basemaps

```{code-cell} ipython3
m = geemap.Map()
url = "https://mt1.google.com/vt/lyrs=y&x={x}&y={y}&z={z}"
m.add_tile_layer(url, name="Google Satellite", attribution="Google")
m
```

```{code-cell} ipython3
m.add_text(text="Hello from Earth Engine", position="bottomright")
```

## Introduction to Interactive Maps and Tools

### Basemap Selector

```{code-cell} ipython3
m = geemap.Map()
m.add("basemap_selector")
m
```

### Layer Manager

```{code-cell} ipython3
m = geemap.Map(center=(40, -100), zoom=4)
dem = ee.Image("USGS/SRTMGL1_003")
states = ee.FeatureCollection("TIGER/2018/States")
vis_params = {
    "min": 0,
    "max": 4000,
    "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
}
m.add_layer(dem, vis_params, "SRTM DEM")
m.add_layer(states, {}, "US States")
m.add("layer_manager")
m
```

### Inspector Tool

```{code-cell} ipython3
m = geemap.Map(center=(40, -100), zoom=4)
dem = ee.Image("USGS/SRTMGL1_003")
landsat7 = ee.Image("LANDSAT/LE7_TOA_5YEAR/1999_2003")
states = ee.FeatureCollection("TIGER/2018/States")
vis_params = {
    "min": 0,
    "max": 4000,
    "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
}
m.add_layer(dem, vis_params, "SRTM DEM")
m.add_layer(
    landsat7,
    {"bands": ["B4", "B3", "B2"], "min": 20, "max": 200, "gamma": 2.0},
    "Landsat 7",
)
m.add_layer(states, {}, "US States")
m.add("inspector")
m
```

### Layer Editor

#### Single-Band image

```{code-cell} ipython3
m = geemap.Map(center=(40, -100), zoom=4)
dem = ee.Image("USGS/SRTMGL1_003")
vis_params = {
    "min": 0,
    "max": 4000,
    "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
}
m.add_layer(dem, vis_params, "SRTM DEM")
m.add("layer_editor", layer_dict=m.ee_layers["SRTM DEM"])
m
```

#### Multi-Band image

```{code-cell} ipython3
m = geemap.Map(center=(40, -100), zoom=4)
landsat7 = ee.Image("LANDSAT/LE7_TOA_5YEAR/1999_2003")
m.add_layer(
    landsat7,
    {"bands": ["B4", "B3", "B2"], "min": 20, "max": 200, "gamma": 2.0},
    "Landsat 7",
)
m.add("layer_editor", layer_dict=m.ee_layers["Landsat 7"])
m
```

#### Feature Collection

```{code-cell} ipython3
m = geemap.Map(center=(40, -100), zoom=4)
states = ee.FeatureCollection("TIGER/2018/States")
m.add_layer(states, {}, "US States")
m.add("layer_editor", layer_dict=m.ee_layers["US States"])
m
```

### Draw Control

```{code-cell} ipython3
m = geemap.Map(center=(40, -100), zoom=4)
dem = ee.Image("USGS/SRTMGL1_003")
vis_params = {
    "min": 0,
    "max": 4000,
    "palette": "terrain",
}
m.add_layer(dem, vis_params, "SRTM DEM")
m.add("layer_manager")
m
```

```{code-cell} ipython3
if m.user_roi is not None:
    image = dem.clip(m.user_roi)
    m.layers[1].visible = False
    m.add_layer(image, vis_params, "Clipped DEM")
```

## The Earth Engine Data Catalog

### Searching Datasets on the Earth Engine Website

### Searching Datasets Within Geemap

```{code-cell} ipython3
m = geemap.Map()
m
```

### Using the Datasets Module in Geemap

```{code-cell} ipython3
from geemap.datasets import DATA
```

```{code-cell} ipython3
m = geemap.Map()
dataset = ee.Image(DATA.USGS_GAP_AK_2001)
m.add_layer(dataset, {}, "GAP Alaska")
m.centerObject(dataset, zoom=4)
m
```

```{code-cell} ipython3
from geemap.datasets import get_metadata

get_metadata(DATA.USGS_GAP_AK_2001)
```

## Earth Engine Data Types

## Earth Engine Raster Data

### Image

#### Loading Earth Engine Images

```{code-cell} ipython3
image = ee.Image("USGS/SRTMGL1_003")
image
```

#### Visualizing Earth Engine Images

```{code-cell} ipython3
m = geemap.Map(center=[21.79, 70.87], zoom=3)
image = ee.Image("USGS/SRTMGL1_003")
vis_params = {
    "min": 0,
    "max": 6000,
    "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],  # 'terrain'
}
m.add_layer(image, vis_params, "SRTM")
m
```

### ImageCollection

#### Loading Image Collections

```{code-cell} ipython3
collection = ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
```

#### Filtering Image Collections

```{code-cell} ipython3
geometry = ee.Geometry.Point([-83.909463, 35.959111])
images = collection.filterBounds(geometry)
images.size()
```

```{code-cell} ipython3
images.first()
```

```{code-cell} ipython3
images = (
    collection.filterBounds(geometry)
    .filterDate("2024-07-01", "2024-10-01")
    .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 5))
)
images.size()
```

```{code-cell} ipython3
m = geemap.Map()
image = images.first()

vis = {
    "min": 0.0,
    "max": 3000,
    "bands": ["B4", "B3", "B2"],
}

m.add_layer(image, vis, "Sentinel-2")
m.centerObject(image, 8)
m
```

#### Visualizing Image Collections

```{code-cell} ipython3
m = geemap.Map()
image = images.median()

vis = {
    "min": 0.0,
    "max": 3000,
    "bands": ["B8", "B4", "B3"],
}

m.add_layer(image, vis, "Sentinel-2")
m.centerObject(geometry, 8)
m
```

## Earth Engine Vector Data

### Loading Feature Collections

```{code-cell} ipython3
m = geemap.Map()
fc = ee.FeatureCollection("TIGER/2016/Roads")
m.set_center(-83.909463, 35.959111, 12)
m.add_layer(fc, {}, "Census roads")
m
```

### Filtering Feature Collections

```{code-cell} ipython3
m = geemap.Map()
states = ee.FeatureCollection("TIGER/2018/States")
fc = states.filter(ee.Filter.eq("NAME", "Tennessee"))
m.add_layer(fc, {}, "Tennessee")
m.center_object(fc, 7)
m
```

```{code-cell} ipython3
feat = fc.first()
feat.toDictionary()
```

```{code-cell} ipython3
geemap.ee_to_df(fc)
```

```{code-cell} ipython3
m = geemap.Map()
states = ee.FeatureCollection("TIGER/2018/States")
fc = states.filter(ee.Filter.inList("NAME", ["California", "Oregon", "Washington"]))
m.add_layer(fc, {}, "West Coast")
m.center_object(fc, 5)
m
```

```{code-cell} ipython3
region = m.user_roi
if region is None:
    region = ee.Geometry.BBox(-88.40, 29.88, -77.90, 35.39)

fc = ee.FeatureCollection("TIGER/2018/States").filterBounds(region)
m.add_layer(fc, {}, "Southeastern U.S.")
m.center_object(fc, 6)
```

```{code-cell} ipython3
m = geemap.Map(center=(40, -100), zoom=4)
landsat7 = ee.Image("LANDSAT/LE7_TOA_5YEAR/1999_2003")
countries = ee.FeatureCollection("FAO/GAUL_SIMPLIFIED_500m/2015/level0")
fc = countries.filter(ee.Filter.eq("ADM0_NAME", "Germany"))
image = landsat7.clipToCollection(fc)
m.add_layer(
    image,
    {"bands": ["B4", "B3", "B2"], "min": 20, "max": 200, "gamma": 2.0},
    "Landsat 7",
)
m.center_object(fc, 6)
m
```

### Visualizing Feature Collections

```{code-cell} ipython3
m = geemap.Map(center=[40, -100], zoom=4)
states = ee.FeatureCollection("TIGER/2018/States")
m.add_layer(states, {}, "US States")
m
```

```{code-cell} ipython3
m = geemap.Map(center=[40, -100], zoom=4)
states = ee.FeatureCollection("TIGER/2018/States")
style = {"color": "0000ffff", "width": 2, "lineType": "solid", "fillColor": "FF000080"}
m.add_layer(states.style(**style), {}, "US States")
m
```

```{code-cell} ipython3
m = geemap.Map(center=[40, -100], zoom=4)
states = ee.FeatureCollection("TIGER/2018/States")
vis_params = {
    "color": "000000",
    "colorOpacity": 1,
    "pointSize": 3,
    "pointShape": "circle",
    "width": 2,
    "lineType": "solid",
    "fillColorOpacity": 0.66,
}
palette = ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"]
m.add_styled_vector(
    states, column="NAME", palette=palette, layer_name="Styled vector", **vis_params
)
m
```

## More Tools for Visualizing Earth Engine Data

### Using the Plotting Tool

```{code-cell} ipython3
m = geemap.Map(center=[40, -100], zoom=4)

landsat7 = ee.Image("LANDSAT/LE7_TOA_5YEAR/1999_2003").select(
    ["B1", "B2", "B3", "B4", "B5", "B7"]
)

landsat_vis = {"bands": ["B4", "B3", "B2"], "gamma": 1.4}
m.add_layer(landsat7, landsat_vis, "Landsat")

hyperion = ee.ImageCollection("EO1/HYPERION").filter(
    ee.Filter.date("2016-01-01", "2017-03-01")
)

hyperion_vis = {
    "min": 1000.0,
    "max": 14000.0,
    "gamma": 2.5,
}
m.add_layer(hyperion, hyperion_vis, "Hyperion")
m.add_plot_gui()
m
```

```{code-cell} ipython3
m.set_plot_options(add_marker_cluster=True, overlay=True)
```

```{code-cell} ipython3
m.set_plot_options(add_marker_cluster=True, plot_type="bar")
```

### Legends

#### Built-in Legends

```{code-cell} ipython3
from geemap.legends import builtin_legends

for legend in builtin_legends:
    print(legend)
```

```{code-cell} ipython3
m = geemap.Map(center=[40, -100], zoom=4)
m.add_basemap("Esri.WorldImagery")
m.add_basemap("NLCD 2021 CONUS Land Cover")
m.add_legend(builtin_legend="NLCD", max_width="100px", height="455px")
m
```

```{code-cell} ipython3
m = geemap.Map(center=[40, -100], zoom=4)
m.add_basemap("Esri.WorldImagery")

nlcd = ee.Image("USGS/NLCD_RELEASES/2021_REL/NLCD/2021")
landcover = nlcd.select("landcover")

m.add_layer(landcover, {}, "NLCD Land Cover 2021")
m.add_legend(
    title="NLCD Land Cover Classification", builtin_legend="NLCD", height="455px"
)
m
```

#### Custom Legends

```{code-cell} ipython3
m = geemap.Map(center=[40, -100], zoom=4)
m.add_basemap("Esri.WorldImagery")

legend_dict = {
    "11 Open Water": "466b9f",
    "12 Perennial Ice/Snow": "d1def8",
    "21 Developed, Open Space": "dec5c5",
    "22 Developed, Low Intensity": "d99282",
    "23 Developed, Medium Intensity": "eb0000",
    "24 Developed High Intensity": "ab0000",
    "31 Barren Land (Rock/Sand/Clay)": "b3ac9f",
    "41 Deciduous Forest": "68ab5f",
    "42 Evergreen Forest": "1c5f2c",
    "43 Mixed Forest": "b5c58f",
    "51 Dwarf Scrub": "af963c",
    "52 Shrub/Scrub": "ccb879",
    "71 Grassland/Herbaceous": "dfdfc2",
    "72 Sedge/Herbaceous": "d1d182",
    "73 Lichens": "a3cc51",
    "74 Moss": "82ba9e",
    "81 Pasture/Hay": "dcd939",
    "82 Cultivated Crops": "ab6c28",
    "90 Woody Wetlands": "b8d9eb",
    "95 Emergent Herbaceous Wetlands": "6c9fb8",
}

nlcd = ee.Image("USGS/NLCD_RELEASES/2021_REL/NLCD/2021")
landcover = nlcd.select("landcover")

m.add_layer(landcover, {}, "NLCD Land Cover 2021")
m.add_legend(title="NLCD Land Cover Classification", legend_dict=legend_dict)
m
```

### Color Bars

```{code-cell} ipython3
m = geemap.Map()

dem = ee.Image("USGS/SRTMGL1_003")
vis_params = {
    "min": 0,
    "max": 4000,
    "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
}

m.add_layer(dem, vis_params, "SRTM DEM")
m.add_colorbar(vis_params, label="Elevation (m)", layer_name="SRTM DEM")
m
```

```{code-cell} ipython3
m.add_colorbar(
    vis_params,
    label="Elevation (m)",
    layer_name="SRTM DEM",
    orientation="vertical",
    max_width="100px",
)
```

### Split-panel Maps

```{code-cell} ipython3
m = geemap.Map()
m.split_map(left_layer="Esri.WorldTopoMap", right_layer="OpenTopoMap")
m
```

```{code-cell} ipython3
m = geemap.Map(center=(40, -100), zoom=4, height="600px")

nlcd_2001 = ee.Image("USGS/NLCD_RELEASES/2019_REL/NLCD/2001").select("landcover")
nlcd_2021 = ee.Image("USGS/NLCD_RELEASES/2021_REL/NLCD/2021").select("landcover")

left_layer = geemap.ee_tile_layer(nlcd_2001, {}, "NLCD 2001")
right_layer = geemap.ee_tile_layer(nlcd_2021, {}, "NLCD 2021")

m.split_map(left_layer, right_layer)
m
```

### Linked Maps

```{code-cell} ipython3
image = (
    ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
    .filterDate("2024-07-01", "2024-10-01")
    .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", 5))
    .map(lambda img: img.divide(10000))
    .median()
)

vis_params = [
    {"bands": ["B4", "B3", "B2"], "min": 0, "max": 0.3, "gamma": 1.3},
    {"bands": ["B8", "B11", "B4"], "min": 0, "max": 0.3, "gamma": 1.3},
    {"bands": ["B8", "B4", "B3"], "min": 0, "max": 0.3, "gamma": 1.3},
    {"bands": ["B12", "B12", "B4"], "min": 0, "max": 0.3, "gamma": 1.3},
]

labels = [
    "Natural Color (B4/B3/B2)",
    "Land/Water (B8/B11/B4)",
    "Color Infrared (B8/B4/B3)",
    "Vegetation (B12/B11/B4)",
]

geemap.linked_maps(
    rows=2,
    cols=2,
    height="300px",
    center=[35.959111, -83.909463],
    zoom=12,
    ee_objects=[image],
    vis_params=vis_params,
    labels=labels,
    label_position="topright",
)
```

### Timeseries Inspector

```{code-cell} ipython3
m = geemap.Map(center=[40, -100], zoom=4)
collection = ee.ImageCollection("USGS/NLCD_RELEASES/2019_REL/NLCD").select("landcover")
vis_params = {"bands": ["landcover"]}
years = collection.aggregate_array("system:index").getInfo()
years
```

```{code-cell} ipython3
m.ts_inspector(
    left_ts=collection,
    right_ts=collection,
    left_names=years,
    right_names=years,
    left_vis=vis_params,
    right_vis=vis_params,
    width="80px",
)
m
```

### Time Slider

```{code-cell} ipython3
m = geemap.Map()

collection = (
    ee.ImageCollection("MODIS/MCD43A4_006_NDVI")
    .filter(ee.Filter.date("2018-06-01", "2018-07-01"))
    .select("NDVI")
)
vis_params = {
    "min": 0.0,
    "max": 1.0,
    "palette": "ndvi",
}

m.add_time_slider(collection, vis_params, time_interval=2)
m
```

```{code-cell} ipython3
m = geemap.Map()

collection = (
    ee.ImageCollection("NOAA/GFS0P25")
    .filterDate("2018-12-22", "2018-12-23")
    .limit(24)
    .select("temperature_2m_above_ground")
)

vis_params = {
    "min": -40.0,
    "max": 35.0,
    "palette": ["blue", "purple", "cyan", "green", "yellow", "red"],
}

labels = [str(n).zfill(2) + ":00" for n in range(0, 24)]
m.add_time_slider(collection, vis_params, labels=labels, time_interval=1, opacity=0.8)
m
```

```{code-cell} ipython3
m = geemap.Map()

collection = (
    ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
    .filterBounds(ee.Geometry.Point([-83.909463, 35.959111]))
    .filterMetadata("CLOUDY_PIXEL_PERCENTAGE", "less_than", 10)
    .filter(ee.Filter.calendarRange(6, 8, "month"))
)

vis_params = {"min": 0, "max": 4000, "bands": ["B8", "B4", "B3"]}

m.add_time_slider(collection, vis_params)
m.set_center(-83.909463, 35.959111, 12)
m
```

## Vector Data Processing

### From GeoJSON

```{code-cell} ipython3
in_geojson = "https://github.com/gee-community/geemap/blob/master/examples/data/countries.geojson"
m = geemap.Map()
fc = geemap.geojson_to_ee(in_geojson)
m.add_layer(fc.style(**{"color": "ff0000", "fillColor": "00000000"}), {}, "Countries")
m
```

### From Shapefile

```{code-cell} ipython3
url = "https://github.com/gee-community/geemap/blob/master/examples/data/countries.zip"
geemap.download_file(url, overwrite=True)
```

```{code-cell} ipython3
in_shp = "countries.shp"
fc = geemap.shp_to_ee(in_shp)
m = geemap.Map()
m.add_layer(fc, {}, "Countries")
m
```

### From GeoDataFrame

```{code-cell} ipython3
import geopandas as gpd

gdf = gpd.read_file(in_shp)
fc = geemap.gdf_to_ee(gdf)
m = geemap.Map()
m.add_layer(fc, {}, "Countries")
m
```

### To GeoJSON

```{code-cell} ipython3
m = geemap.Map()
states = ee.FeatureCollection("TIGER/2018/States")
fc = states.filter(ee.Filter.eq("NAME", "Tennessee"))
m.add_layer(fc, {}, "Tennessee")
m.center_object(fc, 7)
m
```

```{code-cell} ipython3
geemap.ee_to_geojson(fc, filename="Tennessee.geojson")
```

### To Shapefile

```{code-cell} ipython3
geemap.ee_to_shp(fc, filename="Tennessee.shp")
```

### To GeoDataFrame

```{code-cell} ipython3
gdf = geemap.ee_to_gdf(fc)
gdf
```

```{code-cell} ipython3
gdf.explore()
```

### To DataFrame

```{code-cell} ipython3
df = geemap.ee_to_df(fc)
df
```

### To CSV

```{code-cell} ipython3
geemap.ee_to_csv(fc, filename="Indiana.csv")
```

## Raster Data Processing

### Extract Pixel Values

#### Extracting Values to Points

```{code-cell} ipython3
m = geemap.Map(center=[40, -100], zoom=4)

dem = ee.Image("USGS/SRTMGL1_003")
landsat7 = ee.Image("LANDSAT/LE7_TOA_5YEAR/1999_2003")

vis_params = {
    "min": 0,
    "max": 4000,
    "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
}

m.add_layer(
    landsat7,
    {"bands": ["B4", "B3", "B2"], "min": 20, "max": 200, "gamma": 2},
    "Landsat 7",
)
m.add_layer(dem, vis_params, "SRTM DEM", True, 1)
m
```

```{code-cell} ipython3
in_shp = "us_cities.shp"
url = "https://github.com/opengeos/data/raw/main/us/us_cities.zip"
geemap.download_file(url)
```

```{code-cell} ipython3
in_fc = geemap.shp_to_ee(in_shp)
m.add_layer(in_fc, {}, "Cities")
```

```{code-cell} ipython3
geemap.extract_values_to_points(in_fc, dem, out_fc="dem.shp", scale=90)
```

```{code-cell} ipython3
gdf = geemap.shp_to_gdf("dem.shp")
gdf.head()
```

```{code-cell} ipython3
geemap.extract_values_to_points(in_fc, landsat7, "landsat.csv", scale=90)
```

```{code-cell} ipython3
df = geemap.csv_to_df("landsat.csv")
df.head()
```

#### Extracting Pixel Values Along a Transect

```{code-cell} ipython3
m = geemap.Map(center=[40, -100], zoom=4)
m.add_basemap("TERRAIN")

image = ee.Image("USGS/SRTMGL1_003")
vis_params = {
    "min": 0,
    "max": 4000,
    "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
}
m.add_layer(image, vis_params, "SRTM DEM", True, 0.5)
m
```

```{code-cell} ipython3
line = m.user_roi
if line is None:
    line = ee.Geometry.LineString(
        [[-120.2232, 36.3148], [-118.9269, 36.7121], [-117.2022, 36.7562]]
    )
    m.add_layer(line, {}, "ROI")
m.centerObject(line)
```

```{code-cell} ipython3
reducer = "mean"
transect = geemap.extract_transect(
    image, line, n_segments=100, reducer=reducer, to_pandas=True
)
transect
```

```{code-cell} ipython3
geemap.line_chart(
    data=transect,
    x="distance",
    y="mean",
    markers=True,
    x_label="Distance (m)",
    y_label="Elevation (m)",
    height=400,
)
```

```{code-cell} ipython3
transect.to_csv("transect.csv")
```

### Zonal Statistics

#### Zonal Statistics with an Image and a Feature Collection

```{code-cell} ipython3
m = geemap.Map(center=[40, -100], zoom=4)

# Add NASA SRTM
dem = ee.Image("USGS/SRTMGL1_003")
dem_vis = {
    "min": 0,
    "max": 4000,
    "palette": ["006633", "E5FFCC", "662A00", "D8D8D8", "F5F5F5"],
}
m.add_layer(dem, dem_vis, "SRTM DEM")

# Add 5-year Landsat TOA composite
landsat = ee.Image("LANDSAT/LE7_TOA_5YEAR/1999_2003")
landsat_vis = {"bands": ["B4", "B3", "B2"], "gamma": 1.4}
m.add_layer(landsat, landsat_vis, "Landsat", False)

# Add US Census States
states = ee.FeatureCollection("TIGER/2018/States")
style = {"fillColor": "00000000"}
m.add_layer(states.style(**style), {}, "US States")
m
```

```{code-cell} ipython3
out_dem_stats = "dem_stats.csv"
geemap.zonal_stats(
    dem, states, out_dem_stats, statistics_type="MEAN", scale=1000, return_fc=False
)
```

```{code-cell} ipython3
out_landsat_stats = "landsat_stats.csv"
geemap.zonal_stats(
    landsat,
    states,
    out_landsat_stats,
    statistics_type="MEAN",
    scale=1000,
    return_fc=False,
)
```

#### Zonal Statistics by Group

```{code-cell} ipython3
m = geemap.Map(center=[40, -100], zoom=4)

# Add NLCD data
dataset = ee.Image("USGS/NLCD_RELEASES/2019_REL/NLCD/2019")
landcover = dataset.select("landcover")
m.add_layer(landcover, {}, "NLCD 2019")

# Add US census states
states = ee.FeatureCollection("TIGER/2018/States")
style = {"fillColor": "00000000"}
m.add_layer(states.style(**style), {}, "US States")

# Add NLCD legend
m.add_legend(title="NLCD Land Cover", builtin_legend="NLCD")
m
```

```{code-cell} ipython3
nlcd_stats = "nlcd_stats.csv"

geemap.zonal_stats_by_group(
    landcover,
    states,
    nlcd_stats,
    stat_type="SUM",
    denominator=1e6,
    decimal_places=2,
    scale=300
)
```

```{code-cell} ipython3
nlcd_stats = "nlcd_stats_pct.csv"

geemap.zonal_stats_by_group(
    landcover,
    states,
    nlcd_stats,
    stat_type="PERCENTAGE",
    denominator=1e6,
    decimal_places=2,
    scale=300
)
```

#### Zonal Statistics with Two Images

```{code-cell} ipython3
m = geemap.Map(center=[40, -100], zoom=4)
dem = ee.Image("USGS/3DEP/10m")
vis = {"min": 0, "max": 4000, "palette": "terrain"}
m.add_layer(dem, vis, "DEM")
landcover = ee.Image("USGS/NLCD_RELEASES/2019_REL/NLCD/2019").select("landcover")
m.add_layer(landcover, {}, "NLCD 2019")
m.add_legend(title="NLCD Land Cover Classification", builtin_legend="NLCD")
m
```

```{code-cell} ipython3
stats = geemap.image_stats_by_zone(dem, landcover, reducer="MEAN", scale=90)
stats
```

```{code-cell} ipython3
stats.to_csv("mean.csv", index=False)
```

```{code-cell} ipython3
geemap.image_stats_by_zone(dem, landcover, out_csv="std.csv", reducer="STD")
```

### Map Algebra

```{code-cell} ipython3
m = geemap.Map()

# Load a 5-year Landsat 7 composite 1999-2003.
landsat_1999 = ee.Image("LANDSAT/LE7_TOA_5YEAR/1999_2003")

# Compute NDVI.
ndvi_1999 = (
    landsat_1999.select("B4")
    .subtract(landsat_1999.select("B3"))
    .divide(landsat_1999.select("B4").add(landsat_1999.select("B3")))
)

vis = {"min": 0, "max": 1, "palette": "ndvi"}
m.add_layer(ndvi_1999, vis, "NDVI")
m.add_colorbar(vis, label="NDVI")
m
```

```{code-cell} ipython3
# Load a Landsat 8 image.
image = ee.Image("LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318")

# Compute the EVI using an expression.
evi = image.expression(
    "2.5 * ((NIR - RED) / (NIR + 6 * RED - 7.5 * BLUE + 1))",
    {
        "NIR": image.select("B5"),
        "RED": image.select("B4"),
        "BLUE": image.select("B2"),
    },
)

# Define a map centered on San Francisco Bay.
m = geemap.Map(center=[37.4675, -122.1363], zoom=9)

vis = {"min": 0, "max": 1, "palette": "ndvi"}
m.add_layer(evi, vis, "EVI")
m.add_colorbar(vis, label="EVI")
m
```

## Exporting Earth Engine Data

### Exporting Images

```{code-cell} ipython3
m = geemap.Map()

image = ee.Image("LANDSAT/LC08/C02/T1_TOA/LC08_044034_20140318").select(
    ["B5", "B4", "B3"]
)

vis_params = {"min": 0, "max": 0.5, "gamma": [0.95, 1.1, 1]}

m.center_object(image)
m.add_layer(image, vis_params, "Landsat")
m
```

```{code-cell} ipython3
region = ee.Geometry.BBox(-122.5955, 37.5339, -122.0982, 37.8252)
fc = ee.FeatureCollection(region)
style = {"color": "ffff00ff", "fillColor": "00000000"}
m.add_layer(fc.style(**style), {}, "ROI")
```

```{code-cell} ipython3
geemap.ee_export_image(image, filename="landsat.tif", scale=30, region=region)
```

```{code-cell} ipython3
projection = image.select(0).projection().getInfo()
projection
```

```{code-cell} ipython3
crs = projection["crs"]
crs_transform = projection["transform"]
```

```{code-cell} ipython3
geemap.ee_export_image(
    image,
    filename="landsat_crs.tif",
    crs=crs,
    crs_transform=crs_transform,
    region=region,
)
```

```{code-cell} ipython3
geemap.ee_export_image_to_drive(
    image, description="landsat", folder="export", region=region, scale=30
)
```

```{code-cell} ipython3
geemap.download_ee_image(image, "landsat.tif", scale=90)
```

### Exporting Image Collections

```{code-cell} ipython3
point = ee.Geometry.Point(-99.2222, 46.7816)
collection = (
    ee.ImageCollection("USDA/NAIP/DOQQ")
    .filterBounds(point)
    .filterDate("2008-01-01", "2018-01-01")
    .filter(ee.Filter.listContains("system:band_names", "N"))
)
collection.aggregate_array("system:index")
```

```{code-cell} ipython3
geemap.ee_export_image_collection(collection, out_dir=".", scale=10)
```

```{code-cell} ipython3
geemap.ee_export_image_collection_to_drive(collection, folder="export", scale=10)
```

### Exporting Feature Collections

```{code-cell} ipython3
m = geemap.Map()
states = ee.FeatureCollection("TIGER/2018/States")
fc = states.filter(ee.Filter.eq("NAME", "Alaska"))
m.add_layer(fc, {}, "Alaska")
m.center_object(fc, 4)
m
```

```{code-cell} ipython3
geemap.ee_to_shp(fc, filename="Alaska.shp")
geemap.ee_export_vector(fc, filename="Alaska.shp")
geemap.ee_to_geojson(fc, filename="Alaska.geojson")
geemap.ee_to_csv(fc, filename="Alaska.csv")
gdf = geemap.ee_to_gdf(fc)
df = geemap.ee_to_df(fc)
```

```{code-cell} ipython3
geemap.ee_export_vector_to_drive(
    fc, description="Alaska", fileFormat="SHP", folder="export"
)
```

## Creating Timelapse Animations

### Landsat Timelapse

```{code-cell} ipython3
m = geemap.Map()
roi = ee.Geometry.BBox(-115.5541, 35.8044, -113.9035, 36.5581)
m.add_layer(roi)
m.center_object(roi)
m
```

```{code-cell} ipython3
timelapse = geemap.landsat_timelapse(
    roi,
    out_gif="las_vegas.gif",
    start_year=1984,
    end_year=2025,
    bands=["NIR", "Red", "Green"],
    frames_per_second=5,
    title="Las Vegas, NV",
    font_color="blue",
)
geemap.show_image(timelapse)
```

```{code-cell} ipython3
m = geemap.Map()
roi = ee.Geometry.BBox(113.8252, 22.1988, 114.0851, 22.3497)
m.add_layer(roi)
m.center_object(roi)
m
```

```{code-cell} ipython3
timelapse = geemap.landsat_timelapse(
    roi,
    out_gif="hong_kong.gif",
    start_year=1990,
    end_year=2025,
    start_date="01-01",
    end_date="12-31",
    bands=["SWIR1", "NIR", "Red"],
    frames_per_second=3,
    title="Hong Kong",
)
geemap.show_image(timelapse)
```

### Sentinel-2 Timelapse

```{code-cell} ipython3
m = geemap.Map(center=[-8.4506, -74.5079], zoom=12)
m
```

```{code-cell} ipython3
roi = m.user_roi
if roi is None:
    roi = ee.Geometry.BBox(-74.7222, -8.5867, -74.1596, -8.2824)
    m.add_layer(roi)
    m.center_object(roi)
```

```{code-cell} ipython3
timelapse = geemap.sentinel2_timelapse(
    roi,
    out_gif="sentinel2.gif",
    start_year=2017,
    end_year=2025,
    start_date="05-01",
    end_date="09-31",
    frequency="year",
    bands=["SWIR1", "NIR", "Red"],
    frames_per_second=3,
    title="Sentinel-2 Timelapse",
)
geemap.show_image(timelapse)
```

### MODIS Timelapse

```{code-cell} ipython3
m = geemap.Map()
m
```

```{code-cell} ipython3
roi = m.user_roi
if roi is None:
    roi = ee.Geometry.BBox(-18.6983, -36.1630, 52.2293, 38.1446)
    m.add_layer(roi)
    m.center_object(roi)
```

```{code-cell} ipython3
timelapse = geemap.modis_ndvi_timelapse(
    roi,
    out_gif="ndvi.gif",
    data="Terra",
    band="NDVI",
    start_date="2000-01-01",
    end_date="2022-12-31",
    frames_per_second=3,
    title="MODIS NDVI Timelapse",
    overlay_data="countries",
)
geemap.show_image(timelapse)
```

```{code-cell} ipython3
m = geemap.Map()
m
```

```{code-cell} ipython3
roi = m.user_roi
if roi is None:
    roi = ee.Geometry.BBox(-171.21, -57.13, 177.53, 79.99)
    m.add_layer(roi)
    m.center_object(roi)
```

```{code-cell} ipython3
timelapse = geemap.modis_ocean_color_timelapse(
    satellite="Aqua",
    start_date="2018-01-01",
    end_date="2020-12-31",
    roi=roi,
    frequency="month",
    out_gif="temperature.gif",
    overlay_data="continents",
    overlay_color="yellow",
    overlay_opacity=0.5,
)
geemap.show_image(timelapse)
```

### GOES Timelapse

```{code-cell} ipython3
roi = ee.Geometry.BBox(167.1898, -28.5757, 202.6258, -12.4411)
start_date = "2022-01-15T03:00:00"
end_date = "2022-01-15T07:00:00"
data = "GOES-17"
scan = "full_disk"
```

```{code-cell} ipython3
timelapse = geemap.goes_timelapse(
    roi, "goes.gif", start_date, end_date, data, scan, framesPerSecond=5
)
geemap.show_image(timelapse)
```

```{code-cell} ipython3
roi = ee.Geometry.BBox(-159.5954, 24.5178, -114.2438, 60.4088)
start_date = "2021-10-24T14:00:00"
end_date = "2021-10-25T01:00:00"
data = "GOES-17"
scan = "full_disk"
```

```{code-cell} ipython3
timelapse = geemap.goes_timelapse(
    roi, "hurricane.gif", start_date, end_date, data, scan, framesPerSecond=5
)
geemap.show_image(timelapse)
```

```{code-cell} ipython3
roi = ee.Geometry.BBox(-121.0034, 36.8488, -117.9052, 39.0490)
start_date = "2020-09-05T15:00:00"
end_date = "2020-09-06T02:00:00"
data = "GOES-17"
scan = "full_disk"
```

```{code-cell} ipython3
timelapse = geemap.goes_fire_timelapse(
    roi, "fire.gif", start_date, end_date, data, scan, framesPerSecond=5
)
geemap.show_image(timelapse)
```

## Charting Earth Engine Data

### Charting Features

#### Import libraries

```{code-cell} ipython3
import calendar
from geemap import chart
```

#### feature_by_feature

```{code-cell} ipython3
ecoregions = ee.FeatureCollection("projects/google/charts_feature_example")
features = ecoregions.select("[0-9][0-9]_tmean|label")
geemap.ee_to_df(features)
```

```{code-cell} ipython3
x_property = "label"
y_properties = [str(x).zfill(2) + "_tmean" for x in range(1, 13)]

labels = calendar.month_abbr[1:]  # a list of month labels, e.g. ['Jan', 'Feb', ...]

colors = [
    "#604791",
    "#1d6b99",
    "#39a8a7",
    "#0f8755",
    "#76b349",
    "#f0af07",
    "#e37d05",
    "#cf513e",
    "#96356f",
    "#724173",
    "#9c4f97",
    "#696969",
]
title = "Average Monthly Temperature by Ecoregion"
x_label = "Ecoregion"
y_label = "Temperature"

fig = chart.feature_by_feature(
    features,
    x_property,
    y_properties,
    colors=colors,
    labels=labels,
    title=title,
    x_label=x_label,
    y_label=y_label,
)
fig
```

#### feature.by_property

```{code-cell} ipython3
ecoregions = ee.FeatureCollection("projects/google/charts_feature_example")
features = ecoregions.select("[0-9][0-9]_ppt|label")
geemap.ee_to_df(features)
```

```{code-cell} ipython3
keys = [str(x).zfill(2) + "_ppt" for x in range(1, 13)]
values = calendar.month_abbr[1:]  # a list of month labels, e.g. ['Jan', 'Feb', ...]
x_properties = dict(zip(keys, values))
series_property = "label"
title = "Average Ecoregion Precipitation by Month"
colors = ["#f0af07", "#0f8755", "#76b349"]
fig = chart.feature_by_property(
    features,
    x_properties,
    series_property,
    title=title,
    colors=colors,
    x_label="Month",
    y_label="Precipitation (mm)",
    legend_location="top-left",
)
fig
```

#### feature_groups

```{code-cell} ipython3
ecoregions = ee.FeatureCollection("projects/google/charts_feature_example")
features = ecoregions.select("[0-9][0-9]_ppt|label")
x_property = "label"
y_property = "01_tmean"
series_property = "warm"
title = "Average January Temperature by Ecoregion"
colors = ["#cf513e", "#1d6b99"]
labels = ["Warm", "Cold"]

fig = chart.feature_groups(
    features,
    x_property,
    y_property,
    series_property,
    title=title,
    colors=colors,
    x_label="Ecoregion",
    y_label="January Temperature (°C)",
    legend_location="top-right",
    labels=labels,
)
fig
```

#### feature_histogram

```{code-cell} ipython3
source = ee.ImageCollection("OREGONSTATE/PRISM/Norm91m").toBands()
region = ee.Geometry.Rectangle(-123.41, 40.43, -116.38, 45.14)
features = source.sample(region, 5000)
geemap.ee_to_df(features.limit(5).select(["07_ppt"]))
```

```{code-cell} ipython3
property = "07_ppt"
title = "July Precipitation Distribution for NW USA"
fig = chart.feature_histogram(
    features,
    property,
    max_buckets=None,
    title=title,
    x_label="Precipitation (mm)",
    y_label="Pixel Count",
    colors=["#1d6b99"],
)
fig
```

### Charting Images

#### image_by_region

```{code-cell} ipython3
ecoregions = ee.FeatureCollection("projects/google/charts_feature_example")
image = (
    ee.ImageCollection("OREGONSTATE/PRISM/Norm91m").toBands().select("[0-9][0-9]_tmean")
)
labels = calendar.month_abbr[1:]  # a list of month labels, e.g. ['Jan', 'Feb', ...]
title = "Average Monthly Temperature by Ecoregion"
fig = chart.image_by_region(
    image,
    ecoregions,
    reducer="mean",
    scale=500,
    x_property="label",
    title=title,
    x_label="Ecoregion",
    y_label="Temperature",
    labels=labels,
)
fig
```

#### image_regions

```{code-cell} ipython3
ecoregions = ee.FeatureCollection("projects/google/charts_feature_example")
image = (
    ee.ImageCollection("OREGONSTATE/PRISM/Norm91m").toBands().select("[0-9][0-9]_ppt")
)
keys = [str(x).zfill(2) + "_ppt" for x in range(1, 13)]
values = calendar.month_abbr[1:]  # a list of month labels, e.g. ['Jan', 'Feb', ...]
x_properties = dict(zip(keys, values))
title = "Average Ecoregion Precipitation by Month"
colors = ["#f0af07", "#0f8755", "#76b349"]
fig = chart.image_regions(
    image,
    ecoregions,
    reducer="mean",
    scale=500,
    series_property="label",
    x_labels=x_properties,
    title=title,
    colors=colors,
    x_label="Month",
    y_label="Precipitation (mm)",
    legend_location="top-left",
)
fig
```

#### image_by_class

```{code-cell} ipython3
ecoregions = ee.FeatureCollection("projects/google/charts_feature_example")
image = (
    ee.ImageCollection("MODIS/061/MOD09A1")
    .filter(ee.Filter.date("2018-06-01", "2018-09-01"))
    .select("sur_refl_b0[0-7]")
    .mean()
    .select([2, 3, 0, 1, 4, 5, 6])
)
wavelengths = [469, 555, 655, 858, 1240, 1640, 2130]
fig = chart.image_by_class(
    image,
    class_band="label",
    region=ecoregions,
    reducer="MEAN",
    scale=500,
    x_labels=wavelengths,
    title="Ecoregion Spectral Signatures",
    x_label="Wavelength (nm)",
    y_label="Reflectance (x1e4)",
    colors=["#f0af07", "#0f8755", "#76b349"],
    legend_location="top-left",
    interpolation="basis",
)
fig
```

#### image_histogram

```{code-cell} ipython3
image = (
    ee.ImageCollection("MODIS/061/MOD09A1")
    .filter(ee.Filter.date("2018-06-01", "2018-09-01"))
    .select(["sur_refl_b01", "sur_refl_b02", "sur_refl_b06"])
    .mean()
)
region = ee.Geometry.Rectangle([-112.60, 40.60, -111.18, 41.22])
fig = chart.image_histogram(
    image,
    region,
    scale=500,
    max_buckets=200,
    min_bucket_width=1.0,
    max_raw=1000,
    max_pixels=int(1e6),
    title="MODIS SR Reflectance Histogram",
    labels=["Red", "NIR", "SWIR"],
    colors=["#cf513e", "#1d6b99", "#f0af07"],
)
fig
```

### Charting Image Collections

#### image_series

```{code-cell} ipython3
# Define the forest feature collection.
forest = ee.FeatureCollection("projects/google/charts_feature_example").filter(
    ee.Filter.eq("label", "Forest")
)

# Load MODIS vegetation indices data and subset a decade of images.
veg_indices = (
    ee.ImageCollection("MODIS/061/MOD13A1")
    .filter(ee.Filter.date("2010-01-01", "2020-01-01"))
    .select(["NDVI", "EVI"])
)

title = "Average Vegetation Index Value by Date for Forest"
x_label = "Year"
y_label = "Vegetation index (x1e4)"
colors = ["#e37d05", "#1d6b99"]

fig = chart.image_series(
    veg_indices,
    region=forest,
    reducer=ee.Reducer.mean(),
    scale=500,
    x_property="system:time_start",
    chart_type="LineChart",
    x_cols="date",
    y_cols=["NDVI", "EVI"],
    colors=colors,
    title=title,
    x_label=x_label,
    y_label=y_label,
    legend_location="right",
)
fig
```

#### image_series_by_region

```{code-cell} ipython3
ecoregions = ee.FeatureCollection("projects/google/charts_feature_example")

veg_indices = (
    ee.ImageCollection("MODIS/061/MOD13A1")
    .filter(ee.Filter.date("2010-01-01", "2020-01-01"))
    .select(["NDVI"])
)

title = "Average NDVI Value by Date"
x_label = "Date"
y_label = "NDVI (x1e4)"
x_cols = "index"
y_cols = ["Desert", "Forest", "Grassland"]
colors = ["#f0af07", "#0f8755", "#76b349"]

fig = chart.image_series_by_region(
    veg_indices,
    regions=ecoregions,
    reducer=ee.Reducer.mean(),
    band="NDVI",
    scale=500,
    x_property="system:time_start",
    series_property="label",
    chart_type="LineChart",
    x_cols=x_cols,
    y_cols=y_cols,
    title=title,
    x_label=x_label,
    y_label=y_label,
    colors=colors,
    stroke_width=3,
    legend_location="bottom-left",
)
fig
```

#### image_doy_series

```{code-cell} ipython3
# Import the example feature collection and subset the grassland feature.
grassland = ee.FeatureCollection("projects/google/charts_feature_example").filter(
    ee.Filter.eq("label", "Grassland")
)

# Load MODIS vegetation indices data and subset a decade of images.
veg_indices = (
    ee.ImageCollection("MODIS/061/MOD13A1")
    .filter(ee.Filter.date("2010-01-01", "2020-01-01"))
    .select(["NDVI", "EVI"])
)

title = "Average Vegetation Index Value by Day of Year for Grassland"
x_label = "Day of Year"
y_label = "Vegetation Index (x1e4)"
colors = ["#f0af07", "#0f8755"]

fig = chart.image_doy_series(
    image_collection=veg_indices,
    region=grassland,
    scale=500,
    chart_type="LineChart",
    title=title,
    x_label=x_label,
    y_label=y_label,
    colors=colors,
    stroke_width=5,
)
fig
```

#### image_doy_series_by_year

```{code-cell} ipython3
# Import the example feature collection and subset the grassland feature.
grassland = ee.FeatureCollection("projects/google/charts_feature_example").filter(
    ee.Filter.eq("label", "Grassland")
)

# Load MODIS vegetation indices data and subset years 2012 and 2019.
veg_indices = (
    ee.ImageCollection("MODIS/061/MOD13A1")
    .filter(
        ee.Filter.Or(
            ee.Filter.date("2012-01-01", "2013-01-01"),
            ee.Filter.date("2019-01-01", "2020-01-01"),
        )
    )
    .select(["NDVI", "EVI"])
)

title = "Average Vegetation Index Value by Day of Year for Grassland"
x_label = "Day of Year"
y_label = "Vegetation Index (x1e4)"
colors = ["#e37d05", "#1d6b99"]

fig = chart.doy_series_by_year(
    veg_indices,
    band_name="NDVI",
    region=grassland,
    scale=500,
    chart_type="LineChart",
    colors=colors,
    title=title,
    x_label=x_label,
    y_label=y_label,
    stroke_width=5,
)
fig
```

#### image_doy_series_by_region

```{code-cell} ipython3
# Import the example feature collection and subset the grassland feature.
ecoregions = ee.FeatureCollection("projects/google/charts_feature_example")

# Load MODIS vegetation indices data and subset a decade of images.
veg_indices = (
    ee.ImageCollection("MODIS/061/MOD13A1")
    .filter(ee.Filter.date("2010-01-01", "2020-01-01"))
    .select(["NDVI"])
)

title = "Average Vegetation Index Value by Day of Year for Grassland"
x_label = "Day of Year"
y_label = "Vegetation Index (x1e4)"
colors = ["#f0af07", "#0f8755", "#76b349"]

fig = chart.image_doy_series_by_region(
    veg_indices,
    "NDVI",
    ecoregions,
    region_reducer="mean",
    scale=500,
    year_reducer=ee.Reducer.mean(),
    start_day=1,
    end_day=366,
    series_property="label",
    stroke_width=5,
    chart_type="LineChart",
    title=title,
    x_label=x_label,
    y_label=y_label,
    colors=colors,
    legend_location="right",
)
fig
```

### Charting Array and List

#### Scatter Plot

```{code-cell} ipython3
# Import the example feature collection and subset the forest feature.
forest = ee.FeatureCollection("projects/google/charts_feature_example").filter(
    ee.Filter.eq("label", "Forest")
)

# Define a MODIS surface reflectance composite.
modisSr = (
    ee.ImageCollection("MODIS/061/MOD09A1")
    .filter(ee.Filter.date("2018-06-01", "2018-09-01"))
    .select("sur_refl_b0[0-7]")
    .mean()
)

# Reduce MODIS reflectance bands by forest region; get a dictionary with
# band names as keys, pixel values as lists.
pixel_vals = modisSr.reduceRegion(
    **{"reducer": ee.Reducer.toList(), "geometry": forest.geometry(), "scale": 2000}
)

# Convert NIR and SWIR value lists to an array to be plotted along the y-axis.
y_values = pixel_vals.toArray(["sur_refl_b02", "sur_refl_b06"])

# Get the red band value list; to be plotted along the x-axis.
x_values = ee.List(pixel_vals.get("sur_refl_b01"))

title = "Relationship Among Spectral Bands for Forest Pixels"
colors = ["rgba(29,107,153,0.4)", "rgba(207,81,62,0.4)"]

fig = chart.array_values(
    y_values,
    axis=1,
    x_labels=x_values,
    series_names=["NIR", "SWIR"],
    chart_type="ScatterChart",
    colors=colors,
    title=title,
    x_label="Red reflectance (x1e4)",
    y_label="NIR & SWIR reflectance (x1e4)",
    default_size=15,
    xlim=(0, 800),
)
fig
```

#### Transect Line Plot

```{code-cell} ipython3
# Define a line across the Olympic Peninsula, USA.
transect = ee.Geometry.LineString([[-122.8, 47.8], [-124.5, 47.8]])

# Define a pixel coordinate image.
lat_lon_img = ee.Image.pixelLonLat()

# Import a digital surface model and add latitude and longitude bands.
elev_img = ee.Image("USGS/SRTMGL1_003").select("elevation").addBands(lat_lon_img)

# Reduce elevation and coordinate bands by transect line; get a dictionary with
# band names as keys, pixel values as lists.
elev_transect = elev_img.reduceRegion(
    reducer=ee.Reducer.toList(),
    geometry=transect,
    scale=1000,
)

# Get longitude and elevation value lists from the reduction dictionary.
lon = ee.List(elev_transect.get("longitude"))
elev = ee.List(elev_transect.get("elevation"))

# Sort the longitude and elevation values by ascending longitude.
lon_sort = lon.sort(lon)
elev_sort = elev.sort(lon)

fig = chart.array_values(
    elev_sort,
    x_labels=lon_sort,
    series_names=["Elevation"],
    chart_type="AreaChart",
    colors=["#1d6b99"],
    title="Elevation Profile Across Longitude",
    x_label="Longitude",
    y_label="Elevation (m)",
    stroke_width=5,
    fill="bottom",
    fill_opacities=[0.4],
    ylim=(0, 2500),
)
fig
```

#### Metadata Scatter Plot

```{code-cell} ipython3
# Import a Landsat 8 collection and filter to a single path/row.
col = ee.ImageCollection("LANDSAT/LC08/C02/T1_L2").filter(
    ee.Filter.expression("WRS_PATH ==  45 && WRS_ROW == 30")
)

# Reduce image properties to a series of lists; one for each selected property.
propVals = col.reduceColumns(
    reducer=ee.Reducer.toList().repeat(2),
    selectors=["CLOUD_COVER", "GEOMETRIC_RMSE_MODEL"],
).get("list")

# Get selected image property value lists; to be plotted along x and y axes.
x = ee.List(ee.List(propVals).get(0))
y = ee.List(ee.List(propVals).get(1))

colors = [geemap.hex_to_rgba("#96356f", 0.4)]
fig = chart.array_values(
    y,
    x_labels=x,
    series_names=["RMSE"],
    chart_type="ScatterChart",
    colors=colors,
    title="Landsat 8 Image Collection Metadata (045030)",
    x_label="Cloud cover (%)",
    y_label="Geometric RMSE (m)",
    default_size=15,
)
fig
```

#### Mapped Function Scatter & Line Plot

```{code-cell} ipython3
import math

start = -2 * math.pi
end = 2 * math.pi
points = ee.List.sequence(start, end, None, 50)

def sin_func(val):
    return ee.Number(val).sin()

values = points.map(sin_func)
fig = chart.array_values(
    values,
    points,
    chart_type="LineChart",
    colors=["#39a8a7"],
    title="Sine Function",
    x_label="radians",
    y_label="sin(x)",
    marker="circle",
)
fig
```

### Charting Data Table

#### Manual DataTable chart

```{code-cell} ipython3
import pandas as pd

data = {
    "State": ["CA", "NY", "IL", "MI", "OR"],
    "Population": [37253956, 19378102, 12830632, 9883640, 3831074],
}

df = pd.DataFrame(data)
df
```

```{code-cell} ipython3
fig = chart.Chart(
    df,
    x_cols=["State"],
    y_cols=["Population"],
    chart_type="ColumnChart",
    colors=["#1d6b99"],
    title="State Population (US census, 2010)",
    x_label="State",
    y_label="Population",
)
fig
```

#### Computed DataTable chart

```{code-cell} ipython3
# Import the example feature collection and subset the forest feature.
forest = ee.FeatureCollection("projects/google/charts_feature_example").filter(
    ee.Filter.eq("label", "Forest")
)

# Load MODIS vegetation indices data and subset a decade of images.
veg_indices = (
    ee.ImageCollection("MODIS/061/MOD13A1")
    .filter(ee.Filter.date("2010-01-01", "2020-01-01"))
    .select(["NDVI", "EVI"])
)

# Build a feature collection where each feature has a property that represents
# a DataFrame row.


def aggregate(img):
    # Reduce the image to the mean of pixels intersecting the forest ecoregion.
    stat = img.reduceRegion(
        **{"reducer": ee.Reducer.mean(), "geometry": forest, "scale": 500}
    )

    # Extract the reduction results along with the image date.
    date = geemap.image_date(img)
    evi = stat.get("EVI")
    ndvi = stat.get("NDVI")

    # Make a list of observation attributes to define a row in the DataTable.
    row = ee.List([date, evi, ndvi])

    # Return the row as a property of an ee.Feature.
    return ee.Feature(None, {"row": row})


reduction_table = veg_indices.map(aggregate)

# Aggregate the 'row' property from all features in the new feature collection
# to make a server-side 2-D list (DataTable).
data_table_server = reduction_table.aggregate_array("row")

# Define column names and properties for the DataTable. The order should
# correspond to the order in the construction of the 'row' property above.
column_header = ee.List([["Date", "EVI", "NDVI"]])

# Concatenate the column header to the table.
data_table_server = column_header.cat(data_table_server)
data_table = chart.DataTable(data_table_server, date_column="Date")
data_table.head()
```

```{code-cell} ipython3
fig = chart.Chart(
    data_table,
    chart_type="LineChart",
    x_cols="Date",
    y_cols=["EVI", "NDVI"],
    colors=["#e37d05", "#1d6b99"],
    title="Average Vegetation Index Value by Date for Forest",
    x_label="Date",
    y_label="Vegetation index (x1e4)",
    stroke_width=3,
    legend_location="right",
)
fig
```

#### Interval chart

```{code-cell} ipython3
# Define a point to extract an NDVI time series for.
geometry = ee.Geometry.Point([-121.679, 36.479])

# Define a band of interest (NDVI), import the MODIS vegetation index dataset,
# and select the band.
band = "NDVI"
ndvi_col = ee.ImageCollection("MODIS/061/MOD13Q1").select(band)

# Map over the collection to add a day of year (doy) property to each image.


def set_doy(img):
    doy = ee.Date(img.get("system:time_start")).getRelative("day", "year")
    # Add 8 to day of year number so that the doy label represents the middle of
    # the 16-day MODIS NDVI composite.
    return img.set("doy", ee.Number(doy).add(8))


ndvi_col = ndvi_col.map(set_doy)

# Join all coincident day of year observations into a set of image collections.
distinct_doy = ndvi_col.filterDate("2013-01-01", "2014-01-01")
filter = ee.Filter.equals(**{"leftField": "doy", "rightField": "doy"})
join = ee.Join.saveAll("doy_matches")
join_col = ee.ImageCollection(join.apply(distinct_doy, ndvi_col, filter))

# Calculate the absolute range, interquartile range, and median for the set
# of images composing each coincident doy observation group. The result is
# an image collection with an image representative per unique doy observation
# with bands that describe the 0, 25, 50, 75, 100 percentiles for the set of
# coincident doy images.


def cal_percentiles(img):
    doyCol = ee.ImageCollection.fromImages(img.get("doy_matches"))

    return doyCol.reduce(
        ee.Reducer.percentile([0, 25, 50, 75, 100], ["p0", "p25", "p50", "p75", "p100"])
    ).set({"doy": img.get("doy")})


comp = ee.ImageCollection(join_col.map(cal_percentiles))

# Extract the inter-annual NDVI doy percentile statistics for the
# point of interest per unique doy representative. The result is
# is a feature collection where each feature is a doy representative that
# contains a property (row) describing the respective inter-annual NDVI
# variance, formatted as a list of values.


def order_percentiles(img):
    stats = ee.Dictionary(
        img.reduceRegion(
            **{"reducer": ee.Reducer.first(), "geometry": geometry, "scale": 250}
        )
    )

    # Order the percentile reduction elements according to how you want columns
    # in the DataTable arranged (x-axis values need to be first).
    row = ee.List(
        [
            img.get("doy"),
            stats.get(band + "_p50"),
            stats.get(band + "_p0"),
            stats.get(band + "_p25"),
            stats.get(band + "_p75"),
            stats.get(band + "_p100"),
        ]
    )

    # Return the row as a property of an ee.Feature.
    return ee.Feature(None, {"row": row})


reduction_table = comp.map(order_percentiles)

# Aggregate the 'row' properties to make a server-side 2-D array (DataTable).
data_table_server = reduction_table.aggregate_array("row")

# Define column names and properties for the DataTable. The order should
# correspond to the order in the construction of the 'row' property above.
column_header = ee.List([["DOY", "median", "p0", "p25", "p75", "p100"]])

# Concatenate the column header to the table.
data_table_server = column_header.cat(data_table_server)
df = chart.DataTable(data_table_server)
df.head()
```

```{code-cell} ipython3
fig = chart.Chart(
    df,
    chart_type="IntervalChart",
    x_cols="DOY",
    y_cols=["p0", "p25", "median", "p75", "p100"],
    title="Annual NDVI Time Series with Inter-Annual Variance",
    x_label="Day of Year",
    y_label="Vegetation index (x1e4)",
    stroke_width=1,
    fill="between",
    fill_colors=["#b6d1c6", "#83b191", "#83b191", "#b6d1c6"],
    fill_opacities=[0.6] * 4,
    labels=["p0", "p25", "median", "p75", "p100"],
    display_legend=True,
    legend_location="top-right",
    ylim=(0, 10000),
)
fig
```

## Key Takeaways

## Exercises

### Exercise 1: Visualizing DEM Data

```{code-cell} ipython3

```

### Exercise 2: Cloud-Free Composite with Sentinel-2 or Landsat

```{code-cell} ipython3

```

### Exercise 3: Visualizing NAIP Imagery

```{code-cell} ipython3

```

### Exercise 4: Visualizing Watershed Boundaries

```{code-cell} ipython3

```

### Exercise 5: Visualizing Land Cover Change

```{code-cell} ipython3

```

### Exercise 6: Creating a Landsat Timelapse Animation

```{code-cell} ipython3

```
