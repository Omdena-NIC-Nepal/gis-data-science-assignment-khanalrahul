import numpy as np
import rasterio
import matplotlib.pyplot as plt

# Define the file paths
temperature_2020_path = 'Nepal_Climate_change/nepal_temperature_2020.tif'
temperature_2050_path = 'Nepal_Climate_change/nepal_temperature_2050.tif'
precipitation_2020_path = 'Nepal_Climate_change/nepal_precipitation_2020.tif'
precipitation_2050_path = 'Nepal_Climate_change/nepal_precipitation_2050.tif'

# Read raster data using rasterio
with rasterio.open(temperature_2020_path) as src:
    temperature_2020 = src.read(1)

with rasterio.open(temperature_2050_path) as src:
    temperature_2050 = src.read(1)

with rasterio.open(precipitation_2020_path) as src:
    precipitation_2020 = src.read(1)

with rasterio.open(precipitation_2050_path) as src:
    precipitation_2050 = src.read(1)

# Compute basic statistics
def compute_statistics(data, label):
    print(f'{label} Statistics:')
    print(f'Mean: {np.mean(data)}')
    print(f'Median: {np.median(data)}')
    print(f'Min: {np.min(data)}')
    print(f'Max: {np.max(data)}')
    print('')

compute_statistics(temperature_2020, 'Temperature 2020')
compute_statistics(temperature_2050, 'Temperature 2050')
compute_statistics(precipitation_2020, 'Precipitation 2020')
compute_statistics(precipitation_2050, 'Precipitation 2050')

# Plot histograms
def plot_histogram(data, label):
    plt.hist(data.flatten(), bins=50, alpha=0.7, label=label)

plt.figure(figsize=(10, 5))
plot_histogram(temperature_2020, 'Temperature 2020')
plot_histogram(temperature_2050, 'Temperature 2050')
plt.title('Temperature Distribution')
plt.xlabel('Temperature')
plt.ylabel('Frequency')
plt.legend()
plt.show()

plt.figure(figsize=(10, 5))
plot_histogram(precipitation_2020, 'Precipitation 2020')
plot_histogram(precipitation_2050, 'Precipitation 2050')
plt.title('Precipitation Distribution')
plt.xlabel('Precipitation')
plt.ylabel('Frequency')
plt.legend()
plt.show()