# import lightningchart as lc
# import pandas as pd
# import numpy as np


# with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
#     mylicensekey = f.read().strip()
# lc.set_license(mylicensekey)


# file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project4/NRCAN_Laurentian_Basin/Export/Seis/output.csv'
# data = pd.read_csv(file_path, header=None)

# distances = data.iloc[:, 0]
# amplitudes = data.iloc[:, 3:].values  

# depths = np.arange(amplitudes.shape[1])

# amplitudes_rotated = np.rot90(amplitudes)

# amplitudes_normalized = (amplitudes_rotated - np.min(amplitudes_rotated)) / (np.max(amplitudes_rotated) - np.min(amplitudes_rotated))

# with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
#     mylicensekey = f.read().strip()
# lc.set_license(mylicensekey)

# chart = lc.ChartXY(
#     theme=lc.Themes.Dark,
#     title='2D Seismic Section')

# heatmap_series = chart.add_heatmap_grid_series(columns=amplitudes_normalized.shape[1], rows=amplitudes_normalized.shape[0])
# # heatmap_series.set_intensity_interpolation(False)
# # heatmap_series.hide_wireframe()
# heatmap_series.invalidate_intensity_values(amplitudes_normalized.tolist())
# print(amplitudes_normalized)
# heatmap_series.set_palette_colors(
#     steps=[
#         {'value': 0.0, 'color': lc.Color('blue')},
#         {'value': 0.5, 'color': lc.Color('yellow')},
#         {'value': 1.0, 'color': lc.Color('red')},
#     ],
#     look_up_property='value',
#     percentage_values=True
# )

# chart.get_default_x_axis().set_title('Depth')
# chart.get_default_y_axis().set_title('Distance')

# heatmap_series.set_step(x=1, y=1)
# heatmap_series.hide_wireframe()
# heatmap_series.set_intensity_interpolation(False)

# chart.open()




# import lightningchart as lc
# import pandas as pd
# import numpy as np

# # Load the data
# file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project4/NRCAN_Laurentian_Basin/Export/Seis/output.csv'
# data = pd.read_csv(file_path, header=None)

# # Debug: Print the first few rows of the data to ensure it is loaded correctly
# print("Data head:")
# print(data.head())

# # Extract distance and amplitude values
# distances = data.iloc[:, 0]
# amplitudes = data.iloc[:, 3:].values  # Assuming amplitude data starts from the fourth column

# # Debug: Print the shapes of distances and amplitudes
# print("Distances shape:", distances.shape)
# print("Amplitudes shape:", amplitudes.shape)

# # Debug: Print a sample of distances and amplitudes to check their values
# print("Sample distances:")
# print(distances.head())
# print("Sample amplitudes:")
# print(amplitudes[:5, :5])  # Print a 5x5 sample of the amplitude values

# # Create a 2D grid
# depths = np.arange(amplitudes.shape[1])

# # Rotate the image by 90 degrees
# amplitudes_rotated = np.rot90(amplitudes)

# # Debug: Print the shape of the rotated amplitudes
# print("Rotated amplitudes shape:", amplitudes_rotated.shape)

# # Normalize the amplitude values for better visualization
# amplitudes_normalized = (amplitudes_rotated - np.min(amplitudes_rotated)) / (np.max(amplitudes_rotated) - np.min(amplitudes_rotated))

# # Debug: Print the min and max values of the normalized amplitudes
# print("Min normalized amplitude:", np.min(amplitudes_normalized))
# print("Max normalized amplitude:", np.max(amplitudes_normalized))

# # Debug: Print a small part of normalized amplitudes to check their values
# print("Sample normalized amplitudes (5x5 part):")
# print(amplitudes_normalized[:5, :5])  # Print a 5x5 sample of the normalized amplitude values

# # Initialize LightningChart
# with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
#     mylicensekey = f.read().strip()
# lc.set_license(mylicensekey)

# # Create a chart
# chart = lc.ChartXY(
#     theme=lc.Themes.Dark,
#     title='2D Seismic Section'
# )

# # Debug: Print a small part of the intensity values being set for the heatmap
# print("Sample intensity values being set for the heatmap (5x5 part):")
# print(amplitudes_normalized[:5, :5].tolist())  # Print a 5x5 sample of the intensity values

# # Create a heatmap series
# heatmap_series = chart.add_heatmap_grid_series(columns=amplitudes_normalized.shape[1], rows=amplitudes_normalized.shape[0])

# # Set the intensity values for the heatmap
# heatmap_series.invalidate_intensity_values(amplitudes_normalized.tolist())

# # Customize the heatmap color palette
# heatmap_series.set_palette_colors(
#     steps=[
#         {'value': 0.0, 'color': lc.Color(0, 0, 128, 255)},  # Dark Blue
#         {'value': 0.25, 'color': lc.Color(0, 0, 255, 255)},  # Blue
#         {'value': 0.5, 'color': lc.Color(0, 255, 255, 255)},  # Cyan
#         {'value': 0.75, 'color': lc.Color(255, 255, 0, 255)},  # Yellow
#         {'value': 1.0, 'color': lc.Color(255, 0, 0, 255)},  # Red
#     ],
#     look_up_property='value',
#     percentage_values=True
# )

# # Customize axes titles
# chart.get_default_x_axis().set_title('Depth')
# chart.get_default_y_axis().set_title('Distance')

# # Customize the heatmap grid
# heatmap_series.set_step(x=1, y=1)
# heatmap_series.hide_wireframe()
# heatmap_series.set_intensity_interpolation(False)

# # Show the chart
# chart.open()





# import lightningchart as lc
# import pandas as pd
# import numpy as np

# # Load the data
# file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project4/NRCAN_Laurentian_Basin/Export/Seis/output.csv'
# data = pd.read_csv(file_path, header=None)

# # Extract distance and amplitude values
# distances = data.iloc[:, 0]
# amplitudes = data.iloc[:, 3:].values  # Assuming amplitude data starts from the fourth column

# # Create a 2D grid
# depths = np.arange(amplitudes.shape[1])

# # Rotate the image by 90 degrees
# amplitudes_rotated = np.rot90(amplitudes)

# # Enhance contrast using histogram equalization
# amplitudes_flat = amplitudes_rotated.flatten()
# hist, bin_edges = np.histogram(amplitudes_flat, bins=256, range=(np.min(amplitudes_flat), np.max(amplitudes_flat)))
# cdf = hist.cumsum()  # Cumulative distribution function
# cdf_normalized = cdf / cdf.max()  # Normalize to the range [0, 1]

# amplitudes_equalized = np.interp(amplitudes_flat, bin_edges[:-1], cdf_normalized)
# amplitudes_equalized = amplitudes_equalized.reshape(amplitudes_rotated.shape)

# # Print the range of equalized amplitude values
# print("Range of equalized amplitude values:")
# print(f"Min: {np.min(amplitudes_equalized)}")
# print(f"Max: {np.max(amplitudes_equalized)}")
# print(f"Mean: {np.mean(amplitudes_equalized)}")
# print(f"Std: {np.std(amplitudes_equalized)}")

# # Initialize LightningChart
# with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
#     mylicensekey = f.read().strip()
# lc.set_license(mylicensekey)

# # Create a chart
# chart = lc.ChartXY(
#     theme=lc.Themes.Dark,
#     title='2D Seismic Section'
# )

# # Create a heatmap series
# heatmap_series = chart.add_heatmap_grid_series(columns=amplitudes_equalized.shape[1], rows=amplitudes_equalized.shape[0])

# # Set the intensity values for the heatmap
# heatmap_series.invalidate_intensity_values(amplitudes_equalized.tolist())

# # Set start and end coordinates for the heatmap
# heatmap_series.set_start(x=0, y=0)
# heatmap_series.set_end(x=amplitudes_equalized.shape[1], y=amplitudes_equalized.shape[0])

# # Customize the heatmap color palette
# heatmap_series.set_palette_colors(
#     steps=[
#         {'value': 0.0, 'color': lc.Color(0, 0, 139)},  # Deep blue
#         {'value': 0.25, 'color': lc.Color(0, 104, 204)},  # Bright blue
#         {'value': 0.5, 'color': lc.Color(255, 140, 0)},  # Bright orange
#         {'value': 0.75, 'color': lc.Color(255, 185, 110)},  # Light orange
#         {'value': 1.0, 'color': lc.Color(255, 255, 255)},  # White
#     ],
#     look_up_property='value',
#     percentage_values=True
# )

# # Customize axes titles
# chart.get_default_x_axis().set_title('Depth')
# chart.get_default_y_axis().set_title('Distance')

# # Customize the heatmap grid
# heatmap_series.set_step(x=1, y=1)
# heatmap_series.hide_wireframe()
# heatmap_series.set_intensity_interpolation(False)

# # Show the chart
# chart.open()

# # Additional debug print to verify heatmap data
# print("Intensity values being set for the heatmap (sample):")
# print(amplitudes_equalized[:5, :5].tolist())
# print("Intensity values range:")
# print(f"Min: {amplitudes_equalized.min()}, Max: {amplitudes_equalized.max()}")







import lightningchart as lc
import numpy as np
import pandas as pd
from scipy.interpolate import griddata

# # Read the license key from a file
with open('D:/Computer Aplication/WorkPlacement/Projects/shared_variable.txt', 'r') as f:
    mylicensekey = f.read().strip()
lc.set_license(mylicensekey)

# Load the seismic data
file_path = 'D:/Computer Aplication/WorkPlacement/Projects/Project4/NRCAN_Laurentian_Basin/Export/Seis/output.csv'
data = pd.read_csv(file_path, header=None)

# Extract distance and amplitude values
distances = data.iloc[:, 0].values
amplitudes = data.iloc[:, 3:].values

# Create interpolated grid
grid_size = 500
x_values = distances.astype(float).tolist()
y_values = np.arange(amplitudes.shape[1]).astype(float).tolist()
grid_x, grid_y = np.mgrid[min(x_values):max(x_values):complex(grid_size), min(y_values):max(y_values):complex(grid_size)]
grid_z = griddata((np.repeat(distances, amplitudes.shape[1]), np.tile(y_values, distances.size)), amplitudes.ravel(), (grid_x, grid_y), method='nearest')

# Convert numpy int to Python int
grid_z = grid_z.astype(float)

# Rotate the grid by 180 degrees
grid_z = np.flip(grid_z, axis=(0, 1)).tolist()

# Initialize a chart
chart = lc.ChartXY(theme=lc.Themes.Dark, title='2D Seismic Section')

# Create HeatmapGridSeries
heatmap = chart.add_heatmap_grid_series(
    columns=grid_size,
    rows=grid_size,
)

# Set start and end coordinates
heatmap.set_start(x=min(x_values), y=min(y_values))
heatmap.set_end(x=max(x_values), y=max((y_values)))

# Set step size
heatmap.set_step(x=(max(x_values) - min(x_values)) / grid_size, y=(max(y_values) - min(y_values)) / grid_size)

# Enable intensity interpolation
heatmap.set_intensity_interpolation(True)

# Invalidate intensity values
heatmap.invalidate_intensity_values(grid_z)

# Hide wireframe
heatmap.hide_wireframe()

# Define custom palette to match the second image
custom_palette = [
    {"value": -30000, "color": lc.Color(0, 0, 0)},    # Black
    {"value": -20000, "color": lc.Color(50, 50, 50)},  # Dark Gray
    {"value": 0, "color": lc.Color(255, 255, 255)},   # White
    {"value": 10000, "color": lc.Color(150, 75, 0)},   # Brown
    {"value": 20000, "color": lc.Color(0, 0, 255)},   # Blue
    {"value": 30000, "color": lc.Color(255, 0, 0)}  # Red
]

heatmap.set_palette_colors(
    steps=custom_palette,
    look_up_property='value',
    interpolate=True
)

# Set axis titles
chart.get_default_x_axis().set_title('Distance')
chart.get_default_y_axis().set_title('Depth')

# Set axis limits based on the actual data ranges
chart.get_default_x_axis().set_interval(min(x_values), max(x_values))
chart.get_default_y_axis().set_interval(min(y_values), max(y_values))

# Display chart
chart.open()
