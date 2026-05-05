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

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/intro-gispro/blob/main/book/geospatial/xarray.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/intro-gispro/main?urlpath=lab/tree/book/geospatial/xarray.ipynb)

# Multi-dimensional Data Analysis with Xarray

## Introduction

## Learning Objectives

## Understanding Xarray's Data Model

### Core Data Structures

### Why This Structure Matters

## Setting Up Your Environment

### Installing Required Packages

```{code-cell} ipython3
%pip install xarray pooch pygis
```

### Importing Libraries and Configuration

```{code-cell} ipython3
import matplotlib.pyplot as plt
import numpy as np
import xarray as xr

# Configure Xarray for better display and performance
xr.set_options(keep_attrs=True, display_expand_data=False)

# Configure NumPy display for cleaner output
np.set_printoptions(threshold=10, edgeitems=2)

# Configure matplotlib for better plots
plt.rcParams["figure.dpi"] = 150
```

## Loading and Exploring Real Climate Data

### Loading Tutorial Data

```{code-cell} ipython3
# Load a climate dataset with air temperature measurements
ds = xr.tutorial.open_dataset("air_temperature")
ds
```

## Working with DataArrays

### Accessing DataArrays from Datasets

```{code-cell} ipython3
# Extract the air temperature DataArray using dictionary notation
temperature = ds["air"]
temperature
```

```{code-cell} ipython3
# Same result using attribute access
temperature = ds.air
temperature
```

### Exploring DataArray Components

```{code-cell} ipython3
# Examine the actual data values (a NumPy array)
print("Data shape:", temperature.values.shape)
print("Data type:", temperature.values.dtype)
print("First few values:", temperature.values.flat[:5])
```

```{code-cell} ipython3
# Understand the dimension structure
print("Dimensions:", temperature.dims)
print("Dimension sizes:", temperature.sizes)
```

```{code-cell} ipython3
# Explore the coordinate information
print("Coordinates:")
for name, coord in temperature.coords.items():
    print(f"  {name}: {coord.values[:3]}... (showing first 3 values)")
```

```{code-cell} ipython3
# Examine metadata attributes
print("Attributes:")
for key, value in temperature.attrs.items():
    print(f"  {key}: {value}")
```

## Intuitive Data Selection and Indexing

### Label-Based Selection

```{code-cell} ipython3
# Select data for a specific date and location
point_data = temperature.sel(time="2013-01-01", lat=40.0, lon=260.0)
point_data
```

### Time Range Selection

```{code-cell} ipython3
# Select all data for January 2013
january_data = temperature.sel(time=slice("2013-01-01", "2013-01-31"))
print(f"January 2013 data shape: {january_data.shape}")
print(f"Time range: {january_data.time.values[0]} to {january_data.time.values[-1]}")
```

### Nearest Neighbor Selection

```{code-cell} ipython3
# Select data nearest to a location that might not be exactly on the grid
nearest_data = temperature.sel(lat=40.5, lon=255.7, method="nearest")
actual_coords = nearest_data.sel(time="2013-01-01")
print(f"Requested: lat=40.5, lon=255.7")
print(f"Actual: lat={actual_coords.lat.values}, lon={actual_coords.lon.values}")
```

## Performing Operations on Multi-Dimensional Data

### Statistical Operations Across Dimensions

```{code-cell} ipython3
# Calculate the temporal mean (average temperature at each location)
mean_temperature = temperature.mean(dim="time")
print(f"Original data shape: {temperature.shape}")
print(f"Time-averaged data shape: {mean_temperature.shape}")
print(
    f"Temperature range: {mean_temperature.min().values:.1f} to {mean_temperature.max().values:.1f} K"
)
```

### Computing Anomalies

```{code-cell} ipython3
# Calculate temperature anomalies by subtracting the time mean from each time step
anomalies = temperature - mean_temperature
print(f"Anomaly range: {anomalies.min().values:.1f} to {anomalies.max().values:.1f} K")

# Find the location and time of the largest positive anomaly
max_anomaly = anomalies.max()
max_location = anomalies.where(anomalies == max_anomaly, drop=True)
print(f"Largest positive anomaly: {max_anomaly.values:.1f} K")
```

### Spatial Statistics

```{code-cell} ipython3
# Calculate area-weighted spatial mean for each time step
spatial_mean = temperature.mean(dim=["lat", "lon"])
print(f"Spatial mean temperature time series shape: {spatial_mean.shape}")

# Find the warmest and coldest time periods
warmest_date = spatial_mean.time[spatial_mean.argmax()]
coldest_date = spatial_mean.time[spatial_mean.argmin()]
print(f"Warmest period: {warmest_date.values}")
print(f"Coldest period: {coldest_date.values}")
```

## Data Visualization with Xarray

### Plotting 2D Spatial Data

```{code-cell} ipython3
# Create a map of long-term average temperature
fig, ax = plt.subplots(figsize=(12, 6))
mean_temperature.plot(ax=ax, cmap="RdYlBu_r", add_colorbar=True)
plt.title("Long-term Average Air Temperature", fontsize=14, fontweight="bold")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.tight_layout()
plt.show()
```

### Customizing Spatial Plots

```{code-cell} ipython3
# Create a more customized visualization
fig, ax = plt.subplots(figsize=(12, 6))
plot = mean_temperature.plot(
    ax=ax,
    cmap="RdYlBu_r",
    levels=20,  # Number of contour levels
    add_colorbar=True,
    cbar_kwargs={"label": "Temperature (K)", "shrink": 0.8, "pad": 0.02},
)
plt.title("Mean Air Temperature (2013)", fontsize=16, fontweight="bold")
plt.xlabel("Longitude (°E)", fontsize=12)
plt.ylabel("Latitude (°N)", fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Time Series Visualization

```{code-cell} ipython3
# Select and plot time series for a specific location
location_ts = temperature.sel(lat=40.0, lon=260.0)

fig, ax = plt.subplots(figsize=(12, 6))
location_ts.plot(ax=ax, linewidth=1.5, color="darkblue")
plt.title("Temperature Time Series at 40°N, 260°E", fontsize=14, fontweight="bold")
plt.xlabel("Time")
plt.ylabel("Temperature (K)")
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

## Working with Datasets: Multiple Variables

### Exploring Dataset Structure

```{code-cell} ipython3
# Examine all variables in the dataset
print("Data variables in the dataset:")
for var_name, var_info in ds.data_vars.items():
    print(f"  {var_name}: {var_info.dims}, shape {var_info.shape}")

print(f"\nShared coordinates: {list(ds.coords.keys())}")
print(f"Global attributes: {len(ds.attrs)} metadata items")
```

### Dataset-Level Operations

```{code-cell} ipython3
# Calculate temporal statistics for all variables in the dataset
dataset_means = ds.mean(dim="time")
dataset_means
```

## The Power of Label-Based Operations

### The NumPy Approach: Index-Based Selection

```{code-cell} ipython3
# Extract raw arrays and coordinates
lat_values = ds.air.lat.values
lon_values = ds.air.lon.values
temp_values = ds.air.values

print(f"Data shape: {temp_values.shape}")
print("To plot the first time step, you need to remember:")
print("- Time is dimension 0")
print("- Latitude is dimension 1")
print("- Longitude is dimension 2")
```

```{code-cell} ipython3
# Plot using NumPy approach - requires careful index management
fig, ax = plt.subplots(figsize=(12, 6))
im = ax.pcolormesh(lon_values, lat_values, temp_values[0, :, :], cmap="RdYlBu_r")
plt.colorbar(im, ax=ax, label="Temperature (K)")
plt.title("First Time Step (NumPy approach)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.show()
```

### The Xarray Approach: Label-Based Selection

```{code-cell} ipython3
# Same result with Xarray - much more readable and less error-prone
ds.air.isel(time=0).plot(figsize=(12, 6), cmap="RdYlBu_r")
plt.title("First Time Step (Xarray approach)")
plt.show()
```

```{code-cell} ipython3
# Select by actual date rather than array index
ds.air.sel(time="2013-01-01T00:00:00").plot(figsize=(12, 6), cmap="RdYlBu_r")
plt.title("Temperature on January 1, 2013")
plt.show()
```

## Advanced Indexing Techniques

### Position-Based vs. Label-Based Indexing

```{code-cell} ipython3
# Position-based indexing using isel() - useful for systematic sampling
first_last_times = ds.air.isel(time=[0, -1])  # First and last time steps
print(f"Selected time steps: {first_last_times.time.values}")

# Label-based indexing using sel() - useful for specific values
specific_months = ds.air.sel(time=slice("2013-05", "2013-07"))
print(f"May-July 2013 contains {len(specific_months.time)} time steps")
```

### Boolean Indexing and Conditional Selection

```{code-cell} ipython3
# Find locations where average temperature exceeds a threshold
warm_locations = mean_temperature.where(mean_temperature > 280)  # 280 K ≈ 7°C
warm_count = warm_locations.count()
print(f"Number of grid points with mean temperature > 280 K: {warm_count.values}")

# Find time periods when spatial average temperature was unusually high
temp_threshold = spatial_mean.quantile(0.9)  # 90th percentile
warm_periods = spatial_mean.where(spatial_mean > temp_threshold, drop=True)
print(f"Number of exceptionally warm time periods: {len(warm_periods)}")
```

## High-Level Computational Operations

### GroupBy Operations for Temporal Analysis

```{code-cell} ipython3
# Calculate seasonal climatology
seasonal_means = ds.air.groupby("time.season").mean()
print("Seasonal temperature patterns:")
seasonal_means
```

```{code-cell} ipython3
# Visualize seasonal patterns
fig, axes = plt.subplots(2, 2, figsize=(12, 6))
seasons = ["DJF", "MAM", "JJA", "SON"]
season_names = ["Winter", "Spring", "Summer", "Fall"]

for i, (season, name) in enumerate(zip(seasons, season_names)):
    ax = axes[i // 2, i % 2]
    seasonal_means.sel(season=season).plot(ax=ax, cmap="RdYlBu_r", add_colorbar=False)
    ax.set_title(f"{name} ({season})")
    ax.set_xlabel("Longitude")
    ax.set_ylabel("Latitude")

plt.tight_layout()
plt.show()
```

### Rolling Window Operations

```{code-cell} ipython3
# Create a smoothed time series using a rolling window
location_data = temperature.sel(lat=40.0, lon=260.0)

fig, ax = plt.subplots(figsize=(12, 6))

# Plot original data
location_data.plot(ax=ax, alpha=0.5, label="Original", color="lightblue")

# Plot smoothed data using a 7.5-day rolling window (30 time steps at 6-hour intervals)
smoothed_data = location_data.rolling(time=30, center=True).mean()
smoothed_data.plot(ax=ax, label="7.5-day smoothed", color="darkblue", linewidth=2)

plt.title("Temperature Time Series: Original vs Smoothed")
plt.xlabel("Time")
plt.ylabel("Temperature (K)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

### Weighted Operations

```{code-cell} ipython3
# Create simple area weights (this is a simplified example)
# In practice, you would use proper latitude-based area weighting
lat_weights = np.cos(np.radians(ds.air.lat))
area_weighted_mean = ds.air.weighted(lat_weights).mean(dim=["lat", "lon"])

# Compare simple vs area-weighted spatial averages
fig, ax = plt.subplots(figsize=(12, 6))
spatial_mean.plot(ax=ax, label="Simple average", alpha=0.7)
area_weighted_mean.plot(ax=ax, label="Area-weighted average", linewidth=2)
plt.title("Spatial Temperature Averages: Simple vs Area-Weighted")
plt.xlabel("Time")
plt.ylabel("Temperature (K)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()
```

## Data Input and Output

### Understanding NetCDF Format

### Writing Data to NetCDF

```{code-cell} ipython3
# Prepare data for saving (ensure proper data types)
output_ds = ds.copy()
output_ds["air"] = output_ds["air"].astype("float32")  # Reduce file size

# Add processing metadata
output_ds.attrs["processing_date"] = str(np.datetime64("now"))
output_ds.attrs["created_by"] = "GIS Pro"

# Save to NetCDF file
output_ds.to_netcdf("processed_air_temperature.nc")
print("Dataset saved to processed_air_temperature.nc")
```

### Reading Data from NetCDF

```{code-cell} ipython3
# Load the saved dataset
reloaded_ds = xr.open_dataset("processed_air_temperature.nc")
print("Successfully reloaded dataset:")
print(f"Variables: {list(reloaded_ds.data_vars.keys())}")
print(f"Processing date: {reloaded_ds.attrs.get('processing_date', 'Not specified')}")
print(f"Data matches original: {reloaded_ds.air.equals(ds.air.astype('float32'))}")
```

## Key Takeaways

## Further Reading

## Exercises

### Exercise 1: Exploring a New Dataset

```{code-cell} ipython3

```

### Exercise 2: Data Selection and Indexing

```{code-cell} ipython3

```

### Exercise 3: Performing Arithmetic Operations

```{code-cell} ipython3

```

### Exercise 4: GroupBy and Temporal Analysis

```{code-cell} ipython3

```

### Exercise 5: Data Storage and Retrieval

```{code-cell} ipython3

```
