---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.2
kernelspec:
  display_name: Bash
  language: bash
  name: bash
---
# Geospatial Data Processing with GDAL and OGR

## Introduction

### When to Use GDAL Directly

## Learning Objectives

## Installation and Setup

```bash
conda install -c conda-forge gdal pygis
```

## Sample Datasets

```{code-cell}
wget https://github.com/opengeos/datasets/releases/download/gdal/gdal_sample_data.zip
```

```{code-cell}
unzip gdal_sample_data.zip
```

## Understanding Your Data

### Examining Raster Data

```{code-cell}
gdalinfo dem.tif
```

### Examining Vector Data

```{code-cell}
ogrinfo buildings.geojson
```

```{code-cell}
ogrinfo buildings.geojson -al -so
```

## Coordinate Transformation

### Reprojecting Raster Data

```{code-cell}
gdalwarp -t_srs EPSG:4326 dem.tif dem_4326.tif
```

### Reprojecting Vector Data

```{code-cell}
ogr2ogr -t_srs EPSG:3857 buildings_3857.gpkg buildings.geojson
```

## Format Conversion

### Converting Raster Formats

```{code-cell}
gdal_translate dem.tif dem.img
```

### Converting Vector Formats

```{code-cell}
ogr2ogr buildings.gpkg buildings.geojson
```

```{code-cell}
ogr2ogr las_vegas_bbox.fgb las_vegas_bbox.geojson
```

## Clipping and Masking

### Clipping Raster with Vector Boundaries

```{code-cell}
gdalwarp -cutline las_vegas_bbox.geojson -crop_to_cutline landsat.tif las_vegas.tif
```

### Clipping Vector Data

```{code-cell}
ogr2ogr -clipsrc las_vegas_bbox.geojson las_vegas_roads_clipped.geojson las_vegas_roads.geojson
```

```{code-cell}
ogrinfo las_vegas_bbox_4326.geojson -al -so
```

```{code-cell}
ogr2ogr -clipsrc -115.387634 35.943333 -114.883495 36.359161 las_vegas_roads_clipped.geojson las_vegas_roads.geojson
```

## Raster Analysis and Calculations

### Working with Individual Bands

```{code-cell}
gdal_translate -b 5 landsat.tif nir.tif
gdal_translate -b 4 landsat.tif red.tif
gdal_translate -b 3 landsat.tif green.tif
```

### Performing Band Mathematics

```{code-cell}
gdal_calc.py \
  -A nir.tif \
  -B red.tif \
  --outfile=ndvi.tif \
  --calc="(A.astype(float) - B) / (A + B + 1e-6)" \
  --type=Float32 \
  --NoDataValue=-9999
```

```{code-cell}
gdal_calc.py \
  -A ndvi.tif \
  --outfile=ndvi_clipped.tif \
  --calc="(A < -1)*-1 + (A > 1)*1 + ((A >= -1) * (A <= 1))*A" \
  --type=Float32 \
  --NoDataValue=-9999 \
  --overwrite
```

```{code-cell}
gdal_calc.py -A ndvi_clipped.tif --outfile=vegetation.tif --calc="A>0.3"
```

```{code-cell}
gdal_translate -a_nodata 0 vegetation.tif vegetation_bin.tif
```

```{code-cell}
gdal_edit.py -a_nodata 0 vegetation.tif
```

## Converting Between Raster and Vector

### Vectorization

```{code-cell}
gdal_polygonize.py building_masks.tif building_masks.gpkg
```

### Rasterization

```{code-cell}
gdal_rasterize -a uid -tr 0.6 0.6 -l buildings buildings_3857.gpkg buildings.tif
```

```{code-cell}
gdal_rasterize -burn 1 -tr 0.6 0.6 -l buildings buildings_3857.gpkg buildings2.tif
```

## Geometry Processing

### Simplifying Complex Geometries

```{code-cell}
ogr2ogr -f GPKG -t_srs EPSG:26911 -simplify 1 simplified.gpkg building_masks.gpkg
```

### Dissolving Features by Attributes

```{code-cell}
ogrinfo -al -so us_states.geojson
```

```{code-cell}
ogr2ogr -dialect sqlite -sql "SELECT ST_Union(geometry), country FROM us_states GROUP BY country" us_states_dissolved.gpkg us_states.geojson
```

### Exploding Multi-part Geometries

```{code-cell}
ogr2ogr -explodecollections hawaii_parts.geojson hawaii.geojson
```

## Managing Fields and Layers

### Selecting Specific Fields

```{code-cell}
ogr2ogr -select id,name us_states_select.geojson us_states.geojson
```

### Renaming Layers

```{code-cell}
ogr2ogr -nln states us_states_rename.gpkg us_states_select.geojson
```

### Adding New Fields

```{code-cell}
ogrinfo us_states_rename.gpkg -sql "ALTER TABLE states ADD COLUMN area DOUBLE"
```

## Tiling and Data Management

### Creating Raster Tiles

```{code-cell}
mkdir -p tiles
```

```{code-cell}
gdal_retile.py -targetDir tiles -ps 512 512 -co "TILED=YES" landsat.tif
```

### Merging Raster Data

```{code-cell}
gdal_merge.py -o landsat_merged.tif -of GTiff tiles/*.tif
```

```{code-cell}
gdalwarp -of GTiff tiles/*.tif landsat_merged2.tif
```

### Working with Multiple Vector Files

```{code-cell}
mkdir -p states
```

```{code-cell}
ogrinfo -ro -al -geom=NO us_states.geojson | grep "id (" | awk '{print $4}' | while read id; do
    ogr2ogr -f GeoJSON "states/${id}.geojson" us_states.geojson -where "id = '${id}'"
done
```

```{code-cell}
ogr2ogr -f "ESRI Shapefile" us_states_merged.shp us_states.geojson
```

```{code-cell}
ogr2ogr -f "ESRI Shapefile" -update -append \
  us_states_merged.shp hawaii.geojson -nln us_states_merged
```

## Advanced Raster Processing

### Resampling and Resolution Management

```{code-cell}
gdalwarp -tr 100 100 -r average dem.tif dem_100m.tif
```

### Creating Band Composites

```{code-cell}
gdal_merge.py -separate -o composite.tif nir.tif red.tif green.tif
```

```{code-cell}
gdalbuildvrt -separate stack.vrt nir.tif red.tif green.tif
gdal_translate stack.vrt composite.tif -co COMPRESS=DEFLATE
```

### Handling Missing Data

```{code-cell}
gdal_fillnodata.py -md 5 -of GTiff dem.tif filled_dem.tif
```

```{code-cell}
gdal_translate -a_nodata 0 dem.tif dem_nodata.tif
```

### Cloud Optimized GeoTIFF

```{code-cell}
gdal_translate dem.tif dem_cog.tif -of COG -co COMPRESS=DEFLATE
```

## Terrain Analysis

### Computing Slope

```{code-cell}
gdaldem slope dem.tif slope.tif \
  -of GTiff \
  -compute_edges
```

```{code-cell}
gdaldem slope dem.tif slope_percent.tif \
  -of GTiff \
  -compute_edges \
  -p
```

### Computing Aspect

```{code-cell}
gdaldem aspect dem.tif aspect.tif \
  -of GTiff \
  -compute_edges
```

### Creating Hillshade Visualizations

```{code-cell}
gdaldem hillshade dem.tif hillshade.tif
```

```{code-cell}
gdaldem hillshade dem.tif multidirectional_hillshade.tif -multidirectional
```

### Creating Color Relief Maps

```{code-cell}
cat << EOF > colormap.txt
500,51,51,153
1000,3,147,249
1500,37,211,109
2000,181,240,138
2500,218,208,133
3000,146,115,94
4000,183,163,159
5000,255,255,255
EOF
```

```{code-cell}
gdaldem color-relief dem.tif colormap.txt color_relief.tif
```

### Combining Hillshade and Color Relief

```{code-cell}
gdal_calc.py \
  -A color_relief.tif \
  -B hillshade.tif \
  --outfile=shaded_relief.tif \
  --calc="((A.astype(float) * 0.6) + (B.astype(float) * 0.4))" \
  --type=Byte
```

```{code-cell}
gdal_calc.py \
  -A color_relief.tif \
  -B hillshade.tif \
  --outfile=color_hillshade.tif \
  --calc="A * (B / 255.0)" \
  --type=Byte
```

```{code-cell}
gdal_calc.py -A color_relief.tif --A_band=1 -B hillshade.tif --outfile=r.tif --calc="A*(B/255.0)" --type=Byte
gdal_calc.py -A color_relief.tif --A_band=2 -B hillshade.tif --outfile=g.tif --calc="A*(B/255.0)" --type=Byte
gdal_calc.py -A color_relief.tif --A_band=3 -B hillshade.tif --outfile=b.tif --calc="A*(B/255.0)" --type=Byte
```

```{code-cell}
gdal_merge.py -separate -o color_shaded_relief.tif r.tif g.tif b.tif
```

### Generating Contour Lines

```{code-cell}
gdal_contour -i 100 dem.tif contours.shp
```

## Key Takeaways

## References and Further Reading

## Exercises

### Exercise 1: Data Inspection and Understanding

```{code-cell}

```

### Exercise 2: Coordinate Transformation Practice

```{code-cell}

```

### Exercise 3: Format Conversion and Optimization

```{code-cell}

```

### Exercise 4: Spatial Clipping and Analysis

```{code-cell}

```

### Exercise 5: Raster Band Mathematics

```{code-cell}

```

### Exercise 6: Terrain Analysis Workflow

```{code-cell}

```

### Exercise 7: Raster-Vector Conversion

```{code-cell}

```

### Exercise 8: Geometry Processing and Data Management

```{code-cell}

```
