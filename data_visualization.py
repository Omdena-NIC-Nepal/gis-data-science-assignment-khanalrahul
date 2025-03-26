import geopandas as gpd
import matplotlib.pyplot as plt

# Defining the file paths
admin_regions_path = 'Nepal_Climate_change/nepal_admin_regions.gpkg'
rivers_path = 'Nepal_Climate_change/nepal_rivers.gpkg'
glaciers_path = 'Nepal_Climate_change/nepal_glaciers.gpkg'

# Reading vector data using geopandas
admin_regions = gpd.read_file(admin_regions_path)
rivers = gpd.read_file(rivers_path)
glaciers = gpd.read_file(glaciers_path)

# Plotting the data
fig, ax = plt.subplots(figsize=(10, 10))
admin_regions.plot(ax=ax, color='lightgrey', edgecolor='black')
rivers.plot(ax=ax, color='blue', linewidth=1)
glaciers.plot(ax=ax, color='white', edgecolor='black')

plt.title('Nepal Administrative Regions, Rivers, and Glaciers')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.show()