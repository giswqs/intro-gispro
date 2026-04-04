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
# High-Performance Geospatial Analytics with DuckDB

## Introduction

### What Makes DuckDB Special for Geospatial Work?

## Learning Objectives

## Installation and Setup

### Installing Required Packages

```{code-cell} ipython3
# %pip install duckdb pygis
```

### Library Import and Configuration

```{code-cell} ipython3
# Configure jupysql for optimal output
%config SqlMagic.autopandas = True
%config SqlMagic.feedback = False
%config SqlMagic.displaycon = False
```

```{code-cell} ipython3
import duckdb
import leafmap
import pandas as pd

# Import jupysql Jupyter extension for SQL magic commands
%load_ext sql
```

### Understanding DuckDB Connections

```{code-cell} ipython3
# Connect to in-memory database
con = duckdb.connect()

# Connect to persistent file-based database
con = duckdb.connect('filename.db')

# Connect using SQL magic for jupyter notebooks
%sql duckdb:///:memory:
```

### Installing and Loading Extensions

```{code-cell} ipython3
# Install and load essential extensions
con.install_extension("httpfs")  # For remote file access
con.load_extension("httpfs")

con.install_extension("spatial")  # For spatial operations
con.load_extension("spatial")
```

```{code-cell} ipython3
con.sql("FROM duckdb_extensions();")
```

```{code-cell} ipython3
con.sql("FROM duckdb_extensions();").df()
```

## SQL Basics for Spatial Analysis

### Understanding SQL for Geospatial Work

### Sample Datasets

### Reading Data Directly from URLs

```{code-cell} ipython3
%%sql
SELECT * FROM 'https://opengeos.org/data/duckdb/cities.csv';
```

```{code-cell} ipython3
%%sql
SELECT * FROM 'https://opengeos.org/data/duckdb/countries.csv';
```

### Creating Persistent Tables

```{code-cell} ipython3
%%sql
CREATE OR REPLACE TABLE cities AS SELECT * FROM 'https://opengeos.org/data/duckdb/cities.csv';
```

```{code-cell} ipython3
%%sql
CREATE OR REPLACE TABLE countries AS SELECT * FROM 'https://opengeos.org/data/duckdb/countries.csv';
```

### Viewing Your Data

```{code-cell} ipython3
%%sql
FROM cities;
```

```{code-cell} ipython3
%%sql
FROM countries;
```

### Essential SQL Commands

#### Selecting Data

```{code-cell} ipython3
%%sql
SELECT * FROM cities LIMIT 10;
```

#### Choosing Specific Columns

```{code-cell} ipython3
%%sql
SELECT name, country FROM cities LIMIT 10;
```

#### Finding Unique Values

```{code-cell} ipython3
%%sql
SELECT DISTINCT country FROM cities LIMIT 10;
```

#### Counting and Aggregation

```{code-cell} ipython3
%%sql
SELECT COUNT(*) FROM cities;
```

```{code-cell} ipython3
%%sql
SELECT COUNT(DISTINCT country) FROM cities;
```

```{code-cell} ipython3
%%sql
SELECT MAX(population) FROM cities;
```

```{code-cell} ipython3
%%sql
SELECT MIN(population) FROM cities;
```

```{code-cell} ipython3
%%sql
SELECT AVG(population) FROM cities;
```

### Filtering and Sorting Data

#### Filtering with WHERE Clauses

```{code-cell} ipython3
%%sql
SELECT * FROM cities WHERE population > 1000000 LIMIT 10;
```

#### Sorting Your Results

```{code-cell} ipython3
%%sql
SELECT * FROM cities ORDER BY population DESC LIMIT 10;
```

#### Grouping and Aggregating Data

```{code-cell} ipython3
%%sql
SELECT country, COUNT(*) as city_count, AVG(population) as avg_population
FROM cities
GROUP BY country
ORDER BY city_count DESC
LIMIT 10;
```

## Python API Integration

### Understanding Result Formats

```{code-cell} ipython3
# Execute SQL and get different result formats
con.sql('SELECT 42').fetchall()        # Python objects
```

```{code-cell} ipython3
con.sql('SELECT 42').df()              # Pandas DataFrame
```

```{code-cell} ipython3
con.sql('SELECT 42').fetchnumpy()      # NumPy Arrays
```

### Seamless DataFrame Integration

```{code-cell} ipython3
# Query Pandas DataFrames directly
pandas_df = pd.DataFrame({'a': [42]})
con.sql('SELECT * FROM pandas_df')
```

```{code-cell} ipython3
# Convert remote data to DataFrame
df = con.read_csv('https://opengeos.org/data/duckdb/cities.csv').df()
df.head()
```

### Result Conversion and Export

```{code-cell} ipython3
# Write results to various formats
con.sql('SELECT 42').write_parquet('out.parquet')
con.sql('SELECT 42').write_csv('out.csv')
con.sql("COPY (SELECT 42) TO 'out.parquet'")
```

### Persistent Storage

```{code-cell} ipython3
# Create persistent database connection
# create a connection to a file called 'file.db'
con_persistent = duckdb.connect('file.db')
# create a table and load data into it
con_persistent.sql(
    'CREATE TABLE IF NOT EXISTS cities AS FROM read_csv_auto("https://opengeos.org/data/duckdb/cities.csv")'
)
# query the table
con_persistent.table('cities').show()
```

```{code-cell} ipython3
# explicitly close the connection
con_persistent.close()
```

```{code-cell} ipython3
with duckdb.connect('file.db') as con:
    con.sql(
        'CREATE TABLE IF NOT EXISTS cities AS FROM read_csv_auto("https://opengeos.org/data/duckdb/cities.csv")'
    )
    con.table('cities').show(max_rows=5)
    # the context manager closes the connection automatically
```

## Data Import

### Understanding Data Formats in Geospatial Work

### Downloading Sample Data

```{code-cell} ipython3
url = "https://opengeos.org/data/duckdb/cities.zip"
leafmap.download_file(url, unzip=True)
```

### Working with CSV Files

```{code-cell} ipython3
# Read CSV with auto-detection
con = duckdb.connect()
con.read_csv('cities.csv')
```

```{code-cell} ipython3
# Read CSV with specific options
con.read_csv('cities.csv', header=True, sep=',')
```

```{code-cell} ipython3
# Use parallel CSV reader
con.read_csv('cities.csv', parallel=True)
```

```{code-cell} ipython3
# Read CSV directly in SQL
con.sql("SELECT * FROM 'cities.csv'")
```

```{code-cell} ipython3
# Call read_csv from within SQL
con.sql("SELECT * FROM read_csv_auto('cities.csv')")
```

### JSON Files

```{code-cell} ipython3
# Read JSON files
con.read_json('cities.json')
```

```{code-cell} ipython3
# Read JSON directly in SQL
con.sql("SELECT * FROM 'cities.json'")
```

```{code-cell} ipython3
# Call read_json from within SQL
con.sql("SELECT * FROM read_json_auto('cities.json')")
```

### DataFrames

```{code-cell} ipython3
df = pd.read_csv('cities.csv')
df
```

```{code-cell} ipython3
con.sql('SELECT * FROM df').fetchall()
```

### Parquet Files

```{code-cell} ipython3
# Read from a single Parquet file
con.read_parquet('cities.parquet')
```

```{code-cell} ipython3
# Read Parquet directly in SQL
con.sql("SELECT * FROM 'cities.parquet'")
```

```{code-cell} ipython3
# Call read_parquet from within SQL
con.sql("SELECT * FROM read_parquet('cities.parquet')")
```

### Spatial Data Formats

```{code-cell} ipython3
con.load_extension('spatial')
```

```{code-cell} ipython3
con.sql('SELECT * FROM ST_Drivers()')
```

```{code-cell} ipython3
# Read GeoJSON
con.sql("SELECT * FROM ST_Read('cities.geojson')")
```

```{code-cell} ipython3
# Create spatial table from GeoJSON
con.sql("CREATE TABLE cities AS SELECT * FROM ST_Read('cities.geojson')")
```

```{code-cell} ipython3
con.table('cities')
```

```{code-cell} ipython3
con.sql("SELECT * FROM ST_Read('cities.shp')")
```

```{code-cell} ipython3
con.sql(
    """
        CREATE TABLE IF NOT EXISTS cities2 AS
        SELECT * FROM ST_Read('cities.shp')
        """
)
```

```{code-cell} ipython3
con.table('cities2')
```

## Data Export

### Sample Spatial Data Setup

```{code-cell} ipython3
con = duckdb.connect()
con.load_extension('spatial')
con.sql("""
CREATE TABLE IF NOT EXISTS cities AS
FROM 'https://opengeos.org/data/duckdb/cities.parquet'
""")
```

```{code-cell} ipython3
con.table("cities").show()
```

### Export to DataFrames

```{code-cell} ipython3
con.table("cities").df()
```

### Export to Files

```{code-cell} ipython3
# Export to CSV
con.sql("COPY cities TO 'cities.csv' (HEADER, DELIMITER ',')")
```

```{code-cell} ipython3
con.sql(
    "COPY (SELECT * FROM cities WHERE country='USA') TO 'cities_us.csv' (HEADER, DELIMITER ',')"
)
```

### Export to JSON

```{code-cell} ipython3
con.sql("COPY cities TO 'cities.json'")
```

```{code-cell} ipython3
con.sql("COPY (SELECT * FROM cities WHERE country='USA') TO 'cities_us.json'")
```

### Export to Excel

```{code-cell} ipython3
con.sql(
    "COPY (SELECT * EXCLUDE geometry FROM cities) TO 'cities.xlsx' WITH (FORMAT GDAL, DRIVER 'XLSX')"
)
```

### Export to Parquet

```{code-cell} ipython3
con.sql("COPY cities TO 'cities.parquet' (FORMAT PARQUET)")
```

```{code-cell} ipython3
con.sql(
    "COPY (SELECT * FROM cities WHERE country='USA') TO 'cities_us.parquet' (FORMAT PARQUET)"
)
```

### Export Spatial Formats

```{code-cell} ipython3
# Export to GeoJSON
con.sql("COPY cities TO 'cities.geojson' WITH (FORMAT GDAL, DRIVER 'GeoJSON')")
```

```{code-cell} ipython3
con.sql(
    "COPY (SELECT * FROM cities WHERE country='USA') TO 'cities_us.geojson' WITH (FORMAT GDAL, DRIVER 'GeoJSON')"
)
```

```{code-cell} ipython3
# Export to Shapefile
con.sql("COPY cities TO 'cities.shp' WITH (FORMAT GDAL, DRIVER 'ESRI Shapefile')")
```

```{code-cell} ipython3
# Export to GeoPackage
con.sql("COPY cities TO 'cities.gpkg' WITH (FORMAT GDAL, DRIVER 'GPKG')")
```

## Working with Geometries

### Understanding Spatial Data Types

### Sample Data Setup

```{code-cell} ipython3
# Download NYC sample data
url = "https://opengeos.org/data/duckdb/nyc_data.db.zip"
leafmap.download_file(url, unzip=True)
```

```{code-cell} ipython3
# Connect to spatial database
con = duckdb.connect("nyc_data.db")
con.install_extension("spatial")
con.load_extension("spatial")
```

```{code-cell} ipython3
con.sql("SHOW TABLES;")
```

### Creating and Understanding Geometries

```{code-cell} ipython3
con.sql("""

CREATE or REPLACE TABLE samples (name VARCHAR, geom GEOMETRY);

INSERT INTO samples VALUES
  ('Point', ST_GeomFromText('POINT(-100 40)')),
  ('Linestring', ST_GeomFromText('LINESTRING(0 0, 1 1, 2 1, 2 2)')),
  ('Polygon', ST_GeomFromText('POLYGON((0 0, 1 0, 1 1, 0 1, 0 0))')),
  ('PolygonWithHole', ST_GeomFromText('POLYGON((0 0, 10 0, 10 10, 0 10, 0 0),(1 1, 1 2, 2 2, 2 1, 1 1))')),
  ('Collection', ST_GeomFromText('GEOMETRYCOLLECTION(POINT(2 0),POLYGON((0 0, 1 0, 1 1, 0 1, 0 0)))'));

SELECT * FROM samples;

  """)
```

```{code-cell} ipython3
con.sql("SELECT name, ST_AsText(geom) AS geometry FROM samples;")
```

```{code-cell} ipython3
con.sql("""
COPY samples TO 'samples.geojson' (FORMAT GDAL, DRIVER GeoJSON);
""")
```

### Working with Points

```{code-cell} ipython3
con.sql("""
SELECT ST_AsText(geom)
  FROM samples
  WHERE name = 'Point';
""")
```

```{code-cell} ipython3
con.sql("""
SELECT ST_X(geom), ST_Y(geom)
  FROM samples
  WHERE name = 'Point';
""")
```

```{code-cell} ipython3
con.sql("""
SELECT * FROM nyc_subway_stations
""")
```

```{code-cell} ipython3
con.sql("""
SELECT name, ST_AsText(geom)
  FROM nyc_subway_stations
  LIMIT 10;
""")
```

### Working with LineStrings

```{code-cell} ipython3
con.sql("""
SELECT ST_AsText(geom)
  FROM samples
  WHERE name = 'Linestring';
""")
```

```{code-cell} ipython3
con.sql("""
SELECT ST_Length(geom)
  FROM samples
  WHERE name = 'Linestring';
""")
```

### Working with Polygons

```{code-cell} ipython3
con.sql("""
SELECT ST_AsText(geom)
  FROM samples
  WHERE name = 'Polygon';
""")
```

```{code-cell} ipython3
con.sql("""
SELECT
    ST_Area(geom) as area,
    ST_Perimeter(geom) as perimeter
FROM samples
WHERE name = 'Polygon';
""")
```

## Spatial Relationships

### Understanding Spatial Predicates

### Working with Real Spatial Data

```{code-cell} ipython3
# Find subway station
con.sql("""
SELECT name, geom
FROM nyc_subway_stations
WHERE name = 'Broad St';
""")
```

### Testing Spatial Equality

```{code-cell} ipython3
# Test spatial equality
con.sql("""
SELECT name
FROM nyc_subway_stations
WHERE ST_Equals(geom, ST_GeomFromText('POINT (583571.9059213118 4506714.341192182)'));
""")
```

### Point-in-Polygon Analysis

```{code-cell} ipython3
con.sql("FROM nyc_neighborhoods LIMIT 5")
```

```{code-cell} ipython3
# Find neighborhood containing a point
con.sql("""
SELECT name, boroname
FROM nyc_neighborhoods
WHERE ST_Intersects(geom, ST_GeomFromText('POINT(583571 4506714)'));
""")
```

### Proximity Analysis with Distance

```{code-cell} ipython3
# Find features within distance
con.sql("""
SELECT COUNT(*) as nearby_stations
FROM nyc_subway_stations
WHERE ST_DWithin(geom, ST_GeomFromText('POINT(583571 4506714)'), 500);
""")
```

## Spatial Joins

### Understanding Spatial vs. Regular Joins

### Exploring Our Data

```{code-cell} ipython3
con.sql("FROM nyc_neighborhoods SELECT * LIMIT 5;")
```

```{code-cell} ipython3
con.sql("FROM nyc_subway_stations SELECT * LIMIT 5;")
```

### Your First Spatial Join

```{code-cell} ipython3
# Find subway stations and their neighborhoods
con.sql("""
SELECT
  subways.name AS subway_name,
  neighborhoods.name AS neighborhood_name,
  neighborhoods.boroname AS borough
FROM nyc_neighborhoods AS neighborhoods
JOIN nyc_subway_stations AS subways
ON ST_Intersects(neighborhoods.geom, subways.geom)
WHERE subways.NAME = 'Broad St';
""")
```

### Advanced Spatial Analysis

```{code-cell} ipython3
con.sql("""
SELECT DISTINCT COLOR FROM nyc_subway_stations;
""")
```

```{code-cell} ipython3
# Find RED subway stations and their neighborhoods
con.sql("""
SELECT
  subways.name AS subway_name,
  neighborhoods.name AS neighborhood_name,
  neighborhoods.boroname AS borough
FROM nyc_neighborhoods AS neighborhoods
JOIN nyc_subway_stations AS subways
ON ST_Intersects(neighborhoods.geom, subways.geom)
WHERE subways.color = 'RED';
""")
```

### Distance-Based Analysis

```{code-cell} ipython3
# Get baseline demographics
con.sql("""
SELECT
  100.0 * Sum(popn_white) / Sum(popn_total) AS white_pct,
  100.0 * Sum(popn_black) / Sum(popn_total) AS black_pct,
  Sum(popn_total) AS popn_total
FROM nyc_census_blocks;
""")
```

```{code-cell} ipython3
con.sql("""
SELECT DISTINCT routes
FROM nyc_subway_stations AS subways
WHERE strpos(subways.routes,'A') > 0;
""")
```

```{code-cell} ipython3
# Demographics within 200 meters of A-train
con.sql("""
SELECT
  100.0 * Sum(popn_white) / Sum(popn_total) AS white_pct,
  100.0 * Sum(popn_black) / Sum(popn_total) AS black_pct,
  Sum(popn_total) AS popn_total
FROM nyc_census_blocks AS census
JOIN nyc_subway_stations AS subways
ON ST_DWithin(census.geom, subways.geom, 200)
WHERE strpos(subways.routes,'A') > 0;
""")
```

### Advanced Multi-Table Joins

```{code-cell} ipython3
# Create subway lines reference table
con.sql("""
CREATE OR REPLACE TABLE subway_lines ( route char(1) );
INSERT INTO subway_lines (route) VALUES
  ('A'),('B'),('C'),('D'),('E'),('F'),('G'),
  ('J'),('L'),('M'),('N'),('Q'),('R'),('S'),
  ('Z'),('1'),('2'),('3'),('4'),('5'),('6'),
  ('7');
""")
```

```{code-cell} ipython3
# Analyze demographics by subway line
con.sql("""
SELECT
  lines.route,
  100.0 * Sum(popn_white) / Sum(popn_total) AS white_pct,
  100.0 * Sum(popn_black) / Sum(popn_total) AS black_pct,
  Sum(popn_total) AS popn_total
FROM nyc_census_blocks AS census
JOIN nyc_subway_stations AS subways
ON ST_DWithin(census.geom, subways.geom, 200)
JOIN subway_lines AS lines
ON strpos(subways.routes, lines.route) > 0
GROUP BY lines.route
ORDER BY black_pct DESC;
""")
```

## Large-Scale Data Analysis

### Analyzing the National Wetlands Inventory

```{code-cell} ipython3
# Connect and prepare for large-scale analysis
con = duckdb.connect()
con.install_extension("spatial")
con.load_extension("spatial")
```

```{code-cell} ipython3
# Analyze single state data
state = "DC"    # Change to the US State of your choice
url = f"https://data.source.coop/giswqs/nwi/wetlands/{state}_Wetlands.parquet"
con.sql(f"SELECT * FROM '{url}'")
```

```{code-cell} ipython3
# Inspect the table schema
con.sql(f"DESCRIBE FROM '{url}'")
```

### Scaling Up: Nationwide Wetland Analysis

#### Count the Total Number of Wetlands

```{code-cell} ipython3
con.sql(f"""
SELECT COUNT(*) AS Count
FROM 's3://us-west-2.opendata.source.coop/giswqs/nwi/wetlands/*.parquet'
""")
```

#### Count Wetlands by State

```{code-cell} ipython3
# Count wetlands by state using filename
df = con.sql(f"""
SELECT filename, COUNT(*) AS Count
FROM read_parquet('s3://us-west-2.opendata.source.coop/giswqs/nwi/wetlands/*.parquet', filename=true)
GROUP BY filename
ORDER BY COUNT(*) DESC;
""").df()
df.head()
```

```{code-cell} ipython3
# Extract state codes from filenames
count_df = con.sql(f"""
SELECT SUBSTRING(filename, LENGTH(filename) - 18, 2) AS State, COUNT(*) AS Count
FROM read_parquet('s3://us-west-2.opendata.source.coop/giswqs/nwi/wetlands/*.parquet', filename=true)
GROUP BY State
ORDER BY COUNT(*) DESC;
""").df()
count_df.head(10)
```

```{code-cell} ipython3
# Create a wetlands table from the DataFrame
con.sql("CREATE OR REPLACE TABLE wetlands AS FROM count_df")
con.sql("FROM wetlands")
```

### Mapping Wetland Counts by State

```{code-cell} ipython3
# Create states table with geometries
url = 'https://opengeos.org/data/us/us_states.parquet'
con.sql(
    f"""
CREATE OR REPLACE TABLE states AS
SELECT * FROM '{url}'
"""
)
```

```{code-cell} ipython3
con.sql(
    """
SELECT * FROM states INNER JOIN wetlands ON states.id = wetlands.State
"""
)
```

```{code-cell} ipython3
# Join wetlands count with state geometries for visualization
file_path = "states_with_wetlands.geojson"
con.sql(f"""
    COPY (
    SELECT s.name, s.id, w.Count, s.geometry
    FROM states s
    JOIN wetlands w ON s.id = w.State
    ORDER BY w.Count DESC
    ) TO '{file_path}' WITH (FORMAT GDAL, DRIVER 'GeoJSON')
""")
```

```{code-cell} ipython3
m = leafmap.Map()
m.add_data(
    file_path, column="Count", scheme="Quantiles", cmap="Greens", legend_title="Wetland Count"
)
m
```

### Wetland Distribution Charts

#### Pie Chart of Wetlands by State

```{code-cell} ipython3
leafmap.pie_chart(
    count_df, "State", "Count", height=800, title="Number of Wetlands by State"
)
```

#### Bar Chart of Wetlands by State

```{code-cell} ipython3
leafmap.bar_chart(count_df, "State", "Count", title="Number of Wetlands by State")
```

### Wetland Area Analysis

#### Total Wetland Area in the U.S.

```{code-cell} ipython3
con.sql(
    f"""
SELECT SUM(Shape_Area) /  1000000 AS Area_SqKm
FROM 's3://us-west-2.opendata.source.coop/giswqs/nwi/wetlands/*.parquet'
"""
)
```

#### Wetland Area by State

```{code-cell} ipython3
area_df = con.sql(
    f"""
SELECT SUBSTRING(filename, LENGTH(filename) - 18, 2) AS State, SUM(Shape_Area) /  1000000 AS Area_SqKm
FROM read_parquet('s3://us-west-2.opendata.source.coop/giswqs/nwi/wetlands/*.parquet', filename=true)
GROUP BY State
ORDER BY COUNT(*) DESC;
"""
).df()
area_df.head(10)
```

#### Pie Chart of Wetland Area by State

```{code-cell} ipython3
leafmap.pie_chart(
    area_df, "State", "Area_SqKm", height=850, title="Wetland Area by State"
)
```

#### Bar Chart of Wetland Area by State

```{code-cell} ipython3
leafmap.bar_chart(area_df, "State", "Area_SqKm", title="Wetland Area by State")
```

## Key Takeaways

### Fundamental Concepts You've Learned

### Why This Approach is Powerful

### Building Your Spatial Analysis Skills

## Exercises

### Exercise 1: Creating Tables

```{code-cell} ipython3

```

### Exercise 2: Column Filtering

```{code-cell} ipython3

```

### Exercise 3: Row Filtering

```{code-cell} ipython3

```

### Exercise 4: Sorting Results

```{code-cell} ipython3

```

### Exercise 5: Unique Values

```{code-cell} ipython3

```

### Exercise 6: Counting Rows

```{code-cell} ipython3

```

### Exercise 7: Aggregating Data

```{code-cell} ipython3

```

### Exercise 8: Joining Tables

```{code-cell} ipython3

```

### Exercise 9: String Manipulation

```{code-cell} ipython3

```

### Exercise 10: Filtering with Multiple Conditions

```{code-cell} ipython3

```

### Exercise 11: Basic Setup and Data Loading

```{code-cell} ipython3

```

### Exercise 12: Spatial Relationships Analysis

```{code-cell} ipython3

```

### Exercise 13: Advanced Spatial Joins

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

### Exercise 14: Data Import and Export

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

### Exercise 15: Large-Scale Analysis

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3

```

```{code-cell} ipython3

```
