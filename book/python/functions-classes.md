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
# Functions and Classes

## Introduction

## Learning Objectives

## Functions: Building Reusable Code Blocks

### Defining a Simple Function

```{code-cell} ipython3
def add(a, b):
    return a + b


# Example usage
result = add(5, 3)
print(f"Result: {result}")
```

### Parameters with Default Values

```{code-cell} ipython3
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"


# Example usage
print(greet("Alice"))  # Uses the default greeting
print(greet("Bob", "Hi"))  # Overrides the default greeting
```

### Understanding Function Calls

```{code-cell} ipython3
# Function to multiply two numbers
def multiply(a, b):
    return a * b


# Calling the function
result = multiply(4, 5)
print(f"Multiplication Result: {result}")
```

### Geospatial Example: Haversine Function

```{code-cell} ipython3
from math import radians, sin, cos, sqrt, atan2
```

```{code-cell} ipython3
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth radius in kilometers
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance


# Example usage
distance = haversine(35.6895, 139.6917, 34.0522, -118.2437)
print(f"Distance: {distance:.2f} km")
```

### Function with Default Values and Geospatial Application

```{code-cell} ipython3
def haversine(lat1, lon1, lat2, lon2, radius=6371.0):
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)
    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = radius * c
    return distance


# Example usage in kilometers
distance_km = haversine(35.6895, 139.6917, 34.0522, -118.2437)
print(f"Distance in kilometers: {distance_km:.2f} km")

# Example usage in miles (radius of Earth is approximately 3958.8 miles)
distance_miles = haversine(35.6895, 139.6917, 34.0522, -118.2437, radius=3958.8)
print(f"Distance in miles: {distance_miles:.2f} miles")
```

### Processing Multiple Coordinates

```{code-cell} ipython3
def batch_haversine(coord_list):
    distances = []
    for i in range(len(coord_list) - 1):
        lat1, lon1 = coord_list[i]
        lat2, lon2 = coord_list[i + 1]
        distance = haversine(lat1, lon1, lat2, lon2)
        distances.append(distance)
    return distances


# Example usage
coordinates = [(35.6895, 139.6917), (34.0522, -118.2437), (40.7128, -74.0060)]
distances = batch_haversine(coordinates)
print(f"Distances: {distances}")
```

### Advanced Parameter Handling

#### Variable Arguments with \*args

```{code-cell} ipython3
def average(*numbers):
    return sum(numbers) / len(numbers)


# Example usage
print(average(10, 20, 30))  # 20.0
print(average(5, 15, 25, 35))  # 20.0
```

#### Keyword Arguments with \*\*kwargs

```{code-cell} ipython3
def describe_point(latitude, longitude, **kwargs):
    description = f"Point at ({latitude}, {longitude})"

    # Add optional keyword arguments to the description
    for key, value in kwargs.items():
        description += f", {key}: {value}"

    return description


# Example usage
print(describe_point(35.6895, 139.6917, name="Tokyo", population=37400000))
print(describe_point(34.0522, -118.2437, name="Los Angeles", state="California"))
```

## Classes: Organizing Data and Behavior Together

### Defining a Simple Class

```{code-cell} ipython3
class Point:
    def __init__(self, latitude, longitude, name=None):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name

    def __str__(self):
        return f"{self.name or 'Point'} ({self.latitude}, {self.longitude})"


# Example usage
point1 = Point(35.6895, 139.6917, "Tokyo")
print(point1)
```

### Adding Methods to a Class

```{code-cell} ipython3
class Point:
    def __init__(self, latitude, longitude, name=None):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name

    def distance_to(self, other_point):
        return haversine(
            self.latitude, self.longitude, other_point.latitude, other_point.longitude
        )


# Example usage
point1 = Point(35.6895, 139.6917, "Tokyo")
point2 = Point(34.0522, -118.2437, "Los Angeles")
print(
    f"Distance from {point1.name} to {point2.name}: {point1.distance_to(point2):.2f} km"
)
```

### Constructor with Default Values

```{code-cell} ipython3
class Point:
    def __init__(self, latitude, longitude, name="Unnamed"):
        self.latitude = latitude
        self.longitude = longitude
        self.name = name
```

## Combining Functions and Classes

```{code-cell} ipython3
class Route:
    def __init__(self, points):
        self.points = points

    def total_distance(self):
        total_dist = 0
        for i in range(len(self.points) - 1):
            total_dist += self.points[i].distance_to(self.points[i + 1])
        return total_dist


# Example usage
route = Route([point1, point2])
print(f"Total distance: {route.total_distance():.2f} km")
```

## Function and Class Design Guidelines

## Key Takeaways

## Exercises

### Exercise 1: Calculating Distances with Functions

```{code-cell} ipython3

```

### Exercise 2: Batch Distance Calculation

```{code-cell} ipython3

```

### Exercise 3: Creating and Using a Point Class

```{code-cell} ipython3

```
