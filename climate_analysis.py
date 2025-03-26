import geopandas as gpd
import rasterio

# Defining the file paths
admin_regions_path = 'Nepal_Climate_change/nepal_admin_regions.gpkg'
rivers_path = 'Nepal_Climate_change/nepal_rivers.gpkg'
glaciers_path = 'Nepal_Climate_change/nepal_glaciers.gpkg'
temperature_2020_path = 'Nepal_Climate_change/nepal_temperature_2020.tif'
temperature_2050_path = 'Nepal_Climate_change/nepal_temperature_2050.tif'
precipitation_2020_path = 'Nepal_Climate_change/nepal_precipitation_2020.tif'
precipitation_2050_path = 'Nepal_Climate_change/nepal_precipitation_2050.tif'

# Reading the vector data using geopandas
admin_regions = gpd.read_file(admin_regions_path)
rivers = gpd.read_file(rivers_path)
glaciers = gpd.read_file(glaciers_path)

# Reading raster data using rasterio
with rasterio.open(temperature_2020_path) as src:
    temperature_2020 = src.read()

with rasterio.open(temperature_2050_path) as src:
    temperature_2050 = src.read()

with rasterio.open(precipitation_2020_path) as src:
    precipitation_2020 = src.read()

with rasterio.open(precipitation_2050_path) as src:
    precipitation_2050 = src.read()

# Printing the data to verify
print(admin_regions.head())
print(rivers.head())
print(glaciers.head())
print(temperature_2020.shape)
print(temperature_2050.shape)
print(precipitation_2020.shape)
print(precipitation_2050.shape)