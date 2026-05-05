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

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/intro-gispro/blob/main/book/python/looping.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/intro-gispro/main?urlpath=lab/tree/book/python/looping.ipynb)

# Loops and Conditional Statements

## Introduction

## Learning Objectives

## For Loops

### Basic For Loop Syntax

```{code-cell} ipython3
coordinates = [
    (35.6895, 139.6917),
    (34.0522, -118.2437),
    (51.5074, -0.1278),
]  # List of tuples representing coordinates

for lat, lon in coordinates:
    print(f"Latitude: {lat}, Longitude: {lon}")
```

### Processing Multiple Data Points

```{code-cell} ipython3
def calculate_distance(lat1, lon1, lat2, lon2):
    # Placeholder for distance calculation logic
    return ((lat2 - lat1) ** 2 + (lon2 - lon1) ** 2) ** 0.5


reference_point = (0, 0)  # Reference point (latitude, longitude)

for lat, lon in coordinates:
    distance = calculate_distance(reference_point[0], reference_point[1], lat, lon)
    print(f"Distance from {reference_point} to ({lat}, {lon}): {distance:.2f}")
```

### Iterating Through Geographic Collections

```{code-cell} ipython3
# Working with a list of place names
cities = ["New York", "Los Angeles", "Chicago", "Houston", "Phoenix"]

print("Major US Cities:")
for i, city in enumerate(cities):
    print(f"{i+1}. {city}")
```

## While Loops

### Basic While Loop Structure

```{code-cell} ipython3
counter = 0
while counter < len(coordinates):
    lat, lon = coordinates[counter]
    print(f"Processing coordinate: ({lat}, {lon})")
    counter += 1
```

### Practical While Loop Example

```{code-cell} ipython3
# Simulate searching for a coordinate within a certain range
import random

target_latitude = 40.0
tolerance = 0.1
attempts = 0
max_attempts = 10

print(f"Searching for coordinates near latitude {target_latitude}")

while attempts < max_attempts:
    # Simulate getting a new coordinate
    random_lat = random.uniform(39.5, 40.5)
    random_lon = random.uniform(-74.5, -73.5)
    attempts += 1

    print(f"Attempt {attempts}: Found coordinate ({random_lat:.4f}, {random_lon:.4f})")

    # Check if we're close enough to the target
    if abs(random_lat - target_latitude) <= tolerance:
        print(f"✓ Found coordinate within tolerance after {attempts} attempts!")
        break
else:
    print(f"✗ Could not find suitable coordinate within {max_attempts} attempts")
```

## Control Statements: Making Decisions in Your Code

### The if Statement

```{code-cell} ipython3
for lat, lon in coordinates:
    if lat > 0:
        print(f"{lat} is in the Northern Hemisphere")
    elif lat < 0:
        print(f"{lat} is in the Southern Hemisphere")
    else:
        print(f"{lat} is near the equator")
```

### Multiple Conditions and Complex Logic

```{code-cell} ipython3
for lat, lon in coordinates:
    if lat > 0:
        hemisphere = "Northern"
    else:
        hemisphere = "Southern"

    if lon > 0:
        direction = "Eastern"
    else:
        direction = "Western"

    print(
        f"The coordinate ({lat}, {lon}) is in the {hemisphere} Hemisphere and {direction} Hemisphere."
    )
```

### Logical Operators for Complex Conditions

```{code-cell} ipython3
# Classify coordinates by quadrant
for lat, lon in coordinates:
    if lat > 0 and lon > 0:
        quadrant = "Northeast"
    elif lat > 0 and lon < 0:
        quadrant = "Northwest"
    elif lat < 0 and lon > 0:
        quadrant = "Southeast"
    else:  # lat < 0 and lon < 0
        quadrant = "Southwest"

    print(f"Coordinate ({lat}, {lon}) is in the {quadrant} quadrant")
```

## Combining Loops and Control Statements

```{code-cell} ipython3
filtered_coordinates = []
for lat, lon in coordinates:
    if lon > 0:
        filtered_coordinates.append((lat, lon))
print(f"Filtered coordinates (only with positive longitude): {filtered_coordinates}")
```

### Counting and Analyzing Data

```{code-cell} ipython3
southern_count = 0
for lat, lon in coordinates:
    if lat < 0:
        southern_count += 1
print(f"Number of coordinates in the Southern Hemisphere: {southern_count}")
```

### Building Summary Statistics

```{code-cell} ipython3
# Analyze a set of coordinates
analysis_coordinates = [
    (40.7128, -74.0060),  # New York
    (-33.8688, 151.2093),  # Sydney
    (51.5074, -0.1278),  # London
    (-1.2921, 36.8219),  # Nairobi
    (35.6762, 139.6503),  # Tokyo
]

# Initialize counters
northern_count = 0
southern_count = 0
eastern_count = 0
western_count = 0
valid_coordinates = []

print("Coordinate Analysis:")
print("-" * 40)

for lat, lon in analysis_coordinates:
    # Validate coordinates (basic check)
    if -90 <= lat <= 90 and -180 <= lon <= 180:
        valid_coordinates.append((lat, lon))

        # Count by hemisphere
        if lat >= 0:
            northern_count += 1
        else:
            southern_count += 1

        # Count by longitude
        if lon >= 0:
            eastern_count += 1
        else:
            western_count += 1

        print(f"Valid: ({lat:7.4f}, {lon:8.4f})")
    else:
        print(f"Invalid: ({lat}, {lon}) - coordinates out of range")

print(f"\nSummary:")
print(f"Valid coordinates: {len(valid_coordinates)}")
print(f"Northern Hemisphere: {northern_count}")
print(f"Southern Hemisphere: {southern_count}")
print(f"Eastern Longitude: {eastern_count}")
print(f"Western Longitude: {western_count}")
```

## Loop and Control Statement Decision Guide

## Key Takeaways

## Exercises

### Exercise 1: Using For Loops to Process Coordinate Lists

```{code-cell} ipython3

```

### Exercise 2: While Loops for Iterative Processing

```{code-cell} ipython3

```

### Exercise 3: Conditional Logic in Loops

```{code-cell} ipython3

```

### Exercise 4: Filtering Data with Combined Loops and Conditionals

```{code-cell} ipython3

```

### Exercise 5: Generating and Analyzing Random Coordinates

```{code-cell} ipython3

```
