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
# String Operations

## Introduction

## Learning Objectives

## Creating and Manipulating Strings

### Creating Strings

```{code-cell} ipython3
# Different ways to create strings
location_name = "Mount Everest"  # Using double quotes
country = 'Nepal'  # Using single quotes
description = """Mount Everest is the highest peak
in the world, located in the Himalayas."""  # Multi-line string

print(f"Location: {location_name}")
print(f"Country: {country}")
print(f"Description: {description}")
```

### String Concatenation

```{code-cell} ipython3
# Basic concatenation using the + operator
location_full = location_name + ", " + country
print(f"Full location: {location_full}")

# Building a file path
data_folder = "geographic_data"
filename = "mountain_peaks.csv"
file_path = data_folder + "/" + filename
print(f"File path: {file_path}")
```

### String Repetition

```{code-cell} ipython3
# Create visual separators
separator = "-" * 30
print(separator)
print("Geographic Data Report")
print(separator)

# Create formatted spacing
tab_space = " " * 4
print(f"Location:{tab_space}{location_name}")
print(f"Elevation:{tab_space}8,848 meters")
```

### String Length and Basic Properties

```{code-cell} ipython3
# Get the length of a string
location_length = len(location_name)
print(f"The location name '{location_name}' has {location_length} characters")

# Check if a string contains only letters
city_name = "SanFrancisco"
print(f"Is '{city_name}' alphabetic? {city_name.isalpha()}")

# Check if a string contains only digits (useful for coordinate validation)
zip_code = "94102"
print(f"Is '{zip_code}' numeric? {zip_code.isdigit()}")
```

### Building Dynamic Content

```{code-cell} ipython3
# Building dynamic location descriptions
latitude = 27.9881
longitude = 86.9250
elevation = 8848

location_info = (
    location_name
    + " is located at coordinates "
    + str(latitude)
    + ", "
    + str(longitude)
)
print(location_info)

# A more complex example - building a geographic summary
cities = ["Kathmandu", "Pokhara", "Lalitpur"]
summary = "Major cities in " + country + " include: " + ", ".join(cities)
print(summary)
```

## String Methods for Geospatial Data

### Case Conversion Methods

```{code-cell} ipython3
# Case conversion examples
mountain_name = "Mount Everest"

# Convert to different cases
print(f"Original: {mountain_name}")
print(f"Uppercase: {mountain_name.upper()}")
print(f"Lowercase: {mountain_name.lower()}")
print(f"Title case: {mountain_name.title()}")
print(f"Capitalize: {mountain_name.capitalize()}")
```

### Whitespace Removal Methods

```{code-cell} ipython3
# Whitespace removal examples
messy_location = "   San Francisco   "
messy_left = "   Los Angeles"
messy_right = "Chicago   "

print(f"Original: '{messy_location}'")
print(f"strip(): '{messy_location.strip()}'")  # Remove both sides
print(f"lstrip(): '{messy_left.lstrip()}'")  # Remove left side
print(f"rstrip(): '{messy_right.rstrip()}'")  # Remove right side
```

### String Replacement

```{code-cell} ipython3
# Basic replacement
location = "Mount Everest, Nepal"
updated_location = location.replace("Everest", "Kilimanjaro")
print(f"Original: {location}")
print(f"Updated: {updated_location}")

# Replace multiple occurrences
path_string = "data/raw_data/geographic_data/raw_data/points.csv"
clean_path = path_string.replace("raw_data/", "")
print(f"Original path: {path_string}")
print(f"Clean path: {clean_path}")
```

### String Splitting

```{code-cell} ipython3
# Basic splitting
location_full = "Mount Everest, Nepal, Asia"
location_parts = location_full.split(", ")
print(f"Original: {location_full}")
print(f"Split into parts: {location_parts}")

# Extract individual components
mountain, country, continent = location_parts
print(f"Mountain: {mountain}")
print(f"Country: {country}")
print(f"Continent: {continent}")
```

```{code-cell} ipython3
# Splitting coordinate strings
coordinate_string = "40.7128,-74.0060"
lat_str, lon_str = coordinate_string.split(",")
latitude = float(lat_str)
longitude = float(lon_str)
print(f"Parsed coordinates: Lat={latitude}, Lon={longitude}")
```

```{code-cell} ipython3
# Splitting file paths
file_path = "data/geographic/cities/world_cities.csv"
path_components = file_path.split("/")
print(f"Path components: {path_components}")
print(f"Filename: {path_components[-1]}")  # Last component is the filename
```

### String Joining

```{code-cell} ipython3
# Basic joining
city_names = ["San Francisco", "New York", "Tokyo"]
city_name = ", ".join(city_names)
print(f"Joined city name: {city_name}")

```

```{code-cell} ipython3
# Creating file paths
path_parts = ["data", "geographic", "elevation", "dem.tif"]
full_path = "/".join(path_parts)
print(f"Full path: {full_path}")
```

```{code-cell} ipython3
# Practical example: creating coordinate strings
coordinates = ["40.7128", "-74.0060"]
coordinate_string = ",".join(coordinates)
print(f"Coordinate string: {coordinate_string}")
```

## String Formatting

### F-String Formatting (Recommended)

```{code-cell} ipython3
# Basic f-string formatting with geographic data
location = "Mount Everest"
latitude = 27.9881
longitude = 86.9250
elevation = 8848

# Simple variable insertion
location_info = f"Location: {location}"
print(location_info)

# Multiple variables
coordinates = f"Coordinates: ({latitude}, {longitude})"
print(coordinates)

# Complete geographic summary
summary = f"{location} is located at {latitude}°N, {longitude}°E with an elevation of {elevation} meters"
print(summary)
```

### Formatting Numbers in Strings

```{code-cell} ipython3
# Controlling decimal places for coordinates
precise_lat = 40.712776
precise_lon = -74.005974

# Round to different decimal places
coords_2_places = f"Coordinates: ({precise_lat:.2f}, {precise_lon:.2f})"
coords_4_places = f"Coordinates: ({precise_lat:.4f}, {precise_lon:.4f})"

print(coords_2_places)
print(coords_4_places)

# Adding thousands separators for large numbers
population = 8336817
area_sqkm = 783.8

formatted_stats = f"NYC Population: {population:,} people, Area: {area_sqkm:.1f} km²"
print(formatted_stats)
```

### Legacy Formatting Methods

```{code-cell} ipython3
# Using .format() method
location = "San Francisco"
lat = 37.7749
lon = -122.4194

# Basic format method
formatted_1 = "Location: {} at coordinates ({}, {})".format(location, lat, lon)
print(formatted_1)

# With positional arguments
formatted_2 = "Location: {0} at coordinates ({1}, {2})".format(location, lat, lon)
print(formatted_2)

# With named arguments
formatted_3 = "Location: {name} at coordinates ({latitude}, {longitude})".format(
    name=location, latitude=lat, longitude=lon
)
print(formatted_3)
```

### Practical Formatting Examples

```{code-cell} ipython3
# Creating file names with timestamps and coordinates
import datetime

current_time = datetime.datetime.now()
survey_lat = 45.3311
survey_lon = -121.7113

filename = f"survey_{current_time.strftime('%Y%m%d')}_{survey_lat:.4f}N_{abs(survey_lon):.4f}W.csv"
print(f"Generated filename: {filename}")

# Creating Well-Known Text (WKT) representations
wkt_point = f"POINT({survey_lon} {survey_lat})"
print(f"WKT Point: {wkt_point}")
```

```{code-cell} ipython3
# Building SQL queries with formatting
table_name = "cities"
min_population = 1000000
region = "North America"

sql_query = f"""SELECT name, latitude, longitude
FROM {table_name}
WHERE population > {min_population:,}
AND region = '{region}'"""

print("Generated SQL Query:")
print(sql_query)
```

## String Operation Decision Guide

### When to Use Each Operation

## Key Takeaways

## Exercises

### Exercise 1: Manipulating Geographic Location Strings

```{code-cell} ipython3

```

### Exercise 2: Extracting and Formatting Coordinates

```{code-cell} ipython3

```

### Exercise 3: Building Dynamic SQL Queries

```{code-cell} ipython3

```

### Exercise 4: String Normalization and Cleaning

```{code-cell} ipython3

```

### Exercise 5: Parsing and Extracting Address Information

```{code-cell} ipython3

```
