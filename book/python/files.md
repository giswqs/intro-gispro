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

[![image](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/giswqs/intro-gispro/blob/main/book/python/files.ipynb)
[![image](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/giswqs/intro-gispro/main?urlpath=lab/tree/book/python/files.ipynb)

# Working with Files

## Introduction

## Learning Objectives

## Creating a Sample File

```{code-cell} ipython3
sample_data = """35.6895,139.6917
34.0522,-118.2437
51.5074,-0.1278
-33.8688,151.2093
48.8566,2.3522"""

output_file = "coordinates.txt"

try:
    with open(output_file, "w") as file:
        file.write(sample_data)
    print(f"Sample file '{output_file}' has been created successfully.")
except Exception as e:
    print(f"An error occurred while creating the file: {e}")
```

## Reading and Writing Files

```{code-cell} ipython3
# Example of reading coordinates from a file and writing to another file
input_file = "coordinates.txt"
output_file = "output_coordinates.txt"

try:
    # Step 1: Read the coordinate data from our input file
    with open(input_file, "r") as infile:
        # readlines() returns a list where each element is a line from the file
        # Each line still includes the newline character (\n) at the end
        coordinates = infile.readlines()

    # Step 2: Process the data and write it to a new file with better formatting
    with open(output_file, "w") as outfile:
        for line in coordinates:
            # strip() removes whitespace (including \n) from both ends of the string
            # split(",") breaks the line into parts wherever it finds a comma
            lat, lon = line.strip().split(",")

            # Write the formatted data to our output file
            # The \n adds a newline character so each coordinate is on its own line
            outfile.write(f"Latitude: {lat}, Longitude: {lon}\n")

    print(f"Coordinates have been written to {output_file}")

except FileNotFoundError:
    print(f"Error: The file {input_file} was not found.")
    print(
        "Make sure you ran the previous code cell to create the coordinates.txt file."
    )
```

## Exception Handling

```{code-cell} ipython3
# Example of exception handling when parsing coordinates
def parse_coordinates(line):
    """
    Parse a line of text into latitude and longitude coordinates.

    Args:
        line (str): A string containing coordinates in the format "lat,lon"

    Returns:
        tuple: (latitude, longitude) as floats, or None if parsing fails
    """
    try:
        # Attempt to split the line and convert to numbers
        lat, lon = line.strip().split(",")
        lat = float(lat)  # This might raise ValueError if lat isn't a valid number
        lon = float(lon)  # This might raise ValueError if lon isn't a valid number
        return lat, lon

    except ValueError as e:
        # This happens when we can't convert to float or split doesn't work as expected
        print(f"Data format error: {e}. Could not parse line: '{line.strip()}'")
        return None

    except Exception as e:
        # This catches any other unexpected errors
        print(f"An unexpected error occurred: {e}")
        return None


# Test with both valid and invalid data
test_lines = [
    "35.6895,139.6917",  # Valid coordinates (Tokyo)
    "invalid data",  # Invalid format
    "45.0,-119.0",  # Valid coordinates
    "45.0,not_a_number",  # Invalid longitude
    "only_one_value",  # Missing comma
]

print("Testing coordinate parsing:")
for line in test_lines:
    coordinates = parse_coordinates(line)
    if coordinates:
        print(f"✓ Successfully parsed: {coordinates}")
    else:
        print(f"✗ Failed to parse: '{line}'")
```

## Combining File Handling and Exception Handling

```{code-cell} ipython3
# Example of robust file handling with exceptions
def process_geospatial_file(input_file):
    """
    Process a file containing coordinate data, handling various potential errors.

    This function demonstrates robust file processing by:
    - Handling missing files gracefully
    - Continuing processing even when individual lines fail
    - Providing informative feedback about the processing results
    """
    processed_count = 0
    error_count = 0

    try:
        print(f"Starting to process file: {input_file}")

        with open(input_file, "r") as infile:
            for line_number, line in enumerate(infile, 1):
                # Skip empty lines
                if not line.strip():
                    continue

                coordinates = parse_coordinates(line)
                if coordinates:
                    lat, lon = coordinates
                    print(
                        f"Line {line_number}: Processed coordinates ({lat:.4f}, {lon:.4f})"
                    )
                    processed_count += 1
                else:
                    print(f"Line {line_number}: Skipped due to parsing error")
                    error_count += 1

    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        print("Please check the file path and make sure the file exists.")
        return

    except PermissionError:
        print(f"Error: Permission denied when trying to read '{input_file}'.")
        print("Please check if you have read permissions for this file.")
        return

    except Exception as e:
        print(f"An unexpected error occurred while processing the file: {e}")
        return

    finally:
        # This block always runs, whether there was an error or not
        print(f"\n--- Processing Summary ---")
        print(f"Successfully processed: {processed_count} coordinates")
        print(f"Errors encountered: {error_count} lines")
        print(f"Finished processing {input_file}")


# Example usage with our coordinates file
process_geospatial_file("coordinates.txt")
```

## Working with Different File Formats

```{code-cell} ipython3
# Create a CSV-style file with city names and coordinates
csv_data = """City,Latitude,Longitude
Tokyo,35.6895,139.6917
Los Angeles,34.0522,-118.2437
London,51.5074,-0.1278
Sydney,-33.8688,151.2093
Paris,48.8566,2.3522"""

csv_file = "cities.csv"

try:
    with open(csv_file, "w") as file:
        file.write(csv_data)
    print(f"CSV file '{csv_file}' created successfully.")
except Exception as e:
    print(f"Error creating CSV file: {e}")
```

```{code-cell} ipython3
def read_city_coordinates(filename):
    """
    Read city coordinate data from a CSV-style file.

    Returns a list of dictionaries containing city information.
    """
    cities = []

    try:
        with open(filename, "r") as file:
            lines = file.readlines()

            # Skip the header line (first line)
            for line_num, line in enumerate(lines[1:], 2):  # Start from line 2
                try:
                    # Parse each line
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        city_name = parts[0]
                        latitude = float(parts[1])
                        longitude = float(parts[2])

                        cities.append(
                            {
                                "name": city_name,
                                "latitude": latitude,
                                "longitude": longitude,
                            }
                        )

                except ValueError as e:
                    print(f"Warning: Could not parse line {line_num}: {line.strip()}")
                    continue

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
        return []
    except Exception as e:
        print(f"Error reading file: {e}")
        return []

    return cities


# Read and display the city data
cities = read_city_coordinates("cities.csv")

print(f"Successfully loaded {len(cities)} cities:")
for city in cities:
    print(f"- {city['name']}: ({city['latitude']:.4f}, {city['longitude']:.4f})")
```

## Key Takeaways

## Exercises

### Exercise 1: Reading and Writing Files

```{code-cell} ipython3

```

### Exercise 2: Processing Coordinates from a File

```{code-cell} ipython3
# Create a sample coordinates.txt file
sample_data = """35.6895,139.6917
34.0522,-118.2437
51.5074,-0.1278
-33.8688,151.2093
48.8566,2.3522"""

output_file = "coordinates.txt"

try:
    with open(output_file, "w") as file:
        file.write(sample_data)
    print(f"Sample file '{output_file}' has been created successfully.")
except Exception as e:
    print(f"An error occurred while creating the file: {e}")
```

```{code-cell} ipython3

```

### Exercise 3: Exception Handling in Data Processing

```{code-cell} ipython3

```
