---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.17.2
kernelspec:
  name: python3
  display_name: Python 3
  language: python
---

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/intro-gispro/blob/main/book/python/variables.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/intro-gispro/main?urlpath=lab/tree/book/python/variables.ipynb)

# Variables and Data Types

## Introduction

## Learning Objectives

## Variables in Python

```{code-cell} ipython3
num_points = 120
```

```{code-cell} ipython3
print(num_points)
```

```{code-cell} ipython3
num_points
```

### Variable Assignment

```{code-cell} ipython3
# Start with a number
location_data = 42.3601

# Change to text
location_data = "Boston"

# Change to a list of coordinates
location_data = [42.3601, -71.0589]

print(location_data)
```

## Naming Variables

### Good Naming Examples for Geospatial Data

```{code-cell} ipython3
# Good variable names for geospatial data
latitude = 42.3601
longitude = -71.0589
elevation = 147.2
city_name = "Boston"
population = 685094
coordinate_system = "WGS 84"
```

### Poor Naming Examples to Avoid

```{code-cell} ipython3
# Poor variable names - avoid these
x = 42.3601          # Too generic
data = "Boston"      # Too vague
temp = 25.6         # Ambiguous - temperature or temporary?
l = [42.36, -71.06] # Single letter variables are hard to understand
```

## Data Types

```{code-cell} ipython3
num_features = 500  # Represents the number of features in a geospatial dataset
```

```{code-cell} ipython3
latitude = 35.6895  # Represents the latitude of a point on Earth's surface
longitude = 139.6917  # Represents the longitude of a point on Earth's surface
```

```{code-cell} ipython3
coordinate_system = "WGS 84"  # Represents a commonly used coordinate system
```

```{code-cell} ipython3
is_georeferenced = True  # Represents whether a dataset is georeferenced or not
```

```{code-cell} ipython3
coordinates = [
    35.6895,
    139.6917,
]  # A list representing latitude and longitude of a point
```

```{code-cell} ipython3
feature_attributes = {
    "name": "Mount Fuji",
    "height_meters": 3776,
    "type": "Stratovolcano",
    "location": [35.3606, 138.7274],
}
```

## Escape Characters

```{code-cell} ipython3
print("Hello World!\nThis is a Python script.")
```

```{code-cell} ipython3
print("This is the first line.\n\tThis is the second line. It is indented.")
```

```{code-cell} ipython3
print("What's your name?")
```

```{code-cell} ipython3
print('What\'s your name?')
```

## Comments in Python

```{code-cell} ipython3
# This is a comment
num_points = 120  # This is an inline comment
```

## Working with Variables and Data Types

```{code-cell} ipython3
num_features += 20
print("Updated number of features:", num_features)
```

```{code-cell} ipython3
import math

latitude = 35.6895
latitude_radians = math.radians(latitude)
print("Latitude in radians:", latitude_radians)
```

```{code-cell} ipython3
coordinates = [35.6895, 139.6917]
coordinates.append(34.0522)  # Adding latitude of Los Angeles
coordinates.append(-118.2437)  # Adding longitude of Los Angeles
print("Updated coordinates:", coordinates)
```

```{code-cell} ipython3
mount_fuji_name = feature_attributes["name"]
mount_fuji_height = feature_attributes["height_meters"]
print(f"{mount_fuji_name} is {mount_fuji_height} meters high.")
```

## Basic String Operations

### Changing Case

```{code-cell} ipython3
city_name = "San Francisco"

# Convert to lowercase
city_lowercase = city_name.lower()
print("Lowercase:", city_lowercase)

# Convert to uppercase
city_uppercase = city_name.upper()
print("Uppercase:", city_uppercase)

# Convert to title case (first letter of each word capitalized)
city_title = city_name.title()
print("Title case:", city_title)
```

### Replacing Text

```{code-cell} ipython3
original_city = "San Francisco"
new_city = original_city.replace("San", "Los")
print("Original:", original_city)
print("Modified:", new_city)
```

### Other Useful String Methods

```{code-cell} ipython3
location_data = "  Mount Everest  "

# Remove whitespace from beginning and end
clean_location = location_data.strip()
print("Cleaned:", clean_location)
```

## Key Takeaways

## Exercises

### Exercise 1: Variable Assignment and Basic Operations

```{code-cell} ipython3

```

### Exercise 2: Working with Strings

```{code-cell} ipython3

```
