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
# Python Data Structures

## Introduction

## Learning Objectives

## Tuples

### Creating and Using Tuples

```{code-cell} ipython3
tokyo_point = (
    35.6895,
    139.6917,
)  # Tuple representing Tokyo's coordinates (latitude, longitude)
print(f"Tokyo coordinates: {tokyo_point}")
```

### Accessing Tuple Elements

```{code-cell} ipython3
latitude = tokyo_point[0]
longitude = tokyo_point[1]
print(f"Latitude: {latitude}")
print(f"Longitude: {longitude}")
```

### Tuple Unpacking

```{code-cell} ipython3
lat, lon = tokyo_point  # Unpacking the tuple into two variables
print(f"Tokyo is located at {lat}°N, {lon}°E")
```

### Multiple Coordinate Points

```{code-cell} ipython3
# Different geographic locations as tuples
new_york = (40.7128, -74.0060)
london = (51.5074, -0.1278)
sydney = (-33.8688, 151.2093)

print(f"New York: {new_york}")
print(f"London: {london}")
print(f"Sydney: {sydney}")
```

## Lists

### Creating Lists

```{code-cell} ipython3
# A list of coordinate tuples representing a travel route
route = [
    (35.6895, 139.6917),  # Tokyo
    (34.0522, -118.2437),  # Los Angeles
    (51.5074, -0.1278),  # London
]
print("Travel route:", route)
```

```{code-cell} ipython3
# A list of elevation measurements (in meters)
elevations = [120.5, 135.2, 150.8, 168.3, 185.7, 203.1]
print("Elevation profile:", elevations)
```

```{code-cell} ipython3
# A list of city names
cities = ["Tokyo", "Los Angeles", "London", "Paris"]
print("Cities to visit:", cities)
```

### Adding Elements to Lists

```{code-cell} ipython3
# Add Paris to our travel route
route.append((48.8566, 2.3522))  # Adding Paris coordinates
print("Updated route:", route)
```

```{code-cell} ipython3
# Add a new elevation measurement
elevations.append(221.4)
print("Updated elevations:", elevations)
```

### Accessing List Elements

```{code-cell} ipython3
# Access the first city in our route
first_stop = route[0]
print(f"First stop: {first_stop}")

# Access the last city using negative indexing
last_stop = route[-1]
print(f"Last stop: {last_stop}")
```

### List Slicing

```{code-cell} ipython3
# Get the first two stops of our route
first_two_stops = route[:2]
print("First two stops:", first_two_stops)

# Get the middle portion of elevation data
middle_elevations = elevations[2:5]
print("Middle elevation readings:", middle_elevations)
```

### Useful List Operations

```{code-cell} ipython3
# Find the number of waypoints in our route
num_waypoints = len(route)
print(f"Number of waypoints: {num_waypoints}")

# Find the highest elevation
max_elevation = max(elevations)
print(f"Highest elevation: {max_elevation} meters")

# Calculate average elevation
avg_elevation = sum(elevations) / len(elevations)
print(f"Average elevation: {avg_elevation:.1f} meters")
```

## Sets

### Creating Sets

```{code-cell} ipython3
# Create a set of geographic regions
regions_visited = {"North America", "Europe", "Asia"}
print("Regions visited:", regions_visited)
```

```{code-cell} ipython3
# Create a set from a list (automatically removes duplicates)
country_codes = ["US", "CA", "MX", "US", "CA"]  # Notice the duplicates
unique_codes = set(country_codes)
print("Original list:", country_codes)
print("Unique country codes:", unique_codes)
```

```{code-cell} ipython3
# Create a set of coordinate system codes
crs_codes = {"EPSG:4326", "EPSG:3857", "EPSG:32633"}
print("Coordinate reference systems:", crs_codes)
```

### Adding Elements to Sets

```{code-cell} ipython3
# Add a new region
print("Original set:", regions_visited)
regions_visited.add("Africa")
print("After adding Africa:", regions_visited)

# Try to add a duplicate region
regions_visited.add("Europe")  # This won't change the set
print("After trying to add Europe again:", regions_visited)
```

### Practical Set Operations

```{code-cell} ipython3
# Two different survey areas with their observed species
area_a_species = {"oak", "pine", "maple", "birch"}
area_b_species = {"pine", "birch", "cedar", "fir"}

print("Species in Area A:", area_a_species)
print("Species in Area B:", area_b_species)

# Find species common to both areas
common_species = area_a_species.intersection(area_b_species)
print("Species found in both areas:", common_species)

# Find species unique to Area A
unique_to_a = area_a_species - area_b_species
print("Species only in Area A:", unique_to_a)

# Find all species across both areas
all_species = area_a_species.union(area_b_species)
print("All species found:", all_species)
```

### Checking Set Membership

```{code-cell} ipython3
# Check if we've visited a particular region
if "Asia" in regions_visited:
    print("We have visited Asia")

if "Antarctica" in regions_visited:
    print("We have visited Antarctica")
else:
    print("Antarctica not yet visited")
```

## Dictionaries

### Creating Dictionaries

```{code-cell} ipython3
# Dictionary storing attributes of a city
tokyo_info = {
    "name": "Tokyo",
    "population": 13929286,
    "coordinates": (35.6895, 139.6917),
    "country": "Japan",
    "established": 1603,
}
print("Tokyo information:", tokyo_info)
```

```{code-cell} ipython3
# Dictionary for a geographic survey point
survey_point = {
    "point_id": "SP001",
    "latitude": 40.7589,
    "longitude": -73.9851,
    "elevation": 87.3,
    "land_cover": "urban",
    "date_surveyed": "2023-06-15",
}
print("Survey point data:", survey_point)
```

### Accessing Dictionary Values

```{code-cell} ipython3
# Access specific information about Tokyo
city_name = tokyo_info["name"]
city_population = tokyo_info["population"]
city_coords = tokyo_info["coordinates"]

print(f"City: {city_name}")
print(f"Population: {city_population:,}")
print(f"Coordinates: {city_coords}")
```

### Safe Access with get()

```{code-cell} ipython3
# Safe access to dictionary values
area = tokyo_info.get("area_km2", "Not specified")
timezone = tokyo_info.get("timezone", "Unknown")

print(f"Area: {area}")
print(f"Timezone: {timezone}")
```

### Adding and Updating Values

```{code-cell} ipython3
# Add new information to our Tokyo dictionary
tokyo_info["area_km2"] = 2191
tokyo_info["timezone"] = "JST"
tokyo_info["population"] = 14000000  # Update population

print("Updated Tokyo info:", tokyo_info)
```

### Working with Geographic Feature Collections

```{code-cell} ipython3
# Collection of world capitals
world_capitals = {
    "Japan": {
        "capital": "Tokyo",
        "coordinates": (35.6895, 139.6917),
        "population": 13929286,
    },
    "France": {
        "capital": "Paris",
        "coordinates": (48.8566, 2.3522),
        "population": 2161000,
    },
    "UK": {
        "capital": "London",
        "coordinates": (51.5074, -0.1278),
        "population": 8982000,
    },
}

# Access information about France's capital
france_info = world_capitals["France"]
print(f"France's capital: {france_info['capital']}")
print(f"Population: {france_info['population']:,}")
```

### Dictionary Methods for Data Exploration

```{code-cell} ipython3
# Explore the structure of our Tokyo dictionary
print("Keys in tokyo_info:", list(tokyo_info.keys()))
print("Values in tokyo_info:", list(tokyo_info.values()))

# Check if a key exists
if "coordinates" in tokyo_info:
    print("Coordinate information is available")

# Get all countries in our capitals dictionary
countries = list(world_capitals.keys())
print("Countries in our database:", countries)
```

### Practical Example: GPS Waypoint Management

```{code-cell} ipython3
# GPS waypoint with comprehensive metadata
waypoint = {
    "id": "WP001",
    "name": "Trail Start",
    "latitude": 45.3311,
    "longitude": -121.7113,
    "elevation": 1200,
    "description": "Beginning of Pacific Crest Trail section",
    "waypoint_type": "trailhead",
    "facilities": ["parking", "restrooms", "water"],
    "difficulty": "easy",
}

print(f"Waypoint: {waypoint['name']}")
print(f"Location: {waypoint['latitude']}, {waypoint['longitude']}")
print(f"Elevation: {waypoint['elevation']} meters")
print(f"Available facilities: {', '.join(waypoint['facilities'])}")
```

## Data Structure Selection Guide

### When to Use Each Data Structure

## Key Takeaways

## Exercises

### Exercise 1: Using Lists

```{code-cell} ipython3

```

### Exercise 2: Using Tuples

```{code-cell} ipython3

```

### Exercise 3: Working with Sets

```{code-cell} ipython3

```

### Exercise 4: Working with Dictionaries

```{code-cell} ipython3

```

### Exercise 5: Nested Data Structures

```{code-cell} ipython3

```
