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
# Distributed Computing with Apache Sedona

## Introduction

## Learning Objectives

## Installing and Setting Up Apache Sedona

### Installation Requirements

```bash
docker run -it -p 8888:8888 -p 4040:4040 -p 8080:8080 -p 8082:8081 -p 7077:7077 -p 8085:8085 -v $(pwd):/app/workspace giswqs/pygis:sedona
```

### Core Imports and Configuration

```{code-cell} ipython3
import leafmap
import geopandas as gpd
import pandas as pd
from sedona.spark import *
from pyspark.sql.functions import col, expr
```

### Creating a Sedona-Enabled Spark Session

```{code-cell} ipython3
config = (
    SedonaContext.builder()
    .appName("SedonaApp")  # Application name for tracking in Spark UI
    .config(
        "spark.serializer", "org.apache.spark.serializer.KryoSerializer"
    )  # Faster serialization
    .config(
        "spark.kryo.registrator", "org.apache.sedona.core.serde.SedonaKryoRegistrator"
    )  # Spatial object serialization
    .config(
        "spark.jars.packages",
        "org.apache.sedona:sedona-spark-shaded-3.5_2.12:1.7.2,org.datasyslab:geotools-wrapper:1.7.2-28.5",
    )  # Core Sedona packages
    .config(
        "spark.jars.repositories",
        "https://artifacts.unidata.ucar.edu/repository/unidata-all",
    )  # Additional repositories
    .config(
        "spark.hadoop.fs.s3a.connection.ssl.enabled", "true"
    )  # Enable SSL for S3 connections
    .config(
        "spark.hadoop.fs.s3a.path.style.access", "true"
    )  # Use path-style access for S3
    .config(
        "spark.hadoop.fs.s3a.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem"
    )  # S3 filesystem implementation
    .config(
        "spark.hadoop.fs.s3a.aws.credentials.provider",
        "org.apache.hadoop.fs.s3a.AnonymousAWSCredentialsProvider",
    )  # Anonymous access to public S3 buckets
    .getOrCreate()
)

# Create the Sedona context which adds spatial capabilities to the Spark session
sedona = SedonaContext.create(config)
```

## Downloading Sample Data

```{code-cell} ipython3
url = (
    "https://github.com/opengeos/datasets/releases/download/book/sedona-sample-data.zip"
)
leafmap.download_file(url)
```

## Core Concepts and Data Structures

### Understanding Spatial DataFrames

### Spatial Data Types

### Creating Spatial DataFrames

```{code-cell} ipython3
# Create sample city data with coordinates for major US cities
cities_data = [
    ("New York", 40.7128, -74.0060),
    ("Los Angeles", 34.0522, -118.2437),
    ("Chicago", 41.8781, -87.6298),
    ("Houston", 29.7604, -95.3698),
    ("Phoenix", 33.4484, -112.0740),
]

# Convert to Spark DataFrame - this creates a distributed dataset
cities_df = sedona.createDataFrame(
    data=cities_data, schema=["city", "latitude", "longitude"]
)

# Create geometry column using ST_Point function - this transforms coordinates into spatial objects
cities_spatial = cities_df.withColumn("geometry", expr("ST_Point(longitude, latitude)"))

# Display the resulting spatial DataFrame
cities_spatial.show(truncate=False)
```

### Working with Real Geospatial Data

```{code-cell} ipython3
# Load NYC boroughs GeoJSON using GeoPandas for initial processing
boroughs_gdf = gpd.read_file("nybb.geojson")

# Reproject from New York State Plane (EPSG:2263) to Albers Equal Area (EPSG:5070)
# This ensures accurate area calculations for our later analysis
boroughs_gdf = boroughs_gdf.to_crs("EPSG:5070")
boroughs_gdf
```

```{code-cell} ipython3
# Convert to Pandas DataFrame and extract WKT (Well-Known Text) representation of geometries
boroughs_pd = pd.DataFrame(boroughs_gdf.drop(columns="geometry"))
boroughs_pd["wkt_geometry"] = boroughs_gdf.geometry.to_wkt()

# Create Spark DataFrame from the Pandas DataFrame
boroughs_df = sedona.createDataFrame(boroughs_pd)

# Convert WKT strings back to spatial geometry objects using Sedona's ST_GeomFromWKT function
boroughs_spatial = boroughs_df.withColumn(
    "geometry", expr("ST_GeomFromWKT(wkt_geometry)")
)

# Display the key columns of our spatial DataFrame
boroughs_spatial.select("BoroCode", "BoroName", "geometry").show()
```

## Spatial Operations and Functions

### Basic Geometric Properties

```{code-cell} ipython3
# Calculate geometric properties for each borough
boroughs_with_metrics = (
    boroughs_spatial.withColumn(
        "area_km2", expr("ROUND(ST_Area(geometry) / 1e6, 2)")
    )  # Convert from m² to km²
    .withColumn(
        "perimeter_km", expr("ROUND(ST_Perimeter(geometry) / 1000, 2)")
    )  # Convert from m to km
    .withColumn("centroid", expr("ST_Centroid(geometry)"))  # Calculate geometric center
)

# Display the calculated metrics
boroughs_with_metrics.select("BoroName", "area_km2", "perimeter_km", "centroid").show()
```

### Distance Calculations

```{code-cell} ipython3
# Transform city coordinates from geographic (EPSG:4326) to projected (EPSG:5070) coordinate system
# This is essential for accurate distance calculations in linear units (meters)
cities_projected = cities_spatial.withColumn(
    "geometry", expr("ST_Transform(geometry, 'EPSG:4326', 'EPSG:5070')")
)

# View the transformed coordinates
cities_projected.show(truncate=False)
```

```{code-cell} ipython3
# Calculate distances from each city to Manhattan's centroid
# First, extract Manhattan's centroid as a reference point
manhattan_centroid = (
    boroughs_spatial.filter(col("BoroName") == "Manhattan")
    .select(expr("ST_Centroid(geometry)").alias("manhattan_center"))
    .collect()[0][0]  # collect() brings the result to the driver node
)

# Create a new DataFrame with distance calculations
cities_with_distances = (
    cities_projected.withColumn(
        "manhattan_center",
        expr(
            f"ST_GeomFromWKT('{manhattan_centroid.wkt}')"
        ),  # Add Manhattan center as reference
    )
    .withColumn(
        "distance_to_manhattan_meters",
        expr("ST_Distance(geometry, manhattan_center)"),  # Calculate distance in meters
    )
    .withColumn(
        "distance_to_manhattan_km",
        expr(
            "ROUND(ST_Distance(geometry, manhattan_center) / 1000, 2)"
        ),  # Convert to kilometers and round
    )
)

# Display results ordered by distance (closest first)
cities_with_distances.select("city", "distance_to_manhattan_km").orderBy(
    "distance_to_manhattan_km"
).show()
```

### Spatial Relationships

```{code-cell} ipython3
# Create a 5-kilometer buffer around Manhattan's boundary
manhattan_with_buffer = boroughs_spatial.filter(
    col("BoroName") == "Manhattan"
).withColumn(
    "buffer_5km", expr("ST_Buffer(geometry, 5000)")  # 5000 meters = 5km buffer
)

# Perform spatial join to find cities within the buffer zone
cities_in_buffer = (
    cities_projected.crossJoin(
        manhattan_with_buffer.select("buffer_5km")
    )  # Cross join to compare all cities with the buffer
    .withColumn(
        "within_buffer", expr("ST_Within(geometry, buffer_5km)")
    )  # Test if city point is within buffer
    .filter(col("within_buffer") == True)  # Keep only cities that are within the buffer
)

# Display cities that fall within the 5km buffer of Manhattan
cities_in_buffer.select("city").show()
```

## Spatial Joins and Indexing

### Understanding Spatial Join Types

### Performing Spatial Joins with World Cities

```{code-cell} ipython3
world_cities_pd = pd.read_csv("world_cities.csv")
world_cities_pd.head()
```

```{code-cell} ipython3
# Convert Pandas DataFrame to Spark DataFrame for distributed processing
world_cities_df = sedona.createDataFrame(world_cities_pd)

# Create spatial point geometries from longitude and latitude columns
world_cities_spatial = world_cities_df.withColumn(
    "geometry", expr("ST_Point(longitude, latitude)")
)

# Display sample data showing the spatial DataFrame structure
world_cities_spatial.show(10)
```

### Spatial Join Example: Cities by Country

```{code-cell} ipython3
# Create simplified country boundaries for demonstration
# In production, you would load actual country boundary data from sources like Natural Earth
sample_countries = [
    (
        "Australia",
        "POLYGON ((112 -44, 112 -10, 154 -10, 154 -44, 112 -44))",
    ),  # Simplified Australia bbox
    (
        "UK",
        "POLYGON ((-8.65 49.9, -8.65 60.9, 1.75 60.9, 1.75 49.9, -8.65 49.9))",
    ),  # Simplified UK bbox
]

# Create DataFrame with country boundaries
countries_df = sedona.createDataFrame(sample_countries, schema=["country", "wkt"])
countries_spatial = countries_df.withColumn("geometry", expr("ST_GeomFromWKT(wkt)"))

# Perform spatial join to find cities within country boundaries
# This operation tests each city point against each country polygon
cities_in_countries = world_cities_spatial.alias("cities").join(
    countries_spatial.alias("countries"),
    expr(
        "ST_Within(cities.geometry, countries.geometry)"
    ),  # Spatial predicate: city within country
    "inner",  # Only keep cities that are within a country boundary
)
cities_in_countries.show()
```

```{code-cell} ipython3
# Aggregate cities by country to get summary statistics
city_counts = cities_in_countries.groupBy("countries.country").count()
city_counts.show()
```

## Advanced Spatial Analysis

### Spatial Aggregations

```{code-cell} ipython3
# Perform spatial and statistical aggregations on North American cities
country_unions = (
    world_cities_spatial.filter(
        col("country").isin(
            ["USA", "CAN", "MEX"]
        )  # Filter for North American countries
    )
    .groupBy("country")
    .agg(
        expr("ST_Union_Aggr(geometry)").alias(
            "union_geometry"
        ),  # Create union of all city points per country
        expr("COUNT(*)").alias("city_count"),  # Count cities per country
        expr("CAST(AVG(population) AS INT)").alias(
            "avg_population"
        ),  # Calculate average population per country
    )
)

country_unions.show()
```

### Spatial Clustering Analysis

```{code-cell} ipython3
# Create a 2-degree geographic grid for clustering analysis
grid_analysis = (
    world_cities_spatial.filter(
        col("population") > 100000
    )  # Focus on major cities only
    .withColumn(
        "grid_x", expr("floor(longitude / 2) * 2")
    )  # Create 2-degree longitude grid cells
    .withColumn(
        "grid_y", expr("floor(latitude / 2) * 2")
    )  # Create 2-degree latitude grid cells
    .groupBy("grid_x", "grid_y")  # Group cities by grid cell
    .agg(
        expr("COUNT(*)").alias("city_count"),  # Count cities in each grid cell
        expr("SUM(population)").alias(
            "total_population"
        ),  # Sum population in each grid cell
        expr("ST_Centroid(ST_Union_Aggr(geometry))").alias(
            "grid_center"
        ),  # Calculate center of city cluster
    )
)

# Identify and display high-density urban clusters
high_density_grids = grid_analysis.filter(
    col("city_count") >= 5
)  # Grid cells with 5+ major cities
high_density_grids.orderBy(col("city_count").desc()).show()
```

## Reading Vector Data

### Reading CSV

```{code-cell} ipython3
# Read CSV file and create spatial geometries from coordinate columns
cities_df = (
    sedona.read.option("header", True)  # CSV has header row
    .format("CSV")
    .load("world_cities.csv")
    .withColumn(
        "geometry", expr("ST_Point(longitude, latitude)")
    )  # Create point geometries from coords
)
cities_df.show()
```

### Reading GeoJSON

```{code-cell} ipython3
# Read GeoJSON file - initial structure shows nested format
cables_df = sedona.read.format("geojson").load("cables.geojson")
cables_df.printSchema()
```

```{code-cell} ipython3
# Flatten GeoJSON structure for easier analysis
cables_df = (
    sedona.read.format("geojson")
    .load("cables.geojson")
    .selectExpr("explode(features) as features")  # Expand the features array
    .select("features.*")  # Select all fields from features
    .withColumn("id", expr("properties['id']"))  # Extract property fields
    .withColumn("name", expr("properties['name']"))
    .withColumn("color", expr("properties['color']"))
    .drop("properties")  # Remove nested properties object
    .drop("type")  # Remove type field
)
cables_df.show(5)
```

### Reading Shapefiles

```{code-cell} ipython3
# Read shapefile directly into spatial DataFrame
countries_df = sedona.read.format("shapefile").load("countries.shp")
countries_df.show()
```

### Reading GeoPackage

```{code-cell} ipython3
# Read specific table from GeoPackage file
countries_df = (
    sedona.read.format("geopackage")
    .option("tableName", "countries")  # Specify the table/layer name
    .load("countries.gpkg")
)
countries_df.show()
```

### Reading GeoParquet

```{code-cell} ipython3
# Read GeoParquet files - optimized for large datasets
states_df = sedona.read.format("geoparquet").load("us_states.parquet")
states_df.show()
```

```{code-cell} ipython3
# GeoParquet is excellent for point datasets like cities
us_cities_df = sedona.read.format("geoparquet").load("us_cities.parquet")
us_cities_df.show()
```

### Reading Cloud-Stored Data

```{code-cell} ipython3
# Read individual state wetlands data from S3 (DC wetlands - smaller dataset for demonstration)
url = "s3a://us-west-2.opendata.source.coop/giswqs/nwi/wetlands/DC_Wetlands.parquet"
df = sedona.read.format("parquet").load(url)
```

```{code-cell} ipython3
# Display basic information about the dataset
df.show()
```

```{code-cell} ipython3
# Convert WKB geometry to readable WKT format for inspection
df_wkt = df.withColumn("geometry", expr("ST_AsText(ST_GeomFromWKB(geometry))"))
df_wkt.show()
```

```{code-cell} ipython3
# Read all state wetlands data using wildcard pattern (75.8 GB total)
url = "s3a://us-west-2.opendata.source.coop/giswqs/nwi/wetlands/*.parquet"
df = sedona.read.format("parquet").load(url)
```

```{code-cell} ipython3
# Count total wetland features across all states
# This operation may take several minutes due to the dataset size
df.count()
```

## Visualizing Vector Data

### Using KeplerGL

```{code-cell} ipython3
# Configure the initial map view for global data
config = {
    "mapState": {
        "latitude": 20,  # Center latitude
        "longitude": 0,  # Center longitude (prime meridian)
        "zoom": 1,  # Global zoom level
        "pitch": 0,  # Map tilt angle
        "bearing": 0,  # Map rotation
    },
}
# Create initial map with cities data
m = SedonaKepler.create_map(cities_df, name="Cities", config=config)
```

```{code-cell} ipython3
# Add additional layer to the existing map
SedonaKepler.add_df(m, countries_df, name="Countries")
```

```{code-cell} ipython3
# Display the interactive map
m
```

### Using PyDeck

```{code-cell} ipython3
# Create 3D geometry visualization for country boundaries
m = SedonaPyDeck.create_geometry_map(countries_df)
m
```

```{code-cell} ipython3
# Create scatterplot visualization for cities with custom point size
m = SedonaPyDeck.create_scatterplot_map(cities_df, radius_min_pixels=3)
m
```

## Writing Vector Data

```{code-cell} ipython3
# Load the wetlands data for processing
url = "s3a://us-west-2.opendata.source.coop/giswqs/nwi/wetlands/DC_Wetlands.parquet"
df = sedona.read.format("parquet").load(url)
df.show()
```

```{code-cell} ipython3
# Convert WKB geometry to Sedona geometry objects for spatial operations
df = df.withColumn("geometry", expr("ST_GeomFromWKB(geometry)"))
```

```{code-cell} ipython3
# Write to GeoParquet format with optimized partitioning
# Repartitioning to 10 partitions creates 10 output files for better performance
df.repartition(10).write.format("geoparquet").mode("overwrite").save("DE_Wetlands")
```

```{code-cell} ipython3
# Write to GeoJSON format for compatibility with web applications
# GeoJSON is widely supported but less efficient for large datasets
df.write.format("geojson").mode("overwrite").save("DE_Wetlands_GeoJSON")
```

## Reading Raster Data

### Reading NetCDF

```{code-cell} ipython3
# Load NetCDF file as binary data
df = sedona.read.format("binaryFile").load("wind_global.nc")

# Extract metadata information to understand the file structure
record_info_df = df.selectExpr("RS_NetCDFInfo(content) as record_info")

# Display metadata about variables, dimensions, and attributes
record_info = record_info_df.first()["record_info"]
print(record_info)
```

```{code-cell} ipython3
# Extract the u_wind variable as a raster using lon/lat coordinates
df = df.withColumn("raster", expr("RS_FromNetCDF(content, 'u_wind', 'lon', 'lat')"))
df.show()
```

### Reading GeoTIFF

```{code-cell} ipython3
dem_df = sedona.read.format("binaryFile").load("dem_90m.tif")
dem_df = dem_df.withColumn("raster", expr("RS_FromGeoTiff(content)"))
```

```{code-cell} ipython3
dem_df.show()
```

```{code-cell} ipython3
# Create a temporary view to enable SQL operations on the raster data
dem_df.createOrReplaceTempView("dem_df")
```

```{code-cell} ipython3
# Tile the raster into 256x256 pixel chunks for distributed processing
tiles_df = dem_df.selectExpr("RS_TileExplode(raster, 256, 256) as (x, y, raster)")
```

```{code-cell} ipython3
# Display the tiled dataset - each row represents one tile
tiles_df.show()
```

## Visualizing Raster Data

```{code-cell} ipython3
# Convert raster data to image format for visualization
htmlDF = dem_df.selectExpr("RS_AsImage(raster, 1000) as raster_image")
SedonaUtils.display_image(htmlDF)
```

## Raster Map Algebra

```{code-cell} ipython3
dem_df.printSchema()
```

```{code-cell} ipython3
dem_df.createOrReplaceTempView("dem_df")
```

```{code-cell} ipython3
# Create binary mask for areas above 2000m elevation using map algebra
mountain = sedona.sql(
    """
SELECT
  RS_MapAlgebra(
    raster,
    'D',
    'out = (rast[0] > 2000) ? 1 : 0;'
  ) AS mountain
FROM dem_df
"""
)
```

```{code-cell} ipython3
# Display the results of the map algebra operation
mountain.show()
```

```{code-cell} ipython3
# Visualize the binary mountain mask
htmlDF = mountain.selectExpr("RS_AsImage(mountain, 1000) as raster_image")
SedonaUtils.display_image(htmlDF)
```

```{code-cell} ipython3
# Save the mountain classification raster as a GeoTIFF file
mountain.withColumn("raster_binary", expr("RS_AsGeoTiff(mountain)")).write.format(
    "raster"
).option("rasterField", "raster_binary").option("fileExtension", ".tiff").mode(
    "overwrite"
).save(
    "mountain"
)
```

## Raster Zonal Statistics

```{code-cell} ipython3
# Display the elevation raster structure for reference
dem_df.show()
```

```{code-cell} ipython3
# Define a polygon representing a study area in the Sierra Nevada mountains
polygon = "POLYGON((-119.715885 37.995326, -118.452104 37.995326, -118.452104 37.373679, -119.715885 37.373679, -119.715885 37.995326))"
```

```{code-cell} ipython3
# Calculate average elevation within the study area polygon
mount_elev = sedona.sql(
    f"""
select
RS_ZonalStats(dem_df.raster, ST_Transform(
    ST_GeomFromText('{polygon}'), 'EPSG:4326', 'EPSG:3857'
    ), 1, 'avg', false, false) as avg_elev
from dem_df
"""
)
```

```{code-cell} ipython3
# Display the calculated average elevation
mount_elev.show()
```

## Writing Raster Data

```{code-cell} ipython3
# Write the digital elevation model to GeoTIFF with compression
dem_df.withColumn(
    "raster_binary", expr("RS_AsGeoTiff(raster, 'LZW', '0.75')")
).write.format("raster").option("rasterField", "raster_binary").option(
    "pathField", "path"
).option(
    "fileExtension", ".tiff"
).mode(
    "overwrite"
).save(
    "dem"
)
```

```{code-cell} ipython3
# Load NetCDF file containing global wind data
netcdf_df = sedona.read.format("binaryFile").load("wind_global.nc")

# Extract and display metadata to understand the data structure
record_info_df = netcdf_df.selectExpr("RS_NetCDFInfo(content) as record_info")

# Display metadata information
record_info = record_info_df.first()["record_info"]
print(record_info)
```

```{code-cell} ipython3
# Extract the u_wind component as a raster for analysis
netcdf_df = netcdf_df.withColumn(
    "raster", expr("RS_FromNetCDF(content, 'u_wind', 'lon', 'lat')")
)
netcdf_df.show()
```

## Integration with GeoPandas

### From Sedona DataFrame to GeoPandas GeoDataFrame

```{code-cell} ipython3
# Load and create spatial data in Sedona format
cities_df = (
    sedona.read.option("header", True)
    .format("CSV")
    .load("world_cities.csv")
    .withColumn("geometry", expr("ST_Point(longitude, latitude)"))
)
cities_df.show()
```

```{code-cell} ipython3
# Convert Sedona DataFrame to GeoPandas GeoDataFrame
df = cities_df.toPandas()  # Convert to Pandas DataFrame
gdf = gpd.GeoDataFrame(
    df, geometry="geometry"
)
gdf.crs = "EPSG:4326"  # Set coordinate reference system
```

```{code-cell} ipython3
gdf.explore()
```

### From Sedona DataFrame To GeoArrow

```{code-cell} ipython3
# Convert Sedona DataFrame to Apache Arrow format for efficient interchange
arrow = dataframe_to_arrow(cities_df)
arrow
```

### From GeoPandas GeoDataFrame to Sedona DataFrame

```{code-cell} ipython3
# Load geospatial data using GeoPandas
gdf = gpd.read_file("world_cities.geojson")
gdf.head()
```

```{code-cell} ipython3
# Check the coordinate reference system
gdf.crs
```

```{code-cell} ipython3
# Convert GeoPandas GeoDataFrame directly to Sedona DataFrame
# Sedona automatically handles the geometry conversion
df = sedona.createDataFrame(gdf)
df.show()
```

### Advanced Integration: Converting Through GeoArrow

```{code-cell} ipython3
# Convert Sedona DataFrame to Arrow format
arrow = dataframe_to_arrow(df)
```

```{code-cell} ipython3
# Convert Arrow format back to GeoPandas
gdf = gpd.GeoDataFrame.from_arrow(arrow)
```

```{code-cell} ipython3
# Display the reconstructed GeoPandas DataFrame
gdf.head()
```

```{code-cell} ipython3
# Convert back to Sedona for further distributed processing
df = sedona.createDataFrame(gdf)
df.show()
```

### Custom Conversion Functions

```{code-cell} ipython3
# Custom function to convert Sedona DataFrame to GeoPandas with error handling
def sedona_to_geopandas(sedona_df, geometry_col="geometry"):
    """Convert Sedona DataFrame to GeoPandas DataFrame with robust error handling"""
    # Convert spatial geometries to WKT format for transfer
    with_wkt = sedona_df.withColumn("wkt_geom", expr(f"ST_AsText({geometry_col})"))

    # Convert to Pandas DataFrame
    pandas_df = with_wkt.toPandas()

    # Convert WKT strings to Shapely geometries
    from shapely import wkt

    pandas_df["geometry"] = pandas_df["wkt_geom"].apply(wkt.loads)

    # Create GeoPandas GeoDataFrame
    gdf = gpd.GeoDataFrame(pandas_df.drop("wkt_geom", axis=1), geometry="geometry")

    return gdf


# Example usage: convert filtered dataset to GeoPandas
major_cities = world_cities_spatial.filter(col("population") > 1000000)
major_cities_gdf = sedona_to_geopandas(major_cities)

print(f"Converted {len(major_cities_gdf)} major cities to GeoPandas")
```

```{code-cell} ipython3
# Display the converted major cities dataset
major_cities_gdf
```

## Real-World Use Cases

### Use Case 1: Global Urban Density Analysis

```{code-cell} ipython3
# Analyze urban density patterns for cities with population > 500,000
urban_analysis = (
    world_cities_spatial.filter(col("population") > 500000)  # Focus on major cities
    .withColumn(
        "urban_density",
        col("population")
        / expr("ST_Area(ST_Buffer(geometry, 10000))"),  # People per m² in 10km radius
    )
    .withColumn(
        "city_category",
        expr(
            """
        CASE
            WHEN population > 5000000 THEN 'Megacity'      -- Cities > 5M people
            WHEN population > 1000000 THEN 'Large City'    -- Cities 1-5M people
            ELSE 'Medium City'                              -- Cities 500K-1M people
        END
    """
        ),
    )
)

# Calculate average density by city category
urban_analysis.groupBy("city_category").agg(
    expr("count(*)").alias("count"),  # Number of cities in each category
    expr("avg(urban_density)").alias("avg_density"),  # Average density per category
).show()
```

### Use Case 2: Transit Accessibility Assessment

```{code-cell} ipython3
# Analyze potential transit coverage for cities with population > 100,000
transit_analysis = (
    world_cities_spatial.filter(col("population") > 100000)
    .withColumn(
        "transit_coverage",
        expr("ST_Buffer(geometry, 1000)"),  # 1km radius transit catchment area
    )
    .withColumn(
        "coverage_area_km2",
        expr("ST_Area(ST_Buffer(geometry, 1000)) / 1000000"),  # Convert m² to km²
    )
)

# Calculate global transit accessibility metrics
accessibility_metrics = transit_analysis.agg(
    expr("avg(coverage_area_km2)").alias(
        "avg_coverage_area"
    ),  # Average coverage area per city
    expr("sum(coverage_area_km2)").alias(
        "total_coverage_area"
    ),  # Total potential coverage globally
)

accessibility_metrics.show()
```

## Key Takeaways

## References and Further Reading

## Exercises

### Exercise 1: Setting Up Sedona and Basic Spatial Operations

```{code-cell} ipython3

```

### Exercise 2: Working with Real Geospatial Data

```{code-cell} ipython3

```

### Exercise 3: Distance Analysis

```{code-cell} ipython3

```

### Exercise 4: Spatial Joins

```{code-cell} ipython3

```

### Exercise 5: Spatial Aggregation and Clustering

```{code-cell} ipython3

```

### Exercise 6: Buffer Analysis

```{code-cell} ipython3

```

### Exercise 7: Spatial SQL Queries

```{code-cell} ipython3

```

### Exercise 8: Advanced Spatial Analysis

```{code-cell} ipython3

```
