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

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/intro-gispro/blob/main/book/geospatial/maplibre.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/intro-gispro/main?urlpath=lab/tree/book/geospatial/maplibre.ipynb)

# 3D Mapping with MapLibre

## Introduction

## Learning Objectives

## Useful Resources

## Installation and Setup

```{code-cell} ipython3
# %pip install -U leafmap pygis
```

```{code-cell} ipython3
import leafmap.maplibregl as leafmap
```

## Creating Interactive Maps

### Basic Map Setup

```{code-cell} ipython3
m = leafmap.Map()
m
```

### Customizing the Map's Center and Zoom Level

```{code-cell} ipython3
m = leafmap.Map(center=[-100, 40], zoom=3, pitch=0, bearing=0)
m
```

### Choosing a Basemap Style

```{code-cell} ipython3
m = leafmap.Map(style="positron")
m
```

```{code-cell} ipython3
m = leafmap.Map(style="liberty", projection="globe")
m
```

### Adding Background Colors

```{code-cell} ipython3
m = leafmap.Map(style="background-lightgray")
m
```

```{code-cell} ipython3
style = "https://demotiles.maplibre.org/style.json"
m = leafmap.Map(style=style)
m
```

## Adding Map Controls

### Available Controls

### Adding Geolocate Control

```{code-cell} ipython3
m = leafmap.Map()
m.add_control("geolocate", position="top-left")
m
```

### Adding Fullscreen Control

```{code-cell} ipython3
m = leafmap.Map(center=[11.255, 43.77], zoom=13, style="positron", controls={})
m.add_control("fullscreen", position="top-right")
m
```

### Adding Navigation Control

```{code-cell} ipython3
m = leafmap.Map(center=[11.255, 43.77], zoom=13, style="positron", controls={})
m.add_control("navigation", position="top-left")
m
```

### Adding Draw Control

```{code-cell} ipython3
m = leafmap.Map(center=[-100, 40], zoom=3, style="positron")
m.add_draw_control(position="top-left")
m
```

```{code-cell} ipython3
m = leafmap.Map(center=[-100, 40], zoom=3, style="positron")
geojson = {
    "type": "FeatureCollection",
    "features": [
        {
            "id": "abc",
            "type": "Feature",
            "properties": {},
            "geometry": {
                "coordinates": [
                    [
                        [-119.08, 45.95],
                        [-119.79, 42.08],
                        [-107.28, 41.43],
                        [-108.15, 46.44],
                        [-119.08, 45.95],
                    ]
                ],
                "type": "Polygon",
            },
        },
        {
            "id": "xyz",
            "type": "Feature",
            "properties": {},
            "geometry": {
                "coordinates": [
                    [
                        [-103.87, 38.08],
                        [-108.54, 36.44],
                        [-106.25, 33.00],
                        [-99.91, 31.79],
                        [-96.82, 35.48],
                        [-98.80, 37.77],
                        [-103.87, 38.08],
                    ]
                ],
                "type": "Polygon",
            },
        },
    ],
}
m.add_draw_control(position="top-left", geojson=geojson)
m
```

```{code-cell} ipython3
m.draw_features_selected
```

```{code-cell} ipython3
m.draw_feature_collection_all
```

## Adding Layers

### Adding Basemaps

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("OpenTopoMap")
m.add_layer_control()
m
```

```{code-cell} ipython3
m.add_basemap("Esri.WorldImagery")
```

```{code-cell} ipython3
m = leafmap.Map()
m
```

```{code-cell} ipython3
m.add_basemap()
```

### Adding XYZ Tile Layer

```{code-cell} ipython3
m = leafmap.Map()
url = "https://basemap.nationalmap.gov/arcgis/rest/services/USGSTopo/MapServer/tile/{z}/{y}/{x}"
m.add_tile_layer(url, name="USGS TOpo", attribution="USGS", opacity=1.0, visible=True)
m
```

### Adding WMS Layer

```{code-cell} ipython3
m = leafmap.Map(center=[-74.5447, 40.6892], zoom=8, style="liberty")
url = "https://img.nj.gov/imagerywms/Natural2015"
layers = "Natural2015"
m.add_wms_layer(url, layers=layers, before_id="aeroway_fill")
m.add_layer_control()
m
```

```{code-cell} ipython3
m = leafmap.Map(center=[-100.307965, 46.98692], zoom=13, pitch=45, style="liberty")
m.add_basemap("Esri.WorldImagery")
url = "https://fwspublicservices.wim.usgs.gov/wetlandsmapservice/services/Wetlands/MapServer/WMSServer"
m.add_wms_layer(url, layers="1", name="NWI", opacity=0.6)
m.add_layer_control()
m.add_legend(builtin_legend="NWI", title="Wetland Type")
m
```

## Using MapTiler

```{code-cell} ipython3
# import os
# os.environ["MAPTILER_KEY"] = "YOUR_API_KEY"
```

```{code-cell} ipython3
m = leafmap.Map(style="streets")
m
```

```{code-cell} ipython3
m = leafmap.Map(style="satellite")
m
```

```{code-cell} ipython3
m = leafmap.Map(style="hybrid")
m
```

```{code-cell} ipython3
m = leafmap.Map(style="topo")
m
```

## 3D Mapping

### 3D Terrain

```{code-cell} ipython3
m = leafmap.Map(
    center=[-122.1874314, 46.2022386], zoom=13, pitch=60, bearing=220, style="3d-hybrid"
)
m.add_layer_control(bg_layers=True)
m
```

```{code-cell} ipython3
m = leafmap.Map(
    center=[-122.1874314, 46.2022386],
    zoom=13,
    pitch=60,
    bearing=220,
    style="3d-satellite",
)
m.add_layer_control(bg_layers=True)
m
```

```{code-cell} ipython3
m = leafmap.Map(
    center=[-122.1874314, 46.2022386],
    zoom=13,
    pitch=60,
    bearing=220,
    style="3d-topo",
    exaggeration=1.5,
    hillshade=False,
)
m.add_layer_control(bg_layers=True)
m
```

```{code-cell} ipython3
m = leafmap.Map(
    center=[-122.1874314, 46.2022386],
    zoom=13,
    pitch=60,
    bearing=220,
    style="3d-terrain",
)
m.add_layer_control(bg_layers=True)
m
```

```{code-cell} ipython3
m = leafmap.Map(style="3d-ocean", exaggeration=1.5, hillshade=True)
m.add_layer_control(bg_layers=True)
m
```

### 3D Buildings

```{code-cell} ipython3
m = leafmap.Map(
    center=[-74.01201, 40.70473], zoom=16, pitch=60, bearing=35, style="basic-v2"
)
MAPTILER_KEY = leafmap.get_api_key("MAPTILER_KEY")
m.add_basemap("Esri.WorldImagery", visible=False)
source = {
    "url": f"https://api.maptiler.com/tiles/v3/tiles.json?key={MAPTILER_KEY}",
    "type": "vector",
}

layer = {
    "id": "3d-buildings",
    "source": "openmaptiles",
    "source-layer": "building",
    "type": "fill-extrusion",
    "min-zoom": 15,
    "paint": {
        "fill-extrusion-color": [
            "interpolate",
            ["linear"],
            ["get", "render_height"],
            0,
            "lightgray",
            200,
            "royalblue",
            400,
            "lightblue",
        ],
        "fill-extrusion-height": [
            "interpolate",
            ["linear"],
            ["zoom"],
            15,
            0,
            16,
            ["get", "render_height"],
        ],
        "fill-extrusion-base": [
            "case",
            [">=", ["get", "zoom"], 16],
            ["get", "render_min_height"],
            0,
        ],
    },
}
m.add_source("openmaptiles", source)
m.add_layer(layer)
m.add_layer_control()
m
```

```{code-cell} ipython3
m = leafmap.Map(
    center=[-74.01201, 40.70473], zoom=16, pitch=60, bearing=35, style="basic-v2"
)
m.add_basemap("Esri.WorldImagery", visible=False)
m.add_3d_buildings(min_zoom=15)
m.add_layer_control()
m
```

### 3D Indoor Mapping

```{code-cell} ipython3
data = "https://maplibre.org/maplibre-gl-js/docs/assets/indoor-3d-map.geojson"
gdf = leafmap.geojson_to_gdf(data)
gdf.explore()
```

```{code-cell} ipython3
gdf.head()
```

```{code-cell} ipython3
m = leafmap.Map(
    center=(-87.61694, 41.86625), zoom=17, pitch=40, bearing=20, style="positron"
)
m.add_basemap("OpenStreetMap.Mapnik")
m.add_geojson(
    data,
    layer_type="fill-extrusion",
    name="floorplan",
    paint={
        "fill-extrusion-color": ["get", "color"],
        "fill-extrusion-height": ["get", "height"],
        "fill-extrusion-base": ["get", "base_height"],
        "fill-extrusion-opacity": 0.5,
    },
)
m.add_layer_control()
m
```

### 3D Choropleth Map

```{code-cell} ipython3
m = leafmap.Map(center=[19.43, 49.49], zoom=3, pitch=60, style="basic")
source = {
    "type": "geojson",
    "data": "https://docs.maptiler.com/sdk-js/assets/Mean_age_of_women_at_first_marriage_in_2019.geojson",
}
m.add_source("countries", source)
layer = {
    "id": "eu-countries",
    "source": "countries",
    "type": "fill-extrusion",
    "paint": {
        "fill-extrusion-color": [
            "interpolate",
            ["linear"],
            ["get", "age"],
            23.0,
            "#fff5eb",
            24.0,
            "#fee6ce",
            25.0,
            "#fdd0a2",
            26.0,
            "#fdae6b",
            27.0,
            "#fd8d3c",
            28.0,
            "#f16913",
            29.0,
            "#d94801",
            30.0,
            "#8c2d04",
        ],
        "fill-extrusion-opacity": 1,
        "fill-extrusion-height": ["*", ["get", "age"], 5000],
    },
}
first_symbol_layer_id = m.find_first_symbol_layer()["id"]
m.add_layer(layer, first_symbol_layer_id)
m.add_layer_control()
m
```

```{code-cell} ipython3
m = leafmap.Map(center=[-100, 40], zoom=3, pitch=60, style="basic", projection="globe")
source = {
    "type": "geojson",
    "data": "https://opengeos.org/data/us/us_counties.geojson",
}
m.add_source("counties", source)
layer = {
    "id": "us-counties",
    "source": "counties",
    "type": "fill-extrusion",
    "paint": {
        "fill-extrusion-color": [
            "interpolate",
            ["linear"],
            ["get", "CENSUSAREA"],
            400,
            "#fff5eb",
            600,
            "#fee6ce",
            800,
            "#fdd0a2",
            1000,
            "#fdae6b",
        ],
        "fill-extrusion-opacity": 1,
        "fill-extrusion-height": ["*", ["get", "CENSUSAREA"], 50],
    },
}
first_symbol_layer_id = m.find_first_symbol_layer()["id"]
m.add_layer(layer, first_symbol_layer_id)
m.add_layer_control()
m
```

## Visualizing Vector Data

### Point Data

```{code-cell} ipython3
m = leafmap.Map(center=[12.550343, 55.665957], zoom=8, style="positron")
m.add_marker(lng_lat=[12.550343, 55.665957])
m
```

```{code-cell} ipython3
m = leafmap.Map(center=[12.550343, 55.665957], zoom=8, style="positron")
m.add_marker(lng_lat=[12.550343, 55.665957], options={"draggable": True})
m
```

```{code-cell} ipython3
url = (
    "https://github.com/opengeos/datasets/releases/download/world/world_cities.geojson"
)
geojson = leafmap.read_geojson(url)
```

```{code-cell} ipython3
m = leafmap.Map(style="streets")
m.add_geojson(geojson, name="cities")
m.add_popup("cities")
m
```

```{code-cell} ipython3
m = leafmap.Map(style="streets")
source = {"type": "geojson", "data": geojson}

layer = {
    "id": "cities",
    "type": "symbol",
    "source": "point",
    "layout": {
        "icon-image": "marker_15",
        "icon-size": 1,
    },
}
m.add_source("point", source)
m.add_layer(layer)
m.add_popup("cities")
m
```

#### Customizing Marker Icon Image

```{code-cell} ipython3
m = leafmap.Map(center=[0, 0], zoom=1, style="positron")
image = "https://maplibre.org/maplibre-gl-js/docs/assets/osgeo-logo.png"
m.add_image("custom-marker", image)

url = "https://github.com/opengeos/datasets/releases/download/places/osgeo_conferences.geojson"
geojson = leafmap.read_geojson(url)

source = {"type": "geojson", "data": geojson}

m.add_source("conferences", source)
layer = {
    "id": "conferences",
    "type": "symbol",
    "source": "conferences",
    "layout": {
        "icon-image": "custom-marker",
        "text-field": ["get", "year"],
        "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
        "text-offset": [0, 1.25],
        "text-anchor": "top",
    },
}

m.add_layer(layer)
m
```

### Line Data

```{code-cell} ipython3
m = leafmap.Map(center=[-122.486052, 37.830348], zoom=15, style="streets")

source = {
    "type": "geojson",
    "data": {
        "type": "Feature",
        "properties": {},
        "geometry": {
            "type": "LineString",
            "coordinates": [
                [-122.48369693756104, 37.83381888486939],
                [-122.48348236083984, 37.83317489144141],
                [-122.48339653015138, 37.83270036637107],
                [-122.48356819152832, 37.832056363179625],
                [-122.48404026031496, 37.83114119107971],
                [-122.48404026031496, 37.83049717427869],
                [-122.48348236083984, 37.829920943955045],
                [-122.48356819152832, 37.82954808664175],
                [-122.48507022857666, 37.82944639795659],
            ],
        },
    },
}

layer = {
    "id": "route",
    "type": "line",
    "source": "route",
    "layout": {"line-join": "round", "line-cap": "round"},
    "paint": {"line-color": "#888", "line-width": 8},
}
m.add_source("route", source)
m.add_layer(layer)
m
```

### Polygon Data

```{code-cell} ipython3
m = leafmap.Map(style="hybrid")
geojson = "https://github.com/opengeos/datasets/releases/download/places/wa_overture_buildings.geojson"
paint = {"fill-color": "#ffff00", "fill-opacity": 0.5, "fill-outline-color": "#ff0000"}
m.add_geojson(geojson, layer_type="fill", paint=paint, name="Fill")
m
```

```{code-cell} ipython3
m = leafmap.Map(style="hybrid")
geojson = "https://github.com/opengeos/datasets/releases/download/places/wa_overture_buildings.geojson"
paint_line = {"line-color": "#ff0000", "line-width": 3}
m.add_geojson(geojson, layer_type="line", paint=paint_line, name="Outline")
paint_fill = {"fill-color": "#ffff00", "fill-opacity": 0.5}
m.add_geojson(geojson, layer_type="fill", paint=paint_fill, name="Fill")
m.add_layer_control()
m
```

### Multiple Geometries

```{code-cell} ipython3
m = leafmap.Map(
    center=[-123.13, 49.254], zoom=11, style="dark-matter", pitch=45, bearing=0
)
url = "https://raw.githubusercontent.com/visgl/deck.gl-data/master/examples/geojson/vancouver-blocks.json"
paint_line = {
    "line-color": "white",
    "line-width": 2,
}
paint_fill = {
    "fill-extrusion-color": {
        "property": "valuePerSqm",
        "stops": [
            [0, "grey"],
            [1000, "yellow"],
            [5000, "orange"],
            [10000, "darkred"],
            [50000, "lightblue"],
        ],
    },
    "fill-extrusion-height": ["*", 10, ["sqrt", ["get", "valuePerSqm"]]],
    "fill-extrusion-opacity": 0.9,
}
m.add_geojson(url, layer_type="line", paint=paint_line, name="blocks-line")
m.add_geojson(url, layer_type="fill-extrusion", paint=paint_fill, name="blocks-fill")
m
```

### Marker Cluster

```{code-cell} ipython3
m = leafmap.Map(center=[-103.59179, 40.66995], zoom=3, style="streets")
data = "https://docs.mapbox.com/mapbox-gl-js/assets/earthquakes.geojson"
source_args = {
    "cluster": True,
    "cluster_radius": 50,
    "cluster_min_points": 2,
    "cluster_max_zoom": 14,
    "cluster_properties": {
        "maxMag": ["max", ["get", "mag"]],
        "minMag": ["min", ["get", "mag"]],
    },
}

m.add_geojson(
    data,
    layer_type="circle",
    name="earthquake-circles",
    filter=["!", ["has", "point_count"]],
    paint={"circle-color": "darkblue"},
    source_args=source_args,
)

m.add_geojson(
    data,
    layer_type="circle",
    name="earthquake-clusters",
    filter=["has", "point_count"],
    paint={
        "circle-color": [
            "step",
            ["get", "point_count"],
            "#51bbd6",
            100,
            "#f1f075",
            750,
            "#f28cb1",
        ],
        "circle-radius": ["step", ["get", "point_count"], 20, 100, 30, 750, 40],
    },
    source_args=source_args,
)

m.add_geojson(
    data,
    layer_type="symbol",
    name="earthquake-labels",
    filter=["has", "point_count"],
    layout={
        "text-field": ["get", "point_count_abbreviated"],
        "text-size": 12,
    },
    source_args=source_args,
)
m
```

### Local Vector Data

```{code-cell} ipython3
url = "https://github.com/opengeos/datasets/releases/download/us/us_states.geojson"
filepath = "data/us_states.geojson"
leafmap.download_file(url, filepath, quiet=True)
```

```{code-cell} ipython3
m = leafmap.Map(center=[-100, 40], zoom=3)
m
```

```{code-cell} ipython3
m.open_geojson()
```

### Changing Building Color

```{code-cell} ipython3
m = leafmap.Map(center=[-90.73414, 14.55524], zoom=13, style="basic")
m.set_paint_property(
    "building",
    "fill-color",
    ["interpolate", ["exponential", 0.5], ["zoom"], 15, "#e2714b", 22, "#eee695"],
)
m.set_paint_property(
    "building",
    "fill-opacity",
    ["interpolate", ["exponential", 0.5], ["zoom"], 15, 0, 22, 1],
)
m.add_layer_control(bg_layers=True)
m
```

```{code-cell} ipython3
m.add_call("zoomTo", 19, {"duration": 9000})
```

### Adding a New Layer Below Labels

```{code-cell} ipython3
m = leafmap.Map(center=[-88.137343, 35.137451], zoom=4, style="streets")
source = {
    "type": "geojson",
    "data": "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_50m_urban_areas.geojson",
}
m.add_source("urban-areas", source)
first_symbol_layer = m.find_first_symbol_layer()
layer = {
    "id": "urban-areas-fill",
    "type": "fill",
    "source": "urban-areas",
    "layout": {},
    "paint": {"fill-color": "#f08", "fill-opacity": 0.4},
}
m.add_layer(layer, before_id=first_symbol_layer["id"])
m
```

### Visualizing Population Density

```{code-cell} ipython3
m = leafmap.Map(center=[30.0222, -1.9596], zoom=7, style="streets")
source = {
    "type": "geojson",
    "data": "https://maplibre.org/maplibre-gl-js/docs/assets/rwanda-provinces.geojson",
}
m.add_source("rwanda-provinces", source)
layer = {
    "id": "rwanda-provinces",
    "type": "fill",
    "source": "rwanda-provinces",
    "layout": {},
    "paint": {
        "fill-color": [
            "let",
            "density",
            ["/", ["get", "population"], ["get", "sq-km"]],
            [
                "interpolate",
                ["linear"],
                ["zoom"],
                8,
                [
                    "interpolate",
                    ["linear"],
                    ["var", "density"],
                    274,
                    ["to-color", "#edf8e9"],
                    1551,
                    ["to-color", "#006d2c"],
                ],
                10,
                [
                    "interpolate",
                    ["linear"],
                    ["var", "density"],
                    274,
                    ["to-color", "#eff3ff"],
                    1551,
                    ["to-color", "#08519c"],
                ],
            ],
        ],
        "fill-opacity": 0.7,
    },
}
m.add_layer(layer)
m
```

## Visualizing Raster Data

### Local Raster Data

```{code-cell} ipython3
url = "https://github.com/opengeos/datasets/releases/download/raster/landsat.tif"
filepath = "landsat.tif"
leafmap.download_file(url, filepath, quiet=True)
```

```{code-cell} ipython3
m = leafmap.Map(style="streets")
m.add_raster(filepath, indexes=[3, 2, 1], vmin=0, vmax=100, name="Landsat-321")
m.add_raster(filepath, indexes=[4, 3, 2], vmin=0, vmax=100, name="Landsat-432")
m.add_layer_control()
m
```

```{code-cell} ipython3
url = "https://github.com/opengeos/datasets/releases/download/raster/srtm90.tif"
filepath = "srtm90.tif"
leafmap.download_file(url, filepath, quiet=True)
```

```{code-cell} ipython3
m = leafmap.Map(style="satellite")
m.add_raster(filepath, colormap="terrain", name="DEM")
m
```

### Cloud Optimized GeoTIFF (COG)

```{code-cell} ipython3
m = leafmap.Map(style="satellite")
before = (
    "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-07-01.tif"
)
after = (
    "https://github.com/opengeos/datasets/releases/download/raster/Libya-2023-09-13.tif"
)
m.add_cog_layer(before, name="Before", attribution="Maxar")
m.add_cog_layer(after, name="After", attribution="Maxar", fit_bounds=True)
m.add_layer_control()
m
```

### STAC Layer

```{code-cell} ipython3
m = leafmap.Map(style="streets")
url = "https://canada-spot-ortho.s3.amazonaws.com/canada_spot_orthoimages/canada_spot5_orthoimages/S5_2007/S5_11055_6057_20070622/S5_11055_6057_20070622.json"
m.add_stac_layer(url, bands=["pan"], name="Panchromatic", vmin=0, vmax=150)
m.add_stac_layer(url, bands=["B4", "B3", "B2"], name="RGB", vmin=0, vmax=150)
m.add_layer_control()
m
```

```{code-cell} ipython3
collection = "landsat-8-c2-l2"
item = "LC08_L2SP_047027_20201204_02_T1"
```

```{code-cell} ipython3
leafmap.stac_assets(collection=collection, item=item, titiler_endpoint="pc")
```

```{code-cell} ipython3
m = leafmap.Map(style="satellite")
m.add_stac_layer(
    collection=collection,
    item=item,
    assets=["SR_B5", "SR_B4", "SR_B3"],
    name="Color infrared",
)
m
```

## Adding Custom Components

### Adding Image

```{code-cell} ipython3
m = leafmap.Map(center=[0.349419, -1.80921], zoom=3, style="streets")
image = "https://upload.wikimedia.org/wikipedia/commons/7/7c/201408_cat.png"
source = {
    "type": "geojson",
    "data": {
        "type": "FeatureCollection",
        "features": [
            {"type": "Feature", "geometry": {"type": "Point", "coordinates": [0, 0]}}
        ],
    },
}

layer = {
    "id": "points",
    "type": "symbol",
    "source": "point",
    "layout": {
        "icon-image": "cat",
        "icon-size": 0.25,
        "text-field": "I love kitty!",
        "text-font": ["Open Sans Regular"],
        "text-offset": [0, 3],
        "text-anchor": "top",
    },
}
m.add_image("cat", image)
m.add_source("point", source)
m.add_layer(layer)
m
```

```{code-cell} ipython3
m = leafmap.Map(center=[-100, 40], zoom=3, style="positron")
image = "https://i.imgur.com/LmTETPX.png"
m.add_image(image=image, position="bottom-right")
m
```

```{code-cell} ipython3
m = leafmap.Map(center=[-100, 40], zoom=3, style="positron")
content = '<img src="https://i.imgur.com/LmTETPX.png">'
m.add_html(content, bg_color="transparent", position="bottom-right")
m
```

### Adding Text

```{code-cell} ipython3
m = leafmap.Map(center=[-100, 40], zoom=3, style="liberty")
text = "Hello World"
m.add_text(text, fontsize=20, position="bottom-right")
text2 = "Awesome Text!"
m.add_text(text2, fontsize=25, bg_color="rgba(255, 255, 255, 0.8)", position="top-left")
m
```

### Adding GIF

```{code-cell} ipython3
m = leafmap.Map(center=[-100, 40], zoom=3, style="positron")
image = "https://i.imgur.com/KeiAsTv.gif"
m.add_image(image=image, width=250, height=250, position="bottom-right")
text = "I love sloth!🦥"
m.add_text(text, fontsize=35, padding="20px")
image2 = "https://i.imgur.com/kZC2tpr.gif"
m.add_image(image=image2, bg_color="transparent", position="bottom-left")
m
```

### Adding HTML

```{code-cell} ipython3
m = leafmap.Map(center=[-100, 40], zoom=3, style="positron")
html = """
<html>
<style>
body {
  font-size: 20px;
}
</style>
<body>

<span style='font-size:100px;'>&#128640;</span>
<p>I will display &#128641;</p>
<p>I will display &#128642;</p>

</body>
</html>
"""
m.add_html(html, bg_color="transparent")
m
```

### Adding Color bar

```{code-cell} ipython3
import numpy as np
```

```{code-cell} ipython3
m = leafmap.Map(style="topo", height="500px")
dem = "https://github.com/opengeos/datasets/releases/download/raster/dem.tif"
m.add_cog_layer(
    dem,
    name="DEM",
    colormap_name="terrain",
    rescale="0, 1500",
    fit_bounds=True,
    nodata=np.nan,
)
m.add_colorbar(
    cmap="terrain", vmin=0, vmax=1500, label="Elevation (m)", position="bottom-right"
)
m.add_layer_control()
m
```

```{code-cell} ipython3
m = leafmap.Map(style="topo")
m.add_cog_layer(
    dem,
    name="DEM",
    colormap_name="terrain",
    rescale="0, 1500",
    nodata=np.nan,
    fit_bounds=True,
)
m.add_colorbar(
    cmap="terrain",
    vmin=0,
    vmax=1500,
    label="Elevation (m)",
    position="bottom-right",
    transparent=True,
)
m
```

```{code-cell} ipython3
m = leafmap.Map(style="topo")
m.add_cog_layer(
    dem,
    name="DEM",
    colormap_name="terrain",
    rescale="0, 1500",
    nodata=np.nan,
    fit_bounds=True,
)
m.add_colorbar(
    cmap="terrain",
    vmin=0,
    vmax=1500,
    label="Elevation (m)",
    position="bottom-right",
    width=0.2,
    height=3,
    orientation="vertical",
)
m
```

### Adding Legend

```{code-cell} ipython3
m = leafmap.Map(center=[-100, 40], zoom=3, style="positron", height="500px")
m.add_basemap("Esri.WorldImagery")
url = "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2021_Land_Cover_L48/wms"
layers = "NLCD_2021_Land_Cover_L48"
m.add_wms_layer(url, layers=layers, name="NLCD 2021")
m.add_legend(
    title="NLCD Land Cover Type",
    builtin_legend="NLCD",
    bg_color="rgba(255, 255, 255, 0.5)",
    position="bottom-left",
)
m
```

```{code-cell} ipython3
m = leafmap.Map(center=[-100, 40], zoom=3, style="positron")
m.add_basemap("Esri.WorldImagery")
url = "https://www.mrlc.gov/geoserver/mrlc_display/NLCD_2021_Land_Cover_L48/wms"
layers = "NLCD_2021_Land_Cover_L48"
m.add_wms_layer(url, layers=layers, name="NLCD 2021")

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
m.add_legend(
    title="NLCD Land Cover Type",
    legend_dict=legend_dict,
    bg_color="rgba(255, 255, 255, 0.5)",
    position="bottom-left",
)
m
```

### Adding Video

```{code-cell} ipython3
m = leafmap.Map(
    center=[-122.514426, 37.562984], zoom=17, bearing=-96, style="satellite"
)
urls = [
    "https://static-assets.mapbox.com/mapbox-gl-js/drone.mp4",
    "https://static-assets.mapbox.com/mapbox-gl-js/drone.webm",
]
coordinates = [
    [-122.51596391201019, 37.56238816766053],
    [-122.51467645168304, 37.56410183312965],
    [-122.51309394836426, 37.563391708549425],
    [-122.51423120498657, 37.56161849366671],
]
m.add_video(urls, coordinates)
m.add_layer_control()
m
```

```{code-cell} ipython3
m = leafmap.Map(center=[-115, 25], zoom=4, style="satellite")
urls = [
    "https://data.opengeos.org/patricia_nasa.mp4",
    "https://data.opengeos.org/patricia_nasa.webm",
]
coordinates = [
    [-130, 32],
    [-100, 32],
    [-100, 13],
    [-130, 13],
]
m.add_video(urls, coordinates)
m.add_layer_control()
m
```

## Visualizing PMTiles

### Building Footprint Data

```{code-cell} ipython3
url = "https://data.source.coop/vida/google-microsoft-open-buildings/pmtiles/go_ms_building_footprints.pmtiles"
metadata = leafmap.pmtiles_metadata(url)
print(f"layer names: {metadata['layer_names']}")
print(f"bounds: {metadata['bounds']}")
```

```{code-cell} ipython3
m = leafmap.Map(center=[0, 20], zoom=2)
m.add_basemap("Esri.WorldImagery", visible=False)

style = {
    "version": 8,
    "sources": {
        "example_source": {
            "type": "vector",
            "url": "pmtiles://" + url,
            "attribution": "PMTiles",
        }
    },
    "layers": [
        {
            "id": "buildings",
            "source": "example_source",
            "source-layer": "building_footprints",
            "type": "fill",
            "paint": {"fill-color": "#3388ff", "fill-opacity": 0.5},
        },
    ],
}

# style = leafmap.pmtiles_style(url)  # Use default style

m.add_pmtiles(
    url,
    style=style,
    visible=True,
    opacity=1.0,
    tooltip=True,
)
m
```

### Fields of The World

```{code-cell} ipython3
url = "https://data.source.coop/kerner-lab/fields-of-the-world/ftw-sources.pmtiles"
metadata = leafmap.pmtiles_metadata(url)
print(f"layer names: {metadata['layer_names']}")
print(f"bounds: {metadata['bounds']}")
```

```{code-cell} ipython3
m = leafmap.Map()
# Define colors for each last digit (0-9)
style = {
    "layers": [
        {
            "id": "Field Polygon",
            "source": "example_source",
            "source-layer": "ftw-sources",
            "type": "fill",
            "paint": {
                "fill-color": [
                    "case",
                    ["==", ["%", ["to-number", ["get", "id"]], 10], 0],
                    "#FF5733",  # Color for last digit 0
                    ["==", ["%", ["to-number", ["get", "id"]], 10], 1],
                    "#33FF57",  # Color for last digit 1
                    ["==", ["%", ["to-number", ["get", "id"]], 10], 2],
                    "#3357FF",  # Color for last digit 2
                    ["==", ["%", ["to-number", ["get", "id"]], 10], 3],
                    "#FF33A1",  # Color for last digit 3
                    ["==", ["%", ["to-number", ["get", "id"]], 10], 4],
                    "#FF8C33",  # Color for last digit 4
                    ["==", ["%", ["to-number", ["get", "id"]], 10], 5],
                    "#33FFF6",  # Color for last digit 5
                    ["==", ["%", ["to-number", ["get", "id"]], 10], 6],
                    "#A833FF",  # Color for last digit 6
                    ["==", ["%", ["to-number", ["get", "id"]], 10], 7],
                    "#FF333D",  # Color for last digit 7
                    ["==", ["%", ["to-number", ["get", "id"]], 10], 8],
                    "#33FFBD",  # Color for last digit 8
                    ["==", ["%", ["to-number", ["get", "id"]], 10], 9],
                    "#FF9933",  # Color for last digit 9
                    "#FF0000",  # Fallback color if no match
                ],
                "fill-opacity": 0.5,
            },
        },
        {
            "id": "Field Outline",
            "source": "example_source",
            "source-layer": "ftw-sources",
            "type": "line",
            "paint": {"line-color": "#ffffff", "line-width": 1, "line-opacity": 1},
        },
    ],
}

m.add_basemap("Esri.WorldImagery")
m.add_pmtiles(url, style=style, name="FTW", zoom_to_layer=False)
m.add_layer_control()
m
```

### 3D PMTiles

```{code-cell} ipython3
url = "https://data.source.coop/cholmes/overture/overture-buildings.pmtiles"
metadata = leafmap.pmtiles_metadata(url)
print(f"layer names: {metadata['layer_names']}")
print(f"bounds: {metadata['bounds']}")
```

### 3D Buildings

```{code-cell} ipython3
m = leafmap.Map(
    center=[-74.0095, 40.7046], zoom=16, pitch=60, bearing=-17, style="positron", height="500px"
)
m.add_basemap("Esri.WorldImagery", visible=False)
m.add_overture_3d_buildings(template="simple")
m.add_layer_control()
m
```

### 2D Buildings, Transportation, and Other Themes

```{code-cell} ipython3
m = leafmap.Map(center=[-74.0095, 40.7046], zoom=16)
m.add_basemap("Esri.WorldImagery", visible=False)
m.add_overture_data(theme="buildings", opacity=0.8)
m.add_layer_control()
m
```

```{code-cell} ipython3
m = leafmap.Map(center=[-74.0095, 40.7046], zoom=16)
m.add_basemap("Esri.WorldImagery", visible=False)
m.add_overture_data(theme="transportation", opacity=0.8)
m.add_layer_control()
m
```

```{code-cell} ipython3
m = leafmap.Map(center=[-74.0095, 40.7046], zoom=16)
m.add_basemap("Esri.WorldImagery", visible=False)
m.add_overture_data(theme="places", opacity=0.8)
m.add_layer_control()
m
```

```{code-cell} ipython3
m = leafmap.Map(center=[-74.0095, 40.7046], zoom=16)
m.add_basemap("Esri.WorldImagery", visible=False)
m.add_overture_data(theme="addresses", opacity=0.8)
m.add_layer_control()
m
```

```{code-cell} ipython3
m = leafmap.Map(center=[-74.0095, 40.7046], zoom=16)
m.add_basemap("Esri.WorldImagery", visible=False)
m.add_overture_data(theme="base", opacity=0.8)
m.add_layer_control()
m
```

```{code-cell} ipython3
m = leafmap.Map()
m.add_basemap("Esri.WorldImagery", visible=False)
m.add_overture_data(theme="divisions", opacity=0.8)
m.add_layer_control()
m
```

## Adding DeckGL Layers

### Single DeckGL Layer

```{code-cell} ipython3
m = leafmap.Map(
    style="positron",
    center=(-122.4, 37.74),
    zoom=12,
    pitch=40,
)
deck_grid_layer = {
    "@@type": "GridLayer",
    "id": "GridLayer",
    "data": "https://raw.githubusercontent.com/visgl/deck.gl/master/examples/layer-browser/data/sf.bike.parking.json",
    "extruded": True,
    "getPosition": "@@=COORDINATES",
    "getColorWeight": "@@=SPACES",
    "getElevationWeight": "@@=SPACES",
    "elevationScale": 4,
    "cellSize": 200,
    "pickable": True,
}

m.add_deck_layers([deck_grid_layer], tooltip="Number of points: {{ count }}")
m
```

### Multiple DeckGL Layers

```{code-cell} ipython3
url = "https://d2ad6b4ur7yvpq.cloudfront.net/naturalearth-3.3.0/ne_10m_airports.geojson"
data = leafmap.read_geojson(url)
```

```{code-cell} ipython3
m = leafmap.Map(
    style="positron",
    center=(0.45, 51.47),
    zoom=4,
    pitch=30,
)
deck_geojson_layer = {
    "@@type": "GeoJsonLayer",
    "id": "airports",
    "data": data,
    "filled": True,
    "pointRadiusMinPixels": 2,
    "pointRadiusScale": 2000,
    "getPointRadius": "@@=11 - properties.scalerank",
    "getFillColor": [200, 0, 80, 180],
    "autoHighlight": True,
    "pickable": True,
}

deck_arc_layer = {
    "@@type": "ArcLayer",
    "id": "arcs",
    "data": [
        feature
        for feature in data["features"]
        if feature["properties"]["scalerank"] < 4
    ],
    "getSourcePosition": [-0.4531566, 51.4709959],  # London
    "getTargetPosition": "@@=geometry.coordinates",
    "getSourceColor": [0, 128, 200],
    "getTargetColor": [200, 0, 80],
    "getWidth": 2,
    "pickable": True,
}

m.add_deck_layers(
    [deck_geojson_layer, deck_arc_layer],
    tooltip={
        "airports": "{{ &properties.name }}",
        "arcs": "gps_code: {{ properties.gps_code }}",
    },
)
m
```

## Exporting to HTML

```{code-cell} ipython3
# import os
# os.environ["MAPTILER_KEY"] = "YOUR_PRIVATE_API_KEY"
# os.environ["MAPTILER_KEY_PUBLIC"] = "YOUR_PUBLIC_API_KEY"
```

```{code-cell} ipython3
m = leafmap.Map(
    center=[-122.19861, 46.21168], zoom=13, pitch=60, bearing=150, style="3d-terrain"
)
m.add_layer_control(bg_layers=True)
m.to_html(
    "terrain.html",
    title="Awesome 3D Map",
    width="100%",
    height="100%",
    replace_key=True,
)
m
```

## Key Takeaways

## Exercises

### Exercise 1: Setting up MapLibre and Basic Map Creation

```{code-cell} ipython3

```

### Exercise 2: Customizing the Map View

```{code-cell} ipython3

```

### Exercise 3: Adding Map Controls

```{code-cell} ipython3

```

### Exercise 4: Overlaying Data Layers

```{code-cell} ipython3

```

### Exercise 5: Working with 3D Buildings

```{code-cell} ipython3

```

### Exercise 6: Adding Map Elements

```{code-cell} ipython3

```
